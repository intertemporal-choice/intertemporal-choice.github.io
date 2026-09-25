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
  3. the expected number of pages were emitted, not counting the forwarding pages that
     code/write_redirects.py adds for moved URLs

It also enforces that every figure a chapter shows comes from a notebook (content/notebooks/,
built with code/build_site.py). MyST does not: an embed whose label matches no notebook cell
builds, even under --strict, into a figure that shows nothing but its caption. So:

  4. every figure is either an embed of exactly one image output, with nothing beside it and
     no placeholder, or a static image listed in code/figure_exemptions.txt; a figure that
     shows nothing fails
  5. no image appears outside a figure unless it is exempt
  6. the exemptions list stays honest: each entry has a kind (`exception`, data that cannot be
     obtained; `pending`, not yet ported) and a reason, is used by a current page, and every
     file under content/figures/ is listed
  7. notebooks live only under content/notebooks/, every one listed in toc.yml was built as a
     notebook, and each carries outputs (built without --execute, it would carry none)

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

import yaml

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BUILD = Path("_build/html")
REPO_SLUG = "intertemporal-choice.github.io"
MIN_BYTES = 2000
MIN_PAGES = 40
EXEMPTIONS = Path("code/figure_exemptions.txt")
FIGURES = Path("content/figures")
NOTEBOOKS = "content/notebooks/"
KINDS = {"exception", "pending"}

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')
REFRESH = re.compile(r'<meta http-equiv="refresh"', re.IGNORECASE)


def bad_prefixes(html: str, slug: str) -> list[str]:
    """Asset paths that start with the repository name, one directory too deep."""
    return sorted({p for p in ASSET.findall(html) if p.startswith(f"/{slug}/")})


def is_redirect(html: str) -> bool:
    """A forwarding page written by code/write_redirects.py, which is not a page of the book."""
    return bool(REFRESH.search(html))


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

    pages = [
        p
        for p in build.rglob("*.html")
        if not is_redirect(p.read_text(errors="ignore"))
    ]
    if len(pages) < MIN_PAGES:
        failures.append(
            f"only {len(pages)} html pages built, under the {MIN_PAGES} floor"
        )

    return failures


def parse_exemptions(text: str) -> tuple[dict[str, tuple[str, str]], list[str]]:
    """`kind path reason` lines, one per static figure allowed to stay a static image."""
    entries, problems = {}, []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split(None, 2)
        if len(parts) < 3:
            problems.append(f"{EXEMPTIONS} line {n}: expected 'kind path reason', got {line.strip()!r}")
            continue
        kind, path, reason = parts
        if kind not in KINDS:
            problems.append(f"{EXEMPTIONS} line {n}: kind {kind!r} is not one of {sorted(KINDS)}")
        if path in entries:
            problems.append(f"{EXEMPTIONS} line {n}: {path} is listed twice")
        entries[path] = (kind, reason.strip())
    return entries, problems


def current_pages(build: Path) -> dict[str, dict]:
    """The page records of the pages the site currently has (stale JSON left behind is not)."""
    project = json.loads((build / "config.json").read_text())["projects"][0]
    slugs = [p["slug"] for p in project.get("pages", []) if "slug" in p]
    if project.get("index"):
        slugs.append(project["index"])
    return {s: json.loads((build / f"{s}.json").read_text()) for s in slugs if (build / f"{s}.json").exists()}


