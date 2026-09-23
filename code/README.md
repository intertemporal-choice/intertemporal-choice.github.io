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

## `build_site.py`

Builds the site with `myst build --execute`, which runs every page whose frontmatter
declares a `kernelspec` in this repository's uv environment. The first such page,
`content/consumption/KeynesFriedmanModigliani.md`, needs HARK, statsmodels, and a live
FRED download. Pass `myst build` options through, for example `--pdf`; the default is
`--html --strict`.

It starts its own Jupyter server and hands MyST the address in `JUPYTER_BASE_URL` and
`JUPYTER_TOKEN`. When MyST launches the server itself (mystmd 1.10.1 and 1.11.0), the
build fails with "Jupyter server did not respond" and leaves that server running.

## `verify_build.py`

Gates the GitHub Pages deploy on the built output rather than the build's exit code,
because `myst build` exits 0 on a site whose every stylesheet 404s. It checks that
`index.html` carries real content, that no asset path is prefixed with the repository
name (the signature of a project-site `BASE_URL` on a root-served site), that the
expected number of pages were emitted, and that every page MyST records as a notebook (an
`.ipynb`, or a `.md` with a `kernelspec`) shows at least one cell output. A build run without `--execute` exits 0 under `--strict` with no
outputs at all.

`--self-test` runs each check against input it should reject, and fails if any check
passes it. The deploy workflow runs the self-test first, so a check that has quietly
stopped discriminating is caught rather than trusted.
