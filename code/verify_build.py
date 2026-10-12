"""Assert the built site is servable, and its figures are what their notebooks draw, before
it is published.

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

It also enforces that every figure a chapter shows is drawn by the notebook beside it,
content/<part>/<Chapter>/<Chapter>.ipynb, into the chapter's figures/ folder (see
code/build_site.py). MyST does not: a figure whose file is stale builds and deploys. So:

  4. every figure is exactly one image: `figures/<name>.png` beside a chapter that has its
     notebook, or a static image listed in code/figure_exemptions.txt; no notebook output
     is embedded, and no image appears outside a figure unless it is exempt
  5. the exemptions list stays honest: each entry has a kind (`exception`, data that cannot
     be obtained; `pending`, not yet ported) and a reason, is used by a current page, and
     every file under content/figures/ is listed
  6. every notebook in the build sits beside its chapter, is listed in toc.yml as a child of
     that chapter, and carries outputs
  7. the figures are current. A notebook the build re-ran (its code or the environment
     changed) redrew its figures over the committed files, so a file that now differs from
     the committed one beyond a small tolerance means the notebook was changed without its
     figures being re-run and committed; a figure drawn but never committed fails too. The
     tolerance allows the pixel or two of antialiasing that differs between machines.

`--self-test` runs every check against synthetic bad input and fails if any check passes
it, so a check that has silently stopped discriminating is caught rather than trusted.

Usage: uv run python code/verify_build.py [--self-test]
"""

import argparse
import io
import json
import logging
import os
import re
import subprocess
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
KINDS = {"exception", "pending"}
# RMS difference over 0-255 pixel values below which a redrawn figure counts as the same.
TOLERANCE = 3.0

ASSET = re.compile(r'(?:href|src)="(/[^"]*)"')
REFRESH = re.compile(r'<meta http-equiv="refresh"', re.IGNORECASE)
CHAPTER_LOCATION = re.compile(r"^/content/[^/]+/([^/]+)/index\.md$")
NOTEBOOK_LOCATION = re.compile(r"^/content/[^/]+/([^/]+)/\1\.ipynb$")
FIGURE_FILE = re.compile(r"^figures/[A-Za-z0-9][A-Za-z0-9_-]*\.png$")


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


# ---------------------------------------------------------------- figures from notebooks


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


def notebook_beside(repo: Path, location: str) -> bool:
    """Whether the page at `location` is a chapter index with its notebook beside it."""
    m = CHAPTER_LOCATION.match(location)
    return bool(m) and (repo / location.lstrip("/")).parent.joinpath(f"{m.group(1)}.ipynb").is_file()


def figure_problems(slug: str, location: str, mdast, exempt: dict, used: set, repo: Path) -> list[str]:
    """Figures that are not one image drawn by the chapter's notebook or exempt."""
    problems = []

    def image_problem(src: str | None, what: str) -> None:
        src = src or ""
        if src.startswith(f"/{FIGURES}/"):
            used.add(src)
            if src not in exempt:
                problems.append(
                    f"{slug}: {what} is the static image {src}; draw it in the chapter's"
                    f" notebook or list it in {EXEMPTIONS}"
                )
        elif FIGURE_FILE.match(src):
            if not notebook_beside(repo, location):
                problems.append(
                    f"{slug}: {what} uses {src}, but the page is not a chapter with its notebook"
                    " beside it (content/<part>/<Chapter>/<Chapter>.ipynb)"
                )
        else:
            problems.append(
                f"{slug}: {what} uses {src!r}, which is neither figures/<name>.png beside the"
                " chapter nor an exempt static image"
            )

    def one_figure(fig: dict) -> None:
        name = f"figure {fig.get('label') or '(unlabelled)'}"
        nodes = list(descendants(fig.get("children", [])))
        images = [n for n in nodes if n.get("type") == "image"]
        if any(is_output(n) for n in nodes):
            problems.append(f"{slug}: {name} embeds a notebook output; chapters use the file the notebook saves")
        if len(images) != 1:
            problems.append(f"{slug}: {name} shows {len(images)} images, not one")
            return
        if images[0].get("placeholder"):
            problems.append(f"{slug}: {name} falls back to a placeholder image")
        image_problem(images[0].get("urlSource") or images[0].get("url"), name)

    def visit(node) -> None:
        if isinstance(node, list):
            for value in node:
                visit(value)
        elif isinstance(node, dict):
            if node.get("type") == "container" and node.get("kind") == "figure":
                one_figure(node)
                return
            if node.get("type") == "image":
                image_problem(node.get("urlSource") or node.get("url"), "an image outside any figure")
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


