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
     on the site, so the export keeps it as a link; likewise each link to a label on a
     page the PDF leaves out (the Supplemental Notes), which MyST would otherwise export
     as a \\ref to a label the PDF lacks, printed "??". A link with words to a label the
     PDF has, `[the golden rule](#eq:RCK-goldenRule)`, MyST would print as its number
     alone, "(7)", losing the words; it is pointed at a placeholder address instead, so
     the export keeps the words. A `{margin}` note, which MyST's PDF export leaves out
     altogether, becomes a footnote on the paragraph before it, so the PDF keeps it
  3. run `myst build --pdf` in the staged copy
  4. in the generated LaTeX, turn each placeholder link into `\\hyperref[label]{words}`, a
     link inside the PDF that keeps its words; give each page's first heading the labels
     MyST leaves off (the page's own label, and `page:<its path on the site>`), so a link
     to a whole page in the PDF, `\\href{/content/...}`, becomes one inside it too; check
     that every such link has its label. Then rewrite every remaining `\\href{/` to an
     absolute URL on the site, and check that each one names a page the book actually has
  5. tidy the bibliography, map each character the text font lacks (the prime in E′) to
     something it can print, and put the title of each figure marked note-under above it and its
     "Note:" in small type just under it; then rerun MyST's own latexmk command, copy the PDF (with its
     .tex and logs) back to exports/, and fail if LaTeX's log says a character was still
     left out

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

import build_lite  # beside this file: the in-browser notebooks the site publishes

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
    ".ipynb_checkpoints",  # Jupyter autosaves beside the figure notebooks
}

FACT_DEF = re.compile(r"^\((fact:[^)\s]+)\)=", re.MULTILINE)
# A label directly above a page's first heading names the page: MyST lifts that heading
# into the page title, which has no anchor on the site.
# A page may open with front matter (a `math:` block, say) before its title's label.
FRONT_MATTER = r"(?s:---\n.*?\n---\n)?"
TITLE_LABEL = re.compile(r"\A" + FRONT_MATTER + r"\s*\((fact:[^)\s]+)\)=\s*\n#\s")
FACT_LINK = re.compile(r"\]\(#(fact:[^)\s]+)\)")
# Any label: a `(label)=` target, or a directive's `:label:` or `:name:` option.
LABEL_DEF = re.compile(r"^[ \t]*(?:\(([^)\s]+)\)=|:(?:label|name):[ \t]*(\S+))", re.MULTILINE)
PAGE_TITLE_LABEL = re.compile(r"\A" + FRONT_MATTER + r"\s*\(([^)\s]+)\)=\s*\n#\s")
LINK = re.compile(r"\]\(#([^)\s]+)\)")
ROLE = re.compile(r"\{(?:eq|ref|numref)\}`(?:[^`<]*<)?([^`<>]+)>?`")
REL_HREF = re.compile(r"\\href\{/")
# Where step 2 points a link with words to a label the PDF has; no such site exists.
PLACEHOLDER = "https://pdf-internal.invalid/"
PLACEHOLDER_HREF = re.compile(r"\\href\{" + re.escape(PLACEHOLDER) + r"([^}]*)\}\{")
PAGE_HREF = re.compile(r"\\href\{(/[^}#\\]*)\}\{")
# A label \\hyperref can take as it stands.
PLAIN_LABEL = re.compile(r"\A[A-Za-z0-9:._/-]+\Z")
HEADING = re.compile(r"^\\(?:part|chapter|section|subsection|subsubsection)\*?\{.*$", re.MULTILINE)
INCLUDE = re.compile(r"^\\include\{([^}]+)\}", re.MULTILINE)
DEFINED_LABEL = re.compile(r"\\label\{([^}]+)\}")
USED_LABEL = re.compile(r"\\hyperref\[([^\]]+)\]")
SITE_HREF = re.compile(r"\\href\{" + re.escape(SITE) + r"(/[^}#\\]*)")
# Characters the PDF's text font (Latin Modern, T1) lacks, with what prints in their place. XeLaTeX drops a
# character its font lacks, with only a line in its log: the prime that names a new point in a figure, E′ or A′,
# printed E or A.
TEXT_GLYPHS = {"′": r"\ensuremath{{}^{\prime}}"}
MISSING_CHAR = re.compile(r'^Missing character: There is no (.+?) \("([0-9A-F]+)\) in font ([^!]+)!', re.MULTILINE)


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


def pdf_articles(config: str) -> set[str]:
    """The files the tex+pdf export in myst.yml's text puts in the PDF."""
    return set(pdf_article_list(config))


def all_label_targets(text: str, url: str) -> dict[str, str]:
    """Every label in one page's text, each mapped to its URL on the site."""
    title = PAGE_TITLE_LABEL.match(text)
    labels = [a or b for a, b in LABEL_DEF.findall(text)]
    return {label: url if title and label == title.group(1) else f"{url}#{html_id(label)}" for label in labels}


