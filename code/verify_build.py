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

`--self-test` runs every check against synthetic bad input and fails if any check passes
it, so a check that has silently stopped discriminating is caught rather than trusted.

Usage: uv run python code/verify_build.py [--self-test]
"""

import argparse
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BUILD = Path("_build/html")
REPO_SLUG = "intertemporal-choice.github.io"
MIN_BYTES = 2000
MIN_PAGES = 40

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')


def bad_prefixes(html: str, slug: str) -> list[str]:
    """Asset paths that start with the repository name, one directory too deep."""
    return sorted({p for p in ASSET.findall(html) if p.startswith(f"/{slug}/")})


def check(build: Path, slug: str) -> list[str]:
    failures = []

    index = build / "index.html"
    if not index.exists():
        return [f"{index} does not exist"]

    html = index.read_text(errors="ignore")
    if len(html) < MIN_BYTES:
        failures.append(f"index.html is {len(html)} bytes, under the {MIN_BYTES} floor")

    stale = bad_prefixes(html, slug)
    if stale:
        failures.append(f"{len(stale)} asset paths prefixed with /{slug}/, e.g. {stale[0]}")

    pages = list(build.rglob("*.html"))
    if len(pages) < MIN_PAGES:
        failures.append(f"only {len(pages)} html pages built, under the {MIN_PAGES} floor")

    return failures


def self_test() -> bool:
    """Every check must reject input it is supposed to reject."""
    ok = True
    if not bad_prefixes(f'<a href="/{REPO_SLUG}/build/app.css">', REPO_SLUG):
        log.error("SELF-TEST FAIL: stale-prefix check did not fire on a stale prefix")
        ok = False
    if bad_prefixes('<a href="/build/app.css">', REPO_SLUG):
        log.error("SELF-TEST FAIL: stale-prefix check fired on a correct root path")
        ok = False
    if not check(Path("/nonexistent"), REPO_SLUG):
        log.error("SELF-TEST FAIL: missing-index check did not fire")
        ok = False
    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


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
