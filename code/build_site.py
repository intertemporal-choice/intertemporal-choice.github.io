"""Build the book, executing the figure notebooks that changed: `myst build --execute`, run safely.

Every figure a chapter shows is drawn by the notebook beside it, `<Chapter>.ipynb` in the
chapter's folder, into that folder's `figures/`. The site shows the notebooks as pages too, so
the build runs with --execute. This script is the one entry point for that, used by CI and
by local builds.

  - MyST can launch its own Jupyter server, but it waits 20 seconds for the server to print
    its token and on this book that wait times out ("Jupyter server did not respond"). MyST
    documents the route used here instead: start the server first and pass its address in
    JUPYTER_BASE_URL and JUPYTER_TOKEN. (Ported from Alan Lujan's version on the
    migrate-kfm-from-demark branch.)
  - MyST caches executed notebooks in _build/execute, keyed on the kernel name and the cell
    code only, so a notebook that has not changed is not re-run. A change to the shared
    package, the data snapshots or the locked environment would reuse stale outputs, though:
    every notebook declares `execute: {depends_on_env: [IC_EXEC_ENV]}`, and this script sets
    IC_EXEC_ENV to a hash of uv.lock, src/**/*.py and data/**, which puts all three into the
    cache key.
  - A preflight lint refuses to build when a notebook breaks the conventions the checks rely
    on: it must sit beside its chapter as content/<part>/<Chapter>/<Chapter>.ipynb, declare the
    python3 kernel, declare depends_on_env in the frontmatter of its first cell, begin with the
    bootstrap cell (so a downloaded copy runs anywhere), and the figures it saves must be
    exactly the files in its figures/ folder (a saved figure that was not committed, or a file
    no code draws, fails here rather than in the built site).

`--self-test` runs the hash and the lint against input they must accept or reject, and fails
if either misjudges it. `--print-env-hash` prints IC_EXEC_ENV, which CI uses as its cache key.

Usage: uv run python code/build_site.py [--root DIR] [myst build options]  (default: --html --strict)
"""

import argparse
import hashlib
import json
import logging
import os
import re
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
CONTENT = Path("content")
DEFAULT_ARGS = ["--html", "--strict"]
STARTUP_SECONDS = 60
ENV_VAR = "IC_EXEC_ENV"
# What the notebooks' outputs depend on besides their own cells.
HASHED = [("uv.lock", "*"), ("src", "**/*.py"), ("data", "**/*")]

# The first code cell of every notebook, verbatim: a downloaded copy installs what it needs.
BOOTSTRAP = """\
# Run anywhere: install the book's package (it brings econ-ark, numpy and matplotlib) if it
# is missing. Inside the book's own environment this does nothing.
try:
    import intertemporal_choice
except ImportError:
    %pip install -q git+https://github.com/intertemporal-choice/intertemporal-choice.github.io"""

FRONTMATTER = re.compile(r"\A\s*---\n(.*?)\n---", re.S)
SAVE = re.compile(r"\bsave\(\s*[^,()]+,\s*[\"']([^\"']+)[\"']")


def env_hash(root: Path) -> str:
    """sha256 over the files every notebook's outputs depend on (paths and bytes)."""
    h = hashlib.sha256()
    for base, pattern in HASHED:
        top = root / base
        files = [top] if top.is_file() else sorted(top.glob(pattern)) if top.is_dir() else []
        for f in files:
            rel = f.relative_to(root)
            if not f.is_file() or "__pycache__" in rel.parts:
                continue
            if any(part.startswith(".") for part in rel.parts):
                continue
            h.update(str(rel).encode() + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def notebook_files(root: Path) -> list[Path]:
    folder = root / CONTENT
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)


def source(cell: dict) -> str:
    text = cell.get("source", "")
    return "".join(text) if isinstance(text, list) else text