def web_only_targets(root: Path) -> dict[str, str]:
    """Every label on a page the PDF leaves out, mapped to its absolute URL on the site."""
    in_pdf = pdf_articles((root / "myst.yml").read_text())
    targets = {}
    for md in sorted((root / "content").rglob("*.md")):
        if md.relative_to(root).as_posix() not in in_pdf:
            targets |= all_label_targets(md.read_text(), SITE + page_url(md, root))
    return targets


def rewrite_web_only_links(text: str, targets: dict[str, str]) -> tuple[str, int]:
    """Point `](#label)` links to a label on a page the PDF leaves out at the site.

    A role ({eq}, {ref}, {numref}) to such a label has no text of its own to keep as a
    link, so it is an error: write it as a link with words instead.
    """
    roles = sorted({m.group(1) for m in ROLE.finditer(text) if m.group(1) in targets})
    if roles:
        raise ValueError(f"role to a label the PDF leaves out (make it a link with words): {', '.join(roles)}")
    rewritten = [m for m in LINK.finditer(text) if m.group(1) in targets]
    return LINK.sub(lambda m: f"]({targets[m.group(1)]})" if m.group(1) in targets else m.group(0), text), len(rewritten)


def rewrite_staged_web_only() -> None:
    """Step 2, continued: in the pages the PDF has, point links to labels on pages it leaves out at the site."""
    targets = web_only_targets(STAGE)
    n_links = 0
    for rel in sorted(pdf_articles((STAGE / "myst.yml").read_text())):
        md = STAGE / rel
        if md.suffix != ".md":
            continue
        try:
            text, n = rewrite_web_only_links(md.read_text(), targets)
        except ValueError as e:
            raise ValueError(f"{rel}: {e}") from None
        if n:
            md.write_text(text)
            n_links += n
    log.info("links to pages left out of the PDF pointed at the site: %d", n_links)


def pdf_article_list(config: str) -> list[str]:
    """The files the tex+pdf export puts in the PDF, in its order, which is the order of its \\include's."""
    import yaml

    exports = yaml.safe_load(config)["project"]["exports"]
    return [a["file"] for e in exports if "pdf" in e.get("format", "") for a in e.get("articles", [])]


def pdf_labels(root: Path) -> set[str]:
    """Every label on a page the PDF has."""
    labels = set()
    for rel in pdf_article_list((root / "myst.yml").read_text()):
        if rel.endswith(".md"):
            labels |= {a or b for a, b in LABEL_DEF.findall((root / rel).read_text())}
    return labels


def keep_link_words(text: str, labels: set[str]) -> tuple[str, int]:
    """Point each `[words](#label)` link to a label the PDF has at the placeholder address, so
    the export keeps its words; step 4 turns it into \\hyperref. A link without words,
    `[](#label)`, is left for MyST to print as the label's number, and roles are left alone."""
    count = 0

    def sub(m):
        nonlocal count
        label = m.group(1)
        if label not in labels or text[m.start() - 1] == "[":
            return m.group(0)
        if not PLAIN_LABEL.match(label):
            raise ValueError(f"label {label!r} has a character \\hyperref can't take as it stands")
        count += 1
        return f"]({PLACEHOLDER}{label})"

    return LINK.sub(sub, text), count


def rewrite_staged_link_words() -> None:
    """Step 2, last: in the pages the PDF has, keep the words of links to labels it has."""
    labels = pdf_labels(STAGE)
    n_links = 0
    for rel in pdf_article_list((STAGE / "myst.yml").read_text()):
        md = STAGE / rel
        if md.suffix != ".md":
            continue
        try:
            text, n = keep_link_words(md.read_text(), labels)
        except ValueError as e:
            raise ValueError(f"{rel}: {e}") from None
        if n:
            md.write_text(text)
            n_links += n
    log.info("links with words to labels in the PDF kept for \\hyperref: %d", n_links)


def hyperref_placeholders(tex: str) -> tuple[str, int]:
    """Turn each placeholder link back into \\hyperref[label]{words}, a link inside the PDF."""
    def sub(m):
        label = m.group(1).replace("\\_", "_")
        return f"\\hyperref[{label}]{{"

    return PLACEHOLDER_HREF.subn(sub, tex)


def label_first_heading(tex: str, labels: list[str]) -> str:
    """Put labels on a page's first heading, which MyST leaves without the page's own."""
    m = HEADING.search(tex)
    if not m:
        raise ValueError("no heading to label")
    line = m.group(0)
    if line.count("{") != line.count("}"):
        raise ValueError(f"the first heading does not end on its line: {line[:60]}")
    return tex[: m.end()] + "".join(f"\\label{{{label}}}" for label in labels) + tex[m.end() :]


def hyperref_pages(tex: str, pages: set[str]) -> tuple[str, int]:
    """Turn each \\href{/path} to a page the PDF has into \\hyperref[page:/path], a link inside it."""
    count = 0

    def sub(m):
        nonlocal count
        if m.group(1) not in pages:
            return m.group(0)
        count += 1
        return f"\\hyperref[page:{m.group(1)}]{{"

    return PAGE_HREF.sub(sub, tex), count


