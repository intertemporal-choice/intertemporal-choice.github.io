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
     carries at least one cell output; a build run without `--execute` omits them all
     and still exits 0 under `--strict`

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

# The deployed site. Each page's <slug>.json holds its `location`, `kind` and every cell
# output, tables too, which the static HTML leaves to the browser. Records of removed
# pages linger on disk, so config.json decides which pages are current.
BUILD = Path("_build/html")
REPO_SLUG = "intertemporal-choice.github.io"
MIN_BYTES = 2000
MIN_PAGES = 40

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')


def bad_prefixes(html: str, slug: str) -> list[str]:
    """Asset paths that start with the repository name, one directory too deep."""
    return sorted({p for p in ASSET.findall(html) if p.startswith(f"/{slug}/")})


def current_slugs(build: Path) -> set[str]:
    config = build / "config.json"
    if not config.exists():
        return set()
    projects = json.loads(config.read_text())["projects"]
    return {p["slug"] for project in projects for p in project["pages"] if "slug" in p}


def notebook_records(build: Path) -> dict[str, Path]:
    """Source path of each current notebook page, mapped to its page record."""
    current, found = current_slugs(build), {}
    for record in sorted(build.glob("*.json")):
        page = json.loads(record.read_text())
        if (
            isinstance(page, dict)
            and page.get("kind") == "Notebook"
            and page.get("slug") in current
        ):
            found[page["location"]] = record
    return found


def has_output(node: object) -> bool:
    """Whether the tree holds an output node carrying a kernel's result, of any type."""
    stack = [node]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            if item.get("type") == "output" and item.get("jupyter_data"):
                return True
            stack.extend(item.values())
        elif isinstance(item, list):
            stack.extend(item)
    return False


def unexecuted(build: Path) -> list[str]:
    notebooks = notebook_records(build)
    if not notebooks:
        return [f"no notebook page recorded in {build / 'config.json'}"]
    return [
        f"{location} carries no cell output: built without --execute?"
        for location, record in notebooks.items()
        if not has_output(json.loads(record.read_text()))
    ]


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
        failures.append(
            f"{len(stale)} asset paths prefixed with /{slug}/, e.g. {stale[0]}"
        )

    built = list(build.rglob("*.html"))
    if len(built) < MIN_PAGES:
        failures.append(
            f"only {len(built)} html pages built, under the {MIN_PAGES} floor"
        )

    failures.extend(unexecuted(build))
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


def page_record(kind: str, name: str, outputs: list[dict]) -> dict:
    cell = {"type": "block", "children": [{"type": "outputs", "children": outputs}]}
    return {"kind": kind, "location": f"/{name}.md", "slug": f"content.{name}",
            "mdast": {"type": "root", "children": [cell]}}  # fmt: skip


def self_test_execution(tmp: Path) -> list[str]:
    errors = []
    # A table-only notebook, whose one output the static HTML does not render.
    table = [{"type": "output", "jupyter_data": {"output_type": "execute_result"}}]
    listed = ["table", "bare", "prose"]
    (tmp / "config.json").write_text(
        json.dumps(
            {"projects": [{"pages": [{"slug": f"content.{n}"} for n in listed]}]}
        )
    )
    for name, kind, outputs in [
        ("table", "Notebook", table),
        ("bare", "Notebook", [{"type": "output", "children": []}]),
        ("prose", "Article", []),
        ("removed", "Notebook", []),
    ]:
        record = page_record(kind, name, outputs)
        (tmp / f"content.{name}.json").write_text(json.dumps(record))
    (tmp / "myst.search.json").write_text("[]")
    if set(notebook_records(tmp)) != {"/table.md", "/bare.md"}:
        errors.append("notebook_records did not pick out exactly the current notebooks")
    if unexecuted(tmp) != ["/bare.md carries no cell output: built without --execute?"]:
        errors.append("output check did not flag exactly the unexecuted notebook")
    empty = tmp / "empty"
    empty.mkdir()
    if not unexecuted(empty):
        errors.append("an empty set of notebook pages passed")
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
