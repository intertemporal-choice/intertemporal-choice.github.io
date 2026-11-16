"""Publish the book's package as permanent files on its site, at /packages/: a release on every change.

Chris Carroll's decisions (cc:course-choice, 2026-11-13, 18:52 EST): the package is published as "a package file on
the book's site", "not on pypi", and releases are "automatic". So every change to the package that reaches main
becomes a release, one wheel at a permanent address,

    https://intertemporal-choice.github.io/packages/intertemporal_choice-<version>-py3-none-any.whl

which a question's notebook installs by that address, so a posted answer key reruns with the code it was written
against, and a page running Python in the browser installs with micropip (GitHub Pages lets other sites download
it). Install a release by its address, never by name: `intertemporal-choice` is not on PyPI, so
`pip install intertemporal-choice` could fetch a package someone else registered under that name.

  - The version is the release's date (UTC) and a counter: 2026.11.14.1, then 2026.11.14.2. It is set here, never
    by hand, and is always higher than the last.
  - A release happens when src/ or pyproject.toml differs from what the last release was built from (releases.txt
    records their git hashes). That is compared with the last release, not the last commit, so a push whose run
    was dropped from the queue for a newer one is released by the newer one.
  - Published files are permanent: never rebuilt, changed or deleted, since posted answer keys point at them. The
    site is rebuilt whole on every deploy, so they are kept on the `packages` branch, which only this script
    writes, and only by adding a wheel and appending its line to releases.txt. Every build copies that branch
    into the site and writes the list page, /packages/index.html.

The workflow runs it twice:

  stage DIR [--release OUT]   In the build job, which can only read. Copies the kept files into DIR (the built
                              site's packages/ folder), checks that every file the live site serves is among them,
                              byte for byte, and writes the list page. If the package changed since the last release,
                              builds the next version's wheel: on a pull request only to check that it builds; with
                              --release (a push to main) it is added to DIR, and put in OUT with the new releases.txt
                              for the release job, and its version goes to the workflow's outputs.
  publish OUT                 In the release job, the only one that can write. Commits OUT's wheel and releases.txt
                              to the `packages` branch (creating the branch the first time) and pushes. It refuses
                              to replace or delete a file, and to commit if the branch moved after the build copied
                              it. The deploy waits for this job, so the site never serves a file the branch lacks.

`--self-test` runs both against a scratch repository with its own `origin`, with a stand-in for the wheel build,
and checks the versions, the refusals and the live-site check.

Usage: uv run python code/release_package.py stage _build/html/packages [--release _release]
       python3 code/release_package.py publish _release
"""

import argparse
import datetime as dt
import hashlib
import html
import logging
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
BRANCH = "packages"
NAME = "intertemporal_choice"
SITE = "https://intertemporal-choice.github.io/packages/"
COMMITS = "https://github.com/intertemporal-choice/intertemporal-choice.github.io/commit/"
LEDGER = "releases.txt"
WATCHED = ("src", "pyproject.toml")  # a release happens when either differs from the last release's
FIELDS = ("version", "released", "commit", "sha256", "src", "pyproject.toml")
LEDGER_HEAD = (
    "# Every release of the book's package, oldest first; written by code/release_package.py, never edited.\n"
    "# " + "\t".join(FIELDS) + "\n"
)
README = """# The book's package files

Every release of the book's Python package, `intertemporal-choice`, one wheel each, with `releases.txt` listing
them. The site serves them at https://intertemporal-choice.github.io/packages/.

Only `code/release_package.py` writes this branch, from the workflow, and only by adding a wheel and its line. A
file here is never changed or deleted, and the branch is never force-pushed: posted answer keys install these
files by their addresses. Install a release by its address, never by name, since the name is not on PyPI.
"""
WHEEL = re.compile(rf"^{NAME}-(\d+\.\d+\.\d+\.\d+)-py3-none-any\.whl$")
VERSION_LINE = re.compile(r'^version\s*=\s*"[^"]*"', re.M)


class Refused(Exception):
    """A release that must not happen, with the reason."""


def git(repo: Path, *args: str, binary: bool = False, check: bool = True, env: dict | None = None):
    done = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=not binary,
                          env=(os.environ | env) if env else None)
    if check and done.returncode:
        err = done.stderr.decode() if binary else done.stderr
        raise Refused(f"git {' '.join(args)} failed: {err.strip()}")
    return done.stdout if binary else done.stdout.strip()


# ---------------------------------------------------------------- the ledger and versions