def missing_labels(tex_files: dict[str, str]) -> list[str]:
    """Labels a \\hyperref names that no \\label defines, each with a file that uses it."""
    defined = {label for tex in tex_files.values() for label in DEFINED_LABEL.findall(tex)}
    return sorted(
        {f"{name}: \\hyperref[{label}] has no \\label"
         for name, tex in tex_files.items() for label in USED_LABEL.findall(tex) if label not in defined}
    )


def internalize_tex() -> list[str]:
    """Step 4, first: links to labels and pages the PDF has become links inside it."""
    tex_dir = STAGE / TEX_DIR
    articles = pdf_article_list((STAGE / "myst.yml").read_text())
    includes = INCLUDE.findall((tex_dir / f"{NAME}.tex").read_text())
    if len(includes) != len(articles):
        return [f"{NAME}.tex includes {len(includes)} files for {len(articles)} articles; cannot match them"]
    pages = {page_url(STAGE / rel, STAGE) for rel in articles}
    tex_files = {path.name: path.read_text() for path in tex_dir.glob("*.tex")}
    n_words = n_pages = 0
    for rel, include in zip(articles, includes):
        name = f"{include}.tex"
        if name not in tex_files:
            return [f"{NAME}.tex includes {name}, which MyST did not write"]
        title = PAGE_TITLE_LABEL.match((STAGE / rel).read_text()) if rel.endswith(".md") else None
        labels = ([title.group(1)] if title else []) + [f"page:{page_url(STAGE / rel, STAGE)}"]
        try:
            tex_files[name] = label_first_heading(tex_files[name], labels)
        except ValueError as e:
            return [f"{name}: {e}"]
    for name, tex in tex_files.items():
        tex, n = hyperref_placeholders(tex)
        tex, m = hyperref_pages(tex, pages)
        tex_files[name] = tex
        n_words, n_pages = n_words + n, n_pages + m
    failures = missing_labels(tex_files)
    failures += [f"{name} still has a placeholder link" for name, tex in tex_files.items() if PLACEHOLDER in tex]
    for name, tex in tex_files.items():
        (tex_dir / name).write_text(tex)
    log.info("links kept inside the PDF: %d with their words, %d to whole pages", n_words, n_pages)
    return failures


MARGIN = re.compile(r"^:::\{margin\}[^\n]*\n(.*?)\n:::[ \t]*$", re.S | re.M)
FENCE_LINE = re.compile(r"^\s*(`{3,}|:{3,})")


def margins_to_footnotes(text: str) -> tuple[str, int]:
    """Each `{margin}` note as a footnote: its marker at the end of the last line of prose before
    it (outside any fenced block, and not a heading or a label), its text as the definition, where
    the note was. MyST's PDF export drops margin notes; the site keeps them in the margin."""
    lines = text.split("\n")
    fenced, inside = [False] * len(lines), None  # which lines sit inside a fenced block
    for i, line in enumerate(lines):
        m = FENCE_LINE.match(line)
        if inside is None:
            if m:
                inside, fenced[i] = m.group(1), True
        else:
            fenced[i] = True
            if line.strip() == inside:
                inside = None
    notes = []
    for number, m in enumerate(MARGIN.finditer(text), 1):
        first = text[: m.start()].count("\n")
        anchor = next((j for j in range(first - 1, -1, -1)
                       if lines[j].strip() and not fenced[j] and not lines[j].lstrip().startswith("#")
                       and not re.fullmatch(r"\(\S+\)=", lines[j].strip())), None)
        if anchor is None:
            raise ValueError(f"the margin note at line {first + 1} has no prose before it to attach a footnote to")
        label = f"marginnote{number}"
        lines[anchor] = lines[anchor].rstrip() + f"[^{label}]"
        body = m.group(1).strip("\n").split("\n")
        definition = [f"[^{label}]: {body[0]}"] + [("    " + line) if line.strip() else "" for line in body[1:]]
        notes.append((first, m.group(0).count("\n") + 1, definition))
    for first, length, definition in reversed(notes):
        lines[first : first + length] = definition
    return "\n".join(lines), len(notes)


def rewrite_staged_margins() -> None:
    """Step 2, continued: in the pages the PDF has, margin notes become footnotes."""
    n_notes = 0
    for rel in sorted(pdf_articles((STAGE / "myst.yml").read_text())):
        md = STAGE / rel
        if md.suffix != ".md":
            continue
        try:
            text, n = margins_to_footnotes(md.read_text())
        except ValueError as e:
            raise ValueError(f"{rel}: {e}") from None
        if n:
            md.write_text(text)
            n_notes += n
    log.info("margin notes made footnotes for the PDF: %d", n_notes)


def absolutize(tex: str) -> tuple[str, int]:
    """Prefix site-relative \\href targets with the site's URL."""
    return REL_HREF.subn(lambda _: "\\href{" + SITE + "/", tex)


