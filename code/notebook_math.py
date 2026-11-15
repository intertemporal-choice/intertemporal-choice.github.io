"""Keep each chapter's student notebook generated from its source, `<Chapter>_SST.ipynb`.

The source notebook, the SST (single source of truth), is written the way the book writes
everything: every economic object by its macro (rule D, Chris Carroll 2026-11-15),
`\\CRRA`, `\\kap`, `\\ptyGro`. Those macros are defined by the registry and the course block,
which the website reads but Colab, Binder, JupyterLite, GitHub and VS Code do not. So the
notebook students open, `<Chapter>.ipynb` beside the chapter, is generated from the SST: the
same cells, ids and outputs, with each macro in its Markdown math spelled out in the LaTeX it
prints, so it renders anywhere. Edit the SST, never the student notebook.

  - The SST carries one Markdown cell tagged `notation-definitions`: a \\newcommand for each
    macro its Markdown uses, so the SST renders in Jupyter too. Rendered, it shows nothing. It
    comes first, after the frontmatter cell: MathJax defines a macro for the math that follows
    the definition, not the math above it. This script writes that cell; the student notebook
    leaves it out.
  - Code is not rewritten: a figure label is written with the package's `notation.tex`, so it
    runs the same in both notebooks and prints the book's current symbol.
  - The package's `_notation_macros.py`, which `notation.tex` reads, is written here too.

No spurious changes. The SST is read stripped by the repo's own nbstripout command and
options (code/notebooks.py), so execution counts, timings and versions never reach the
output; what is written depends only on the SST's content and the macro definitions; and a
file is rewritten only when its bytes would change. Re-running the SST, or opening and saving
it, changes nothing.

Kept current three ways: run this script after editing an SST or the notation; the pre-commit
hook that code/notebooks.py --install sets up runs it with --hook, regenerating from what is
staged and staging the result; and CI runs --check, which fails when any generated file is not
what this script writes.

Usage: uv run python code/notebook_math.py [--check | --hook | --self-test]
"""

import copy
import json
import logging
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import nbformat
import yaml

import notebooks  # beside this file: the nbstripout options the repo's filter uses
from intertemporal_choice.notation import CONTROL_WORD, arity, expand

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = Path("@resources/notation/econark-math.yml")
COURSE_BLOCK = Path("notation/course-local-math.yml")
MACRO_MODULE = Path("src/intertemporal_choice/_notation_macros.py")
SUFFIX = "_SST"
TAG = "notation-definitions"
GENERATED_NOTE = (
    "<!-- Generated from {sst} by code/notebook_math.py. Don't edit this notebook: edit {sst}, "
    "where the math is written with the book's macros, and run the script. -->"
)
DEFINITIONS_NOTE = (
    "<!-- The book's notation for this notebook: a definition for each macro its Markdown uses, "
    "so that it renders in Jupyter. Written by code/notebook_math.py from the registry and the "
    "course block; don't edit. The student notebook leaves this cell out. -->"
)

FENCE = re.compile(r"(?ms)^[ ]{0,3}(`{3,}|~{3,}).*?^[ ]{0,3}\1[ \t]*$")
CODE_SPAN = re.compile(r"(`+)(?!`).+?(?<!`)\1(?!`)", re.S)
DISPLAY = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$", re.S)
INLINE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)", re.S)


# --- the macros -------------------------------------------------------------------------------

def macros_from(registry_text: str, block_text: str) -> dict[str, str]:
    """The book's definitions: the registry's, with the course block's on top (as myst.yml extends them)."""
    macros = dict(yaml.safe_load(registry_text)["project"]["math"])
    macros.update(yaml.safe_load(block_text)["project"]["math"])
    return macros


def macro_module(macros: dict[str, str]) -> str:
    lines = [
        '"""The book\'s macro definitions, for notation.tex: the registry\'s, with the course block\'s on top.',
        "",
        "Written by code/notebook_math.py from @resources/notation/econark-math.yml and",
        "notation/course-local-math.yml. Do not edit: change those, then run the script.",
        '"""',
        "",
        "MACROS = {",
        *(f"    {name!r}: {body!r}," for name, body in sorted(macros.items())),
        "}",
        "",
    ]
    return "\n".join(lines)


# --- Markdown -----------------------------------------------------------------------------------

