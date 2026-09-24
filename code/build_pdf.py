"""Build exports/intertemporal-choice.pdf with links that work outside the website.

`myst build --pdf` exports every link to another page as a site-relative
`\\href{/content/...}`, which goes nowhere in a PDF, and drops links to Math Facts
entries (`[LogELogNormTimes](#fact:logelognormtimes)`) altogether, leaving bare text.
MyST never emits a LaTeX \\ref to another chapter, so a link to the published site is
the best the PDF can carry. Writing those URLs into the Markdown would fix the PDF but
turn every cross-reference on the website into an unchecked external link that breaks
whenever a page moves, so the Markdown is left alone and the fix happens here:

  1. stage a copy of the project in _build/pdf-src
  2. in the staged Markdown only, rewrite each `](#fact:...)` link to the fact's anchor
     on the site, so the export keeps it as a link
  3. run `myst build --pdf` in the staged copy
  4. rewrite every `\\href{/` in the generated LaTeX to an absolute URL on the site, and
     check that each one names a page the book actually has
  5. rerun MyST's own latexmk command and copy the PDF (with its .tex and logs) back
     to exports/

`--self-test` runs the rewriting and checking functions against input they should
change or reject, and fails if any of them does not.

Usage: uv run python code/build_pdf.py [--self-test]
"""

import argparse
import logging
import re
import shutil
import subprocess
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

SITE = "https://intertemporal-choice.github.io"
STAGE = Path("_build/pdf-src")
NAME = "intertemporal-choice"  # matches `output:` of the tex+pdf export in myst.yml
TEX_DIR = Path("exports") / f"{NAME}_pdf_tex"
LOG_DIR = Path("exports") / f"{NAME}_pdf_logs"
PDF = Path("exports") / f"{NAME}.pdf"
# The command MyST itself runs (jtex pdfTexExportCommand, plain_latex_book's engine).
LATEXMK = [
    "latexmk", "-f", "-xelatex", "-synctex=1", "-interaction=batchmode",
    "-file-line-error", '-latexoption=-shell-escape', f"{NAME}.tex",
]
SKIP = {".git", "_build", ".venv", "exports", "sources", "node_modules", ".DS_Store"}

FACT_DEF = re.compile(r"^\((fact:[^)\s]+)\)=", re.M)
# A label directly above a page's first heading names the page: MyST lifts that heading
# into the page title, which has no anchor on the site.
TITLE_LABEL = re.compile(r"\A\s*\((fact:[^)\s]+)\)=\s*\n#\s")
FACT_LINK = re.compile(r"\]\(#(fact:[^)\s]+)\)")
REL_HREF = re.compile(r"\\href\{/")
SITE_HREF = re.compile(r"\\href\{" + re.escape(SITE) + r"(/[^}#\\]*)")


def slug(name: str) -> str:
    """MyST's URL slug for a file or folder name (mystmd createSlug).

    A leading enumeration is dropped unless it looks like a year or a five-digit
    number, which is why 2PeriodLCModel.md is served at .../periodlcmodel.
    """
    if not re.match(r"^[12][0-9]{3}([^0-9]|$)|^[0-9]{5}", name):
        name = re.sub(r"^[0-9_.-]+", "", name) or name
    name = re.sub(r"[^a-z0-9-]", "-", name.replace("&", "-and-").lower())
    return re.sub(r"-{2,}", "-", name).strip("-")[:50]


def html_id(label: str) -> str:
    """MyST's anchor for a label (mystmd createHtmlId): fact:elognorm -> fact-elognorm."""
    s = re.sub(r"[^a-z0-9-]", "-", label.lower())
    s = re.sub(r"^([0-9-])", r"id-\1", s)
    return re.sub(r"-{2,}", "-", s).strip("-")


def page_url(md: Path, root: Path) -> str:
    """Site path of a Markdown page: content/asset_pricing/C-CAPM.md -> /content/asset-pricing/c-capm."""
    parts = md.relative_to(root).with_suffix("").parts
    return "/" + "/".join(slug(p) for p in parts)


def label_targets(text: str, url: str) -> dict[str, str]:
    """The `(fact:x)=` labels in one page's text, each mapped to its URL on the site."""
    title = TITLE_LABEL.match(text)
    return {
        label: url if title and label == title.group(1) else f"{url}#{html_id(label)}"
        for label in FACT_DEF.findall(text)
    }


def fact_targets(root: Path) -> dict[str, str]:
    """Every `(fact:x)=` label in the content, mapped to its absolute URL on the site."""
    targets = {}
    for md in sorted((root / "content").rglob("*.md")):
        targets |= label_targets(md.read_text(), SITE + page_url(md, root))
    return targets


def rewrite_fact_links(text: str, targets: dict[str, str]) -> tuple[str, int]:
    """Point `](#fact:x)` links at the site; an unknown label is an error, not a skip."""
    def sub(m):
        if m.group(1) not in targets:
            raise KeyError(f"link to undefined fact label {m.group(1)}")
        return f"]({targets[m.group(1)]})"
    return FACT_LINK.subn(sub, text)


def absolutize(tex: str) -> tuple[str, int]:
    """Prefix site-relative \\href targets with the site's URL."""
    return REL_HREF.subn(lambda m: "\\href{" + SITE + "/", tex)


