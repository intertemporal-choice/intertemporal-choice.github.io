"""Build the book with every figure notebook executed: `myst build --execute`, run safely.

Every figure a chapter shows is the output of a labelled cell in a notebook under
content/notebooks/, so the site and the PDF must be built with --execute. This script is the
one entry point for that, used by CI, by local builds and by build_pdf.py.

  - MyST can launch its own Jupyter server, but it waits 20 seconds for the server to print
    its token and on this book that wait times out ("Jupyter server did not respond"). MyST
    documents the route used here instead: start the server first and pass its address in
    JUPYTER_BASE_URL and JUPYTER_TOKEN. (Ported from Alan Lujan's version on the
    migrate-kfm-from-demark branch.)
  - MyST caches executed notebooks in _build/execute, keyed on the kernel name and the cell
    code only. A change to the shared package, the data snapshots or the locked environment
    would therefore reuse stale outputs. Every notebook declares
    `execute: {depends_on_env: [IC_EXEC_ENV]}`, and this script sets IC_EXEC_ENV to a hash of
    uv.lock, src/**/*.py and data/**, which puts all three into the cache key.
  - A preflight lint refuses to build when a notebook would break that, or would lose a figure
    from the PDF: each notebook must declare the python3 kernel and depends_on_env, and no
    figure cell (label nb-...) may carry a hide or remove tag, since hidden outputs are dropped
    from the LaTeX export.

`--self-test` runs the hash and the lint against input they must accept or reject, and fails
if either misjudges it. `--print-env-hash` prints IC_EXEC_ENV, which CI uses as its cache key.

Usage: uv run python code/build_site.py [--root DIR] [myst build options]  (default: --html --strict)
"""

import argparse
import hashlib
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
NOTEBOOKS = Path("content/notebooks")
DEFAULT_ARGS = ["--html", "--strict"]
STARTUP_SECONDS = 60
ENV_VAR = "IC_EXEC_ENV"
# What the notebooks' outputs depend on besides their own cells.
HASHED = [("uv.lock", "*"), ("src", "**/*.py"), ("data", "**/*")]
HIDING_TAGS = {"remove-output", "hide-output", "remove-cell", "hide-cell"}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
CODE_CELL = re.compile(r"^```\{code-cell\}[^\n]*\n(.*?)^```", re.S | re.M)
LABEL = re.compile(r"^#\s?\|\s*label:\s*(\S+)", re.M)
TAGS_OPTION = re.compile(r"^(?::tags:|#\s?\|\s*tags:)\s*(\[.*?\])", re.M)


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
    folder = root / NOTEBOOKS
    return sorted(p for p in folder.glob("*.md") if p.name != "index.md") if folder.is_dir() else []


def lint(path: Path, text: str) -> list[str]:
    """Why a notebook would build wrongly: missing kernel/cache key, or a hidden figure."""
    problems = []
    m = FRONTMATTER.match(text)
    front = (yaml.safe_load(m.group(1)) or {}) if m else {}
    if (front.get("kernelspec") or {}).get("name") != "python3":
        problems.append(f"{path}: frontmatter must declare kernelspec name python3")
    depends = ((front.get("execute") or {}).get("depends_on_env")) or []
    if ENV_VAR not in depends:
        problems.append(f"{path}: frontmatter must declare execute: depends_on_env: [{ENV_VAR}]")
    for cell in CODE_CELL.findall(text):
        label = LABEL.search(cell)
        if not label or not label.group(1).startswith("nb-"):
            continue
        tags = TAGS_OPTION.search(cell)
        found = set(yaml.safe_load(tags.group(1)) or []) if tags else set()
        if found & HIDING_TAGS:
            problems.append(
                f"{path}: figure cell {label.group(1)} is tagged {sorted(found & HIDING_TAGS)},"
                " which drops it from the PDF"
            )
    return problems


def preflight(root: Path) -> list[str]:
    return [p for f in notebook_files(root) for p in lint(f.relative_to(root), f.read_text())]


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
    """Run `myst build --execute` in `root`, with a Jupyter server whose root is `root`.

    `root` is where the kernels run as well as where MyST builds, so build_pdf.py can build
    its staged copy. `exec_env` lets it pass the hash of the original tree, so the staged
    build hits the cache the HTML build filled. `output`, if given, receives MyST's output.
    """
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
        log.info("no notebooks under %s; building without a Jupyter server", NOTEBOOKS)
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


GOOD = """---
kernelspec: {name: python3, display_name: Python 3, language: python}
execute:
  depends_on_env: [IC_EXEC_ENV]
---
```{code-cell} python3
#| label: nb-Test-Figure
x = 1
```
"""


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
        (root / NOTEBOOKS).mkdir(parents=True)
        (root / NOTEBOOKS / "Test.md").write_text(GOOD)
        if env_hash(root) != base:
            failures.append("env hash changed on a __pycache__ file or a notebook edit")
        for path, text in [("uv.lock", "lock 2"), ("src/pkg/mod.py", "x = 2"), ("data/a.csv", "1")]:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text)
            if env_hash(root) == base:
                failures.append(f"env hash did not change when {path} changed")
            base = env_hash(root)
        if preflight(root):
            failures.append(f"preflight rejected a good notebook: {preflight(root)}")
    bad = {
        "no kernelspec": GOOD.replace("kernelspec: {name: python3, display_name: Python 3, language: python}\n", ""),
        "wrong kernel": GOOD.replace("name: python3", "name: julia"),
        "no depends_on_env": GOOD.replace("  depends_on_env: [IC_EXEC_ENV]\n", "  cache: true\n"),
        "hidden figure (#| tags)": GOOD.replace("x = 1", "#| tags: [remove-output]\nx = 1"),
        "hidden figure (:tags:)": GOOD.replace("#| label", ":tags: [hide-output]\n#| label"),
    }
    for name, text in bad.items():
        if not lint(Path("t.md"), text):
            failures.append(f"preflight accepted a notebook with {name}")
    if lint(Path("t.md"), GOOD.replace("nb-Test-Figure", "helper").replace("x = 1", "#| tags: [remove-output]\nx = 1")):
        failures.append("preflight rejected a hidden cell that is not a figure")
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