def math_spans(markdown: str) -> list[tuple[int, int]]:
    """(start, end) of each math span's content, $$...$$ or $...$, outside code."""
    masked = FENCE.sub(lambda m: " " * len(m.group(0)), markdown)
    masked = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), masked)
    spans = [m.span(1) for m in DISPLAY.finditer(masked)]
    for start, end in spans:
        masked = masked[: start - 2] + " " * (end - start + 4) + masked[end + 2 :]
    spans += [m.span(1) for m in INLINE.finditer(masked) if "\n\n" not in m.group(1)]
    return sorted(spans)


def expand_markdown(markdown: str, macros: dict[str, str]) -> str:
    """Markdown with each macro in its math spelled out; text and code untouched."""
    for start, end in reversed(math_spans(markdown)):
        markdown = markdown[:start] + expand(markdown[start:end], macros) + markdown[end:]
    return markdown


def macros_used(markdown: str, macros: dict[str, str]) -> set[str]:
    return {name for s, e in math_spans(markdown) for name in CONTROL_WORD.findall(markdown[s:e]) if name in macros}


def definitions(used: set[str], macros: dict[str, str]) -> str:
    """The definitions cell's source: one \\newcommand per macro, each spelled out in full."""
    lines = [DEFINITIONS_NOTE]
    for name in sorted(used, key=lambda n: (n.lower(), n)):
        body, n = macros[name], arity(macros[name])
        lines.append(f"$\\newcommand{{{name}}}{f'[{n}]' if n else ''}{{{expand(body, macros)}}}$")
    return "\n".join(lines)


# --- notebooks ----------------------------------------------------------------------------------

def stripped(text: str) -> str:
    """The notebook as the repo's filter stores it: no execution counts, timings or versions."""
    done = subprocess.run([sys.executable, "-m", "nbstripout", *notebooks.OPTIONS], input=text,
                          capture_output=True, text=True)
    if done.returncode != 0:
        raise ValueError(f"nbstripout could not read the notebook: {done.stderr.strip()}")
    return done.stdout


def canonical(nb) -> str:
    text = nbformat.writes(nb)
    return text if text.endswith("\n") else text + "\n"


def is_definitions(cell) -> bool:
    return TAG in (cell.get("metadata", {}).get("tags") or [])


def with_definitions(nb, macros: dict[str, str]):
    """The SST with its definitions cell current: first, after the frontmatter cell, since MathJax
    defines a macro only for the math that comes after the definition."""
    nb = copy.deepcopy(nb)
    used = set()
    for cell in nb.cells:
        if cell.cell_type == "markdown" and not is_definitions(cell):
            used |= macros_used(cell.source, macros)
    source = definitions(used, macros)
    cells = [c for c in nb.cells if is_definitions(c)]
    if len(cells) > 1:
        raise ValueError(f"more than one cell is tagged {TAG}")
    cell = cells[0] if cells else nbformat.v4.new_markdown_cell(
        "", id=TAG, metadata={"tags": [TAG], "jupyter": {"source_hidden": True}})
    cell.source = source
    nb.cells = [c for c in nb.cells if not is_definitions(c)]
    front = 1 if nb.cells and nb.cells[0].cell_type in ("markdown", "raw") and nb.cells[0].source.lstrip().startswith("---") else 0
    nb.cells.insert(front, cell)
    return nb


def student(nb, macros: dict[str, str], sst_name: str):
    """The notebook students open: the SST's cells and outputs, macros spelled out, no definitions cell."""
    nb = copy.deepcopy(nb)
    nb.cells = [c for c in nb.cells if not is_definitions(c)]
    noted = False
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        cell.source = expand_markdown(cell.source, macros)
        if not noted and not cell.source.lstrip().startswith("---"):
            cell.source = GENERATED_NOTE.format(sst=sst_name) + "\n" + cell.source
            noted = True
    nb.metadata["intertemporal_choice"] = {"generated_from": sst_name, "by": "code/notebook_math.py"}
    return nb


def generate(sst_text: str, macros: dict[str, str], sst_name: str) -> tuple[str, str]:
    """(the SST as it should be stored, the student notebook) from an SST's text."""
    nb = nbformat.reads(stripped(sst_text), as_version=4)
    nb = with_definitions(nb, macros)
    return canonical(nb), canonical(student(nb, macros, sst_name))