def parse_ledger(text: str) -> list[dict]:
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        cells = line.split("\t")
        if len(cells) != len(FIELDS):
            raise Refused(f"{LEDGER} line {n} has {len(cells)} fields, not {len(FIELDS)}: {line!r}")
        rows.append(dict(zip(FIELDS, cells)))
    return rows


def ledger_line(row: dict) -> str:
    return "\t".join(row[f] for f in FIELDS) + "\n"


def wheel_name(version: str) -> str:
    return f"{NAME}-{version}-py3-none-any.whl"


def as_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(p) for p in version.split("."))


def next_version(today: dt.date, versions: list[str]) -> str:
    """Today's date and the next counter for it; refuses if that is not above every earlier version."""
    day = f"{today.year}.{today.month}.{today.day}"
    counters = [as_tuple(v)[3] for v in versions if v.rsplit(".", 1)[0] == day]
    version = f"{day}.{max(counters, default=0) + 1}"
    if versions and as_tuple(version) <= max(as_tuple(v) for v in versions):
        raise Refused(f"{version} would not be above the last release, {max(versions, key=as_tuple)}")
    return version


def with_version(pyproject: str, version: str) -> str:
    """pyproject.toml with its project version replaced (the first `version = "..."`, in [project])."""
    head = pyproject.find("[project]")
    match = VERSION_LINE.search(pyproject, head)
    if head < 0 or not match or "\n[" in pyproject[head + 1 : match.start()]:
        raise Refused("pyproject.toml has no version in its [project] table")
    return pyproject[: match.start()] + f'version = "{version}"' + pyproject[match.end() :]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def problems_with(files: list[str], rows: list[dict], read) -> list[str]:
    """What is wrong with a set of kept files against their ledger: a wheel not listed, a listed wheel missing
    or altered, a version listed twice, or versions out of order."""
    problems = []
    wheels = {f for f in files if f.endswith(".whl")}
    listed = [wheel_name(r["version"]) for r in rows]
    for name in sorted(wheels - set(listed)):
        problems.append(f"{name} is kept but not in {LEDGER}")
    for name in sorted(set(listed) - wheels):
        problems.append(f"{name} is in {LEDGER} but not kept")
    if len(set(listed)) != len(listed):
        problems.append(f"{LEDGER} lists a version twice")
    versions = [as_tuple(r["version"]) for r in rows]
    if versions != sorted(versions):
        problems.append(f"{LEDGER} is not in the order of its versions")
    for r in rows:
        name = wheel_name(r["version"])
        if name in wheels and sha256(read(name)) != r["sha256"]:
            problems.append(f"{name} is not the file that was released (its sha256 differs)")
    return problems


# ---------------------------------------------------------------- the kept files


def kept_branch(repo: Path) -> str | None:
    """Fetch the packages branch and return its commit, or None if it does not exist yet."""
    if not git(repo, "ls-remote", "--heads", "origin", BRANCH):
        return None
    git(repo, "fetch", "--quiet", "--depth=1", "origin", f"+refs/heads/{BRANCH}:refs/remotes/origin/{BRANCH}")
    return git(repo, "rev-parse", f"refs/remotes/origin/{BRANCH}")


def build_wheel(repo: Path, version: str, out: Path) -> Path:
    """The wheel of the committed package (src/, pyproject.toml, README.md at HEAD), at the given version."""
    with tempfile.TemporaryDirectory() as tmp:
        archive = git(repo, "archive", "--format=tar", "HEAD", "pyproject.toml", "README.md", "src", binary=True)
        subprocess.run(["tar", "-x", "-C", tmp], input=archive, check=True)
        pyproject = Path(tmp, "pyproject.toml")
        pyproject.write_text(with_version(pyproject.read_text(), version))
        built = subprocess.run(["uv", "build", "--quiet", "--wheel", "--out-dir", str(out), tmp],
                               capture_output=True, text=True)
        if built.returncode:
            raise Refused(f"the wheel did not build:\n{built.stderr}")
    wheel = out / wheel_name(version)
    if not wheel.is_file():
        raise Refused(f"the build did not write {wheel.name}: {sorted(p.name for p in out.iterdir())}")
    with zipfile.ZipFile(wheel) as z:
        meta = z.read(f"{NAME}-{version}.dist-info/METADATA").decode()
    if f"\nVersion: {version}\n" not in meta:
        raise Refused(f"{wheel.name} does not carry version {version} in its metadata")
    return wheel