def unknown_pages(tex: str, pages: set[str]) -> list[str]:
    """Absolute site links whose path is not a page of the book."""
    return sorted({p for p in SITE_HREF.findall(tex) if p.rstrip("/") not in pages and p != "/"})


def run(cmd, cwd: Path) -> None:
    log.info("$ %s  (in %s)", " ".join(cmd), cwd)
    subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def stage(root: Path) -> None:
    shutil.rmtree(STAGE, ignore_errors=True)
    shutil.copytree(root, STAGE, ignore=lambda d, names: [n for n in names if n in SKIP])
    # Reuse the downloaded LaTeX template rather than fetching it again.
    templates = root / "_build" / "templates"
    if templates.exists():
        shutil.copytree(templates, STAGE / "_build" / "templates")


def build(root: Path) -> list[str]:
    failures = []
    stage(root)

    targets = fact_targets(STAGE)
    n_facts = 0
    for md in (STAGE / "content").rglob("*.md"):
        text, n = rewrite_fact_links(md.read_text(), targets)
        if n:
            md.write_text(text)
            n_facts += n
    log.info("fact links pointed at the site: %d", n_facts)

    run(["myst", "build", "--pdf"], STAGE)

    pages = {page_url(md, STAGE) for md in (STAGE / "content").rglob("*.md")}
    tex_dir = STAGE / TEX_DIR
    n_pages = 0
    for tex_file in tex_dir.glob("*.tex"):
        tex, n = absolutize(tex_file.read_text())
        n_pages += n
        if n:
            tex_file.write_text(tex)
        if REL_HREF.search(tex):
            failures.append(f"{tex_file.name} still has a site-relative \\href")
        for p in unknown_pages(tex, pages):
            failures.append(f"{tex_file.name} links to {SITE}{p}, which is not a page of the book")
    log.info("page links made absolute: %d", n_pages)
    if failures:
        return failures

    old = tex_dir / f"{NAME}.pdf"
    old.unlink(missing_ok=True)
    try:
        run(LATEXMK, tex_dir)
    except subprocess.CalledProcessError:
        pass  # latexmk -f exits non-zero on warnings; the PDF's existence is the test
    if not old.exists():
        return [f"latexmk produced no PDF; see {tex_dir}/{NAME}.log"]

    for rel in (TEX_DIR, LOG_DIR):
        shutil.rmtree(root / rel, ignore_errors=True)
        if (STAGE / rel).exists():
            shutil.copytree(STAGE / rel, root / rel)
    shutil.copyfile(old, root / PDF)
    log.info("wrote %s", PDF)
    return []


def self_test() -> bool:
    """Every rewrite and check must act on input it is supposed to act on."""
    ok = True
    targets = {"fact:elognorm": f"{SITE}/content/numerical/mathfactslist#fact-elognorm"}
    text, n = rewrite_fact_links("fact [ELogNorm](#fact:elognorm) and [x](#sec:y)", targets)
    if n != 1 or targets["fact:elognorm"] not in text or "#sec:y" not in text:
        log.error("SELF-TEST FAIL: fact link rewrite missed its target or touched a sec link")
        ok = False
    try:
        rewrite_fact_links("[Nope](#fact:nope)", targets)
        log.error("SELF-TEST FAIL: link to an undefined fact label was accepted")
        ok = False
    except KeyError:
        pass
    tex, n = absolutize(r"see \href{/content/consumption/envelope}{Envelope} and \href{https://x.org}{x}")
    if n != 1 or REL_HREF.search(tex) or "https://x.org" not in tex:
        log.error("SELF-TEST FAIL: absolutize did not rewrite exactly the relative link")
        ok = False
    pages = {"/content/consumption/envelope"}
    if unknown_pages(tex, pages):
        log.error("SELF-TEST FAIL: a link to an existing page was reported unknown")
        ok = False
    if not unknown_pages(rf"\href{{{SITE}/content/gone/page}}{{x}}", pages):
        log.error("SELF-TEST FAIL: a link to a missing page was not reported")
        ok = False
    if unknown_pages(rf"\href{{{SITE}/content/consumption/envelope\#fact-x}}{{x}}", pages):
        log.error("SELF-TEST FAIL: an escaped anchor was read as part of the page path")
        ok = False
    for md, want in [
        ("content/asset_pricing/C-CAPM.md", "/content/asset-pricing/c-capm"),
        ("content/consumption/2PeriodLCModel.md", "/content/consumption/periodlcmodel"),
    ]:
        if page_url(Path("r") / md, Path("r")) != want:
            log.error("SELF-TEST FAIL: page_url(%s) no longer matches MyST's slug %s", md, want)
            ok = False
    got = label_targets("(fact:page)=\n# Title\n\n(fact:x)=\n:::{note}\n", "U")
    if got != {"fact:page": "U", "fact:x": "U#fact-x"}:
        log.error("SELF-TEST FAIL: page-title and in-page labels mapped to %s", got)
        ok = False
    if html_id("fact:logelognormtimes") != "fact-logelognormtimes":
        log.error("SELF-TEST FAIL: html_id no longer matches MyST's anchors")
        ok = False
    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    problems = build(Path.cwd())
    for p in problems:
        log.error("FAIL: %s", p)
    sys.exit(1 if problems else 0)