def pairs(root: Path) -> list[tuple[Path, Path]]:
    """(SST, student notebook) for each source notebook, as paths relative to root."""
    return [
        (p.relative_to(root), p.with_name(p.name.replace(f"{SUFFIX}.ipynb", ".ipynb")).relative_to(root))
        for p in sorted((root / "content").rglob(f"*{SUFFIX}.ipynb"))
        if ".ipynb_checkpoints" not in p.parts
    ]


def wanted(root: Path, read) -> dict[Path, str]:
    """Every file this script writes, and what it should hold. `read(path)` gives a file's text."""
    macros = macros_from(read(REGISTRY), read(COURSE_BLOCK))
    files = {MACRO_MODULE: macro_module(macros)}
    for sst, nb in pairs(root):
        files[sst], files[nb] = generate(read(sst), macros, sst.name)
    return files


def read_file(root: Path):
    return lambda path: (root / path).read_text(encoding="utf-8")


def write(root: Path) -> int:
    changed = 0
    for path, text in wanted(root, read_file(root)).items():
        target = root / path
        if not target.is_file() or target.read_text(encoding="utf-8") != text:
            target.write_text(text, encoding="utf-8")
            log.info("wrote %s", path)
            changed += 1
    log.info("%d file(s) rewritten; the rest were current", changed)
    return 0


def stale(root: Path, read) -> list[Path]:
    return [path for path, text in wanted(root, read).items()
            if not (root / path).is_file() or stripped_if_notebook(path, read(path)) != text]


def stripped_if_notebook(path: Path, text: str) -> str:
    return canonical(nbformat.reads(stripped(text), as_version=4)) if path.suffix == ".ipynb" else text


def check(root: Path) -> int:
    """Fail if a generated file, or an SST's definitions cell, is not what this script writes."""
    bad = stale(root, read_file(root))
    for path in bad:
        log.error("%s is not what code/notebook_math.py writes: run it (edit the _SST notebook, not its student copy)", path)
    if not bad:
        log.info("%d source notebook(s): every student notebook and definitions cell is current", len(pairs(root)))
    return 1 if bad else 0


