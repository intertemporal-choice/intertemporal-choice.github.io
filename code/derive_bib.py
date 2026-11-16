"""Derive content/minimal_bibliography.bib from the book's one source of references.

The source is bibtex/bib/economics.bib in llorracc/texmf-local. Every document's references are
derived from it, and corrections are made there (Chris Carroll, 2026-11-08). So the book never
edits its copy: this script copies, verbatim, the entries the chapters cite, together with any
entry they name in a crossref field, since MyST resolves a crossref only within one file. The
file's first line names the texmf-local commit it was derived from.

  (no option)                  derive from texmf-local's main on GitHub and rewrite the file
  --source FILE --commit SHA   derive from a local economics.bib that is at commit SHA
  --check                      derive again from the commit the file names, and fail if the file
                               differs or a cited key is missing from the source (the workflow
                               runs this)
  --self-test                  derive from a small made-up source and check the copying, the
                               crossref parents, the header and --check's verdicts

Usage: uv run python code/derive_bib.py [--check | --self-test | --source FILE --commit SHA]
"""

import argparse
import json
import logging
import re
import sys
import urllib.request
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

REPO = Path(__file__).resolve().parent.parent
BIB = REPO / "content" / "minimal_bibliography.bib"
SOURCE_REPO = "llorracc/texmf-local"
SOURCE_PATH = "bibtex/bib/economics.bib"

CITE = re.compile(r"\{cite(?::[a-z]+)?\}`([^`]+)`")
ENTRY_START = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
CROSSREF = re.compile(r"\bcrossref\s*=\s*[{\"]\s*([^}\"\s]+)\s*[}\"]", re.IGNORECASE)
HEADER_SHA = re.compile(r"texmf-local, commit ([0-9a-f]{40})")


def header(sha: str) -> str:
    # No "@" here: BibTeX reads "@" as the start of an entry even inside a % comment, and MyST
    # then rejects the whole file.
    return (
        f"% Derived from {SOURCE_REPO}, commit {sha}, {SOURCE_PATH}, by code/derive_bib.py.\n"
        "% Don't edit this file: correct the entry in economics.bib, then run the script again.\n"
    )


def cited_keys(root: Path) -> set[str]:
    """Every key in a {cite}, {cite:t} or {cite:p} role in the chapters and notebooks."""
    keys: set[str] = set()
    for path in sorted(root.rglob("*")):
        if path.suffix in (".md", ".ipynb") and "_build" not in path.parts:
            for match in CITE.finditer(path.read_text(encoding="utf-8")):
                keys.update(k.strip() for k in match.group(1).split(",") if k.strip())
    return keys


def entries(text: str) -> dict[str, str]:
    """Each entry's key and its text exactly as written, braces matched.

    Skipped: @string, @preamble, anything inside an @comment, and an entry whose @ sits on a line
    after a %, which is commented out. If a key occurs twice, the first wins.
    """
    found: dict[str, str] = {}
    skip_until = 0
    for match in ENTRY_START.finditer(text):
        if match.start() < skip_until:
            continue
        line_start = text.rfind("\n", 0, match.start()) + 1
        if "%" in text[line_start:match.start()]:
            continue
        depth, end = 1, match.end()
        while end < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[end], 0)
            end += 1
        kind = match.group(1).lower()
        if kind == "comment":
            skip_until = end
        elif kind not in ("string", "preamble"):
            found.setdefault(match.group(2), text[match.start():end])
    return found


def derive(source: str, cited: set[str], sha: str) -> tuple[str, list[str]]:
    """The derived file's text, and the cited keys the source lacks."""
    pool = entries(source)
    missing = sorted(k for k in cited if k not in pool)
    chosen = sorted((k for k in cited if k in pool), key=str.lower)
    parents: list[str] = []
    queue = list(chosen)
    while queue:
        match = CROSSREF.search(pool[queue.pop(0)])
        if match:
            parent = match.group(1)
            if parent not in pool:
                missing.append(f"{parent} (crossref parent)")
            elif parent not in chosen and parent not in parents:
                parents.append(parent)
                queue.append(parent)
    # BibTeX wants a crossref parent after the entries that name it.
    body = "\n\n".join(pool[k] for k in chosen + parents)
    return header(sha) + "\n" + body + "\n", missing


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "intertemporal-choice-derive-bib"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def source_at(sha: str) -> str:
    return fetch(f"https://raw.githubusercontent.com/{SOURCE_REPO}/{sha}/{SOURCE_PATH}").decode("utf-8")


