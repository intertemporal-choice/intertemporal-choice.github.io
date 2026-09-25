"""Shared code for the book's figure notebooks (content/notebooks/).

Every figure a chapter shows is the output of a labelled cell in one of those notebooks, and
the notebooks import what they share from here: the figure style, and later the solvers and
data readers that more than one chapter needs. `uv sync` installs this package editable into
the book's environment, so it is importable from the notebooks in CI and locally.

`uv run python -m intertemporal_choice --self-test` runs every module's self-test.
"""