def frontmatter(nb: dict) -> dict:
    """The YAML block that opens the first cell, which MyST reads as the page's frontmatter."""
    cells = nb.get("cells") or []
    if not cells or cells[0].get("cell_type") not in ("markdown", "raw"):
        return {}
    m = FRONTMATTER.match(source(cells[0]))
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def lint(root: Path, rel: Path, nb: dict) -> list[str]:
    """Why a notebook would build wrongly, or break the checks the build relies on."""
    problems = []
    folder = rel.parent
    if rel.stem != folder.name or not (root / folder / "index.md").is_file() or len(folder.parts) != 3:
        problems.append(
            f"{rel}: a notebook lives beside its chapter, as content/<part>/<Chapter>/<Chapter>.ipynb"
            " next to that chapter's index.md"
        )
    if ((nb.get("metadata") or {}).get("kernelspec") or {}).get("name") != "python3":
        problems.append(f"{rel}: the notebook's kernelspec must be python3")
    depends = ((frontmatter(nb).get("execute") or {}).get("depends_on_env")) or []
    if ENV_VAR not in depends:
        problems.append(
            f"{rel}: the first cell must open with frontmatter declaring"
            f" execute: depends_on_env: [{ENV_VAR}]"
        )
    code = [c for c in nb.get("cells") or [] if c.get("cell_type") == "code"]
    if not code or source(code[0]).strip() != BOOTSTRAP.strip():
        problems.append(f"{rel}: the first code cell must be the bootstrap cell (build_site.BOOTSTRAP)")
    saved = {name for c in code for name in SAVE.findall(source(c))}
    figures = root / folder / "figures"
    present = {p.stem for p in figures.glob("*.png")} if figures.is_dir() else set()
    for name in sorted(saved - present):
        problems.append(f"{rel}: saves figures/{name}.png, which is not committed: run the notebook and commit it")
    for name in sorted(present - saved):
        problems.append(f"{folder}/figures/{name}.png: no cell of {rel.name} draws it; delete it or draw it")
    return problems


def preflight(root: Path) -> list[str]:
    problems = []
    for path in notebook_files(root):
        rel = path.relative_to(root)
        try:
            nb = json.loads(path.read_text())
        except ValueError as e:
            problems.append(f"{rel}: not a notebook: {e}")
            continue
        problems += lint(root, rel, nb)
    return problems


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def server_is_up(url: str, token: str) -> bool:
    try:
        with urllib.request.urlopen(f"{url}/api/status?token={token}", timeout=2):
            return True
    except (urllib.error.URLError, OSError):
        return False


def wait_for_server(proc: subprocess.Popen, url: str, token: str) -> None:
    deadline = time.monotonic() + STARTUP_SECONDS
    while not server_is_up(url, token):
        if proc.poll() is not None:
            raise SystemExit(f"Jupyter server exited with code {proc.returncode}")
        if time.monotonic() > deadline:
            raise SystemExit(f"Jupyter server not up after {STARTUP_SECONDS} s")
        time.sleep(0.5)


def run_myst(command: list[str], root: Path, env: dict, output: Path | None) -> int:
    if output is None:
        return subprocess.run(command, cwd=root, env=env, check=False).returncode
    log.info("$ %s  (in %s, output in %s)", " ".join(command), root, output)
    with Path(output).open("w") as out:
        return subprocess.run(
            command, cwd=root, env=env, stdout=out, stderr=subprocess.STDOUT, check=False
        ).returncode


def build(
    myst_args: list[str],
    root: Path = ROOT,
    exec_env: str | None = None,
    output: Path | None = None,
) -> int:
    """Run `myst build --execute` in `root`, with a Jupyter server whose root is `root`."""
    root = Path(root).resolve()
    problems = preflight(root)
    for p in problems:
        log.error("PREFLIGHT: %s", p)
    if problems:
        return 1
    env = {**os.environ, ENV_VAR: exec_env or env_hash(root)}
    command = ["myst", "build", "--execute", *(myst_args or DEFAULT_ARGS)]
    started = time.monotonic()
    if not notebook_files(root):
        log.info("no notebooks under %s; building without a Jupyter server", CONTENT)
        code = run_myst(command, root, env, output)
        log.info("myst build finished in %.0f s", time.monotonic() - started)
        return code

    # The first import of matplotlib builds its font cache, and the warning it prints would
    # land in a notebook's outputs. Pay that cost here, outside any kernel.
    subprocess.run([sys.executable, "-c", "import matplotlib.pyplot"], check=False)

    port, token = free_port(), secrets.token_hex(16)
    url = f"http://127.0.0.1:{port}"
    server_log = root / "_build" / "jupyter-server.log"
    server_log.parent.mkdir(parents=True, exist_ok=True)
    with open(server_log, "w") as out:
        server = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "jupyter_server",
                "--no-browser",
                f"--ServerApp.root_dir={root}",
                f"--ServerApp.port={port}",
                "--ServerApp.port_retries=0",
                f"--IdentityProvider.token={token}",
            ],
            stdout=out,
            stderr=subprocess.STDOUT,
        )
        try:
            wait_for_server(server, url, token)
            log.info("Jupyter server up at %s (log: %s)", url, server_log)
            env |= {"JUPYTER_BASE_URL": url, "JUPYTER_TOKEN": token}
            code = run_myst(command, root, env, output)
            log.info("myst build --execute finished in %.0f s", time.monotonic() - started)
            return code
        finally:
            server.terminate()
            try:
                server.wait(timeout=30)
            except subprocess.TimeoutExpired:
                server.kill()


