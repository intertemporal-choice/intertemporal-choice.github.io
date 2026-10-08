# Build and verification scripts

Run from the repository root with `uv run python code/<script>.py`.

## Figures come from notebooks

Everything to do with a chapter lives in its folder, and can be downloaded as one unit:

```
content/consumption/Envelope/
  index.md              the chapter; its figures are relative links, figures/<name>.png
  Envelope.ipynb        draws the figures; a page of the site, listed under the chapter
  figures/Envelope.png  committed, and checked against a fresh drawing whenever the notebook runs
```

The chapter is `index.md` so that its address stays `/content/consumption/envelope`. The
notebook is a plain `.ipynb`, committed **with** its outputs, so GitHub, Colab and a
downloaded copy show the figures. Its first code cell installs the book's own package
(which brings econ-ark, numpy and matplotlib) if it is missing, so it runs anywhere with
`pip`; inside the book's environment that cell does nothing. Every figure cell ends with
`style.save(fig, "<name>")`, from the shared `intertemporal_choice` package in `src/`,
which writes `figures/<name>.png` deterministically (no version or date metadata, fixed
size and resolution) and shows the same bytes as the cell's output.

The build runs a notebook only when its cell code or the environment changed, and then
compares what it drew with the committed files: a figure that differs beyond a pixel or
two of antialiasing fails the build, which is how a notebook edited without its figures
being re-run and committed is caught. A static image is allowed only while it is listed
in `figure_exemptions.txt`, as `pending` (not yet ported) or `exception` (data that cannot
be obtained).

Once per clone, run `uv run python code/notebooks.py --install`: it sets up the git filter
that strips the metadata Jupyter rewrites on every save, so opening a notebook and saving
it leaves nothing to commit.

## `build_site.py`

Runs `myst build --execute` (default `--html --strict`) against a Jupyter server it starts
itself, because MyST's own launcher times out on this book. It sets `IC_EXEC_ENV`, a hash of
`uv.lock`, `src/` and `data/`, which each notebook declares in `execute: depends_on_env`, so
MyST's execution cache in `_build/execute` is invalidated when the code or data a notebook
uses changes, not only when its cells do. A preflight lint refuses a notebook that is not
`content/<part>/<Chapter>/<Chapter>.ipynb` beside its chapter, lacks the python3 kernel or
that declaration, does not begin with the bootstrap cell, or whose saved figures are not
exactly the files in its `figures/` folder. `--print-env-hash` prints the hash CI keys its
cache on.

## `notebooks.py`

The one place that says how notebooks are stripped: outputs and cell ids kept, execution
counts, timings and the Python version dropped. `--install` sets nbstripout up as a git
filter in the clone; `--check` fails if a tracked notebook is committed unstripped (the
workflow runs it); `--strip` strips the tracked notebooks in place.

## `mirror_check.py`

Reconciles `sources/` against Carroll's lecture-notes page at econ2.jhu.edu.

`sources/` is a mirror of the per-handout source zips published alongside the notes,
because the zip holds the real LaTeX and the PDF is only its rendering. The script lists
every handout on every section index, reports whether the mirror has it and whether a
source zip exists, and exits non-zero when anything is missing. `--fetch` downloads and
extracts whatever is absent.

Verified 2026-08-23: 46 of the 47 handouts then in `sources/` were byte-identical (md5)
to the `LaTeX/<stem>.tex` inside their source zip.

## `build_pdf.py`

Builds `exports/intertemporal-choice.pdf`. Use it instead of a bare `myst build --pdf`.

MyST exports every link to another page as a site-relative `\href{/content/...}`, which
goes nowhere in a PDF, and drops links to Math Facts entries altogether. The script
builds from a staged copy in `_build/pdf-src`, points those links at the published site
(`https://intertemporal-choice.github.io/...`, with the fact's anchor), and fails if any
link names a page the book does not have. The Markdown keeps its `#label` links, so the
website's cross-references stay internal and follow pages when they move.

Links into Supplemental Notes, which the PDF omits, work the same way. They resolve
once the site carrying those pages has been deployed.

`--self-test` checks the link rewriting, and the reimplementation of MyST's URL and
anchor slugs, against cases they must handle.

## `write_redirects.py`

Writes a forwarding page at each old URL listed in `redirects.txt`, so links to a page
that has been renamed or moved land on its new address instead of a 404. GitHub Pages
has no server-side redirects, so the deploy workflow runs this after `myst build`. The
forwarding keeps any `#anchor`.

When a page moves, add its old path to `redirects.txt`. The script fails the deploy if a
new path is not a page in the build, or if an old path is still a live page, which it
would otherwise overwrite.

## `verify_build.py`

Gates the GitHub Pages deploy on the built output rather than the build's exit code,
because `myst build` exits 0 on a site whose every stylesheet 404s. It checks that
`index.html` carries real content, that no asset path is prefixed with the repository
name (the signature of a project-site `BASE_URL` on a root-served site), and that the
expected number of pages were emitted.

It also enforces the figures-from-notebooks rule on the built pages: every figure is one
image, either `figures/<name>.png` beside a chapter that has its notebook or a static
image listed in `figure_exemptions.txt`; every exemption is in use and every file under
`content/figures/` is listed; every notebook sits beside its chapter, is listed under it
in `toc.yml`, and carries outputs; and no committed figure differs from what its notebook
drew in this build beyond the tolerance.

`--self-test` runs each check against input it should reject, and fails if any check
passes it. The deploy workflow runs the self-test first, so a check that has quietly
stopped discriminating is caught rather than trusted.

## `check_planned.py`

Lists planned changes, meaning deferred rulings to apply to some material once a trigger fires,
and says which are due. Triggers are a year, a pull request merging, or a page going live. The
book's markers live in `dev/planned.md`, not in `content/`, because MyST publishes comments in a
page's JSON and HTML. The workflow runs `--self-test` and then a report-only check, so a due
marker shows up as a warning on the run without blocking the deploy.

This is the only copy. The questions repository's posting tools fetch it from here by a pinned
commit and run it with `--root` set to their own folder, so it uses only the standard library and
`gh`. Its docstring defines the marker syntax, the triggers and the exit codes.
