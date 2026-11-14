"""Install the package's core alone in a fresh environment, and import every module and model there.

The core (pyproject.toml's `dependencies`) is what a notebook installs in Colab or Binder, and what a page running
Python in the browser installs with micropip. So it must not need HARK, which needs numba, which the browser's Python
lacks. The book's own environment has HARK (the `hark` add-on), so a HARK import slipping into a module or a model
would pass every other check. This one:

  - builds the package's wheel and installs it, core only, in a new virtual environment;
  - fails if that installed a package any add-on names (or numba), so the core stays light;
  - imports every module of the package and every model in `models`, and fails on any that cannot be imported;
  - runs the package's own self-test there (`python -m intertemporal_choice --self-test`), which reaches the imports
    made inside functions, such as a slider's.

`--self-test` runs the import probe against a small package with a module that imports a package that is not
installed, and fails unless the probe reports that module, imports the good ones and leaves `__main__` alone.

Usage: uv run python code/check_core.py [--self-test]
"""

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = "intertemporal_choice"
# Not named by an add-on, but what keeps HARK out of the browser.
NEVER_IN_CORE = {"numba"}

# Run by the fresh environment's Python: import every module of the package (but not its __main__, which is a
# command) and every model, and print what failed.
PROBE = """
import importlib, json, pkgutil, sys
name = sys.argv[1]
sys.path[:0] = sys.argv[2:]
package = importlib.import_module(name)
names = [m.name for m in pkgutil.walk_packages(package.__path__, name + ".") if m.name.rpartition(".")[2] != "__main__"]
try:
    models = importlib.import_module(name + ".models")
    names += [f"{models.__name__}.{model}" for model in getattr(models, "__all__", [])]
except ImportError:
    pass
failed = {}
for module in dict.fromkeys(names):
    try:
        importlib.import_module(module)
    except Exception as e:
        failed[module] = f"{type(e).__name__}: {e}"
print(json.dumps({"imported": sorted(set(names) - set(failed)), "failed": failed}))
"""


def normalize(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def add_on_packages(pyproject: Path) -> set[str]:
    """The distributions any add-on (optional dependency) names, normalized, plus NEVER_IN_CORE."""
    extras = tomllib.loads(pyproject.read_text()).get("project", {}).get("optional-dependencies", {})
    names = {normalize(re.match(r"[A-Za-z0-9._-]+", req.strip()).group()) for reqs in extras.values() for req in reqs}
    return names | NEVER_IN_CORE


def probe(python: str, name: str, extra_path: list[str], env: dict) -> dict:
    out = subprocess.run([python, "-I", "-c", PROBE, name, *extra_path], capture_output=True, text=True, env=env)
    if out.returncode:
        return {"imported": [], "failed": {name: out.stderr.strip().splitlines()[-1] if out.stderr.strip() else "exit"}}
    return json.loads(out.stdout.strip().splitlines()[-1])


def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, text=True, **kwargs)


def check(root: Path) -> int:
    problems = []
    env = os.environ | {"MPLBACKEND": "Agg"}
    env.pop("VIRTUAL_ENV", None)
    with tempfile.TemporaryDirectory() as tmp:
        built = run(["uv", "build", "--wheel", "--out-dir", f"{tmp}/dist", str(root)], env=env)
        wheels = sorted(Path(tmp, "dist").glob("*.whl"))
        if built.returncode or len(wheels) != 1:
            log.error("could not build the wheel:\n%s", built.stderr)
            return 1
        venv = Path(tmp, "core")
        python = str(venv / "bin" / "python")
        for step in (["uv", "venv", "--quiet", "--python", sys.executable, str(venv)],
                     ["uv", "pip", "install", "--quiet", "--python", python, str(wheels[0])]):
            done = run(step, env=env)
            if done.returncode:
                log.error("%s failed:\n%s", " ".join(step[:3]), done.stderr)
                return 1
        listed = run(["uv", "pip", "list", "--python", python, "--format", "json"], env=env)
        installed = {normalize(p["name"]) for p in json.loads(listed.stdout)}
        log.info("the core installed %d packages from %s", len(installed), wheels[0].name)
        for name in sorted(installed & add_on_packages(root / "pyproject.toml")):
            problems.append(f"the core installed {name}, which belongs in an add-on, never the core")
        result = probe(python, PACKAGE, [], env)
        log.info("imported %d modules and models in the core alone", len(result["imported"]))
        for module, error in result["failed"].items():
            problems.append(f"{module} cannot be imported with the core alone: {error}")
        tested = run([python, "-I", "-m", PACKAGE, "--self-test"], env=env, cwd=tmp)
        if tested.returncode:
            tail = "\n".join((tested.stdout + tested.stderr).strip().splitlines()[-5:])
            problems.append(f"the package's self-test fails with the core alone:\n{tail}")
    for p in problems:
        log.error("FAIL: %s", p)
    log.info("core %s", "FAILED" if problems else "passed: installs without the add-ons, and every module and model imports")
    return 1 if problems else 0


def self_test() -> bool:
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        pkg = Path(tmp, "fakepkg")
        (pkg / "models").mkdir(parents=True)
        (pkg / "__init__.py").write_text("")
        (pkg / "__main__.py").write_text("raise SystemExit('__main__ was imported')\n")
        (pkg / "good.py").write_text("import json\n")
        (pkg / "bad.py").write_text("import a_package_that_is_not_installed\n")
        (pkg / "models" / "__init__.py").write_text("__all__ = ['model']\n")
        (pkg / "models" / "model.py").write_text("x = 1\n")
        result = probe(sys.executable, "fakepkg", [tmp], dict(os.environ))
        if set(result["failed"]) != {"fakepkg.bad"}:
            failures.append(f"the probe reported {sorted(result['failed'])}, not exactly fakepkg.bad")
        if set(result["imported"]) != {"fakepkg.good", "fakepkg.models", "fakepkg.models.model"}:
            failures.append(f"the probe imported {result['imported']}")
        pyproject = Path(tmp, "pyproject.toml")
        pyproject.write_text('[project]\noptional-dependencies = {hark = ["econ-ark>=0.17", "Sym_Py", '
                             '"aiyagari1994qje @ git+https://example.org/x"]}\n')
        if add_on_packages(pyproject) != {"econ-ark", "sym-py", "aiyagari1994qje", "numba"}:
            failures.append(f"read the add-ons' packages as {sorted(add_on_packages(pyproject))}")
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    sys.exit((0 if self_test() else 1) if args.self_test else check(ROOT))