def toc_parents(toc: str) -> dict[str, str | None]:
    """Every file in toc.yml, mapped to the file it is listed under (None at the top)."""
    parents: dict[str, str | None] = {}

    def walk(entries, parent):
        for entry in entries or []:
            if not isinstance(entry, dict):
                continue
            file = entry.get("file")
            if isinstance(file, str):
                parents[file] = parent
            walk(entry.get("children"), file if isinstance(file, str) else parent)

    walk((yaml.safe_load(toc) or {}).get("project", {}).get("toc"), None)
    return parents


def notebook_problems(pages: dict[str, dict], toc: str) -> list[str]:
    parents = toc_parents(toc)
    listed = [f for f in parents if f.endswith(".ipynb")]
    problems, built = [], 0
    for slug, record in pages.items():
        if record.get("kind") != "Notebook":
            continue
        location = record.get("location", "")
        if not NOTEBOOK_LOCATION.match(location):
            problems.append(
                f"{slug}: notebook page {location} is not content/<part>/<Chapter>/<Chapter>.ipynb"
                " beside its chapter"
            )
            continue
        built += 1
        rel = location.lstrip("/")
        chapter = str(Path(rel).parent / "index.md")
        if parents.get(rel) != chapter:
            problems.append(f"{slug}: {rel} is not listed in toc.yml as a child of {chapter}")
        if not any(is_output(n) for n in descendants(record.get("mdast"))):
            problems.append(f"{slug}: notebook carries no cell output: committed without outputs?")
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
        problems += figure_problems(slug, record.get("location", ""), record.get("mdast"), entries, used, repo)
    figure_files = [
        "/" + str(p.relative_to(repo))
        for p in sorted((repo / FIGURES).rglob("*"))
        if p.is_file() and not p.name.startswith(".")
    ]
    problems += exemption_problems(entries, used, figure_files)
    problems += notebook_problems(pages, (repo / "toc.yml").read_text())
    return problems


# ---------------------------------------------------------------- figures are current


def rms_difference(a: bytes, b: bytes) -> float | None:
    """RMS difference between two PNGs over 0-255 pixel values; None if their sizes differ."""
    import numpy as np
    from PIL import Image

    first, second = Image.open(io.BytesIO(a)).convert("RGBA"), Image.open(io.BytesIO(b)).convert("RGBA")
    if first.size != second.size:
        return None
    diff = np.asarray(first, dtype=float) - np.asarray(second, dtype=float)
    return float(np.sqrt((diff**2).mean()))


# Every chapter's figure files, as a git pathspec (`:(glob)` keeps `*` from crossing `/`),
# so that a figure deleted from the working tree is reported as well as one changed.
FIGURE_PATHSPEC = ":(glob)content/*/*/figures/*.png"


def git_status(repo: Path, pathspec: str = FIGURE_PATHSPEC) -> dict[str, str]:
    """Path -> the two status letters of `git status --porcelain`, for paths that have any."""
    out = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all", "--", pathspec],
        cwd=repo, capture_output=True, text=True, check=True,
    ).stdout
    return {line[3:]: line[:2] for line in out.splitlines() if len(line) > 3}


def committed(repo: Path, path: str) -> bytes | None:
    done = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=repo, capture_output=True)
    return done.stdout if done.returncode == 0 else None


def figure_freshness(repo: Path) -> list[str]:
    """Figures whose file no longer matches what is committed: see check 7."""
    problems = []
    for path, status in sorted(git_status(repo).items()):
        if status == "??" or status.startswith("A"):
            problems.append(f"{path} was drawn but is not committed: commit it")
            continue
        if "M" not in status and "D" not in status:
            continue
        before = committed(repo, path)
        if before is None or "D" in status:
            problems.append(f"{path} is committed but was deleted or replaced: run the notebook and commit")
            continue
        rms = rms_difference(before, (repo / path).read_bytes())
        if rms is None:
            problems.append(f"{path}: the notebook now draws a different size from the committed file: commit it")
        elif rms > TOLERANCE:
            problems.append(
                f"{path}: the notebook draws a different figure from the committed one"
                f" (RMS difference {rms:.1f} > {TOLERANCE}): run it and commit its figures"
            )
        else:
            log.info("%s: redrawn within tolerance of the committed file (RMS %.2f)", path, rms)
    return problems