def lite_pages() -> set[str]:
    """The in-browser notebooks chapters link to: pages of the site, though not of the MyST project."""
    return {f"/lite/notebooks/index.html?path={Path(rel).name}" for rel in build_lite.NOTEBOOKS}


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


def clear(folder: Path) -> None:
    """Delete a stage. The copy keeps @resources/'s read-only modes, so its folders must be made writable first."""
    if folder.exists():
        for path in [folder, *folder.rglob("*")]:
            if path.is_dir() and not path.is_symlink():
                path.chmod(path.stat().st_mode | 0o200)
    shutil.rmtree(folder, ignore_errors=True)


def stage(root: Path) -> None:
    clear(STAGE)
    shutil.copytree(
        root, STAGE, ignore=lambda _, names: [n for n in names if n in SKIP]
    )
    # Reuse the downloaded LaTeX template rather than fetching it again.
    templates = root / "_build" / "templates"
    if templates.exists():
        shutil.copytree(templates, STAGE / "_build" / "templates")


def rewrite_staged_facts() -> None:
    """Step 2: point every fact link in the staged Markdown at the site."""
    targets = fact_targets(STAGE)
    n_facts = 0
    for md in (STAGE / "content").rglob("*.md"):
        text, n = rewrite_fact_links(md.read_text(), targets)
        if n:
            md.write_text(text)
            n_facts += n
    log.info("fact links pointed at the site: %d", n_facts)


def absolutize_tex() -> list[str]:
    """Step 4: make every page link absolute and check that each names a real page."""
    # The notebooks beside the chapters are pages of the site too, and chapters link to them.
    pages = {
        page_url(page, STAGE)
        for pattern in ("*.md", "*.ipynb")
        for page in (STAGE / "content").rglob(pattern)
        if ".ipynb_checkpoints" not in page.parts
    } | lite_pages()
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


BIB_ENTRY = re.compile(r"(?ms)^@\w+\{[^,\n]*,\n.*?^\}")
BIB_FIELD = re.compile(r"^(\s*)(\w+)(\s*=\s*)\{(.*)\},?$")
BARE_URL = re.compile(r"(?<![{/\w])(https?://[^\s{}%\\]+?)(?=[.,;:]?(?:\s|$))")


def tidy_bib_entry(entry: str) -> tuple[str, int]:
    """One entry of MyST's main.bib, with its URLs made breakable.

    MyST's export copies an entry's url into howpublished, and the bibliography prints that as plain text, which
    LaTeX can't break, so a long URL runs into the margin. The url field itself prints through \\url, which can
    break. So a howpublished that only repeats the url goes, and a bare URL left in a note or howpublished is
    wrapped in \\url.

    Two more repairs. A note that only repeats the url prints the address a second time after the url field's, so
    it goes too: economics.bib gives many entries note = {\\url{...}} for styles that print no url, and MyST's
    export strips the \\url, so the note arrives bare. And MyST exports a thesis as @misc, which the style prints
    without its type or school; an @misc with a school is made @phdthesis again, which prints the type field ("PhD
    dissertation") and the school. The style lowercases a type ("Phd"), and the export drops the braces that stop
    it, so the type is braced again. Returns the entry and the number of changes.
    """
    lines = entry.split("\n")
    fields = {m.group(2).lower(): m.group(4) for m in map(BIB_FIELD.match, lines) if m}
    out, n = [], 0
    if lines[0].lower().startswith("@misc{") and "school" in fields:
        lines[0] = "@phdthesis{" + lines[0][len("@misc{"):]
        n += 1
    url = fields.get("url")
    for line in lines:
        m = BIB_FIELD.match(line)
        if m and url and (m.group(2).lower(), m.group(4)) in (("howpublished", url), ("note", url), ("note", f"\\url{{{url}}}")):
            n += 1
            continue
        if m and m.group(2).lower() == "type" and lines[0].startswith("@phdthesis{") and not m.group(4).startswith("{"):
            n += 1
            line = f"{m.group(1)}{m.group(2)}{m.group(3)}{{{{{m.group(4)}}}}}" + ("," if line.rstrip().endswith(",") else "")
        if m and m.group(2).lower() in ("note", "howpublished"):
            value, k = BARE_URL.subn(r"\\url{\1}", m.group(4))
            if k:
                n += k
                line = f"{m.group(1)}{m.group(2)}{m.group(3)}{{{value}}}" + ("," if line.rstrip().endswith(",") else "")
        out.append(line)
    return "\n".join(out), n


def tidy_bib() -> list[str]:
    """Step 5: tidy MyST's bibliography: breakable URLs, no URL printed twice, theses as theses (tidy_bib_entry)."""
    bib = STAGE / TEX_DIR / "main.bib"
    if not bib.exists():
        return [f"{bib} not found: MyST's export no longer writes main.bib"]
    text, total = bib.read_text(), 0

    def sub(m):
        nonlocal total
        entry, n = tidy_bib_entry(m.group(0))
        total += n
        return entry

    text = BIB_ENTRY.sub(sub, text)
    bib.write_text(text)
    log.info("bibliography fields tidied: %d", total)
    return []


