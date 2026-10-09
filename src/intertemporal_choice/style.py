"""The book's figure style, and `save`, which every figure cell ends with.

A chapter keeps its figures as files in the `figures/` folder beside it, drawn by the
notebook in the same folder. `save(fig, name)` writes `figures/<name>.png` and shows the
same bytes as the cell's one and only output, so the notebook's committed output and the
file the chapter uses are one picture. It closes the figure so the inline backend cannot
display it a second time. The figures are committed, and the build compares what a
re-run draws with what is committed, so the file must be the same bytes whenever the
picture is the same:

  - matplotlib's default PNG metadata carries its own version, which would change every
    file on every upgrade; `save` strips it (nothing else in a PNG varies);
  - the size and resolution are fixed here, not left to the notebook's environment.

`figures/` is resolved from the working directory, which Jupyter and the build both set to
the notebook's folder. PNG rather than SVG because the LaTeX export includes images with
\\includegraphics, which needs a raster or PDF file; an SVG would need a converter.
"""

import io
import re
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

DPI = 200
FOLDER = "figures"
NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")

RC = {
    "figure.figsize": (6.4, 4.0),
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
    "lines.linewidth": 1.8,
    "text.usetex": False,
}


def use_book_style() -> None:
    """Apply the book's rcParams. Call once, after the imports."""
    matplotlib.rcParams.update(RC)


def png_bytes(fig) -> bytes:
    """Render a figure to PNG at the book's resolution, with no varying metadata."""
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=DPI, bbox_inches="tight", metadata={"Software": None})
    return buffer.getvalue()


def save(fig, name: str, folder: str | Path = FOLDER) -> None:
    """Write `<folder>/<name>.png`, show it as the cell's only output, close `fig`.

    Returns nothing, so that a cell ending in `style.save(...)` has the image as its only
    output and no echoed value beside it.
    """
    if not NAME.match(name):
        raise ValueError(f"figure name {name!r}: letters, digits, - and _ only")
    data = png_bytes(fig)
    plt.close(fig)
    path = Path(folder) / f"{name}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    try:
        from IPython import get_ipython
        from IPython.display import Image, display
    except ImportError:
        return
    if get_ipython() is not None:  # in a notebook: the figure is the cell's one output
        display(Image(data))


def self_test() -> list[str]:
    import tempfile

    failures = []
    use_book_style()

    def draw():
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1], label="line")
        ax.set_title("t")
        ax.legend()
        return fig

    first, second = png_bytes(draw()), png_bytes(draw())
    plt.close("all")
    if not first.startswith(b"\x89PNG\r\n\x1a\n"):
        failures.append("style: png_bytes did not produce a PNG")
    if first != second:
        failures.append("style: two renders of the same figure differ")
    if b"Software" in first or b"Matplotlib" in first:
        failures.append("style: the PNG carries matplotlib's version metadata")
    with tempfile.TemporaryDirectory() as tmp:
        if save(draw(), "Test", tmp) is not None:
            failures.append("style: save returned a value, which a notebook cell would echo")
        path = Path(tmp) / "Test.png"
        if not path.is_file() or path.read_bytes() != first:
            failures.append("style: save did not write the rendered bytes to <folder>/<name>.png")
        if plt.get_fignums():
            failures.append("style: a figure was left open after save")
        for bad in ("a b", "../x", "", ".hidden"):
            try:
                save(draw(), bad, tmp)
                failures.append(f"style: save accepted the name {bad!r}")
            except ValueError:
                plt.close("all")
    return failures