def git_text(root: Path, spec: str) -> str | None:
    """A file's text as git holds it (":path" staged, "HEAD:path" committed), or None if it has none."""
    done = subprocess.run(["git", "show", spec], cwd=root, capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else None


def hook(root: Path) -> int:
    """For the pre-commit hook: regenerate from what is staged, and stage what changed.

    It refuses, rather than overwrite someone's work, when an SST's definitions cell is stale (run
    the script and add the SST again), when a generated file was edited by hand and staged, and
    when a generated file has unstaged edits.
    """
    def staged(path: Path) -> str:
        text = git_text(root, f":{path.as_posix()}")
        if text is None:
            raise FileNotFoundError(path)
        return text
    problems, to_stage = [], []
    for path, text in wanted(root, staged).items():
        raw = git_text(root, f":{path.as_posix()}")
        current = None if raw is None else stripped_if_notebook(path, raw)
        if current == text:
            continue
        if path.name.endswith(f"{SUFFIX}.ipynb"):
            problems.append(f"{path}: its definitions cell is not current: run code/notebook_math.py and add it again")
            continue
        head = git_text(root, f"HEAD:{path.as_posix()}")
        if raw is not None and head is not None and raw != head:
            problems.append(f"{path} is generated, and an edit to it is staged: make the edit in its _SST notebook")
            continue
        working = root / path
        if working.is_file() and raw is not None and working.read_text(encoding="utf-8") != raw:
            problems.append(f"{path} has unstaged edits, and it is generated: make them in its _SST notebook")
            continue
        working.write_text(text, encoding="utf-8")
        to_stage.append(path.as_posix())
    if to_stage:
        subprocess.run(["git", "add", "--", *to_stage], cwd=root, check=True)
        log.info("notebook_math: regenerated and staged %s", ", ".join(to_stage))
    for p in problems:
        log.error("notebook_math: %s", p)
    return 1 if problems else 0


# --- self-test ----------------------------------------------------------------------------------

def self_test() -> bool:
    failures = []
    macros = {"\\k": "k", "\\r": "\\varrho", "\\g": "\\Gro", "\\Gro": "g", "\\bb": "\\bar{\\bar{#1}}"}
    md = "Text $\\k^{\\r}$ and $$\\bb{\\k}$$, code `$\\k$`, money \\$5, and\n```\n$\\k$\n```\n$\\g$."
    want = "Text $k^{\\varrho}$ and $$\\bar{\\bar{k}}$$, code `$\\k$`, money \\$5, and\n```\n$\\k$\n```\n$g$."
    if expand_markdown(md, macros) != want:
        failures.append(f"Markdown math was not expanded exactly, outside code only: {expand_markdown(md, macros)!r}")
    if macros_used(md, macros) != {"\\k", "\\r", "\\bb", "\\g"}:
        failures.append(f"the macros used were misread: {macros_used(md, macros)}")
    defs = definitions({"\\g", "\\bb"}, macros)
    if "$\\newcommand{\\bb}[1]{\\bar{\\bar{#1}}}$" not in defs or "$\\newcommand{\\g}{g}$" not in defs:
        failures.append(f"the definitions are not spelled out in full, with their arguments: {defs!r}")

    def notebook(count, timing, version):
        nb = nbformat.v4.new_notebook()
        nb.metadata = {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
                       "language_info": {"name": "python", "version": version}}
        code = nbformat.v4.new_code_cell("x = 1\nx", id="code1", execution_count=count,
                                         metadata={"execution": {"iopub.execute_input": timing}})
        code.outputs = [nbformat.v4.new_output("execute_result", data={"text/plain": "1"}, execution_count=count)]
        nb.cells = [nbformat.v4.new_markdown_cell('---\ntitle: "T"\n---', id="front"),
                    nbformat.v4.new_code_cell("pass", id="boot"), code,
                    nbformat.v4.new_markdown_cell("Capital $\\k$ grows at $\\g$.", id="text")]
        return nbformat.writes(nb)

    one, two = notebook(3, "2026-11-15T10:00:00Z", "3.11.13"), notebook(9, "2026-11-16T11:00:00Z", "3.12.1")
    sst1, nb1 = generate(one, macros, "T_SST.ipynb")
    sst2, nb2 = generate(two, macros, "T_SST.ipynb")
    if (sst1, nb1) != (sst2, nb2):
        failures.append("execution counts, timings or the Python version changed what is written")
    if generate(sst1, macros, "T_SST.ipynb") != (sst1, nb1):
        failures.append("generating again from the SST it wrote changed something")
    s, n = nbformat.reads(sst1, as_version=4), nbformat.reads(nb1, as_version=4)
    if [c.id for c in s.cells] != ["front", TAG, "boot", "code1", "text"] or "\\newcommand{\\g}{g}" not in s.cells[1].source:
        failures.append("the SST's definitions cell is missing, not first after the frontmatter, or incomplete")
    moved = nbformat.reads(sst1, as_version=4)
    moved.cells.append(moved.cells.pop(1))  # an author moved it to the end
    if [c.id for c in nbformat.reads(generate(canonical(moved), macros, "T_SST.ipynb")[0], as_version=4).cells] != [c.id for c in s.cells]:
        failures.append("a definitions cell moved away from the top was not put back")
    if any(is_definitions(c) for c in n.cells) or [c.id for c in n.cells] != ["front", "boot", "code1", "text"]:
        failures.append("the student notebook kept the definitions cell, or lost or reordered a cell")
    if "Capital $k$ grows at $g$." not in n.cells[3].source or "Generated from T_SST.ipynb" not in n.cells[3].source:
        failures.append("the student notebook's Markdown was not spelled out, or it lacks the note that it is generated")
    if n.cells[2].outputs[0]["data"]["text/plain"] != "1" or n.cells[2].execution_count is not None:
        failures.append("the outputs were not carried over, or an execution count was")
    if n.metadata.get("intertemporal_choice", {}).get("generated_from") != "T_SST.ipynb":
        failures.append("the student notebook does not say which SST it was generated from")
    if notebooks.OPTIONS != ["--keep-output", "--keep-id", "--extra-keys", "metadata.language_info"]:
        failures.append("code/notebooks.py's options changed: check that stripped() still matches the filter")
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "content/p/T").mkdir(parents=True)
        (root / REGISTRY).parent.mkdir(parents=True)
        (root / COURSE_BLOCK).parent.mkdir(parents=True)
        (root / MACRO_MODULE).parent.mkdir(parents=True)
        (root / REGISTRY).write_text(yaml.safe_dump({"project": {"math": {"\\k": "k", "\\g": "\\Gro", "\\Gro": "G"}}}))
        (root / COURSE_BLOCK).write_text(yaml.safe_dump({"project": {"math": {"\\Gro": "g"}}}))  # the block wins
        (root / "content/p/T/T_SST.ipynb").write_text(one)
        if pairs(root) != [(Path("content/p/T/T_SST.ipynb"), Path("content/p/T/T.ipynb"))]:
            failures.append(f"the SST and its student notebook were not paired: {pairs(root)}")
        if not stale(root, read_file(root)):
            failures.append("--check passed with no student notebook written")
        write(root)
        if stale(root, read_file(root)):
            failures.append("--check failed right after the script wrote everything")
        if "Capital $k$ grows at $g$." not in (root / "content/p/T/T.ipynb").read_text():
            failures.append("the course block did not win over the registry")
        before = (root / "content/p/T/T.ipynb").stat().st_mtime_ns
        write(root)
        if (root / "content/p/T/T.ipynb").stat().st_mtime_ns != before:
            failures.append("a current student notebook was rewritten")
        student_path = root / "content/p/T/T.ipynb"
        student_path.write_text(student_path.read_text().replace("grows at $g$", "grows at $G$"))
        if Path("content/p/T/T.ipynb") not in stale(root, read_file(root)):
            failures.append("--check passed a student notebook edited by hand")
        write(root)
        sst_path = root / "content/p/T/T_SST.ipynb"
        sst_path.write_text(sst_path.read_text().replace("Capital $\\\\k$", "Capital $\\\\k$ and $\\\\Gro$"))
        if Path("content/p/T/T_SST.ipynb") not in stale(root, read_file(root)):
            failures.append("--check passed an SST whose definitions cell lacks a macro its Markdown uses")
    failures += hook_failures(one)
    for f in failures:
        log.error("notebook_math self-test: %s", f)
    if not failures:
        log.info("notebook_math self-test: ok")
    return not failures


