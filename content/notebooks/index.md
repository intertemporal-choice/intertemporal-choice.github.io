(sec:FigureNotebooks)=
# Figure Notebooks

Every figure in the book is drawn by the code in these notebooks, one per chapter. The
site and the PDF are built by running them, so each figure is exactly what its notebook
produces today, and changing a parameter here changes the figure there.

To run a notebook yourself, clone the book's repository and install its environment with
[uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/intertemporal-choice/intertemporal-choice.github.io
cd intertemporal-choice.github.io
uv sync
uv run jupyter lab
```

The notebooks are stored as MyST Markdown. In JupyterLab, open one with
*Open With > Jupytext Notebook* to run it cell by cell. Code that several notebooks share
lives in the `intertemporal_choice` package in the repository's `src/` folder.
