#!/usr/bin/env python3
"""
List planned changes, and say which are due.

A planned change is a deferred ruling: a change to make to some material once something happens.
It is written as a line that starts with

    PLANNED(<trigger>; <who ruled, when>): <what to change>

followed by indented continuation lines. It names the material by name, never by number, and it
names its targets on continuation lines of the form

    Target: "<text that must still be in the file>"
    Target: <file>: "<text>"

so that the checker can tell when the material has already changed or been renamed. <file> is
relative to the folder being checked, or to --root when a single file is checked.
A target is looked for with every marker removed, so a marker never satisfies its own target.

Where markers go:
  - the book (this repository): in dev/planned.md, never in content/. MyST publishes `%` and
    `<!-- -->` comments in a page's JSON and HTML (checked with mystmd 1.10.1), so a marker in a
    chapter would be on the live site. dev/ is not built, and the repository split keeps it private.
    Targets name the material by label, which does not change when the text around it does.
  - a question (ccarrollATjhuecon/questions): in a MyST notebook master, in a cell tagged `answer`
    and `instructor`, which the build removes from both posted versions (the HTML comment around it
    hides nothing); in a LaTeX question as a comment, `% PLANNED(...): ...`, with continuation lines
    `%   ...`; or in any other Markdown file of the question that is never posted.

Triggers, which can be joined with AND (due when every part is):
  from YYYY                  due from year YYYY: for a question, the course year being posted for
                             (Choice-YYYY, --year), not the clock, so a December re-post for the
                             current course is not flagged; for the book, the calendar year.
  when-merged OWNER/REPO#N   due once that pull request has merged, read with `gh api`.
  when-live URL              due once the URL answers 200; with a #fragment, once the page also
                             has an element with that id.

States: DUE; not yet; UNKNOWN (cannot be checked: offline, a gh error, a PR closed without
merging, an unknown trigger); MALFORMED (a line that starts like a marker but does not parse);
STALE (a target is no longer where the marker says).

Usage:
    check_planned.py --root DIR PATH [PATH ...] [--year YYYY] [--quiet] [--json] [--github]
    check_planned.py --root DIR --all [--year YYYY]
    check_planned.py --self-test

--root is required, so that a copy fetched into a cache never searches its own location: it is the
folder that holds what is checked (the questions repository; the book's root). Each PATH, relative
to it, is a folder whose .md and .tex files are read (body.tex excepted), or a single file. --all
checks every folder in it except scripts/, docs/ and names starting with "_" or ".". Paths are
printed relative to it. --github also prints each marker that needs attention as a GitHub Actions
warning. The book's workflow runs `python code/check_planned.py --root . dev/planned.md --github`.
Standard library and gh only, so it runs under any Python 3.8+ with no environment.

Exit status: 0 when nothing needs attention; 4 when something is due; 5 when nothing is due but
something is UNKNOWN, MALFORMED or STALE; 2 on a usage error. A posting tool stops on 4 or 5; the
book's workflow reports and carries on.

This file is the only copy (Chris, 2026-10-08). The questions repository's posting tools fetch it
from this repository by a pinned commit; changes to it are made here.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

STRICT = re.compile(r"^(?P<indent>\s*)(?P<comment>%+\s*)?PLANNED\((?P<inside>[^)]*)\):\s*(?P<text>.*)$")
LOOSE = re.compile(r"^\s*(?:%+\s*)?p\s*l\s*a\s*n+\s*e\s*d\s*\(", re.I)  # starts like a marker
TARGET = re.compile(r'Target:\s*(?:(?P<file>[^"\s][^":]*?):\s*)?"(?P<text>[^"]+)"')
ROOT = Path.cwd()  # set from --root in main()
SKIP_DIRS = {"_build", "_archive", "_history", ".git", ".ipynb_checkpoints", "node_modules"}
DUE, NOT_YET, UNKNOWN, MALFORMED, STALE = "DUE", "not yet", "UNKNOWN", "MALFORMED", "STALE"


def sources(path: Path) -> list[Path]:
    """Every file under `path` that can hold a planned change, or `path` itself if it is a file."""
    if path.is_file():
        return [path]
    found = []
    for p in sorted(path.rglob("*")):
        rel = p.relative_to(path)
        if not p.is_file() or set(rel.parts) & SKIP_DIRS or ".bak" in p.name:
            continue
        if p.suffix == ".md" or (p.suffix == ".tex" and p.name != "body.tex"):
            found.append(p)
    return found


def markers(path: Path) -> list[dict]:
    """Each marker with its continuation lines, and each line that starts like one but does not
    parse."""
    lines = path.read_text(errors="replace").splitlines()
    found, i = [], 0
    while i < len(lines):
        m = STRICT.match(lines[i])
        if not m:
            if LOOSE.match(lines[i]):
                found.append(dict(file=path, line=i + 1, end=i + 1, trigger="?", source="", targets=[],
                                  text=lines[i].strip(), malformed=True))
            i += 1
            continue
        latex, start = bool(m["comment"]), len(m["indent"])
        text, j = [m["text"].strip()], i + 1
        while j < len(lines):
            line = lines[j]
            if latex and not re.match(r"^\s*%", line):
                break
            body = re.sub(r"^\s*%+", "", line) if latex else line
            if not body.strip() or STRICT.match(line) or LOOSE.match(line) or line.strip().startswith("-->"):
                break
            if len(body) - len(body.lstrip()) <= (0 if latex else start):
                break
            text.append(body.strip())
            j += 1
        trigger, _, source = m["inside"].partition(";")
        joined = " ".join(t for t in text if t)
        targets = [(t["file"], t["text"]) for t in TARGET.finditer(joined)]
        found.append(dict(file=path, line=i + 1, end=j, trigger=trigger.strip(), source=source.strip(),
                          targets=targets, text=joined, malformed=False))
        i = j
    return found


def gh_pr(repo: str, number: str) -> tuple[str, str]:
    result = subprocess.run(["gh", "api", f"repos/{repo}/pulls/{number}"], capture_output=True, text=True)
    if result.returncode != 0:
        reason = "not visible to the active gh account, or it does not exist" if "Not Found" in result.stderr \
            else result.stderr.strip()[:80]
        return UNKNOWN, f"gh cannot read {repo}#{number}: {reason}"
    pr = json.loads(result.stdout)
    if pr.get("merged_at"):
        return DUE, f"{repo}#{number} merged {pr['merged_at'][:10]}"
    if pr.get("state") == "closed":
        return UNKNOWN, f"{repo}#{number} was closed without merging: decide what happens to this change"
    return NOT_YET, f"{repo}#{number} is open"


def live(spec: str) -> tuple[str, str]:
    url, _, fragment = spec.partition("#")
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            page = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return NOT_YET, f"{url} answers {e.code}"
    except Exception as e:  # offline, DNS, timeout
        return UNKNOWN, f"could not reach {url}: {e.__class__.__name__}"
    if fragment and f'id="{fragment}"' not in page:
        return NOT_YET, f"no #{fragment} on {url} yet"
    return DUE, f"{spec} is live"


def status_one(trigger: str, year: int) -> tuple[str, str]:
    if m := re.fullmatch(r"from\s+(\d{4})", trigger):
        return (DUE if year >= int(m[1]) else NOT_YET), f"checking for {year}"
    if m := re.fullmatch(r"when-merged\s+([\w.-]+/[\w.-]+)#(\d+)", trigger):
        return gh_pr(m[1], m[2])
    if m := re.fullmatch(r"when-live\s+(\S+)", trigger):
        return live(m[1])
    return UNKNOWN, f"unrecognised trigger {trigger!r}"


def without_markers(path: Path) -> str:
    """A file's text with every marker removed, so that a target is never found in a marker that
    describes it."""
    if not path.is_file():
        return ""
    lines = path.read_text(errors="replace").splitlines()
    for m in markers(path):
        lines[m["line"] - 1:m["end"]] = [""] * (m["end"] - m["line"] + 1)
    return " ".join(" ".join(lines).split())


def status(item: dict, base: Path, year: int) -> tuple[str, str]:
    """The marker's state, and why. Parts of a trigger joined by AND must all be due."""
    if item["malformed"]:
        return MALFORMED, "starts like a marker but does not parse: PLANNED(<trigger>; <who, when>): ..."
    for file, text in item["targets"]:
        where = base / file if file else item["file"]
        if " ".join(text.split()) not in without_markers(where):
            return STALE, f'target "{text}" is no longer in {shown(where)}'
    parts = [status_one(t.strip(), year) for t in re.split(r"\s+AND\s+", item["trigger"])]
    why = "; ".join(w for _, w in parts)
    states = {s for s, _ in parts}
    if NOT_YET in states:
        return NOT_YET, why
    return (UNKNOWN if UNKNOWN in states else DUE), why