def map_glyphs(tex: str) -> str:
    """The main .tex, with each character of TEXT_GLYPHS mapped to what prints in its place, by newunicodechar."""
    if "\\begin{document}" not in tex:
        raise KeyError("\\begin{document}")
    maps = "".join(f"\\newunicodechar{{{ch}}}{{{glyph}}}\n" for ch, glyph in TEXT_GLYPHS.items())
    return tex.replace("\\begin{document}", "\\usepackage{newunicodechar}\n" + maps + "\\begin{document}", 1)


def map_glyphs_tex() -> list[str]:
    """Step 6: give the characters the text font lacks something to print (TEXT_GLYPHS)."""
    main = STAGE / TEX_DIR / f"{NAME}.tex"
    try:
        main.write_text(map_glyphs(main.read_text()))
    except KeyError:
        return [f"{main.name} has no \\begin{{document}} to put the character maps before"]
    log.info("characters mapped for the text font: %d", len(TEXT_GLYPHS))
    return []


# A figure marked `:class: note-under` puts its title above the image and its "Note:" paragraph just under it, in
# small type (Chris, 2026-11-27: "Any OTHER content can be a paragraph beginning "Note:" under the figure, in a smaller
# font than the main text and with the minimum possible distance between the figure and the subsequent note"). MyST
# writes the title and the note into one \caption under the image, so this step rearranges those figures.
NOTE_UNDER_OPTIONS = re.compile(r"^:::\{figure\}[^\n]*\n((?::[A-Za-z-]+:[^\n]*\n)+)", re.M)
FIGURE_ENV = re.compile(r"(\\begin\{figure\}(?:\[[^\]]*\])?\n)(.*?)(\\end\{figure\})", re.S)


def note_under_labels(text: str) -> set[str]:
    """The labels of the figures in a page's Markdown that are marked note-under."""
    labels = set()
    for m in NOTE_UNDER_OPTIONS.finditer(text):
        options = m.group(1)
        name = re.search(r"^:name: (\S+)", options, re.M)
        if name and re.search(r"^:class:.*\bnote-under\b", options, re.M):
            labels.add(name.group(1))
    return labels


