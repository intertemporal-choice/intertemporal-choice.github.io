"""Assert the built site is servable before it is published.

`myst build` exits 0 on a site whose every stylesheet 404s. That happened on 2026-09-09:
the repository moved to `<org>.github.io`, which serves from the domain root, while
`BASE_URL` still carried the old project-site prefix. Every asset path was one directory
too deep, the build reported success, and the deployed page rendered unstyled with MyST's
own "Site not loading correctly?" banner.

So the deploy gate cannot be the build's exit code. This checks the output instead:

  1. index.html exists and carries real content
  2. no asset path is prefixed with the repository name, which is the signature of a
     BASE_URL meant for a project site being used on a root-served one
  3. the expected number of pages were emitted
  4. every page MyST records as a notebook (an .ipynb, or a .md with a `kernelspec`)
     shows at least one cell output; a build run without `--execute` omits them all and
     still exits 0 under `--strict`

`--self-test` runs every check against synthetic bad input and fails if any check passes
it, so a check that has silently stopped discriminating is caught rather than trusted.

Usage: uv run python code/verify_build.py [--self-test]
"""

import argparse
import json
import logging
import re
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BUILD = Path("_build/html")
# MyST's per-page records: source `location`, URL `slug`, and `kind` ("Notebook"/"Article").
# Records of pages since removed stay on disk, so config.json decides which are current.
PAGES = Path("_build/site/content")
REPO_SLUG = "intertemporal-choice.github.io"
MIN_BYTES = 2000
MIN_PAGES = 40

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')
OUTPUT = re.compile(r'data-name="safe-output-[a-z]+"')


def bad_prefixes(html: str, slug: str) -> list[str]:
    """Asset paths that start with the repository name, one directory too deep."""
    return sorted({p for p in ASSET.findall(html) if p.startswith(f"/{slug}/")})


def current_slugs(pages: Path) -> set[str]:
    config = pages.parent / "config.json"
    if not config.exists():
        return set()
    projects = json.loads(config.read_text())["projects"]
    return {p["slug"] for project in projects for p in project["pages"] if "slug" in p}


def notebook_pages(pages: Path) -> dict[str, Path]:
    """Source path of each current notebook page, mapped to its HTML file."""
    current, found = current_slugs(pages), {}
    for record in sorted(pages.glob("*.json")):
        page = json.loads(record.read_text())
        if page.get("kind") == "Notebook" and page["slug"] in current:
            found[page["location"]] = Path(*page["slug"].split("."), "index.html")
    return found


def missing_outputs(page: Path) -> list[str]:
    """An executed page shows at least one cell output."""
    if not page.exists():
        return [f"{page} does not exist"]
    if not OUTPUT.search(page.read_text(errors="ignore")):
        return [f"{page} shows no cell output: built without --execute?"]
    return []


def unexecuted(build: Path, pages: Path) -> list[str]:
    notebooks = notebook_pages(pages)
    if not notebooks:
        return [f"no notebook page recorded under {pages}"]
    return [f for html in notebooks.values() for f in missing_outputs(build / html)]


def check(build: Path, slug: str, pages: Path = PAGES) -> list[str]:
    failures = []

    index = build / "index.html"
    if not index.exists():
        return [f"{index} does not exist"]

    html = index.read_text(errors="ignore")
    if len(html) < MIN_BYTES:
        failures.append(f"index.html is {len(html)} bytes, under the {MIN_BYTES} floor")

    stale = bad_prefixes(html, slug)
    if stale:
        failures.append(
            f"{len(stale)} asset paths prefixed with /{slug}/, e.g. {stale[0]}"
        )

    built = list(build.rglob("*.html"))
    if len(built) < MIN_PAGES:
        failures.append(
            f"only {len(built)} html pages built, under the {MIN_PAGES} floor"
        )

    failures.extend(unexecuted(build, pages))
    return failures


def self_test_site() -> list[str]:
    errors = []
    if not bad_prefixes(f'<a href="/{REPO_SLUG}/build/app.css">', REPO_SLUG):
        errors.append("stale-prefix check did not fire on a stale prefix")
    if bad_prefixes('<a href="/build/app.css">', REPO_SLUG):
        errors.append("stale-prefix check fired on a correct root path")
    if not check(Path("/nonexistent"), REPO_SLUG):
        errors.append("missing-index check did not fire")
    return errors


def self_test_execution(tmp: Path) -> list[str]:
    errors = []
    records = tmp / "site" / "content"
    records.mkdir(parents=True)
    listed = [{"slug": "content.periodx"}, {"slug": "content.b"}, {"title": "part"}]
    (tmp / "site" / "config.json").write_text(
        json.dumps({"projects": [{"pages": listed}]})
    )
    for name, kind, slug in [
        ("a", "Notebook", "content.periodx"),
        ("b", "Article", "content.b"),
        ("stale", "Notebook", "content.removed"),
    ]:
        record = {"kind": kind, "location": f"/{name}.md", "slug": slug}
        (records / f"{name}.json").write_text(json.dumps(record))
    if notebook_pages(records) != {"/a.md": Path("content/periodx/index.html")}:
        errors.append("notebook_pages did not pick out exactly the current notebook")
    empty = tmp / "empty"
    empty.mkdir()
    if unexecuted(tmp, empty) != [f"no notebook page recorded under {empty}"]:
        errors.append("an empty set of notebook pages passed")
    page = tmp / "index.html"
    page.write_text('<pre>import numpy as np</pre><div data-name="outputs-container">')
    if not missing_outputs(page):
        errors.append("output check did not fire on an unexecuted page")
    page.write_text('<div data-name="safe-output-stream">a_1 is 0.78</div>')
    if missing_outputs(page):
        errors.append("output check fired on an executed page")
    return errors


def self_test() -> bool:
    """Every check must reject input it is supposed to reject."""
    with tempfile.TemporaryDirectory() as tmp:
        errors = self_test_site() + self_test_execution(Path(tmp))
    for e in errors:
        log.error("SELF-TEST FAIL: %s", e)
    log.info("self-test %s", "FAILED" if errors else "passed")
    return not errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    problems = check(BUILD, REPO_SLUG)
    for p in problems:
        log.error("FAIL: %s", p)
    if problems:
        sys.exit(1)
    log.info("built site looks servable: index.html ok, asset paths root-relative")
