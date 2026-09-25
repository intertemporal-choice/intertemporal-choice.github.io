"""Build exports/intertemporal-choice.pdf with links that work outside the website.

`myst build --pdf` exports every link to another page as a site-relative
`\\href{/content/...}`, which goes nowhere in a PDF, and drops links to Math Facts
entries (`[LogELogNormTimes](#fact:logelognormtimes)`) altogether, leaving bare text.
A link with text to a section heading (`[the appendix on X](#sec:x)`) comes out as
`Section~\\ref{sec:x}`, which drops the text and, for a section too deep to be numbered,
names its numbered parent instead. A page link cannot become a LaTeX \\ref at all, so a
link to the published site is the best the PDF can carry. Writing those URLs into the Markdown would fix the PDF but
turn every cross-reference on the website into an unchecked external link that breaks
whenever a page moves, so the Markdown is left alone and the fix happens here:

  1. stage a copy of the project in _build/pdf-src
  2. in the staged Markdown only, rewrite each `](#fact:...)` link, and each link with
     text to a section heading, to that anchor on the site, so the export keeps the link
     and its text
  3. run `myst build --pdf --execute` in the staged copy through code/build_site.py, reusing
     the execution cache the HTML build filled, so every figure is its notebook's output,
     and check that every figure in the generated LaTeX includes an image that exists
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

import build_site  # code/build_site.py: `myst build --execute` with its own Jupyter server

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

SITE = "https://intertemporal-choice.github.io"
STAGE = Path("_build/pdf-src")
MYST_LOG = Path("_build/pdf-src-myst.log")
LATEXMK_LOG = Path("_build/pdf-src-latexmk.log")
NAME = "intertemporal-choice"  # matches `output:` of the tex+pdf export in myst.yml
TEX_DIR = Path("exports") / f"{NAME}_pdf_tex"
LOG_DIR = Path("exports") / f"{NAME}_pdf_logs"
PDF = Path("exports") / f"{NAME}.pdf"
# The command MyST itself runs (jtex pdfTexExportCommand, plain_latex_book's engine).
LATEXMK = [
    "latexmk",
    "-f",
    "-xelatex",
    "-synctex=1",
    "-interaction=batchmode",
    "-file-line-error",
    "-latexoption=-shell-escape",
    f"{NAME}.tex",
]
SKIP = {
    ".git",
    ".claude",
    "_build",
    ".venv",
    "exports",
    "sources",
    "node_modules",
    ".DS_Store",
    ".ipynb_checkpoints",
}

FACT_DEF = re.compile(r"^\((fact:[^)\s]+)\)=", re.MULTILINE)
# A label directly above a page's first heading names the page: MyST lifts that heading
# into the page title, which has no anchor on the site.
TITLE_LABEL = re.compile(r"\A\s*\((fact:[^)\s]+)\)=\s*\n#\s")
FACT_LINK = re.compile(r"\]\(#(fact:[^)\s]+)\)")
SECTION_DEF = re.compile(r"^\(((?:sub)*sec:[^)\s]+)\)=\s*\n#", re.MULTILINE)
TITLE_SECTION = re.compile(r"\A\s*\(((?:sub)*sec:[^)\s]+)\)=\s*\n#\s")
SECTION_LINK = re.compile(r"\[([^\]]+)\]\(#((?:sub)*sec:[^)\s]+)\)")
REL_HREF = re.compile(r"\\href\{/")
SITE_HREF = re.compile(r"\\href\{" + re.escape(SITE) + r"(/[^}#\\]*)")


def slug(name: str) -> str:
    """MyST's URL slug for a file or folder name (mystmd createSlug).

    A leading enumeration is dropped unless it looks like a year or a five-digit
    number, so a page named 2PeriodLCModel.md would be served at .../periodlcmodel.
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
    """Site path of a Markdown page: content/asset_pricing/C-CAPM.md -> /content/asset-pricing/c-capm.

    A part's index.md is served at the part's own path: content/growth/index.md -> /content/growth.
    """
    parts = md.relative_to(root).with_suffix("").parts
    if parts[-1] == "index":
        parts = parts[:-1]
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


