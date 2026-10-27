"""Build the in-browser copies of the figure notebooks: a JupyterLite site, served at /lite/.

JupyterLite runs Python in the browser (Pyodide), so a reader opens a notebook and runs it
with nothing installed and no server, e.g.
https://intertemporal-choice.github.io/lite/notebooks/index.html?path=Fisher2Period.ipynb

Only notebooks whose packages Pyodide has can go here: numpy, matplotlib and ipywidgets are
enough for those in NOTEBOOKS. HARK cannot run in a browser (it needs numba), so a notebook that
uses it stays with Colab and Binder.

Each notebook is published as the book has it, with three changes the browser needs:

  - the frontmatter cell, which MyST reads and Jupyter would show as a stray heading, becomes
    the page's title;
  - the book's package, `intertemporal_choice`, is copied beside the notebooks. It is pure
    Python, so `import intertemporal_choice` succeeds;
  - the bootstrap cell, whose `%pip install` from GitHub Pyodide cannot do, becomes one that
    installs ipywidgets from PyPI, which Pyodide lacks.

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
BROWSER_BOOTSTRAP = """\
# In the browser (JupyterLite): the book's package is beside this notebook, and the sliders'
# package comes from PyPI.
%pip install -q ipywidgets"""
FRONTMATTER = re.compile(r"\A\s*---\n(.*?)\n---\s*\Z", re.S)
TITLE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M)


def for_the_browser(nb: dict) -> dict:
    """The notebook with its frontmatter cell made a title, and its bootstrap cell the browser's."""
    cells = nb.get("cells") or []
    code = [c for c in cells if c.get("cell_type") == "code"]
    if code and "import intertemporal_choice" in "".join(code[0].get("source", "")):
        code[0]["source"] = BROWSER_BOOTSTRAP
        code[0]["outputs"], code[0]["execution_count"] = [], None
    if cells and cells[0].get("cell_type") in ("markdown", "raw"):
        text = "".join(cells[0].get("source", ""))
        m = FRONTMATTER.match(text)
        if m:
            title = TITLE.search(m.group(1))
            name = title.group(1).removeprefix("Figures: ") if title else ""
            cells[0] = {"cell_type": "markdown", "id": cells[0].get("id", "title"), "metadata": {},
                        "source": f"# {name}" if name else ""}
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
        subprocess.run(
            ["jupyter", "lite", "build", "--contents", str(contents), "--output-dir", str(output.resolve()),
             "--no-sourcemaps"],
            cwd=CONFIG, check=True,
        )
    log.info("JupyterLite site with %d notebooks in %s", len(NOTEBOOKS), output)


def self_test() -> bool:
    nb = {"cells": [
        {"cell_type": "markdown", "id": "a", "metadata": {},
         "source": '---\ntitle: "Figures: The Fisher Two-Period Problem"\nexecute:\n  depends_on_env: [IC_EXEC_ENV]\n---'},
        {"cell_type": "code", "id": "b", "metadata": {}, "outputs": [], "execution_count": None,
         "source": "try:\n    import intertemporal_choice\nexcept ImportError:\n    %pip install -q git+https://example"},
        {"cell_type": "code", "id": "c", "metadata": {}, "source": "x = 1", "outputs": [], "execution_count": None},
    ]}
    out = for_the_browser(json.loads(json.dumps(nb)))
    failures = []
    if out["cells"][0]["source"] != "# The Fisher Two-Period Problem":
        failures.append(f"frontmatter became {out['cells'][0]['source']!r}")
    if out["cells"][1]["source"] != BROWSER_BOOTSTRAP:
        failures.append("the bootstrap cell was not replaced by the browser's")
    if out["cells"][2] != nb["cells"][2]:
        failures.append("a cell after the bootstrap changed")
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
