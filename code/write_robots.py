"""Keep search engines off the preview of the next release.

`myst build` writes a robots.txt that allows everything. The preview is a folder of the
same domain as the published book, so the published book's robots.txt is the one crawlers
read for both: in a build of the published book (`BASE_URL` empty) this replaces the
`Allow: /` line with a `Disallow` for the preview folder, and keeps the rest. A preview
build's own robots.txt is not at the domain root, so crawlers never read it; it is
written to disallow everything all the same, so that it says the right thing if one does.

`--self-test` checks both rewrites, and that a second pass changes nothing.

Usage: BASE_URL=... python code/write_robots.py [--self-test]   (after `myst build --html`)
"""

import argparse
import logging
import os
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROBOTS = Path("_build/html/robots.txt")
PREVIEW_FOLDER = "/intertemporal-choice.github.io-source/"


def disallow_line(base: str) -> str:
    return "Disallow: /" if base else f"Disallow: {PREVIEW_FOLDER}"


def rewrite(text: str, base: str) -> str:
    """`text` with `Allow: /` and any earlier Disallow replaced by the one that applies."""
    lines = [
        line
        for line in text.splitlines()
        if line.strip() != "Allow: /" and not line.startswith("Disallow: ")
    ]
    if "User-agent: *" not in lines:
        lines.append("User-agent: *")
    lines.insert(lines.index("User-agent: *") + 1, disallow_line(base))
    return "\n".join(lines) + "\n"


def self_test() -> bool:
    ok = True

    def expect(condition: bool, failure: str) -> None:
        nonlocal ok
        if not condition:
            log.error("SELF-TEST FAIL: %s", failure)
            ok = False

    myst = "# https://www.robotstxt.org/robotstxt.html\n\nUser-agent: *\nAllow: /\nSitemap: x\n"
    root = rewrite(myst, "")
    expect(
        root.splitlines() == ["# https://www.robotstxt.org/robotstxt.html", "", "User-agent: *",
                              f"Disallow: {PREVIEW_FOLDER}", "Sitemap: x"],
        f"the published book's robots.txt came out as {root!r}",
    )
    preview = rewrite(myst, "/intertemporal-choice.github.io-source")
    expect(
        "Disallow: /" in preview.splitlines() and "Allow: /" not in preview,
        f"the preview's robots.txt came out as {preview!r}",
    )
    expect(rewrite(root, "") == root, "a second pass changed the file")
    expect("User-agent: *" in rewrite("", "").splitlines(), "an empty file got no User-agent")

    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    base = os.environ.get("BASE_URL", "").rstrip("/")
    text = ROBOTS.read_text() if ROBOTS.exists() else ""
    ROBOTS.write_text(rewrite(text, base))
    log.info("robots.txt: %s", disallow_line(base))