def section_label_targets(text: str, url: str) -> dict[str, str]:
    """The `(sec:x)=` labels on one page's headings, each mapped to its anchor on the site.

    A label on the page's title is left out: MyST exports a link to it as a link to the
    page, which step 4 makes absolute.
    """
    title = TITLE_SECTION.match(text)
    return {
        label: f"{url}#{html_id(label)}"
        for label in SECTION_DEF.findall(text)
        if not (title and label == title.group(1))
    }


def rewrite_section_links(text: str, targets: dict[str, str]) -> tuple[str, int]:
    """Point `[text](#sec:x)` links to a heading below a page title at the site.

    A link without text is left alone: MyST fills in the section's title, and
    `Section~\\ref` is then the right rendering.
    """
    count = 0

    def sub(m):
        nonlocal count
        if m.group(2) not in targets:
            return m.group(0)
        count += 1
        return f"[{m.group(1)}]({targets[m.group(2)]})"

    return SECTION_LINK.sub(sub, text), count


def absolutize(tex: str) -> tuple[str, int]:
    """Prefix site-relative \\href targets with the site's URL."""
    return REL_HREF.subn(lambda _: "\\href{" + SITE + "/", tex)


def unknown_pages(tex: str, pages: set[str]) -> list[str]:
    """Absolute site links whose path is not a page of the book."""
    return sorted(
        {p for p in SITE_HREF.findall(tex) if p.rstrip("/") not in pages and p != "/"}
    )


def run(cmd, cwd: Path, output: Path) -> int:
    """Run cmd in cwd with its output saved to output; return its exit code."""
    log.info("$ %s  (in %s, output in %s)", " ".join(cmd), cwd, output)
    with output.open("w") as out:
        return subprocess.run(
            cmd, cwd=cwd, stdout=out, stderr=subprocess.STDOUT, check=False
        ).returncode


def stage(root: Path) -> None:
    shutil.rmtree(STAGE, ignore_errors=True)
    shutil.copytree(
        root, STAGE, ignore=lambda _, names: [n for n in names if n in SKIP]
    )
    # Reuse the downloaded LaTeX template rather than fetching it again, and the executed
    # notebooks: their cache key is the cell code plus IC_EXEC_ENV, which the staged build is
    # given from the original tree, so nothing that the HTML build ran runs again.
    for cached in ("templates", "execute"):
        if (root / "_build" / cached).exists():
            shutil.copytree(root / "_build" / cached, STAGE / "_build" / cached)


def rewrite_staged_facts() -> None:
    """Step 2: point every fact link, and every link with text to a section, at the site."""
    targets = fact_targets(STAGE)
    sections = {}
    for md in sorted((STAGE / "content").rglob("*.md")):
        sections |= section_label_targets(md.read_text(), SITE + page_url(md, STAGE))
    n_facts = n_sections = 0
    for md in (STAGE / "content").rglob("*.md"):
        text, n = rewrite_fact_links(md.read_text(), targets)
        text, m = rewrite_section_links(text, sections)
        if n or m:
            md.write_text(text)
            n_facts += n
            n_sections += m
    log.info("fact links pointed at the site: %d", n_facts)
    log.info("section links pointed at the site: %d", n_sections)


def absolutize_tex() -> list[str]:
    """Step 4: make every page link absolute and check that each names a real page."""
    pages = {page_url(md, STAGE) for md in (STAGE / "content").rglob("*.md")}
    failures, n_pages = [], 0
    for tex_file in (STAGE / TEX_DIR).glob("*.tex"):
        tex, n = absolutize(tex_file.read_text())
        n_pages += n
        if n:
            tex_file.write_text(tex)
        if REL_HREF.search(tex):
            failures.append(f"{tex_file.name} still has a site-relative \\href")
        failures += [
            f"{tex_file.name} links to {SITE}{p}, which is not a page of the book"
            for p in unknown_pages(tex, pages)
        ]
    log.info("page links made absolute: %d", n_pages)
    return failures