def live_ledger() -> str:
    """The releases.txt the live site serves now, or "" before the first release."""
    try:
        with urllib.request.urlopen(SITE + LEDGER, timeout=30) as r:
            return r.read().decode()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return ""
        raise Refused(f"could not read the live site's {LEDGER}: {e}") from e
    except urllib.error.URLError as e:
        raise Refused(f"could not read the live site's {LEDGER}: {e}") from e


def list_page(rows: list[dict]) -> str:
    """/packages/index.html: every release, newest first, and how to install one."""
    newest = wheel_name(rows[-1]["version"]) if rows else wheel_name("<version>")
    body = "\n".join(
        f'<tr><td><a href="{wheel_name(r["version"])}">{r["version"]}</a></td>'
        f'<td>{html.escape(r["released"].replace("T", " ").rstrip("Z"))}</td>'
        f'<td><a href="{COMMITS}{r["commit"]}"><code>{r["commit"][:7]}</code></a></td></tr>'
        for r in reversed(rows)
    ) or '<tr><td colspan="3">No release yet.</td></tr>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Package files</title>
<style>
:root {{ --bg: #ffffff; --fg: #1f2328; --muted: #59636e; --line: #d1d9e0; --code: #f6f8fa; --link: #0969da; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg: #0d1117; --fg: #e6edf3; --muted: #9198a1; --line: #3d444d; --code: #151b23; --link: #4493f8; }}
}}
body {{ background: var(--bg); color: var(--fg); margin: 0; font: 16px/1.55 system-ui, sans-serif; }}
main {{ max-width: 46rem; margin: 0 auto; padding: 2rem 16px 3rem; }}
a {{ color: var(--link); }}
p.note {{ color: var(--muted); }}
pre {{ background: var(--code); border: 1px solid var(--line); border-radius: 6px; padding: .75rem; overflow-x: auto; }}
code, pre {{ font: 13.5px/1.45 ui-monospace, SFMono-Regular, Menlo, monospace; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ text-align: left; padding: .4rem .6rem; border-bottom: 1px solid var(--line); }}
th {{ color: var(--muted); font-weight: 600; }}
</style>
</head>
<body>
<main>
<h1>Package files</h1>
<p>Every release of <code>intertemporal-choice</code>, the Python package with the code of
<a href="/">the book's</a> chapters and their models, newest first. A file here is never changed or removed,
so a notebook that installs one runs the same way later.</p>
<p>Install a release by its address:</p>
<pre>%pip install -q {SITE}{newest}</pre>
<p>and with HARK, for the chapters that use it:</p>
<pre>%pip install -q "intertemporal-choice[hark] @ {SITE}{newest}"</pre>
<p class="note">Never by name: the package is not on PyPI, so <code>pip install intertemporal-choice</code> could
fetch a different package registered under that name.</p>
<table>
<thead><tr><th>Version</th><th>Released (UTC)</th><th>Built from</th></tr></thead>
<tbody>
{body}
</tbody>
</table>
<p class="note">The same list, for programs: <a href="{LEDGER}">{LEDGER}</a>.</p>
</main>
</body>
</html>
"""


def stage(repo: Path, site: Path, out: Path | None, today: dt.date, build=build_wheel, live=live_ledger) -> str | None:
    """Copy the kept files into `site` with the list page; build the next release if the package changed.
    With `out`, add that release to `site` and put it in `out` for `publish`; return its version."""
    base = kept_branch(repo)
    ref = f"refs/remotes/origin/{BRANCH}"
    files = git(repo, "ls-tree", "--name-only", ref).splitlines() if base else []
    ledger = git(repo, "show", f"{ref}:{LEDGER}") + "\n" if base and LEDGER in files else LEDGER_HEAD
    rows = parse_ledger(ledger)
    read = lambda name: git(repo, "show", f"{ref}:{name}", binary=True)  # noqa: E731
    problems = problems_with(files, rows, read)
    if problems:
        raise Refused(f"the {BRANCH} branch is inconsistent: " + "; ".join(problems))
    site.mkdir(parents=True, exist_ok=True)
    for r in rows:
        (site / wheel_name(r["version"])).write_bytes(read(wheel_name(r["version"])))
    served = parse_ledger(live())
    kept = {r["version"]: r["sha256"] for r in rows}
    for r in served:
        if kept.get(r["version"]) != r["sha256"]:
            raise Refused(f"the live site serves {wheel_name(r['version'])}, which the {BRANCH} branch does not keep "
                          "as it was released; a deploy must never drop or change a published file")
    log.info("%d release(s) kept on the %s branch, and every file the live site serves is among them",
             len(rows), BRANCH)

    head = {path: git(repo, "rev-parse", f"HEAD:{path}") for path in WATCHED}
    last = rows[-1] if rows else None
    version = None
    if last and all(last[path] == head[path] for path in WATCHED):
        log.info("the package is unchanged since %s: no release", last["version"])
    else:
        version = next_version(today, [r["version"] for r in rows])
        with tempfile.TemporaryDirectory() as tmp:
            wheel = build(repo, version, Path(tmp))
            data = wheel.read_bytes()
        if out is None:
            log.info("the package changed since the last release; merged, it would be released as %s "
                     "(built to check, not kept)", version)
            version = None
        else:
            row = {"version": version, "released": dt.datetime.now(dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
                   "commit": git(repo, "rev-parse", "HEAD"), "sha256": sha256(data), **head}
            rows.append(row)
            ledger += ledger_line(row)
            out.mkdir(parents=True, exist_ok=True)
            for folder in (site, out):
                (folder / wheel.name).write_bytes(data)
            (out / LEDGER).write_text(ledger)
            (out / "BASE").write_text((base or "none") + "\n")
            log.info("released %s, built from %s; the release job keeps it", version, row["commit"][:7])
    (site / LEDGER).write_text(ledger)
    (site / "index.html").write_text(list_page(rows))
    return version


BOT = {"GIT_AUTHOR_NAME": "github-actions[bot]", "GIT_AUTHOR_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com"}
BOT |= {"GIT_COMMITTER_NAME": BOT["GIT_AUTHOR_NAME"], "GIT_COMMITTER_EMAIL": BOT["GIT_AUTHOR_EMAIL"]}


def publish(repo: Path, out: Path) -> str:
    """Add the staged release to the packages branch: one new wheel and one new ledger line, nothing else."""
    wheels = sorted(out.glob("*.whl"))
    if len(wheels) != 1 or not WHEEL.match(wheels[0].name):
        raise Refused(f"{out} must hold exactly one release wheel, not {[w.name for w in wheels]}")
    wheel, ledger = wheels[0], (out / LEDGER).read_text()
    staged_from = (out / "BASE").read_text().strip()
    base = kept_branch(repo)
    if (base or "none") != staged_from:
        raise Refused(f"the {BRANCH} branch moved after the build copied it ({staged_from[:7]}, now "
                      f"{(base or 'none')[:7]}); nothing published, and the next push to main releases again")
    ref = f"refs/remotes/origin/{BRANCH}"
    files = git(repo, "ls-tree", "--name-only", ref).splitlines() if base else []
    before = git(repo, "show", f"{ref}:{LEDGER}") + "\n" if base else LEDGER_HEAD
    if wheel.name in files:
        raise Refused(f"{wheel.name} is already published; a published file is never replaced")
    added = parse_ledger(ledger[len(before):]) if ledger.startswith(before) else None
    if not added or len(added) != 1 or wheel_name(added[0]["version"]) != wheel.name:
        raise Refused(f"the new {LEDGER} must be the old one with one line added, for {wheel.name}")
    if added[0]["sha256"] != sha256(wheel.read_bytes()):
        raise Refused(f"{wheel.name} is not the file its {LEDGER} line describes")
    with tempfile.TemporaryDirectory() as tmp:
        index = {"GIT_INDEX_FILE": str(Path(tmp, "index"))}
        if base:
            git(repo, "read-tree", ref, env=index)
        else:
            Path(tmp, "README.md").write_text(README)
            git(repo, "update-index", "--add", "--cacheinfo",
                f"100644,{git(repo, 'hash-object', '-w', str(Path(tmp, 'README.md')))},README.md", env=index)
        Path(tmp, LEDGER).write_text(ledger)
        for path, name in ((wheel, wheel.name), (Path(tmp, LEDGER), LEDGER)):
            blob = git(repo, "hash-object", "-w", str(path))
            git(repo, "update-index", "--add", "--cacheinfo", f"100644,{blob},{name}", env=index)
        tree = git(repo, "write-tree", env=index)
    version = added[0]["version"]
    message = (f"Release {version}, built from {added[0]['commit'][:7]}\n\n{SITE}{wheel.name}\n\n"
               "Written by code/release_package.py; a file on this branch is never changed or deleted.\n")
    commit = git(repo, "commit-tree", tree, *(["-p", base] if base else []), "-m", message, env=BOT)
    if base:
        changes = git(repo, "diff-tree", "--no-renames", "--name-status", base, commit).splitlines()
        if sorted(changes) != sorted([f"A\t{wheel.name}", f"M\t{LEDGER}"]):
            raise Refused(f"the release commit would change more than a new wheel and its line: {changes}")
    git(repo, "push", "--quiet", "origin", f"{commit}:refs/heads/{BRANCH}")
    log.info("published %s%s (%s on the %s branch)", SITE, wheel.name, commit[:7], BRANCH)
    return version


# ---------------------------------------------------------------- self-test


def self_test() -> bool:
    failures = []

    def expect_refused(what: str, call, reason: str) -> None:
        """`call` must be refused, and for `reason` (a phrase of the message), not by some other check."""
        try:
            call()
            failures.append(f"accepted {what}")
        except Refused as e:
            if reason not in str(e):
                failures.append(f"refused {what}, but not for the right reason: {e}")

    d = dt.date(2026, 11, 14)
    for versions, today, want in [([], d, "2026.11.14.1"), (["2026.11.13.4"], d, "2026.11.14.1"),
                                  (["2026.11.14.1", "2026.11.14.2"], d, "2026.11.14.3"),
                                  (["2026.11.9.1"], dt.date(2026, 11, 10), "2026.11.10.1")]:
        if next_version(today, versions) != want:
            failures.append(f"next_version({versions}) gave {next_version(today, versions)}, not {want}")
    expect_refused("a version below the last (a clock gone back)", lambda: next_version(d, ["2026.11.15.1"]),
                   "would not be above")
    toml = '[project]\nname = "x"\nversion = "0.1.0"\n\n[tool.other]\nversion = "9"\n'
    if with_version(toml, "2026.11.14.1") != toml.replace("0.1.0", "2026.11.14.1"):
        failures.append("with_version changed the wrong line")
    expect_refused("a pyproject.toml whose [project] has no version",
                   lambda: with_version('[project]\nname = "x"\n[tool.other]\nversion = "9"\n', "1.1.1.1"), "no version")

    def fake_build(repo: Path, version: str, out: Path) -> Path:
        wheel = out / wheel_name(version)
        wheel.write_bytes(f"{version} {git(repo, 'rev-parse', 'HEAD:src')}".encode())
        return wheel

    with tempfile.TemporaryDirectory() as tmp:
        try:
            scratch_repository(Path(tmp), d, toml, fake_build, expect_refused, failures)
        except Exception as e:  # a check that stopped working can make a later step fail outright
            failures.append(f"the scratch run stopped: {type(e).__name__}: {e}")
    one, two = {"version": "1.1.1.1", "sha256": sha256(b"w")}, {"version": "1.1.1.2", "sha256": sha256(b"w")}
    for what, files, rows, content, want in [
        ("a wheel not in the ledger", ["a.whl", wheel_name("1.1.1.1")], [one], b"w", "is kept but not in"),
        ("a listed wheel missing", [], [one], b"w", "but not kept"),
        ("a kept wheel that was altered", [wheel_name("1.1.1.1")], [one], b"x", "not the file that was released"),
        ("a version listed twice", [wheel_name("1.1.1.1")], [one, one], b"w", "lists a version twice"),
        ("versions out of order", [wheel_name("1.1.1.1"), wheel_name("1.1.1.2")], [two, one], b"w", "not in the order"),
    ]:
        found = problems_with(files, rows, lambda name: content)
        if not any(want in f for f in found):
            failures.append(f"{what} on the branch gave {found}")
    if problems_with([wheel_name("1.1.1.1"), "README.md", LEDGER], [one], lambda name: b"w"):
        failures.append("a consistent branch was found inconsistent")
    for f in failures:
        log.error("SELF-TEST FAIL: %s", f)
    log.info("self-test %s", "FAILED" if failures else "passed")
    return not failures


def scratch_repository(tmp: Path, d: dt.date, toml: str, fake_build, expect_refused, failures: list) -> None:
    """Release, publish and refuse in a scratch repository with its own origin."""
    git(tmp, "init", "--quiet", "--bare", "origin.git")
    repo = tmp / "work"
    git(tmp, "init", "--quiet", "-b", "main", "work")
    git(repo, "remote", "add", "origin", str(tmp / "origin.git"))
    (repo / "src").mkdir()
    (repo / "src" / "m.py").write_text("x = 1\n")
    (repo / "pyproject.toml").write_text(toml)
    (repo / "README.md").write_text("readme\n")

    def commit(message: str) -> None:
        git(repo, "add", "-A")
        git(repo, "commit", "--quiet", "-m", message, env=BOT)

    commit("start")
    served = {"text": ""}
    run = lambda site, out, today=d: stage(repo, tmp / site, tmp / out if out else None, today,  # noqa: E731
                                           build=fake_build, live=lambda: served["text"])
    if run("pr", None) is not None or list((tmp / "pr").glob("*.whl")):
        failures.append("a pull request's stage released or kept a wheel")
    if run("site1", "out1") != "2026.11.14.1":
        failures.append("the first release is not 2026.11.14.1")
    publish(repo, tmp / "out1")
    if git(repo, "ls-tree", "--name-only", f"refs/remotes/origin/{BRANCH}").split() != sorted(
            ["README.md", LEDGER, wheel_name("2026.11.14.1")]):
        failures.append("the first publish did not create the branch with README.md, the wheel and the ledger")
    served["text"] = (tmp / "site1" / LEDGER).read_text()
    if run("site2", "out2") is not None:
        failures.append("released an unchanged package")
    if not (tmp / "site2" / wheel_name("2026.11.14.1")).is_file() or "2026.11.14.1" not in (tmp / "site2" / "index.html").read_text():
        failures.append("a later build dropped the kept wheel or its line on the list page")
    (repo / "src" / "m.py").write_text("x = 2\n")
    commit("change the package")
    if run("site3", "out3") != "2026.11.14.2":
        failures.append("the second release that day is not 2026.11.14.2")
    publish(repo, tmp / "out3")
    expect_refused("a publish staged before another release reached the branch",
                   lambda: publish(repo, tmp / "out3"), "moved after the build copied it")
    (tmp / "out3" / "BASE").write_text(git(repo, "rev-parse", f"refs/remotes/origin/{BRANCH}"))
    expect_refused("a wheel that is already published", lambda: publish(repo, tmp / "out3"), "already published")
    (repo / "pyproject.toml").write_text(toml + "# changed\n")
    commit("change pyproject.toml")
    if run("site4", "out4", dt.date(2026, 11, 15)) != "2026.11.15.1":
        failures.append("a change to pyproject.toml on a new day is not released as 2026.11.15.1")
    bad = tmp / "out4"
    good = (bad / LEDGER).read_text()
    (bad / LEDGER).write_text(good.replace("2026.11.14.1\t", "2026.11.14.9\t"))
    expect_refused("a ledger that rewrites an earlier line", lambda: publish(repo, bad), "one line added")
    (bad / LEDGER).write_text(good)
    wheel = bad / wheel_name("2026.11.15.1")
    data = wheel.read_bytes()
    wheel.write_bytes(data + b"tampered")
    expect_refused("a wheel that is not the one its ledger line describes", lambda: publish(repo, bad),
                   "is not the file its")
    wheel.write_bytes(data)
    live_now = (tmp / "site3" / LEDGER).read_text()
    served["text"] = live_now + "2026.11.14.7\t2026-11-14T00:00:00Z\tc\ts\ta\tb\n"
    expect_refused("a build that drops a file the live site serves", lambda: run("site5", None),
                   "the live site serves")
    first = parse_ledger(live_now)[0]["sha256"]
    served["text"] = live_now.replace(first, "0" * 64)
    expect_refused("a build whose file differs from the one the live site serves", lambda: run("site5", None),
                   "the live site serves")
    served["text"] = live_now
    publish(repo, bad)
    if run("site6", None) is not None:
        failures.append("a pull request's stage returned a version")
    rows = parse_ledger((tmp / "site6" / LEDGER).read_text())
    if [r["version"] for r in rows] != ["2026.11.14.1", "2026.11.14.2", "2026.11.15.1"]:
        failures.append(f"the kept releases are {[r['version'] for r in rows]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="command")
    staging = sub.add_parser("stage")
    staging.add_argument("site", type=Path)
    staging.add_argument("--release", type=Path, metavar="OUT")
    publishing = sub.add_parser("publish")
    publishing.add_argument("out", type=Path)
    args = parser.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    try:
        if args.command == "stage":
            version = stage(ROOT, args.site, args.release, dt.datetime.now(dt.UTC).date())
            if version and os.environ.get("GITHUB_OUTPUT"):
                with open(os.environ["GITHUB_OUTPUT"], "a") as f:
                    f.write(f"version={version}\n")
        elif args.command == "publish":
            publish(ROOT, args.out)
        else:
            parser.error("say stage, publish or --self-test")
    except Refused as e:
        log.error("REFUSED: %s", e)
        sys.exit(1)
