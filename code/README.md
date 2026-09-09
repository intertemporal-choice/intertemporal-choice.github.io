# Build and verification scripts

Run from the repository root with `uv run python code/<script>.py`.

## `mirror_check.py`

Reconciles `sources/` against Carroll's lecture-notes page at econ2.jhu.edu.

`sources/` is a mirror of the per-handout source zips published alongside the notes,
because the zip holds the real LaTeX and the PDF is only its rendering. The script lists
every handout on every section index, reports whether the mirror has it and whether a
source zip exists, and exits non-zero when anything is missing. `--fetch` downloads and
extracts whatever is absent.

Verified 2026-08-23: 46 of the 47 handouts then in `sources/` were byte-identical (md5)
to the `LaTeX/<stem>.tex` inside their source zip.

## `execute_fisher_inplace.py`

Re-executes `content/consumption/FisherTwoPeriod.ipynb` in place so its stored outputs
and ipywidgets state match the current source. Run it after changing any cell in that
notebook, or the stored figures go stale.

## `verify_fisher_tangency.py`

Checks the notebook's plotted optimum against the closed form on both conditions the
figures assert: the point lies on the drawn budget line, and it satisfies the Euler
equation.

It evaluates the corrected rule (`MPCmin * W`) and the original one (`cFunc(W)`)
side by side, so the check is shown to reject the code it replaced rather than merely
passing on the new. HARK's `cFunc` is normalized by permanent income and credits the
agent with a unit of terminal-period income the hand-drawn budget constraint omits,
which is why applying the MPC to drawn wealth is what restores tangency.