def compile_and_copy(root: Path) -> list[str]:
    """Step 5: rerun latexmk on the fixed LaTeX and copy the results back to exports/."""
    tex_dir = STAGE / TEX_DIR
    pdf = tex_dir / f"{NAME}.pdf"
    pdf.unlink(missing_ok=True)
    # latexmk -f exits non-zero on warnings; the PDF's existence is the test.
    run(LATEXMK, tex_dir, root / LATEXMK_LOG)
    if not pdf.exists():
        return [f"latexmk produced no PDF; see {tex_dir}/{NAME}.log and {LATEXMK_LOG}"]
    for rel in (TEX_DIR, LOG_DIR):
        shutil.rmtree(root / rel, ignore_errors=True)
        if (STAGE / rel).exists():
            shutil.copytree(STAGE / rel, root / rel)
    shutil.copyfile(pdf, root / PDF)
    log.info("wrote %s", PDF)
    return []


FIGURE_ENV = re.compile(r"\\begin\{figure\}(.*?)\\end\{figure\}", re.S)
INCLUDE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")


def missing_graphics(tex: str, exists) -> list[str]:
    """Figures in the LaTeX with no \\includegraphics, or one naming a file that is absent."""
    problems = []
    for n, body in enumerate(FIGURE_ENV.findall(tex), 1):
        files = INCLUDE.findall(body)
        if not files:
            problems.append(f"figure {n} includes no image")
        problems += [f"figure {n} includes {f}, which does not exist" for f in files if not exists(f)]
    return problems


def figure_failures() -> list[str]:
    """Step 3's check: every figure in the generated LaTeX shows an image that exists."""
    tex_dir = STAGE / TEX_DIR
    return [
        f"{tex_file.name}: {p}"
        for tex_file in sorted(tex_dir.glob("*.tex"))
        for p in missing_graphics(tex_file.read_text(), lambda f: (tex_dir / f).is_file())
    ]


def build(root: Path) -> list[str]:
    stage(root)
    rewrite_staged_facts()
    if build_site.build(
        ["--pdf"],
        root=STAGE,
        exec_env=build_site.env_hash(root),
        output=root / MYST_LOG,
    ):
        return [f"myst build --pdf --execute failed; see {MYST_LOG}"]
    # Keep anything the staged build had to execute, so the next build need not.
    if (STAGE / "_build" / "execute").exists():
        shutil.copytree(STAGE / "_build" / "execute", root / "_build" / "execute", dirs_exist_ok=True)
    return absolutize_tex() or figure_failures() or compile_and_copy(root)


def raises_key_error(fn, *args) -> bool:
    try:
        fn(*args)
    except KeyError:
        return True
    return False


def fact_failures() -> list[str]:
    """Failures of the fact-link rewrite and the label-to-URL mapping."""
    targets = {"fact:elognorm": f"{SITE}/content/numerical/mathfactslist#fact-elognorm"}
    text, n = rewrite_fact_links(
        "fact [ELogNorm](#fact:elognorm) and [x](#sec:y)", targets
    )
    title = label_targets("(fact:page)=\n# Title\n\n(fact:x)=\n:::{note}\n", "U")
    return [
        msg
        for bad, msg in [
            (
                n != 1 or targets["fact:elognorm"] not in text or "#sec:y" not in text,
                "fact link rewrite missed its target or touched a sec link",
            ),
            (
                not raises_key_error(rewrite_fact_links, "[Nope](#fact:nope)", targets),
                "link to an undefined fact label was accepted",
            ),
            (
                title != {"fact:page": "U", "fact:x": "U#fact-x"},
                f"page-title and in-page labels mapped to {title}",
            ),
            (
                html_id("fact:logelognormtimes") != "fact-logelognormtimes",
                "html_id no longer matches MyST's anchors",
            ),
        ]
        if bad
    ]