def check(path: Path, year: int) -> list[dict]:
    base = path if path.is_dir() else ROOT
    items = [m for p in sources(path) for m in markers(p)]
    for item in items:
        item["state"], item["why"] = status(item, base, year)
        if not item["source"] and not item["malformed"]:
            item["why"] += "; no ruling recorded"
    return items


def exit_code(items: list[dict]) -> int:
    states = {i["state"] for i in items}
    return 4 if DUE in states else 5 if states & {UNKNOWN, MALFORMED, STALE} else 0


def shown(path: Path) -> str:
    return os.path.relpath(path, ROOT)


def report(path: Path, items: list[dict], year: int, quiet: bool, github: bool) -> None:
    pending = [i for i in items if i["state"] != NOT_YET]
    if not items:
        if not quiet:
            print(f"{shown(path)}: no planned changes")
        return
    if quiet and not pending:
        return
    print(f"{shown(path)} (checking for {year}): {len(items)} planned change(s), {len(pending)} need attention")
    for i in items:
        if quiet and i["state"] == NOT_YET:
            continue
        print(f"  {i['state']:9} PLANNED({i['trigger']})  ({i['source'] or 'no ruling recorded'})")
        print(f"            {shown(i['file'])}:{i['line']}  [{i['why']}]")
        print(f"            {i['text']}")
    if github:
        for i in pending:
            print(f"::warning file={shown(i['file'])},line={i['line']}::Planned change {i['state']}: "
                  f"{i['text'][:200]} [{i['why']}]")


