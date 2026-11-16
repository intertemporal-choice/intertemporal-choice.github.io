"""Keep the figure notebooks' committed form stable: strip what Jupyter rewrites on every save.

Opening a notebook and saving it rewrites execution counts, timestamps and the versions of
the kernel and of Python, none of which is content. The notebooks are committed WITH their
outputs, so that GitHub and a downloaded copy show the figures; what has to go is only that
metadata. nbstripout does it as a git filter, applied when a file is staged, so the working
copy can carry whatever Jupyter wrote while the committed form changes only when the code or
the outputs do: an inspect-and-save leaves nothing to commit, and nothing to build.

The options live here, in one place, and the three uses share them:

  --install   set the filter up in this clone (once per clone; .gitattributes names it), and
              the pre-commit hook that regenerates each student notebook from its _SST source
              (code/notebook_math.py --hook)
  --check     fail if any tracked notebook is committed unstripped (the workflow runs this)
  --strip     strip the tracked notebooks in place (what the filter does, by hand)

`--self-test` strips a synthetic notebook and checks that outputs and cell ids survive while
counts, timings and version metadata do not, and that --check tells the two states apart.

Usage: uv run python code/notebooks.py --install | --check | --strip | --self-test
"""

import argparse
import json
import logging
import subprocess
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
# Keep outputs and cell ids; drop counts, timings (nbstripout's defaults) and the Python
# version, which language_info records and which differs between environments.
OPTIONS = ["--keep-output", "--keep-id", "--extra-keys", "metadata.language_info"]
FILTER = "uv run nbstripout " + " ".join(OPTIONS)
# The pre-commit hook: each student notebook regenerated from its staged _SST source, and staged.
# A branch without the script skips it, since one hook serves every worktree of the clone.
HOOK = """#!/bin/sh
# Installed by code/notebooks.py --install: regenerate each student notebook from its _SST
# source, from what is staged, and stage it (code/notebook_math.py --hook).
[ -f code/notebook_math.py ] || exit 0
exec uv run --locked python code/notebook_math.py --hook
"""


def tracked_notebooks(root: Path) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", "*.ipynb"], cwd=root, capture_output=True, text=True, check=True
    ).stdout
    return out.split()


def nbstripout(args: list[str], cwd: Path) -> int:
    return subprocess.run([sys.executable, "-m", "nbstripout", *OPTIONS, *args], cwd=cwd).returncode


def install(root: Path) -> None:
    for key, value in [
        ("filter.nbstripout.clean", FILTER),
        ("filter.nbstripout.smudge", "cat"),
        ("filter.nbstripout.required", "true"),
        ("diff.ipynb.textconv", FILTER + " --textconv"),
    ]:
        subprocess.run(["git", "config", key, value], cwd=root, check=True)
    log.info("nbstripout filter installed in this clone: %s", FILTER)
    install_hook(root)


def install_hook(root: Path) -> bool:
    """Write the pre-commit hook, unless the clone already has a different one: that is left alone."""
    where = subprocess.run(["git", "rev-parse", "--git-path", "hooks"], cwd=root, capture_output=True,
                           text=True, check=True).stdout.strip()
    hooks = Path(where) if Path(where).is_absolute() else root / where
    hook = hooks / "pre-commit"
    if hook.exists() and hook.read_text() != HOOK:
        log.warning("left %s as it is, since it is not this script's: add `uv run --locked python "
                    "code/notebook_math.py --hook` to it", hook)
        return False
    hooks.mkdir(parents=True, exist_ok=True)
    hook.write_text(HOOK)
    hook.chmod(0o755)
    log.info("pre-commit hook installed: %s", hook)
    return True


def check(root: Path) -> int:
    """Verify the notebooks as git holds them (the index), not the working copies.

    The filter strips at staging, so a working copy may carry what Jupyter last wrote
    while the staged and committed forms are clean; those are what this checks.
    """
    files = tracked_notebooks(root)
    if not files:
        log.info("no notebooks tracked")
        return 0
    with tempfile.TemporaryDirectory() as tmp:
        staged = []
        for file in files:
            copy = Path(tmp) / file.replace("/", "__")
            copy.write_bytes(
                subprocess.run(["git", "show", f":{file}"], cwd=root, capture_output=True, check=True).stdout
            )
            staged.append(str(copy))
        code = nbstripout(["--verify", *staged], Path(tmp))
    log.info(
        "%d notebooks %s", len(files),
        "are staged and committed stripped" if code == 0
        else "NOT stripped as staged: install the filter (code/notebooks.py --install) and stage them again",
    )
    return code


def strip(root: Path) -> int:
    files = tracked_notebooks(root)
    return nbstripout(files, root) if files else 0


UNSTRIPPED = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
        "language_info": {"name": "python", "version": "3.11.13"},
    },
    "cells": [
        {
            "id": "abc123",
            "cell_type": "code",
            "execution_count": 7,
            "metadata": {"execution": {"iopub.execute_input": "2026-09-29T00:00:00Z"}},
            "source": ["print(1)"],
            "outputs": [{"output_type": "stream", "name": "stdout", "text": ["1\n"]}],
        }
    ],
}


def self_test() -> bool:
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "t.ipynb"
        path.write_text(json.dumps(UNSTRIPPED))
        if nbstripout(["--verify", str(path)], Path(tmp)) == 0:
            failures.append("--check passed an unstripped notebook")
        nbstripout([str(path)], Path(tmp))
        nb = json.loads(path.read_text())
        cell = nb["cells"][0]
        if cell.get("outputs") != UNSTRIPPED["cells"][0]["outputs"]:
            failures.append("stripping removed the outputs")
        if cell.get("id") != "abc123":
            failures.append("stripping removed the cell id")
        if cell.get("execution_count") is not None:
            failures.append("stripping kept the execution count")
        if "execution" in cell.get("metadata", {}):
            failures.append("stripping kept the cell's execution timings")
        if "language_info" in nb["metadata"]:
            failures.append("stripping kept language_info (the Python version)")
        if nb["metadata"].get("kernelspec", {}).get("name") != "python3":
            failures.append("stripping removed the kernelspec")
        if nbstripout(["--verify", str(path)], Path(tmp)) != 0:
            failures.append("--check failed a stripped notebook")
        repo = Path(tmp) / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
        hook = repo / ".git" / "hooks" / "pre-commit"
        if not install_hook(repo) or hook.read_text() != HOOK or not hook.stat().st_mode & 0o100:
            failures.append("the pre-commit hook was not installed, or not executable")
        hook.write_text("#!/bin/sh\necho someone else's\n")
        if install_hook(repo) or "someone else's" not in hook.read_text():
            failures.append("a pre-commit hook that is not this script's was overwritten")
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--install", action="store_true")
    group.add_argument("--check", action="store_true")
    group.add_argument("--strip", action="store_true")
    group.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    if args.install:
        install(ROOT)
        sys.exit(0)
    sys.exit(check(ROOT) if args.check else strip(ROOT))