def good_notebook() -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}},
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": "---\ntitle: Figures\nexecute:\n  depends_on_env: [IC_EXEC_ENV]\n---\nDraws the figure."},
            {"cell_type": "code", "metadata": {}, "source": BOOTSTRAP, "outputs": [], "execution_count": None},
            {"cell_type": "code", "metadata": {}, "source": "from intertemporal_choice import style\nstyle.save(fig, \"Test\")", "outputs": [], "execution_count": None},
        ],
    }


def self_test() -> bool:
    """Every check must act on input it is supposed to act on."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "src/pkg/__pycache__").mkdir(parents=True)
        (root / "uv.lock").write_text("lock 1")
        (root / "src/pkg/mod.py").write_text("x = 1")
        base = env_hash(root)
        (root / "src/pkg/__pycache__/mod.pyc").write_bytes(b"junk")
        chapter = root / CONTENT / "part" / "Test"
        (chapter / "figures").mkdir(parents=True)
        (chapter / "index.md").write_text("# Test\n")
        (chapter / "figures" / "Test.png").write_bytes(b"png")
        (chapter / "Test.ipynb").write_text(json.dumps(good_notebook()))
        if env_hash(root) != base:
            failures.append("env hash changed on a __pycache__ file or a notebook")
        for path, text in [("uv.lock", "lock 2"), ("src/pkg/mod.py", "x = 2"), ("data/a.csv", "1")]:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text)
            if env_hash(root) == base:
                failures.append(f"env hash did not change when {path} changed")
            base = env_hash(root)
        if preflight(root):
            failures.append(f"preflight rejected a good notebook: {preflight(root)}")
        rel = Path("content/part/Test/Test.ipynb")

        def spoiled(mutate) -> dict:
            nb = good_notebook()
            mutate(nb)
            return nb

        bad = {
            "wrong kernel": spoiled(lambda nb: nb["metadata"]["kernelspec"].update(name="julia")),
            "no kernelspec": spoiled(lambda nb: nb["metadata"].pop("kernelspec")),
            "no depends_on_env": spoiled(lambda nb: nb["cells"][0].update(source="---\ntitle: x\n---\n")),
            "frontmatter not in the first cell": spoiled(lambda nb: nb["cells"].insert(0, {"cell_type": "markdown", "source": "intro"})),
            "no bootstrap cell": spoiled(lambda nb: nb["cells"].pop(1)),
            "altered bootstrap cell": spoiled(lambda nb: nb["cells"][1].update(source=BOOTSTRAP.replace("-q ", ""))),
            "a saved figure that is not committed": spoiled(lambda nb: nb["cells"][2].update(source='style.save(fig, "Test")\nstyle.save(g, "Other")')),
            "a figure file no cell draws": spoiled(lambda nb: nb["cells"][2].update(source="x = 1")),
        }
        for name, nb in bad.items():
            if not lint(root, rel, nb):
                failures.append(f"preflight accepted a notebook with {name}")
        for name, where in {
            "a notebook not named after its folder": Path("content/part/Test/Other.ipynb"),
            "a notebook outside a chapter folder": Path("content/part/Test.ipynb"),
        }.items():
            if not lint(root, where, good_notebook()):
                failures.append(f"preflight accepted {name}")
        (chapter / "Test.ipynb").write_text("{not json")
        if not preflight(root):
            failures.append("preflight accepted a file that is not a notebook")
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--print-env-hash", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args, myst_args = parser.parse_known_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    if args.print_env_hash:
        print(env_hash(args.root))
        sys.exit(0)
    sys.exit(build(myst_args, root=args.root))
