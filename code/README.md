# Build and verification scripts

Run from the repository root with `uv run python code/<script>.py`.

## Figures come from notebooks

Every figure a chapter shows is the output of a labelled cell in a notebook under
`content/notebooks/`, one MyST-markdown notebook per chapter. The chapter embeds it with
`:::{figure} #nb-<Chapter>-<Figure>`, keeping the figure's `:name:` label and caption.
Shared code lives in the `intertemporal_choice` package (`src/`), which `uv sync` installs.
A static image is allowed only while it is listed in `figure_exemptions.txt`, either as
`pending` (not yet ported) or as an `exception` (data that cannot be obtained);
`verify_build.py` fails the build on anything else.

Build the site with `uv run python code/build_site.py`, not a bare `myst build`: the
notebooks must be executed for the figures to exist.

## `build_site.py`

Runs `myst build --execute` (default `--html --strict`) against a Jupyter server it starts
itself, because MyST's own launcher times out on this book. It sets `IC_EXEC_ENV`, a hash of
`uv.lock`, `src/` and `data/`, which each notebook declares in `execute: depends_on_env`, so
MyST's execution cache in `_build/execute` is invalidated when the code or data a notebook
uses changes, not only when its cells do. A preflight lint refuses a notebook without that
declaration or the python3 kernel, and a figure cell tagged to hide its output (hidden
outputs are dropped from the PDF). `--root DIR` builds another tree; `build_pdf.py` uses it
for its staged copy. `--print-env-hash` prints the hash CI keys its cache on.

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

The staged build runs through `build_site.py`, so the PDF's figures are the notebooks'
outputs too. It carries `_build/execute` into the stage and passes the original tree's
`IC_EXEC_ENV`, so after an HTML build nothing is executed again. It then checks that every
figure in the generated LaTeX includes an image file that exists.

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

It also enforces the figures-from-notebooks rule. MyST builds an embed whose label matches
no notebook cell, even under `--strict`, into a figure showing only its caption, so the
check reads the built pages instead: every figure must embed exactly one image output, or
be a static image listed in `figure_exemptions.txt`. It also requires that every exemption
is in use, that every file under `content/figures/` is listed, and that each notebook in
`toc.yml` was built as a notebook and carries outputs.

`--self-test` runs each check against input it should reject, and fails if any check
passes it. The deploy workflow runs the self-test first, so a check that has quietly
stopped discriminating is caught rather than trusted.