def balanced(text: str, i: int) -> tuple[str, int]:
    """The text inside the brace group that opens at text[i], and the index just after it."""
    if text[i] != "{":
        raise ValueError("no brace group here")
    depth, j = 0, i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        depth += {"{": 1, "}": -1}.get(c, 0)
        if depth == 0:
            return text[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces")


def notes_under(tex: str, labels: set[str]) -> tuple[str, int]:
    """Each figure whose label is in `labels`: the title alone in a caption above the image, then the note, if any,
    in small ragged-right type as wide as the image, pulled up close under it. Other figures are left alone."""
    count = 0

    def fix(m):
        nonlocal count
        head, body, tail = m.groups()
        label = re.search(r"\\label\{([^}]*)\}", body)
        graphic = re.search(r"\\includegraphics(?:\[([^\]]*)\])?\{[^}]*\}", body)
        caption = re.search(r"\\caption(?:\[[^\]]*\])?\{", body)
        if not (label and label.group(1) in labels and graphic and caption):
            return m.group(0)
        inner, _ = balanced(body, caption.end() - 1)
        title, sep, note = inner.partition("\n\nNote:")
        width = re.search(r"width=([^,\]]+)", graphic.group(1) or "")
        width = width.group(1) if width else "\\linewidth"
        parts = ["\\centering\n", "\\captionsetup{position=top}\n", f"\\caption[]{{{title.strip()}}}\n",
                 f"\\label{{{label.group(1)}}}\n", graphic.group(0) + "\n"]
        if sep:
            parts.append(f"\\par\\vspace{{-0.3\\baselineskip}}\n\\begin{{minipage}}{{{width}}}\\small\\raggedright Note:{note}\\end{{minipage}}\n")
        count += 1
        return head + "".join(parts) + tail

    return FIGURE_ENV.sub(fix, tex), count


def notes_under_tex() -> list[str]:
    """Step 7: rearrange the figures marked note-under (NOTE_UNDER_OPTIONS) in the generated LaTeX."""
    labels = set()
    for md in STAGE.rglob("*.md"):
        if "_build" not in md.relative_to(STAGE).parts:
            labels |= note_under_labels(md.read_text())
    done = 0
    for tex_file in (STAGE / TEX_DIR).glob("*.tex"):
        new, n = notes_under(tex_file.read_text(), labels)
        if n:
            tex_file.write_text(new)
            done += n
    log.info("figures with their note under them: %d of %d marked", done, len(labels))
    return []


def missing_glyphs(latex_log: str) -> list[str]:
    """Each character LaTeX's log says a font lacks, which the PDF therefore leaves out, once, with its count."""
    found: dict[tuple[str, str, str], int] = {}
    for m in MISSING_CHAR.finditer(latex_log):
        found[m.groups()] = found.get(m.groups(), 0) + 1
    return [
        f"the PDF leaves out {ch} (U+{code}) {n} time(s): font {font} lacks it; map it in TEXT_GLYPHS"
        for (ch, code, font), n in found.items()
    ]


def compile_and_copy(root: Path) -> list[str]:
    """Step 7: rerun latexmk on the fixed LaTeX, copy the results back to exports/, and check no character is lost."""
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
    return missing_glyphs((tex_dir / f"{NAME}.log").read_text(errors="replace"))


def build(root: Path) -> list[str]:
    stage(root)
    rewrite_staged_facts()
    rewrite_staged_web_only()
    rewrite_staged_margins()
    rewrite_staged_link_words()
    if run(["myst", "build", "--pdf"], STAGE, root / MYST_LOG):
        return [f"myst build --pdf failed; see {MYST_LOG}"]
    return internalize_tex() or absolutize_tex() or tidy_bib() or map_glyphs_tex() or notes_under_tex() or compile_and_copy(root)


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


def web_only_failures() -> list[str]:
    """Failures of the rewrite of links to labels on pages the PDF leaves out."""
    page = ("(sec:page)=\n# Title\n\n(sec:x)=\n## X\n\n```{math}\n:label: eq:y\n```\n\n"
            ":::{figure} f.png\n:name: fig:z\n:::\n\n[^n]:\n\n    ```{math}\n    :label: eq:inFootnote\n    ```\n")
    found = all_label_targets(page, "U")
    targets = {"sec:x": "U#sec-x"}
    text, n = rewrite_web_only_links("see [infinite](#sec:x) and [here](#sec:inpdf)", targets)
    config = "project:\n  exports:\n    - format: tex+pdf\n      articles:\n        - file: content/a.md\n"
    try:
        rewrite_web_only_links("by {eq}`eq:y` and {ref}`words <sec:x>`", {"eq:y": "U#eq-y"})
        role_refused = False
    except ValueError:
        role_refused = True
    return [
        msg
        for bad, msg in [
            (
                found != {"sec:page": "U", "sec:x": "U#sec-x", "eq:y": "U#eq-y", "fig:z": "U#fig-z",
                          "eq:inFootnote": "U#eq-infootnote"},
                f"labels of a page mapped to {found}",
            ),
            (
                n != 1 or "](U#sec-x)" not in text or "](#sec:inpdf)" not in text,
                "a link to a page left out of the PDF was missed, or a link inside the PDF was touched",
            ),
            (not role_refused, "a role to a label the PDF leaves out was accepted"),
            (pdf_articles(config) != {"content/a.md"}, "the PDF's articles were misread from myst.yml"),
        ]
        if bad
    ]


def link_words_failures() -> list[str]:
    """Failures of keeping links inside the PDF with their words."""
    labels = {"eq:rule", "sec:Page", "fig:a_b"}
    text, n = keep_link_words(
        "the [golden rule](#eq:rule), [](#eq:rule), [the page](#sec:Page), [a figure](#fig:a_b), "
        "[elsewhere](#sec:web) and {eq}`eq:rule`", labels)
    try:
        keep_link_words("[odd](#eq:a#b)", {"eq:a#b"})
        odd_refused = False
    except ValueError:
        odd_refused = True
    tex, n_tex = hyperref_placeholders(rf"the \href{{{PLACEHOLDER}eq:rule}}{{golden rule}} and \href{{{PLACEHOLDER}fig:a\_b}}{{x}}")
    labeled = label_first_heading("\\chapter{The \\acrshort{mpc} Page}\nText \\section{Later}", ["sec:Page", "page:/c/p"])
    try:
        label_first_heading("\\section{A heading\nthat goes on}", ["x"])
        split_refused = False
    except ValueError:
        split_refused = True
    pages, n_pages = hyperref_pages(r"\href{/c/p}{P}, \href{/c/q}{Q} and \href{/c/p\#x}{X}", {"/c/p"})
    missing = missing_labels({"a.tex": r"\label{eq:rule} \hyperref[eq:rule]{r} \hyperref[sec:gone]{g}"})
    return [
        msg
        for bad, msg in [
            (
                n != 3 or f"]({PLACEHOLDER}eq:rule)" not in text or "[](#eq:rule)" not in text
                or "](#sec:web)" not in text or "{eq}`eq:rule`" not in text,
                f"links with words to labels in the PDF were not all kept, or something else was touched: {text}",
            ),
            (not odd_refused, "a label \\hyperref can't take was accepted"),
            (
                n_tex != 2 or tex != r"the \hyperref[eq:rule]{golden rule} and \hyperref[fig:a_b]{x}",
                f"placeholder links became {tex}",
            ),
            (
                labeled != "\\chapter{The \\acrshort{mpc} Page}\\label{sec:Page}\\label{page:/c/p}\nText \\section{Later}",
                f"the page's first heading was labeled as {labeled!r}",
            ),
            (not split_refused, "a heading that goes on past its line was labeled inside its argument"),
            (
                n_pages != 1 or pages != r"\hyperref[page:/c/p]{P}, \href{/c/q}{Q} and \href{/c/p\#x}{X}",
                f"links to whole pages became {pages}",
            ),
            (missing != ["a.tex: \\hyperref[sec:gone] has no \\label"], f"missing labels reported as {missing}"),
        ]
        if bad
    ]


def margin_failures() -> list[str]:
    """Failures of turning margin notes into footnotes for the PDF."""
    cases = {
        "a note after a paragraph": ("Text one.\n\n:::{margin}\nA note.\n:::\n\nNext.",
                                     "Text one.[^marginnote1]\n\n[^marginnote1]: A note.\n\nNext."),
        "a note after display math": ("Prose before\n\n```{math}\nx = 1\n```\n\n:::{margin}\nOn x.\n:::\n",
                                      "Prose before[^marginnote1]\n\n```{math}\nx = 1\n```\n\n[^marginnote1]: On x.\n"),
        "a note of two paragraphs": ("P.\n\n:::{margin}\nFirst.\n\nSecond, $x$.\n:::\n",
                                     "P.[^marginnote1]\n\n[^marginnote1]: First.\n\n    Second, $x$.\n"),
        "a note after a heading": ("Earlier.\n\n## Head\n\n:::{margin}\nN.\n:::\n",
                                   "Earlier.[^marginnote1]\n\n## Head\n\n[^marginnote1]: N.\n"),
    }
    failures = [f"{name} became {margins_to_footnotes(given)[0]!r}"
                for name, (given, want) in cases.items() if margins_to_footnotes(given)[0] != want]
    if margins_to_footnotes("Plain.\n") != ("Plain.\n", 0):
        failures.append("a page with no margin note was changed")
    try:
        margins_to_footnotes(":::{margin}\nalone\n:::\n")
        failures.append("a margin note with no prose before it was accepted")
    except ValueError:
        pass
    return failures


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
            (
                unknown_pages(rf"\href{{{SITE}/lite/notebooks/index.html?path=Bubbles.ipynb}}{{x}}", lite_pages()),
                "a link to an in-browser notebook was reported unknown",
            ),
            (
                not unknown_pages(rf"\href{{{SITE}/lite/notebooks/index.html?path=Gone.ipynb}}{{x}}", lite_pages()),
                "a link to an in-browser notebook the site does not build was not reported",
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
            ("content/consumption/Envelope/Envelope.ipynb", "/content/consumption/envelope/envelope"),
        ]
        if page_url(Path("r") / md, Path("r")) != want
    ]