def self_test() -> None:
    """Offline: gh and the network are replaced by stubs that answer as the real ones would."""
    global gh_pr, live, ROOT
    real = gh_pr, live, ROOT
    prs = {"econ-ark/DemARK#277": (DUE, "merged"), "econ-ark/econ-ark.org#116": (UNKNOWN, "closed without merging"),
           "o/r#1": (NOT_YET, "open")}
    gh_pr = lambda repo, n: prs[f"{repo}#{n}"]  # noqa: E731
    live = lambda spec: (DUE, "live") if spec.endswith("#subsec-hweffect") else (NOT_YET, "answers 404")  # noqa: E731
    failures = []

    def expect(cond: bool, what: str) -> None:
        if not cond:
            failures.append(what)

    try:
        with tempfile.TemporaryDirectory() as tmp:
            q = Path(tmp) / "Question"
            q.mkdir()
            (q / "Question.md").write_text(
                "Intro.\n"
                "### For students who used the notebook\n"
                "<!--\n"
                "PLANNED(from 2027; Chris 2026-10-08): drop the section by name.\n"
                '  Target: "### For students who used the notebook"\n'
                "-->\n"
                "PLANNED(from 2027; Chris 2026-10-08): change something that is gone.\n"
                '  Target: "only in the marker text"\n'
                "Planned(from 2027; Chris): wrong case.\n"
                "PLANNED (from 2027; Chris): space before the bracket.\n"
                "PLANNED(next term; Chris 2026-10-08): unknown trigger.\n"
                "PLANNED(when-merged econ-ark/econ-ark.org#116; Chris 2026-10-08): closed unmerged.\n"
                "PLANNED(when-merged econ-ark/DemARK#277 AND from 2027; Chris 2026-10-08): both due.\n"
                "PLANNED(when-merged econ-ark/DemARK#277 AND when-merged o/r#1; Chris 2026-10-08): one open.\n"
                "PLANNED(when-live https://x.org/p#subsec-hweffect; Chris 2026-10-08): live.\n"
                "PLANNED(from 2027): no ruling.\n"
                "Planned changes (see the README) are prose, not a marker.\n")
            (q / "Question.tex").write_text(
                "\\section{Q}\n% PLANNED(from 2027; Chris 2026-10-08): reword the LaTeX question.\n"
                '%   Target: Question.md: "Intro."\n')
            (q / "body.tex").write_text("% PLANNED(from 2027; Chris 2026-10-08): generated, never read\n")
            items = check(q, 2027)
            got = [(i["text"].split(".")[0], i["state"]) for i in items]
            want = [("drop the section by name", DUE), ("change something that is gone", STALE),
                    ("Planned(from 2027; Chris): wrong case", MALFORMED),
                    ("PLANNED (from 2027; Chris): space before the bracket", MALFORMED),
                    ("unknown trigger", UNKNOWN), ("closed unmerged", UNKNOWN), ("both due", DUE),
                    ("one open", NOT_YET), ("live", DUE), ("no ruling", DUE),
                    ("reword the LaTeX question", DUE)]
            expect(got == want, f"states: got {got}")
            expect(not any("generated" in i["text"] for i in items), "body.tex was read")
            expect(not any("prose" in i["text"] for i in items), "prose taken for a marker")
            expect(items[-1]["targets"] == [("Question.md", "Intro.")], "LaTeX continuation not read")
            expect("no ruling recorded" in items[9]["why"], "missing ruling not reported")
            expect(exit_code(items) == 4, "exit code with something due")
            expect(exit_code([i for i in items if i["state"] != DUE]) == 5, "exit code with only problems")
            expect(exit_code([i for i in items if i["state"] == NOT_YET]) == 0, "exit code with nothing due")
            expect([i["state"] for i in check(q, 2026)][0] == NOT_YET, "from-year counted before its year")
            # A single file: targets are relative to --root, as dev/planned.md's are.
            (Path(tmp) / "dev").mkdir()
            (Path(tmp) / "dev" / "planned.md").write_text(
                "PLANNED(from 2027; Chris 2026-10-08): edit a chapter.\n"
                '  Target: Question/Question.md: "Intro."\n')
            ROOT = Path(tmp)
            items = check(ROOT / "dev" / "planned.md", 2027)
            expect([i["state"] for i in items] == [DUE], f"file argument: got {[i['state'] for i in items]}")
            expect(shown(items[0]["file"]) == os.path.join("dev", "planned.md"), "paths not shown relative to --root")
            (Path(tmp) / "scripts").mkdir()
            (Path(tmp) / "scripts" / "README.md").write_text("PLANNED(from 2027; Chris): an example.\n")
            expect([f.name for f in every_folder(ROOT)] == ["Question", "dev"], "--all folders")
    finally:
        gh_pr, live, ROOT = real
    if failures:
        print("check_planned self-test FAILED:\n  " + "\n  ".join(failures), file=sys.stderr)
        sys.exit(1)
    print("check_planned self-test passed")