def descendants(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from descendants(value)
    elif isinstance(node, list):
        for value in node:
            yield from descendants(value)


def is_output(node: dict) -> bool:
    return node.get("type") == "output" and "jupyter_data" in node


def figure_problems(slug: str, mdast, exempt: dict, used: set) -> list[str]:
    """Figures that are not one embedded image, or static images that are not exempt."""
    problems = []

    def one_figure(fig: dict) -> None:
        name = fig.get("label") or "(unlabelled)"
        nodes = list(descendants(fig.get("children", [])))
        images = [n for n in nodes if n.get("type") == "image"]
        outputs = [n for n in nodes if is_output(n)]
        for im in images:
            if im.get("placeholder"):
                problems.append(f"{slug}: figure {name} falls back to a placeholder image")
        if outputs:
            if len(outputs) != 1:
                problems.append(f"{slug}: figure {name} embeds {len(outputs)} outputs, not one image")
            data = outputs[0]["jupyter_data"].get("data") or {}
            if not any(mime.startswith("image/") for mime in data):
                problems.append(f"{slug}: figure {name} embeds an output that is not an image")
            if images:
                problems.append(f"{slug}: figure {name} has a static image beside its embedded output")
        elif images:
            for im in images:
                src = im.get("urlSource") or im.get("url")
                used.add(src)
                if src not in exempt:
                    problems.append(
                        f"{slug}: figure {name} is the static image {src}; generate it in a"
                        f" notebook or list it in {EXEMPTIONS}"
                    )
        else:
            problems.append(
                f"{slug}: figure {name} shows nothing: does its embed label match a notebook cell?"
            )

    def visit(node) -> None:
        if isinstance(node, list):
            for value in node:
                visit(value)
        elif isinstance(node, dict):
            if node.get("type") == "container" and node.get("kind") == "figure":
                one_figure(node)
                return
            if node.get("type") == "image":
                src = node.get("urlSource") or node.get("url")
                used.add(src)
                if src not in exempt:
                    problems.append(f"{slug}: image {src} outside a figure is not exempt")
            for value in node.values():
                visit(value)

    visit(mdast)
    return problems


def exemption_problems(entries: dict, used: set, figure_files: list[str]) -> list[str]:
    problems = [
        f"{path} is listed in {EXEMPTIONS} but no current page shows it"
        for path in entries
        if path not in used
    ]
    problems += [f"{f} is not listed in {EXEMPTIONS}" for f in figure_files if f not in entries]
    return problems


def toc_notebooks(toc: str) -> list[str]:
    """Notebook files listed in toc.yml (content/notebooks/, other than its index)."""
    files = [n["file"] for n in descendants(yaml.safe_load(toc)) if isinstance(n.get("file"), str)]
    return [f for f in files if f.startswith(NOTEBOOKS) and not f.endswith("index.md")]


def notebook_problems(pages: dict[str, dict], listed: list[str]) -> list[str]:
    problems, built = [], 0
    for slug, record in pages.items():
        if record.get("kind") != "Notebook":
            continue
        location = record.get("location", "").lstrip("/")
        if not location.startswith(NOTEBOOKS):
            problems.append(f"{slug}: notebook page {location} is outside {NOTEBOOKS}; chapters stay prose")
            continue
        built += 1
        if not any(is_output(n) for n in descendants(record.get("mdast"))):
            problems.append(f"{slug}: notebook carries no cell output: built without --execute?")
    if built != len(listed):
        problems.append(
            f"{len(listed)} notebooks are listed in toc.yml but {built} were built as notebooks"
            " (is a kernelspec missing?)"
        )
    return problems


def check_figures(build: Path, repo: Path) -> list[str]:
    exemptions = repo / EXEMPTIONS
    entries, problems = parse_exemptions(exemptions.read_text() if exemptions.exists() else "")
    pages = current_pages(build)
    used: set = set()
    for slug, record in pages.items():
        problems += figure_problems(slug, record.get("mdast"), entries, used)
    figure_files = [
        "/" + str(p.relative_to(repo))
        for p in sorted((repo / FIGURES).rglob("*"))
        if p.is_file() and not p.name.startswith(".")
    ]
    problems += exemption_problems(entries, used, figure_files)
    problems += notebook_problems(pages, toc_notebooks((repo / "toc.yml").read_text()))
    return problems


# Synthetic page nodes for the self-test.
def _fig(*children, label="fig:t"):
    return {"type": "container", "kind": "figure", "label": label, "children": list(children)}


def _img(src, placeholder=False):
    return {"type": "image", "urlSource": src, **({"placeholder": True} if placeholder else {})}


def _out(*mimes):
    return {"type": "outputs", "children": [{"type": "output", "jupyter_data": {"data": {m: "x" for m in mimes}}}]}


def self_test_figures() -> list[str]:
    failures = []
    png, static = ("image/png", "text/plain"), "/content/figures/A/a.png"
    exempt = {static: ("pending", "port to content/notebooks/A.md")}
    good = {
        "one embedded image": _fig(_out(*png)),
        "an exempt static image": _fig(_img(static)),
    }
    bad = {
        "a text-only output": _fig(_out("text/plain")),
        "two outputs": _fig(_out(*png), _out(*png)),
        "a stream beside an image": _fig(_out("text/plain"), _out(*png)),
        "an unlisted static image": _fig(_img("/content/figures/B/b.png")),
        "an empty figure": _fig({"type": "_lift"}),
        "a placeholder": _fig(_out(*png), _img(static, placeholder=True)),
        "a static image beside an output": _fig(_out(*png), _img(static)),
        "an unlisted image outside a figure": {"type": "root", "children": [_img("/x.png")]},
    }
    for name, node in good.items():
        if figure_problems("p", node, exempt, set()):
            failures.append(f"figure check rejected {name}")
    for name, node in bad.items():
        if not figure_problems("p", node, exempt, set()):
            failures.append(f"figure check accepted {name}")

    for name, text in {
        "a missing reason": "pending /content/figures/A/a.png\n",
        "an unknown kind": "maybe /content/figures/A/a.png some reason\n",
        "a duplicate": f"pending {static} r\npending {static} r\n",
    }.items():
        if not parse_exemptions(text)[1]:
            failures.append(f"exemptions parser accepted {name}")
    if parse_exemptions(f"# comment\n\npending {static} port it # soon\n")[1]:
        failures.append("exemptions parser rejected a comment, a blank line or a # in a reason")
    if not exemption_problems(exempt, set(), []):
        failures.append("an exemption no page uses was accepted")
    if not exemption_problems({}, set(), [static]):
        failures.append("a file under content/figures missing from the exemptions was accepted")

    # End to end on a synthetic build and repo.
    with tempfile.TemporaryDirectory() as tmp:
        build, repo = Path(tmp) / "html", Path(tmp) / "repo"
        build.mkdir()
        (repo / FIGURES / "A").mkdir(parents=True)
        (repo / "code").mkdir()
        (repo / FIGURES / "A" / "a.png").write_bytes(b"png")
        (repo / EXEMPTIONS).write_text(f"pending {static} port to content/notebooks/A.md\n")
        (repo / "toc.yml").write_text(
            "project:\n  toc:\n    - file: content/a.md\n    - file: content/notebooks/index.md\n"
            "      children:\n        - file: content/notebooks/A.md\n"
        )

        def page(slug, kind, location, mdast):
            (build / f"{slug}.json").write_text(json.dumps({"kind": kind, "location": location, "mdast": mdast}))

        def write_config(slugs):
            pages = [{"slug": s} for s in slugs]
            (build / "config.json").write_text(json.dumps({"projects": [{"index": "index", "pages": pages}]}))

        page("index", "Article", "/README.md", {"type": "root", "children": []})
        page("content.a", "Article", "/content/a.md", _fig(_img(static)))
        page("content.notebooks.a", "Notebook", "/content/notebooks/A.md", _out(*png))
        page("content.old", "Notebook", "/content/old.md", {"children": []})  # stale, not current
        write_config(["content.a", "content.notebooks.a"])
        if check_figures(build, repo):
            failures.append(f"end-to-end check rejected a good build: {check_figures(build, repo)}")
        cases = {
            "a notebook built without outputs": lambda: page(
                "content.notebooks.a", "Notebook", "/content/notebooks/A.md", {"children": []}
            ),
            "a notebook outside content/notebooks": lambda: (
                page("content.b", "Notebook", "/content/b.md", _out(*png)),
                write_config(["content.a", "content.notebooks.a", "content.b"]),
            ),
            "a listed notebook that was not built as one": lambda: page(
                "content.notebooks.a", "Article", "/content/notebooks/A.md", _out(*png)
            ),
        }
        for name, spoil in cases.items():
            page("content.notebooks.a", "Notebook", "/content/notebooks/A.md", _out(*png))
            write_config(["content.a", "content.notebooks.a"])
            spoil()
            if not check_figures(build, repo):
                failures.append(f"end-to-end check accepted {name}")
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
    if not is_redirect(
        '<meta http-equiv="refresh" content="0; url=/content/numerical">'
    ):
        log.error("SELF-TEST FAIL: a forwarding page was counted as a page of the book")
        ok = False
    if is_redirect('<meta charset="utf-8"><title>Envelope</title>'):
        log.error("SELF-TEST FAIL: a page of the book was taken for a forwarding page")
        ok = False
    if not check(Path("/nonexistent"), REPO_SLUG):
        log.error("SELF-TEST FAIL: missing-index check did not fire")
        ok = False
    for f in self_test_figures():
        log.error("SELF-TEST FAIL: %s", f)
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
    if not problems:
        problems = check_figures(BUILD, Path("."))
    for p in problems:
        log.error("FAIL: %s", p)
    if problems:
        sys.exit(1)
    log.info(
        "built site looks servable: index.html ok, asset paths root-relative, every figure"
        " embedded from a notebook or exempt"
    )
