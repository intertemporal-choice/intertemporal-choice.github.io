"""The book's figure style, and the one-image display every figure cell ends with.

A chapter pulls a figure in with `:::{figure} #nb-<Chapter>-<Figure>`, which embeds the
outputs of the notebook cell carrying that label. MyST turns a cell with more than one output
into subfigures or stray verbatim blocks, so a figure cell must emit exactly one image and
nothing else. `show(fig)` guarantees that: it renders the figure to PNG itself, closes it so
the inline backend cannot display it a second time, and displays the PNG as the cell's only
output. verify_build.py checks the result.

PNG rather than SVG because the LaTeX export includes images with \\includegraphics, which
needs a raster or PDF file; an SVG would need a converter in the PDF build.
"""

import io

import matplotlib
import matplotlib.pyplot as plt

DPI = 200

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
    """Apply the book's rcParams. Call once, in a notebook's first cell."""
    matplotlib.rcParams.update(RC)


def png_bytes(fig) -> bytes:
    """Render a figure to PNG at the book's resolution."""
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=DPI, bbox_inches="tight")
    return buffer.getvalue()


def show(fig) -> None:
    """Display `fig` as the cell's one and only output, then close it."""
    from IPython.display import Image, display

    data = png_bytes(fig)
    plt.close(fig)
    display(Image(data))


def self_test() -> list[str]:
    failures = []
    use_book_style()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    data = png_bytes(fig)
    plt.close(fig)
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        failures.append("style: png_bytes did not produce a PNG")
    if plt.get_fignums():
        failures.append("style: a figure was left open after closing it")
    return failures
