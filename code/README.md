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

## `verify_build.py`

Gates the GitHub Pages deploy on the built output rather than the build's exit code,
because `myst build` exits 0 on a site whose every stylesheet 404s. It checks that
`index.html` carries real content, that no asset path is prefixed with the repository
name (the signature of a project-site `BASE_URL` on a root-served site), and that the
expected number of pages were emitted.

`--self-test` runs each check against input it should reject, and fails if any check
passes it. The deploy workflow runs the self-test first, so a check that has quietly
stopped discriminating is caught rather than trusted.