# ---------------------------------------------------------------- self-tests



def self_test_site() -> list[str]:
    failures = []
    if not bad_prefixes(f'<a href="/{REPO_SLUG}/build/app.css">', REPO_SLUG):
        failures.append("stale-prefix check did not fire on a stale prefix")
    if bad_prefixes('<a href="/build/app.css">', REPO_SLUG):
        failures.append("stale-prefix check fired on a correct root path")
    if not is_redirect('<meta http-equiv="refresh" content="0; url=/content/numerical">'):
        failures.append("a forwarding page was counted as a page of the book")
    if is_redirect('<meta charset="utf-8"><title>Envelope</title>'):
        failures.append("a page of the book was taken for a forwarding page")
    if not check(Path("/nonexistent"), REPO_SLUG):
        failures.append("missing-index check did not fire")
    return failures


# Synthetic page nodes for the figure self-test.
def _fig(*children, label="fig:t"):
    return {"type": "container", "kind": "figure", "label": label, "children": list(children)}


def _img(src, placeholder=False):
    return {"type": "image", "urlSource": src, **({"placeholder": True} if placeholder else {})}


def _out(*mimes):
    return {"type": "outputs", "children": [{"type": "output", "jupyter_data": {"data": {m: "x" for m in mimes}}}]}


def self_test_figures() -> list[str]:
    failures = []
    png, static = ("image/png", "text/plain"), "/content/figures/A/a.png"
    exempt = {static: ("pending", "port to a notebook beside the chapter")}
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        chapter = repo / "content/part/A"
        (chapter / "figures").mkdir(parents=True)
        (chapter / "index.md").write_text("# A\n")
        (chapter / "A.ipynb").write_text("{}")
        (chapter / "figures/a.png").write_bytes(b"png")
        (repo / "content/part/B").mkdir()
        (repo / "content/part/B/index.md").write_text("# B\n")  # a chapter folder with no notebook
        (repo / FIGURES / "A").mkdir(parents=True)
        (repo / FIGURES / "A/a.png").write_bytes(b"png")
        (repo / "code").mkdir()
        (repo / EXEMPTIONS).write_text(f"pending {static} port to a notebook beside the chapter\n")
        toc = (
            "project:\n  toc:\n    - file: content/a.md\n    - file: content/part/A/index.md\n"
            "      children:\n        - file: content/part/A/A.ipynb\n    - file: content/part/B/index.md\n"
        )
        (repo / "toc.yml").write_text(toc)
        at_a, at_b, plain = "/content/part/A/index.md", "/content/part/B/index.md", "/content/a.md"

        good = {
            "a notebook-drawn figure beside its chapter": (at_a, _fig(_img("figures/a.png"))),
            "an exempt static image": (plain, _fig(_img(static))),
        }
        bad = {
            "an embedded notebook output": (at_a, _fig(_out(*png))),
            "a figure with two images": (at_a, _fig(_img("figures/a.png"), _img("figures/b.png"))),
            "an unlisted static image": (plain, _fig(_img("/content/figures/B/b.png"))),
            "an empty figure": (at_a, _fig({"type": "_lift"})),
            "a placeholder": (at_a, _fig(_img("figures/a.png", placeholder=True))),
            "a figures/ file on a chapter with no notebook": (at_b, _fig(_img("figures/x.png"))),
            "a figures/ file on a page that is not a chapter": (plain, _fig(_img("figures/x.png"))),
            "an image from somewhere else": (at_a, _fig(_img("../pictures/a.png"))),
            "an unlisted image outside a figure": (plain, {"type": "root", "children": [_img("/x.png")]}),
        }
        for name, (location, node) in good.items():
            if figure_problems("p", location, node, exempt, set(), repo):
                failures.append(f"figure check rejected {name}: {figure_problems('p', location, node, exempt, set(), repo)}")
        for name, (location, node) in bad.items():
            if not figure_problems("p", location, node, exempt, set(), repo):
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
        if toc_parents(toc) != {"content/a.md": None, "content/part/A/index.md": None, "content/part/A/A.ipynb": "content/part/A/index.md", "content/part/B/index.md": None}:
            failures.append(f"toc parents misread: {toc_parents(toc)}")

        # End to end on a synthetic build.
        build = Path(tmp) / "html"
        build.mkdir()
        nb_loc = "/content/part/A/A.ipynb"

        def page(slug, kind, location, mdast):
            (build / f"{slug}.json").write_text(json.dumps({"kind": kind, "location": location, "mdast": mdast}))

        def write_config(slugs):
            (build / "config.json").write_text(json.dumps({"projects": [{"index": "index", "pages": [{"slug": s} for s in slugs]}]}))

        def reset():
            page("index", "Article", "/README.md", {"type": "root", "children": []})
            page("content.a", "Article", plain, _fig(_img(static)))
            page("content.part.a", "Article", at_a, _fig(_img("figures/a.png")))
            page("content.part.a.a", "Notebook", nb_loc, _out(*png))
            page("content.old", "Notebook", "/content/old.ipynb", {"children": []})  # stale, not current
            write_config(["content.a", "content.part.a", "content.part.a.a"])

        reset()
        if check_figures(build, repo):
            failures.append(f"end-to-end check rejected a good build: {check_figures(build, repo)}")
        cases = {
            "a notebook built without outputs": lambda: page("content.part.a.a", "Notebook", nb_loc, {"children": []}),
            "a notebook not beside a chapter": lambda: (page("content.b", "Notebook", "/content/b.ipynb", _out(*png)), write_config(["content.a", "content.part.a", "content.part.a.a", "content.b"])),
            "a listed notebook that was not built as one": lambda: page("content.part.a.a", "Article", nb_loc, _out(*png)),
            "a notebook not listed under its chapter": lambda: (repo / "toc.yml").write_text(toc.replace("      children:\n        - file: content/part/A/A.ipynb\n", "    - file: content/part/A/A.ipynb\n")),
        }
        for name, spoil in cases.items():
            reset()
            (repo / "toc.yml").write_text(toc)
            spoil()
            if not check_figures(build, repo):
                failures.append(f"end-to-end check accepted {name}")
    return failures


