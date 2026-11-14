"""Keep the figure notebooks' committed form stable: strip what Jupyter rewrites on every save.

Opening a notebook and saving it rewrites execution counts, timestamps and the versions of
the kernel and of Python, none of which is content. The notebooks are committed WITH their
outputs, so that GitHub and a downloaded copy show the figures; what has to go is only that
metadata. nbstripout does it as a git filter, applied when a file is staged, so the working
copy can carry whatever Jupyter wrote while the committed form changes only when the code or
the outputs do: an inspect-and-save leaves nothing to commit, and nothing to build.

The options live here, in one place, and the three uses share them:

  --install   set the filter up in this clone (once per clone; .gitattributes names it)
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