def main_sha() -> str:
    return json.loads(fetch(f"https://api.github.com/repos/{SOURCE_REPO}/commits/main"))["sha"]


def check(bib: Path, cited: set[str], get_source=source_at) -> list[str]:
    """What is wrong with the committed file, if anything."""
    text = bib.read_text(encoding="utf-8")
    match = HEADER_SHA.search(text.split("\n", 1)[0])
    if not match:
        return [f"{bib.name}'s first line names no {SOURCE_REPO} commit; run code/derive_bib.py"]
    derived, missing = derive(get_source(match.group(1)), cited, match.group(1))
    problems = [f"cited but not in economics.bib: {k}" for k in missing]
    if derived != text:
        have, want = entries(text), entries(derived)
        changed = sorted(k for k in set(have) | set(want) if have.get(k) != want.get(k))
        problems.append(
            f"{bib.name} differs from economics.bib at {match.group(1)[:7]}"
            + (f" in: {', '.join(changed)}" if changed else " (outside the entries)")
            + "; run code/derive_bib.py"
        )
    return problems


def self_test() -> int:
    source = (
        '@preamble{ "\\providecommand{\\noopsort}[1]{}" }\n\n'
        "@article{beta,\n  author = {B},\n  title = {{Nested} braces},\n  crossref = {parent}\n}\n\n"
        "@book{parent,\n  title = {P},\n  year = 2000\n}\n\n"
        "@article{Alpha,\n  title = \"Quoted\",\n  year = 1999\n}\n\n"
        "@article{unused,\n  title = {U}\n}\n\n"
        "% @article{Alpha, title = {Commented out}}\n"
        "@comment{ @article{beta, title = {Inside a comment}} }\n"
    )
    sha = "0" * 40
    failures = []
    derived, missing = derive(source, {"beta", "Alpha"}, sha)
    pool = entries(derived)
    if list(pool) != ["Alpha", "beta", "parent"]:
        failures.append(f"entries or order wrong: {list(pool)}")
    if pool.get("beta") != entries(source)["beta"]:
        failures.append("an entry was not copied verbatim")
    if missing or not derived.startswith(header(sha)):
        failures.append("unexpected missing keys or header")
    if "@" in header(sha):
        failures.append("the header holds an @, which BibTeX and MyST read as the start of an entry")
    _, missing = derive(source, {"Alpha", "gamma"}, sha)
    if missing != ["gamma"]:
        failures.append(f"a missing key was not reported: {missing}")
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        bib = Path(tmp) / "minimal_bibliography.bib"
        bib.write_text(derived, encoding="utf-8")
        if check(bib, {"beta", "Alpha"}, lambda _: source):
            failures.append("--check rejected a file it had just derived")
        bib.write_text(derived.replace("Quoted", "Edited"), encoding="utf-8")
        if not any("Alpha" in p for p in check(bib, {"beta", "Alpha"}, lambda _: source)):
            failures.append("--check missed an edited entry")
    for failure in failures:
        log.error("self-test: %s", failure)
    log.info("derive_bib self-test: %s", "FAILED" if failures else "ok")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--commit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    cited = cited_keys(REPO / "content")
    if args.check:
        problems = check(BIB, cited)
        for problem in problems:
            log.error(problem)
        if not problems:
            log.info("%s matches economics.bib for all %d cited keys", BIB.name, len(cited))
        return 1 if problems else 0
    if args.source:
        if not args.commit or not re.fullmatch(r"[0-9a-f]{40}", args.commit):
            parser.error("--source needs --commit with the source's full 40-character commit")
        sha, source = args.commit, args.source.read_text(encoding="utf-8")
    else:
        sha = main_sha()
        source = source_at(sha)
    derived, missing = derive(source, cited, sha)
    if missing:
        for key in missing:
            log.error("cited but not in economics.bib: %s", key)
        return 1
    BIB.write_text(derived, encoding="utf-8")
    log.info("wrote %s: %d entries from %s@%s", BIB.relative_to(REPO), len(entries(derived)), SOURCE_REPO, sha[:7])
    return 0


if __name__ == "__main__":
    sys.exit(main())