def clear_failures() -> list[str]:
    """A stage holding a read-only folder, as @resources/ is, must still be deleted."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        stage_dir = Path(tmp) / "stage"
        locked = stage_dir / "locked"
        locked.mkdir(parents=True)
        (locked / "file").write_text("x")
        (locked / "file").chmod(0o444)
        locked.chmod(0o555)
        clear(stage_dir)
        return ["clear left a stage with a read-only folder in place"] if stage_dir.exists() else []


def title_label_failures() -> list[str]:
    """Failures of finding a page's title label, with and without front matter before it."""
    cases = {
        "a title label": ("(sec:A)=\n# A\n\nText.\n", "sec:A"),
        "a title label after front matter": ("---\nmath:\n  '\\x': 'y'\n---\n(sec:A)=\n# A\n", "sec:A"),
        "a section label, not the title's": ("# A\n\n(sec:B)=\n## B\n", None),
        "front matter, then a heading with no label": ("---\ntitle: T\n---\n# A\n\n(sec:B)=\n## B\n", None),
    }
    failures = []
    for name, (page, want) in cases.items():
        m = PAGE_TITLE_LABEL.match(page)
        if (m.group(1) if m else None) != want:
            failures.append(f"{name}: found {m.group(1) if m else None}, not {want}")
    m = TITLE_LABEL.match("---\nmath: {}\n---\n(fact:f)=\n# F\n")
    if not m or m.group(1) != "fact:f":
        failures.append("a Math Fact's title label after front matter was not found")
    return failures