def section_failures() -> list[str]:
    """Failures of the section-link rewrite."""
    page = "(sec:page)=\n# Title\n\n(sec:here)=\n## Here\n\n(eq:x)=\n"
    targets = section_label_targets(page, "U")
    links = (
        "See [the part here](#sec:here), [the title](#sec:page), [](#sec:here)"
        " and [elsewhere](#sec:elsewhere)."
    )
    text, n = rewrite_section_links(links, targets)
    return [
        msg
        for bad, msg in [
            (targets != {"sec:here": "U#sec-here"}, f"section labels mapped to {targets}"),
            (n != 1, f"rewrote {n} section links, not 1"),
            ("[the part here](U#sec-here)" not in text, "section link not pointed at its anchor"),
            ("[the title](#sec:page)" not in text, "link to a page's title label was rewritten"),
            (
                "[](#sec:here)" not in text,
                "a link without text was rewritten; MyST fills in its title",
            ),
            ("[elsewhere](#sec:elsewhere)" not in text, "link to an unknown label was rewritten"),
        ]
        if bad
    ]


def href_failures() -> list[str]:
    """Failures of the LaTeX \\href rewrite and the page check."""
    tex, n = absolutize(
        r"see \href{/content/consumption/envelope}{Envelope} and \href{https://x.org}{x}"
    )
    pages = {"/content/consumption/envelope"}
    return [
        msg
        for bad, msg in [
            (
                n != 1 or REL_HREF.search(tex) or "https://x.org" not in tex,
                "absolutize did not rewrite exactly the relative link",
            ),
            (
                unknown_pages(tex, pages),
                "a link to an existing page was reported unknown",
            ),
            (
                not unknown_pages(rf"\href{{{SITE}/content/gone/page}}{{x}}", pages),
                "a link to a missing page was not reported",
            ),
            (
                unknown_pages(
                    rf"\href{{{SITE}/content/consumption/envelope\#fact-x}}{{x}}", pages
                ),
                "an escaped anchor was read as part of the page path",
            ),
        ]
        if bad
    ]


def url_failures() -> list[str]:
    """Failures of the Markdown-path-to-URL mapping."""
    return [
        f"page_url({md}) no longer matches MyST's URL {want}"
        for md, want in [
            ("content/asset_pricing/C-CAPM.md", "/content/asset-pricing/c-capm"),
            (
                "content/consumption/2PeriodLCModel.md",
                "/content/consumption/periodlcmodel",
            ),
            ("content/growth/index.md", "/content/growth"),
        ]
        if page_url(Path("r") / md, Path("r")) != want
    ]


def graphics_failures() -> list[str]:
    """Failures of the figure check on LaTeX it must accept or reject."""
    have = {"files/a.png"}.__contains__
    good = "\\begin{figure}\\includegraphics[width=0.7\\linewidth]{files/a.png}\\end{figure}"
    return [
        msg
        for bad, msg in [
            (bool(missing_graphics(good, have)), "figure check rejected a figure with its image"),
            (
                not missing_graphics(good.replace("files/a.png", "files/b.png"), have),
                "figure check accepted a figure whose image file is missing",
            ),
            (
                not missing_graphics("\\begin{figure}\\caption{x}\\end{figure}", have),
                "figure check accepted a figure with no image",
            ),
        ]
        if bad
    ]


def self_test() -> bool:
    """Every rewrite and check must act on input it is supposed to act on."""
    failures = (
        fact_failures()
        + section_failures()
        + href_failures()
        + url_failures()
        + graphics_failures()
    )
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

    problems = build(Path.cwd())
    for p in problems:
        log.error("FAIL: %s", p)
    sys.exit(1 if problems else 0)
