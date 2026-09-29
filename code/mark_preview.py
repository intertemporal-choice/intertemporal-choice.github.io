"""Configure a preview build so that nobody mistakes it for the published book.

The book is built from two repositories by the same workflow. The public one serves the
published book at https://intertemporal-choice.github.io; the private source repository
serves a preview of the next release one folder down, at
https://intertemporal-choice.github.io/intertemporal-choice.github.io-source/. Page for
page the two look identical. So, before `myst build`, when `BASE_URL` names a folder, this
gives the theme a `navbar_end` part, a banner at the end of the top navbar of every page
linking to the published book, by replacing one comment line of myst.yml:

    # navbar_end: filled in by code/mark_preview.py for a preview build; see code/README.md

When `BASE_URL` is empty it leaves myst.yml alone and checks that the line is still a
comment, so that a rewritten copy cannot reach the published book by being committed.

The banner goes in through the theme rather than into the built HTML because the site
is a React app that re-renders the document on load and drops anything the theme did
not render (tried on 2026-09-28: an injected banner and a noindex tag both vanished). It
is a line of myst.yml rather than a file that myst.yml extends because `extends` does not
carry `site.parts` (also tried). code/verify_build.py checks afterwards that the banner is
on every page of a preview and on no page of the published book; code/write_robots.py
keeps search engines off the preview.

After a local preview build, restore the file with `git checkout myst.yml`.

`--self-test` checks that the rewrite puts the banner in, that the committed myst.yml is
recognised as unrewritten, and that a rewritten file is refused for the published book.

Usage: BASE_URL=... python code/mark_preview.py [--self-test]   (before `myst build --html`)
"""

import argparse
import logging
import os
import sys
import tempfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

MYST_YML = Path("myst.yml")
BOOK_URL = "https://intertemporal-choice.github.io"
# code/verify_build.py looks for this text on every page of a preview.
BANNER_TEXT = "Preview of the next release"
BANNER = f"{BANNER_TEXT}; the published book is at [intertemporal-choice.github.io]({BOOK_URL})."
ANCHOR = (
    "    # navbar_end: filled in by code/mark_preview.py for a preview build; see code/README.md"
)
PART = f"    navbar_end: |  # REWRITTEN by code/mark_preview.py; restore with `git checkout myst.yml`\n      {BANNER}"


def rewrite(text: str) -> str:
    """myst.yml with the banner in place of the anchor comment."""
    if text.count(ANCHOR) != 1:
        raise ValueError(f"expected the anchor comment exactly once in {MYST_YML}:\n{ANCHOR}")
    return text.replace(ANCHOR, PART)


def is_unrewritten(text: str) -> bool:
    """The committed myst.yml: the anchor is still a comment and there is no navbar_end part."""
    return text.count(ANCHOR) == 1 and "\n    navbar_end:" not in text


def configure(path: Path, base: str) -> str:
    """Rewrite `path` for a preview build, or check it is unrewritten for the published book."""
    text = path.read_text()
    if base:
        path.write_text(rewrite(text))
        return f"rewrote {path}: the theme will show the preview banner on every page"
    if "\n    navbar_end:" in text:
        raise ValueError(
            f"{path} carries the preview banner, which the published book must not; "
            f"restore it with `git checkout {path}`"
        )
    if not is_unrewritten(text):
        raise ValueError(f"the anchor comment is missing from {path}:\n{ANCHOR}")
    return f"BASE_URL is empty: this build is the published book, {path} left as committed"


def self_test() -> bool:
    ok = True

    def expect(condition: bool, failure: str) -> None:
        nonlocal ok
        if not condition:
            log.error("SELF-TEST FAIL: %s", failure)
            ok = False

    committed = MYST_YML.read_text()
    expect(is_unrewritten(committed), f"the committed {MYST_YML} is not recognised as unrewritten")
    rewritten = rewrite(committed)
    expect(
        "\n    navbar_end: |" in rewritten and BANNER_TEXT in rewritten and BOOK_URL in rewritten,
        "the rewritten file does not carry the banner",
    )
    expect(not is_unrewritten(rewritten), "the rewritten file passes as unrewritten")
    expect(
        rewritten.replace(PART, ANCHOR) == committed,
        "the rewrite changed more than the anchor line",
    )
    try:
        rewrite(committed.replace(ANCHOR, ""))
        expect(False, "a file without the anchor was rewritten")
    except ValueError:
        pass
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "myst.yml"
        path.write_text(committed)
        configure(path, "")
        expect(path.read_text() == committed, "the published book's myst.yml was altered")
        configure(path, "/intertemporal-choice.github.io-source")
        expect(path.read_text() == rewritten, "configure did not rewrite for the preview")
        try:
            configure(path, "")
            expect(False, "a rewritten file was accepted for the published book")
        except ValueError:
            pass

    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    try:
        log.info(configure(MYST_YML, os.environ.get("BASE_URL", "").rstrip("/")))
    except ValueError as e:
        log.error("FAIL: %s", e)
        sys.exit(1)
