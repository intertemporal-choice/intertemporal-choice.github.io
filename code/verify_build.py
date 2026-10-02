"""Assert the built site is servable before it is published.

`myst build` exits 0 on a site whose every stylesheet 404s. That happened on 2026-09-09:
the repository moved to `<org>.github.io`, which serves from the domain root, while
`BASE_URL` still carried the old project-site prefix. Every asset path was one directory
too deep, the build reported success, and the deployed page rendered unstyled with MyST's
own "Site not loading correctly?" banner.

So the deploy gate cannot be the build's exit code. This checks the output instead:

  1. index.html exists and carries real content
  2. every root-absolute asset path starts with `BASE_URL`, the folder the site is served
     from: `/intertemporal-choice.github.io-source` for the preview that the private source
     repository builds, empty for the published book, whose paths must then NOT carry a
     repository name (the signature of a project-site BASE_URL on a root-served site)
  3. the expected number of pages were emitted, not counting the forwarding pages that
     code/write_redirects.py adds for moved URLs
  4. the preview banner that code/mark_preview.py configures is on every page of a
     preview build and on no page of the published book, and robots.txt carries the
     Disallow line that code/write_robots.py writes for the build in hand
  5. in GitHub Actions, `BASE_URL` is what the repository being built calls for, derived
     again from `GITHUB_REPOSITORY`, so a mistake in the workflow's expression cannot
     deploy a site whose paths point at the wrong folder

`--self-test` runs every check against synthetic bad input and fails if any check passes
it, so a check that has silently stopped discriminating is caught rather than trusted.

Usage: BASE_URL=... python code/verify_build.py [--self-test]
"""

import argparse
import logging
import os
import re
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BUILD = Path("_build/html")
# The published book's repository. On a root-served site, a path starting with a repository
# name is a project-site prefix that should not be there.
REPO_SLUG = "intertemporal-choice.github.io"
MIN_BYTES = 2000
MIN_PAGES = 40

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')
REFRESH = re.compile(r'<meta http-equiv="refresh"', re.IGNORECASE)
# The preview banner's text, as code/mark_preview.py configures it, and the line that
# code/write_robots.py puts into the published book's robots.txt.
MARKER = "Preview of the next release"
PREVIEW_FOLDER = f"/{REPO_SLUG}-source/"


def disallow_line(base: str) -> str:
    return "Disallow: /" if base else f"Disallow: {PREVIEW_FOLDER}"


def bad_prefixes(html: str, base: str) -> list[str]:
    """Root-absolute asset paths served from the wrong folder.

    With a BASE_URL, every path must start with it. Without one, no path may start with a
    repository name.
    """
    paths = set(ASSET.findall(html))
    if base:
        return sorted(p for p in paths if p != base and not p.startswith(base + "/"))
    return sorted(p for p in paths if p.startswith(f"/{REPO_SLUG}"))


def is_redirect(html: str) -> bool:
    """A forwarding page written by code/write_redirects.py, which is not a page of the book."""
    return bool(REFRESH.search(html))


def is_marked(html: str) -> bool:
    return MARKER in html


def expected_base(repository: str | None) -> str | None:
    """The BASE_URL the repository GitHub Actions is building calls for; None outside Actions.

    The workflow derives BASE_URL from the repository's name. This derives it again,
    independently, so that a mistake in the workflow's expression fails the build here
    instead of deploying a site whose paths point at the wrong folder.
    """
    if not repository:
        return None
    name = repository.rsplit("/", 1)[-1]
    return "" if name == REPO_SLUG else f"/{name}"


def check(build: Path, base: str, repository: str | None = None) -> list[str]:
    failures = []

    expected = expected_base(repository)
    if expected is not None and expected != base:
        failures.append(
            f"BASE_URL is {base!r}, but the site of {repository} is served from "
            f"{expected or 'the domain root'}"
        )

    index = build / "index.html"
    if not index.exists():
        return [f"{index} does not exist"]

    html = index.read_text(errors="ignore")
    if len(html) < MIN_BYTES:
        failures.append(f"index.html is {len(html)} bytes, under the {MIN_BYTES} floor")

    pages = {}
    for path in build.rglob("*.html"):
        text = path.read_text(errors="ignore")
        if not is_redirect(text):
            pages[path] = text
    if len(pages) < MIN_PAGES:
        failures.append(
            f"only {len(pages)} html pages built, under the {MIN_PAGES} floor"
        )

    stale = sorted({p for text in pages.values() for p in bad_prefixes(text, base)})
    if stale:
        where = f"under {base}/" if base else "at the domain root"
        failures.append(
            f"{len(stale)} asset paths not served {where}, e.g. {stale[0]}"
        )

    marked = sorted(path for path, text in pages.items() if is_marked(text))
    if base and len(marked) != len(pages):
        failures.append(
            f"a preview build, but only {len(marked)} of {len(pages)} pages carry the "
            "preview marker"
        )
    if not base and marked:
        failures.append(
            f"the published book, but {len(marked)} pages carry the preview marker, "
            f"e.g. {marked[0]}"
        )

    robots = build / "robots.txt"
    wanted = disallow_line(base)
    if not robots.exists() or wanted not in robots.read_text().splitlines():
        failures.append(f"robots.txt lacks the line {wanted!r} (see code/write_robots.py)")

    return failures