def hook_failures(sst_text: str) -> list[str]:
    """The pre-commit hook, in a scratch repository: it regenerates and stages, and refuses hand edits."""
    failures = []
    git = lambda root, *args: subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        git(root, "init", "-q")
        git(root, "config", "user.email", "t@example.com")
        git(root, "config", "user.name", "test")
        for path, text in [(REGISTRY, yaml.safe_dump({"project": {"math": {"\\k": "k", "\\g": "g", "\\h": "h"}}})),
                           (COURSE_BLOCK, yaml.safe_dump({"project": {"math": {}}})),
                           (Path("content/p/T/T_SST.ipynb"), sst_text)]:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text)
        (root / MACRO_MODULE).parent.mkdir(parents=True, exist_ok=True)
        write(root)
        git(root, "add", "-A")
        git(root, "commit", "-q", "-m", "start")
        sst, nb = root / "content/p/T/T_SST.ipynb", root / "content/p/T/T.ipynb"
        sst.write_text(sst.read_text().replace("grows at", "rises at"))
        git(root, "add", str(sst))
        if hook(root) != 0 or "rises at" not in (git_text(root, ":content/p/T/T.ipynb") or ""):
            failures.append("the hook did not regenerate and stage the student notebook of a staged SST")
        git(root, "commit", "-q", "-m", "edit")
        nb.write_text(nb.read_text().replace("rises at", "climbs at"))
        git(root, "add", str(nb))
        if hook(root) == 0 or "climbs at" not in nb.read_text():
            failures.append("the hook accepted, or overwrote, a staged hand edit to a student notebook")
        git(root, "checkout", "-q", "HEAD", "--", str(nb))
        sst.write_text(sst.read_text().replace("Capital $\\\\k$", "Capital $\\\\k$ at $\\\\h$"))
        git(root, "add", str(sst))
        if hook(root) == 0:
            failures.append("the hook accepted an SST whose definitions cell lacks a macro it uses")
    return failures


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    if "--check" in sys.argv:
        sys.exit(check(ROOT))
    if "--hook" in sys.argv:
        sys.exit(hook(ROOT))
    sys.exit(write(ROOT))