def bib_failures() -> list[str]:
    """Failures of tidy_bib_entry on entries shaped like MyST's main.bib."""
    u = "https://www.example.org/a/long/path/File.zip"
    entry = (
        "@misc{K,\n"
        f"\tnote = {{Download {u} and open it}},\n"
        "\ttitle = {T},\n"
        f"\turl = {{{u}}},\n"
        f"\thowpublished = {{{u}}},\n"
        "}"
    )
    got, n = tidy_bib_entry(entry)
    cases = [
        ("howpublished" in got, "a howpublished repeating the url was kept"),
        (f"Download \\url{{{u}}} and open it" not in got, "a bare URL in a note was not wrapped in \\url"),
        (f"\turl = {{{u}}}," not in got, "the url field was changed"),
        (n != 2, f"{n} changes counted, not 2"),
    ]
    kept = f"@misc{{K,\n\thowpublished = {{Mimeo}},\n\tnote = {{see \\url{{{u}}}.}},\n\turl = {{{u}}},\n}}"
    cases.append((tidy_bib_entry(kept) != (kept, 0), "an entry with nothing to tidy was changed"))
    end = f"@misc{{K,\n\tnote = {{At {u}.}},\n}}"
    cases.append((f"At \\url{{{u}}}." not in tidy_bib_entry(end)[0], "a URL before a period was not wrapped, or took the period"))
    thesis = f"@misc{{K,\n\tnote = {{{u}}},\n\tschool = {{S}},\n\ttype = {{PhD dissertation}},\n\turl = {{{u}}},\n}}"
    got, n = tidy_bib_entry(thesis)
    cases += [
        (not got.startswith("@phdthesis{K,"), "an @misc with a school was not made @phdthesis"),
        ("note" in got, "a note that only repeats the url was kept"),
        (f"\turl = {{{u}}}," not in got or "school" not in got, "the thesis lost its url or school"),
        ("\ttype = {{PhD dissertation}}," not in got, "the thesis's type was not braced against lowercasing"),
        (n != 3, f"{n} changes counted on the thesis, not 3"),
    ]
    wrapped = f"@article{{K,\n\tnote = {{\\url{{{u}}}}},\n\turl = {{{u}}},\n}}"
    cases.append(("note" in tidy_bib_entry(wrapped)[0], "a note that only repeats the url in \\url was kept"))
    return [msg for bad, msg in cases if bad]


def glyph_failures() -> list[str]:
    """Failures of map_glyphs and missing_glyphs on a preamble and on log lines shaped like XeLaTeX's."""
    tex = "\\usepackage{lmodern}\n\\begin{document}\nE′\n\\end{document}\n"
    got = map_glyphs(tex)
    head, _, body = got.partition("\\begin{document}")
    line = "Missing character: There is no ′ (\"2032) in font ec-lmr10!"
    cases = [
        ("\\usepackage{newunicodechar}" not in head, "newunicodechar was not loaded before \\begin{document}"),
        ("\\newunicodechar{′}{" not in head, "the prime was not mapped before \\begin{document}"),
        (body != "\nE′\n\\end{document}\n", "the document's body was changed"),
        (not raises_key_error(map_glyphs, "no document here"), "a .tex without \\begin{document} was not rejected"),
        (missing_glyphs(f"x\n{line}\n{line}\ny\n") != ["the PDF leaves out ′ (U+2032) 2 time(s): font ec-lmr10 lacks it; map it in TEXT_GLYPHS"],
         "two missing primes in a log were not reported once, with their count"),
        (missing_glyphs("Overfull \\hbox\nno missing characters\n") != [], "a log without missing characters reported one"),
    ]
    return [msg for bad, msg in cases if bad]


def notes_under_failures() -> list[str]:
    """Failures of note_under_labels and notes_under on a marked figure and an unmarked one."""
    md = (":::{figure} figures/a.png\n:name: fig:A\n:class: note-under\n\nPhase Diagram\n\nNote: The loci cross.\n:::\n\n"
          ":::{figure} figures/b.png\n:name: fig:B\n\nOther\n:::\n")
    fig = ("\\begin{figure}[!htbp]\n\\centering\n\\includegraphics[width=0.7\\linewidth]{files/a.png}\n"
           "\\caption[]{Phase Diagram\n\nNote: The {loci} cross.}\n\\label{fig:A}\n\\end{figure}\n")
    other = fig.replace("fig:A", "fig:B")
    got, n = notes_under(fig + other, note_under_labels(md))
    first, rest = got.split("\\end{figure}\n", 1)
    cases = [
        (note_under_labels(md) != {"fig:A"}, "the marked figure's label was not the only one found"),
        (n != 1, f"{n} figures were rearranged, not 1"),
        ("\\caption[]{Phase Diagram}" not in first, "the caption is not the title alone"),
        ("\\caption" in first and first.index("\\caption") > first.index("\\includegraphics"), "the title is not above the image"),
        ("\\begin{minipage}{0.7\\linewidth}\\small\\raggedright Note: The {loci} cross.\\end{minipage}" not in first,
         "the note is not under the image, in small type, as wide as the image"),
        (rest != other, "an unmarked figure was changed"),
    ]
    return [msg for bad, msg in cases if bad]


def self_test() -> bool:
    """Every rewrite and check must act on input it is supposed to act on."""
    failures = (fact_failures() + web_only_failures() + margin_failures() + link_words_failures() + title_label_failures() + href_failures()
                + url_failures() + clear_failures() + bib_failures() + glyph_failures() + notes_under_failures())
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