def self_test_freshness() -> list[str]:
    failures = []
    from PIL import Image

    def png(shade: int, size=(40, 30), spot: int | None = None) -> bytes:
        image = Image.new("RGB", size, (shade, shade, shade))
        if spot is not None:
            image.putpixel((0, 0), (spot, spot, spot))
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        return buffer.getvalue()

    if rms_difference(png(100), png(100)) != 0.0:
        failures.append("identical images do not have RMS difference 0")
    if rms_difference(png(100), png(100, size=(41, 30))) is not None:
        failures.append("images of different sizes were compared")
    if not 0 < rms_difference(png(100), png(100, spot=110)) < TOLERANCE:
        failures.append("a one-pixel change is not within tolerance")
    if rms_difference(png(100), png(0)) <= TOLERANCE:
        failures.append("a wholly different image is within tolerance")

    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@x", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@x"}

    def git(*args, cwd):
        subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True)

    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp)
        figures = repo / "content/part/A/figures"
        figures.mkdir(parents=True)
        (figures / "a.png").write_bytes(png(100))
        git("init", "-q", "-b", "main", cwd=repo)
        git("add", "-A", cwd=repo)
        git("commit", "-q", "-m", "figures", cwd=repo)
        if figure_freshness(repo):
            failures.append(f"an unchanged figure was rejected: {figure_freshness(repo)}")
        (figures / "a.png").write_bytes(png(100, spot=110))
        if figure_freshness(repo):
            failures.append("a figure redrawn within tolerance was rejected")
        (figures / "a.png").write_bytes(png(0))
        if not figure_freshness(repo):
            failures.append("a figure that differs from the committed one was accepted")
        (figures / "a.png").write_bytes(png(100, size=(41, 30)))
        if not figure_freshness(repo):
            failures.append("a figure of a new size was accepted")
        (figures / "a.png").write_bytes(png(100))
        (figures / "b.png").write_bytes(png(50))
        if not figure_freshness(repo):
            failures.append("a drawn but uncommitted figure was accepted")
        (figures / "b.png").unlink()
        (figures / "a.png").unlink()
        if not figure_freshness(repo):
            failures.append("a deleted committed figure was accepted")
    return failures


def self_test() -> bool:
    """Every check must reject input it is supposed to reject."""
    failures = self_test_site() + self_test_figures() + self_test_freshness()
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    repo = Path(".")
    problems = check(BUILD, REPO_SLUG)
    if not problems:
        problems = check_figures(BUILD, repo) + figure_freshness(repo)
    for p in problems:
        log.error("FAIL: %s", p)
    if problems:
        sys.exit(1)
    log.info(
        "built site looks servable: index.html ok, asset paths root-relative,"
        " every figure drawn by its notebook or exempt, and current"
    )