def every_folder(root: Path) -> list[Path]:
    return [d for d in sorted(root.iterdir()) if d.is_dir() and not d.name.startswith(("_", "."))
            and d.name not in {"scripts", "docs"}]


def main() -> None:
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", type=Path, help="folders or files to check, relative to --root")
    parser.add_argument("--root", type=Path, help="the folder holding what is checked (required)")
    parser.add_argument("--all", action="store_true", help="check every folder in --root")
    parser.add_argument("--year", type=int, default=date.today().year,
                        help="the year to check for: for a question, the course year being posted for")
    parser.add_argument("--quiet", action="store_true", help="print only what needs attention")
    parser.add_argument("--json", action="store_true", help="print the markers as JSON instead")
    parser.add_argument("--github", action="store_true", help="also print GitHub Actions warnings")
    parser.add_argument("--self-test", action="store_true", help="run the offline self-test and exit")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.root is None:
        parser.error("--root is required")
    if not args.root.is_dir():
        print(f"--root {args.root} is not a folder", file=sys.stderr)
        sys.exit(2)
    ROOT = args.root.resolve()
    if bool(args.paths) == args.all:
        parser.error("give folders or files, or --all")
    paths = every_folder(ROOT) if args.all else [ROOT / p for p in args.paths]
    for p in paths:
        if not p.exists():
            print(f"{shown(p)} does not exist under {ROOT}", file=sys.stderr)
            sys.exit(2)
    results = [(p, check(p, args.year)) for p in paths]
    if args.json:
        print(json.dumps([{k: (shown(v) if k == "file" else v) for k, v in i.items()}
                          for _, items in results for i in items], indent=1))
    else:
        for p, items in results:
            report(p, items, args.year, quiet=args.quiet or args.all, github=args.github)
    code = max([exit_code(items) for _, items in results] or [0])
    if args.all and code == 0 and not args.json:
        print(f"nothing needs attention for {args.year}")
    sys.exit(code)


if __name__ == "__main__":
    main()
