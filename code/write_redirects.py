"""Write forwarding pages into the built site for every page that has moved.

GitHub Pages serves static files and has no server-side redirects, so an old URL for a
page that has been renamed or moved simply 404s. For each `old new` line in
code/redirects.txt this writes `_build/html<old>/index.html`, a page that sends the
browser to `<new>` at once, carrying over any #anchor (so a link to a Math Facts entry
still reaches the entry), with a meta refresh and a plain link as fallbacks.

It refuses rather than guesses:

  1. the new path must be a page in the build, so a typo or a second move of the same
     page fails the deploy instead of forwarding readers to a 404
  2. the old path must NOT be a page in the build, so a redirect can never overwrite a
     live page that has since reused the name

`--self-test` runs both checks against input they should reject, and fails if either
passes it.

Usage: uv run python code/write_redirects.py [--self-test]   (after `myst build --html`)
"""

import argparse
import html
import logging
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BUILD = Path("_build/html")
REDIRECTS = Path("code/redirects.txt")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved to {new}</title>
<link rel="canonical" href="{new}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={new}">
<script>location.replace({new_js} + location.hash);</script>
</head>
<body>
<p>This page has moved to <a href="{new}">{new}</a>.</p>
</body>
</html>
"""


def parse(text: str) -> list[tuple[str, str]]:
    """`old new` pairs, ignoring blank lines and # comments."""
    pairs = []
    for n, line in enumerate(text.splitlines(), 1):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2 or not all(p.startswith("/") for p in parts):
            raise ValueError(f"redirects line {n}: expected '/old /new', got {line!r}")
        pairs.append((parts[0].rstrip("/"), parts[1].rstrip("/")))
    return pairs


def is_page(build: Path, path: str) -> bool:
    return (build / path.lstrip("/") / "index.html").exists()


def check(build: Path, pairs: list[tuple[str, str]]) -> list[str]:
    failures = []
    olds = [old for old, _ in pairs]
    for old in {o for o in olds if olds.count(o) > 1}:
        failures.append(f"{old} is listed more than once")
    for old, new in pairs:
        if not is_page(build, new):
            failures.append(f"{old} -> {new}, but {new} is not a page in the build")
        if is_page(build, old):
            failures.append(
                f"{old} is a live page in the build; refusing to overwrite it"
            )
    return failures


def write(build: Path, pairs: list[tuple[str, str]]) -> None:
    for old, new in pairs:
        target = build / old.lstrip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        new_js = '"' + new.replace("\\", "\\\\").replace('"', '\\"') + '"'
        target.write_text(PAGE.format(new=html.escape(new), new_js=new_js))


def self_test() -> bool:
    """Every check must reject input it is supposed to reject."""
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        build = Path(tmp)
        for page in ("content/a", "content/b"):
            (build / page).mkdir(parents=True)
            (build / page / "index.html").write_text("page")
        if check(build, [("/content/old", "/content/a")]):
            log.error("SELF-TEST FAIL: a valid redirect was rejected")
            ok = False
        if not check(build, [("/content/old", "/content/missing")]):
            log.error("SELF-TEST FAIL: a redirect to a missing page was accepted")
            ok = False
        if not check(build, [("/content/b", "/content/a")]):
            log.error("SELF-TEST FAIL: a redirect over a live page was accepted")
            ok = False
        if not check(
            build, [("/content/old", "/content/a"), ("/content/old", "/content/b")]
        ):
            log.error("SELF-TEST FAIL: a duplicated old path was accepted")
            ok = False
    try:
        parse("content/old /content/new")
        log.error("SELF-TEST FAIL: a path without a leading slash was accepted")
        ok = False
    except ValueError:
        pass
    if parse("# note\n/a/ /b  # why\n\n") != [("/a", "/b")]:
        log.error(
            "SELF-TEST FAIL: comments, blank lines or trailing slashes mishandled"
        )
        ok = False
    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    pairs = parse(REDIRECTS.read_text())
    problems = check(BUILD, pairs)
    for p in problems:
        log.error("FAIL: %s", p)
    if problems:
        sys.exit(1)
    write(BUILD, pairs)
    log.info("wrote %d redirect pages", len(pairs))
