"""Build the in-browser copies of the figure notebooks: a JupyterLite site, served at /lite/.

JupyterLite runs Python in the browser (Pyodide), so a reader opens a notebook and runs it
with nothing installed and no server, e.g.
https://intertemporal-choice.github.io/lite/notebooks/index.html?path=Fisher2Period.ipynb

Only notebooks whose packages Pyodide has can go here: numpy, matplotlib and ipywidgets are
enough for those in NOTEBOOKS. HARK cannot run in a browser (it needs numba), so a notebook that
uses it stays with Colab and Binder.

Each notebook is published as the book has it, except that the reader, who is already running
it, sees the economics straight away:

  - the frontmatter cell, which MyST reads and Jupyter would show as a stray heading, becomes
    the title, followed by one line telling the reader to run all the cells;
  - the cell with the links that open the notebook elsewhere is dropped;
  - the bootstrap cell, whose `%pip install` from GitHub Pyodide cannot do, is dropped. The book's
    package, which is pure Python, is copied beside the notebooks, and the site's configuration
    (jupyter-lite.json) loads ipywidgets, which Pyodide lacks, when the page starts.

`--self-test` checks those changes against a synthetic notebook.

Usage: python code/build_lite.py OUTPUT_DIR   (CI: _build/html/lite, after the MyST build)
       python code/build_lite.py --self-test
"""

import argparse
import json
import logging
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "code" / "jupyterlite"  # jupyter-lite.json: the site's name and settings
PACKAGE = ROOT / "src" / "intertemporal_choice"
NOTEBOOKS = [
    "content/consumption/Fisher2Period/Fisher2Period.ipynb",
]
RUN_FIRST = "**First, choose Run \u2192 Run All Cells in the menu above.** The sliders appear at the end."
FRONTMATTER = re.compile(r"\A\s*---\n(.*?)\n---\s*\Z", re.S)
TITLE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M)


def text(cell: dict) -> str:
    return "".join(cell.get("source", ""))


def for_the_browser(nb: dict) -> dict:
    """The notebook as a reader in the browser should see it: title, how to run it, then the economics."""
    cells = nb.get("cells") or []
    m = FRONTMATTER.match(text(cells[0])) if cells and cells[0].get("cell_type") in ("markdown", "raw") else None
    if not m:
        return nb
    title = TITLE.search(m.group(1))
    name = title.group(1).removeprefix("Figures: ") if title else ""
    links = lambda c: c.get("cell_type") == "markdown" and "colab.research.google.com" in text(c) and "mybinder.org" in text(c)
    bootstrap = lambda c: c.get("cell_type") == "code" and "import intertemporal_choice" in text(c) and "%pip install" in text(c)
    kept = [c for c in cells[1:] if not links(c) and not bootstrap(c)]
    nb["cells"] = [
        {"cell_type": "markdown", "id": cells[0].get("id", "title"), "metadata": {}, "source": f"# {name}"},
        {"cell_type": "markdown", "id": "run-first", "metadata": {}, "source": RUN_FIRST},
    ] + kept
    return nb


def stage(folder: Path) -> None:
    for rel in NOTEBOOKS:
        nb = json.loads((ROOT / rel).read_text())
        (folder / Path(rel).name).write_text(json.dumps(for_the_browser(nb), indent=1, ensure_ascii=False) + "\n")
    shutil.copytree(PACKAGE, folder / PACKAGE.name, ignore=shutil.ignore_patterns("__pycache__"))


def build(output: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        contents = Path(tmp) / "contents"
        contents.mkdir()
        stage(contents)
        # Build in the temporary folder, so the build's own cache (.jupyterlite.doit.db) stays out
        # of the repository.
        shutil.copy2(CONFIG / "jupyter-lite.json", tmp)
        subprocess.run(
            ["jupyter", "lite", "build", "--contents", str(contents), "--output-dir", str(output.resolve()),
             "--no-sourcemaps"],
            cwd=tmp, check=True,
        )
    log.info("JupyterLite site with %d notebooks in %s", len(NOTEBOOKS), output)


def self_test() -> bool:
    nb = {"cells": [
        {"cell_type": "markdown", "id": "a", "metadata": {},
         "source": '---\ntitle: "Figures: The Fisher Two-Period Problem"\nexecute:\n  depends_on_env: [IC_EXEC_ENV]\n---'},
        {"cell_type": "markdown", "id": "l", "metadata": {},
         "source": "Open it in [Colab](https://colab.research.google.com/x) or [Binder](https://mybinder.org/x)."},
        {"cell_type": "markdown", "id": "e", "metadata": {}, "source": "The consumer has ..."},
        {"cell_type": "code", "id": "b", "metadata": {}, "outputs": [], "execution_count": None,
         "source": "try:\n    import intertemporal_choice\nexcept ImportError:\n    %pip install -q git+https://example"},
        {"cell_type": "code", "id": "c", "metadata": {}, "source": "x = 1", "outputs": [], "execution_count": None},
    ]}
    out = for_the_browser(json.loads(json.dumps(nb)))
    failures = []
    sources = [c["source"] for c in out["cells"]]
    if sources[:2] != ["# The Fisher Two-Period Problem", RUN_FIRST]:
        failures.append(f"the notebook should open with its title and RUN_FIRST, not {sources[:2]!r}")
    if out["cells"][2:] != [nb["cells"][2], nb["cells"][4]]:
        failures.append("the links and bootstrap cells were not the only ones dropped")
    plain = {"cells": [{"cell_type": "markdown", "id": "a", "metadata": {}, "source": "# Already a title"}]}
    if for_the_browser(json.loads(json.dumps(plain))) != plain:
        failures.append("a notebook without frontmatter changed")
    missing = [rel for rel in NOTEBOOKS if not (ROOT / rel).is_file()]
    if missing:
        failures.append(f"listed notebooks that do not exist: {missing}")
    for f in failures:
        log.error("build_lite self-test: %s", f)
    if not failures:
        log.info("build_lite self-test: ok")
    return not failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return 0 if self_test() else 1
    if not args.output:
        parser.error("OUTPUT_DIR is required")
    build(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