def synthetic_site(root: Path, base: str, marked: bool) -> None:
    """A build that passes every check for `base`, plus one forwarding page."""
    tag = f"<div>{MARKER}; the published book is at ...</div>" if marked else ""
    page = (
        f'<html><head><link href="{base}/build/app.css"></head>'
        f"<body>{tag}<p>{'x' * MIN_BYTES}</p></body></html>"
    )
    (root / "index.html").write_text(page)
    (root / "robots.txt").write_text(f"User-agent: *\n{disallow_line(base)}\n")
    for i in range(MIN_PAGES):
        (root / f"p{i}").mkdir()
        (root / f"p{i}" / "index.html").write_text(page)
    (root / "old").mkdir()
    (root / "old" / "index.html").write_text(
        '<meta http-equiv="refresh" content="0; url=/p0">'
    )


def self_test() -> bool:
    """Every check must reject input it is supposed to reject."""
    ok = True

    def expect(condition: bool, failure: str) -> None:
        nonlocal ok
        if not condition:
            log.error("SELF-TEST FAIL: %s", failure)
            ok = False

    preview = f"/{REPO_SLUG}-source"
    expect(
        bad_prefixes(f'<a href="/{REPO_SLUG}/build/app.css">', "") != [],
        "stale-prefix check did not fire on a project-site prefix at the root",
    )
    expect(
        bad_prefixes(f'<a href="{preview}/build/app.css">', "") != [],
        "stale-prefix check did not fire on the preview's prefix at the root",
    )
    expect(
        bad_prefixes('<a href="/build/app.css">', "") == [],
        "stale-prefix check fired on a correct root path",
    )
    expect(
        bad_prefixes('<a href="/build/app.css">', preview) != [],
        "prefix check did not fire on a root path in a preview build",
    )
    expect(
        bad_prefixes(f'<a href="{preview}/build/app.css"><a href="{preview}">', preview)
        == [],
        "prefix check fired on a correct preview path",
    )
    expect(
        disallow_line("") == "Disallow: /intertemporal-choice.github.io-source/"
        and disallow_line(preview) == "Disallow: /",
        "the robots.txt lines are not what code/write_robots.py writes",
    )
    expect(
        is_redirect('<meta http-equiv="refresh" content="0; url=/content/numerical">'),
        "a forwarding page was counted as a page of the book",
    )
    expect(
        not is_redirect('<meta charset="utf-8"><title>Envelope</title>'),
        "a page of the book was taken for a forwarding page",
    )
    expect(check(Path("/nonexistent"), "") != [], "missing-index check did not fire")

    public = f"intertemporal-choice/{REPO_SLUG}"
    expect(expected_base(None) is None, "a build outside Actions was held to a BASE_URL")
    expect(expected_base(public) == "", "the public repository is not served from the root")
    expect(
        expected_base(f"{public}-source") == preview,
        "the source repository is not served from its own folder",
    )

    with tempfile.TemporaryDirectory() as tmp:
        for base, marked, should_pass in [
            ("", False, True),
            (preview, True, True),
            ("", True, False),
            (preview, False, False),
        ]:
            site = Path(tmp) / f"{'preview' if base else 'root'}-{marked}"
            site.mkdir()
            synthetic_site(site, base, marked)
            problems = check(site, base)
            expect(
                (problems == []) == should_pass,
                f"a {'preview' if base else 'root'} build "
                f"{'with' if marked else 'without'} the marker was "
                f"{'rejected' if should_pass else 'accepted'}: {problems}",
            )
        wrong = Path(tmp) / "wrong-folder"
        wrong.mkdir()
        synthetic_site(wrong, preview, True)
        expect(
            check(wrong, "") != [] and check(wrong, "/elsewhere") != [],
            "a build for one folder passed the check for another",
        )
        expect(
            check(wrong, preview, repository=f"{public}-source") == [],
            "a correct preview build of the source repository was rejected",
        )
        expect(
            check(wrong, preview, repository=public) != [],
            "a preview-folder build of the public repository was accepted",
        )
        root_site = Path(tmp) / "root-False"
        expect(
            check(root_site, "", repository=f"{public}-source") != [],
            "a root build of the source repository was accepted",
        )
        (root_site / "robots.txt").write_text("User-agent: *\nAllow: /\n")
        expect(
            any("robots.txt" in p for p in check(root_site, "")),
            "a robots.txt without the preview Disallow line was accepted",
        )

    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    base = os.environ.get("BASE_URL", "").rstrip("/")
    problems = check(BUILD, base, os.environ.get("GITHUB_REPOSITORY"))
    for p in problems:
        log.error("FAIL: %s", p)
    if problems:
        sys.exit(1)
    log.info(
        "built site looks servable %s: index.html ok, asset paths and preview marker right",
        f"under {base}/" if base else "at the domain root",
    )
