# Build and verification scripts

Run from the repository root with `uv run python code/<script>.py`. The deploy workflow,
`.github/workflows/deploy.yml`, runs each script's `--self-test` before the script itself.

## Two repositories, one workflow

The book is developed in a private repository, `intertemporal-choice.github.io-source`,
and published from a public one, `intertemporal-choice.github.io`. Both run the same
workflow, which configures a preview where one is being built, builds the site with
`myst build --html`, writes the forwarding pages and the robots file, verifies the output
and deploys it to GitHub Pages. Where a site lands follows from its repository's name,
through the workflow's `BASE_URL`:

| repository | site |
|---|---|
| `intertemporal-choice.github.io` (public) | https://intertemporal-choice.github.io, the published book |
| `intertemporal-choice.github.io-source` (private) | https://intertemporal-choice.github.io/intertemporal-choice.github.io-source/, a preview of the next release |

Work happens in pull requests on the source repository; merging one updates the preview
within a few minutes. When the preview looks right, `publish.py` copies the source
repository's `main` into the public one as a single commit, and the public repository's
workflow deploys it. The `dev/` folder never leaves the source repository.

## `publish.py`

Publishes the book: `uv run python code/publish.py -m "what changed"`.

It checks that the checkout is `main`, clean and identical to `origin/main`; clones the
public repository; replaces its tracked files with `git archive HEAD` of this one, which
leaves out `dev/` because `.gitattributes` marks it `export-ignore`; shows what would
change and asks; then commits "Publish YYYY-MM-DD: what changed" and pushes it to `main`.
The public repository's workflow builds, verifies and deploys; if that build fails, the
previous site stays up. `--dry-run` stops before committing. The script refuses to run
from a clone of the public repository.

`--self-test` runs the whole flow against throwaway repositories: a first publication
into an empty repository, an update, a deletion, and each refusal.

## `mark_preview.py`

Runs before `myst build`. When `BASE_URL` names a folder, the build is the preview: this
replaces one comment line of `myst.yml` (`# navbar_end: filled in by
code/mark_preview.py ...`, under `site.parts`) with a `navbar_end` part, so that the theme
puts a banner at the end of the top navbar of every page, linking to the published book.
When `BASE_URL` is empty it leaves `myst.yml` alone and checks that the line is still a
comment, so that a rewritten copy cannot reach the published book. The banner goes in
through the theme because the site is a React app that re-renders the document on load
and drops anything injected into the built HTML; it is a line of `myst.yml` rather than
a file `myst.yml` extends because `extends` does not carry `site.parts`. After a local
preview build, `git checkout myst.yml`.

## `write_robots.py`

Runs after `myst build`. The preview is a folder of the published book's domain, so the
published book's `robots.txt` is the one crawlers read for both: this replaces MyST's
`Allow: /` with a `Disallow` for the preview folder. A preview build's own `robots.txt`,
which crawlers never read, is written to disallow everything.

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
forwarding keeps any `#anchor`, and its target is prefixed with `BASE_URL`, so a
preview's forwarding pages stay on the preview.

When a page moves, add its old path to `redirects.txt`. The script fails the deploy if a
new path is not a page in the build, or if an old path is still a live page, which it
would otherwise overwrite.

## `verify_build.py`

Gates the GitHub Pages deploy on the built output rather than the build's exit code,
because `myst build` exits 0 on a site whose every stylesheet 404s. It checks that
`index.html` carries real content, that every asset path is served from the folder
`BASE_URL` names (and that none carries a repository name when the site is served from
the root), that the expected number of pages were emitted, that the preview banner is on
every page of a preview build and on no page of the published book, that `robots.txt`
carries the right `Disallow` line, and, in GitHub Actions, that `BASE_URL` is what the
repository being built calls for.

`--self-test` runs each check against input it should reject, and fails if any check
passes it. The deploy workflow runs the self-test first, so a check that has quietly
stopped discriminating is caught rather than trusted.
