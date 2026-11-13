"""Import a chapter's notebook into another notebook, so that, for example, a problem set's answer key
computes with the chapter's own code rather than a copy of it:

    from intertemporal_choice import chapter
    lucas = chapter.load("asset_pricing/LucasAssetPrice/LucasAssetPrice.ipynb")
    lucas.pd_series(lucas.Economy(), 1.0)

`load` runs the notebook's code cells, in order, in a new module, and returns the module. It skips the
cells a reader is not shown or that need IPython: the checks of the chapter's numbers (tagged
`remove-cell`), the sliders (`skip-execution`), and the cell that installs the package (any cell with
a `%` or `!` line). The figures the notebook draws are closed, and what it prints is discarded. An
error names the notebook and the cell (counting every cell from zero, as nbformat does) and shows
the cell's lines.

Which copy it reads:
- with no `ref`, the nearest: the book's clone when the package runs from one (its working tree,
  whatever branch is checked out); else the folder the notebook is run in, where the book's
  in-browser site keeps its notebooks; else the book's GitHub repository at main;
- with a `ref` (a branch, tag or commit), that version, always from the book's GitHub repository.

`python -m intertemporal_choice --self-test` runs `self_test`.
"""

import contextlib
import io
import json
import linecache
import sys
import types
from pathlib import Path

REPO = "intertemporal-choice/intertemporal-choice.github.io"
ROOT = Path(__file__).resolve().parents[2]  # the book's clone, when the package is installed from one
SKIP_TAGS = {"remove-cell", "skip-execution"}


def _fetch(url):
    """The text at `url`."""
    if "pyodide" in sys.modules:  # in a browser, where Python's own network calls do not work
        from pyodide.http import open_url

        return open_url(url).read()
    from urllib.request import urlopen

    with urlopen(url) as response:
        return response.read().decode("utf-8")


def _read(path, ref):
    """The notebook's text: the nearest copy with no `ref`, or that version from GitHub."""
    if ref is None:
        for candidate in (ROOT / "content" / path, Path(path), Path.cwd() / Path(path).name):
            if candidate.is_file():
                return candidate.read_text(encoding="utf-8")
        ref = "main"
    return _fetch(f"https://raw.githubusercontent.com/{REPO}/{ref}/content/{path}")


def code_cells(notebook):
    """The code cells `load` runs, in order, as (the cell's position in the notebook, its source)."""
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue
        if SKIP_TAGS & set(cell.get("metadata", {}).get("tags", [])):
            continue
        source = "".join(cell["source"])
        if any(line.lstrip().startswith(("%", "!")) for line in source.splitlines()):
            continue
        yield index, source


def load(path, ref=None):
    """Run the chapter notebook at `content/<path>` and return its definitions as a module."""
    import matplotlib.pyplot as plt

    notebook = json.loads(_read(path, ref))
    module = types.ModuleType(Path(path).stem)
    already_open = set(plt.get_fignums())
    try:
        with contextlib.redirect_stdout(io.StringIO()):  # what the chapter's notebook prints stays there
            for index, source in code_cells(notebook):
                name = f"<{path}, cell {index}>"
                lines = source.splitlines(keepends=True)
                linecache.cache[name] = (len(source), None, lines, name)  # so tracebacks show the lines
                exec(compile(source, name, "exec"), module.__dict__)
    finally:
        for figure in set(plt.get_fignums()) - already_open:
            plt.close(figure)
    return module


def self_test() -> list[str]:
    import tempfile
    import traceback

    import matplotlib.pyplot as plt

    failures = []
    cell = lambda source, tags=(): {"cell_type": "code", "metadata": {"tags": list(tags)}, "source": source}
    notebook = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": "# Title"},
            cell("try:\n    import intertemporal_choice\nexcept ImportError:\n    %pip install -q x\n"),
            cell("import numpy as np\n\ndef double(x):\n    return 2 * x\n"),
            cell("import matplotlib.pyplot as plt\n\nfig, ax = plt.subplots()\nax.plot([0, 1])\n"),
            cell("raise AssertionError('a check ran')\n", ["remove-cell"]),
            cell("raise AssertionError('a slider ran')\n", ["skip-execution"]),
            cell("def broken():\n    return 1 / 0\n"),
        ]
    }
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "Synthetic.ipynb"
        path.write_text(json.dumps(notebook), encoding="utf-8")
        before = len(plt.get_fignums())
        try:
            module = load(str(path))
        except Exception as error:  # noqa: BLE001 (a self-test reports, it does not raise)
            failures.append(f"chapter: load ran a cell it should skip, or failed: {error}")
        else:
            if module.double(3) != 6 or module.__name__ != "Synthetic":
                failures.append("chapter: load does not return the notebook's definitions as a module")
            if len(plt.get_fignums()) != before:
                failures.append("chapter: load leaves the notebook's figures open")
            try:
                module.broken()
            except ZeroDivisionError as error:
                frame = traceback.extract_tb(error.__traceback__)[-1]
                if not frame.filename.endswith(", cell 6>") or frame.line != "return 1 / 0":
                    failures.append(f"chapter: an error does not name its cell and line: {frame.filename} {frame.line!r}")

    global _fetch
    fetch, asked = _fetch, []
    _fetch = lambda url: asked.append(url) or "{}"
    try:
        _read("asset_pricing/LucasAssetPrice/LucasAssetPrice.ipynb", "some-branch")
    finally:
        _fetch = fetch
    if asked != [f"https://raw.githubusercontent.com/{REPO}/some-branch/content/asset_pricing/LucasAssetPrice/LucasAssetPrice.ipynb"]:
        failures.append(f"chapter: load with a ref does not read that version from GitHub: {asked}")
    return failures
