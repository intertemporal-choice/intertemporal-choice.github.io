"""Shared code for the book's figure notebooks.

Every figure a chapter shows is drawn by the notebook beside it,
content/<part>/<Chapter>/<Chapter>.ipynb, into the chapter's figures/ folder, and the
notebooks import what they share from here: the figure style and `style.save`, and later
the solvers and data readers that more than one chapter needs. A chapter's own drawing code can
live here too, as `fisher` does, so that its notebook shows the economics and not the plotting. `uv sync` installs this
package editable into the book's environment; a downloaded notebook installs it from GitHub
with pip in its first cell.

`uv run python -m intertemporal_choice --self-test` runs every module's self-test.
"""
