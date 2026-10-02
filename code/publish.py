"""Publish the book: copy this repository's content into the public repository as one commit.

The book is developed in a private repository, intertemporal-choice.github.io-source, whose
site is a preview of the next release. Readers see the public repository,
intertemporal-choice.github.io, which builds and serves https://intertemporal-choice.github.io
with the same workflow. This script is the whole of the machinery between the two:

  1. it checks that this checkout is `main`, has no uncommitted changes to tracked files,
     and is identical to `origin/main`, so what is published is what was reviewed and
     previewed;
  2. it clones the public repository, removes its tracked files, and unpacks
     `git archive HEAD` of this repository in their place. `git archive` exports the
     committed tree and honours .gitattributes, which marks dev/ as export-ignore, so that
     folder never leaves this repository;
  3. it commits the difference as "Publish YYYY-MM-DD: <message>" and pushes it to `main`.
     The public repository's workflow then builds, verifies and deploys the site; if that
     build fails, the previous site stays up.

If nothing differs it says so and stops. `--dry-run` shows what would be committed and
stops there. It asks before pushing unless `--yes` is given, and refuses to run from a
clone of the public repository.

`--self-test` runs the whole flow against throwaway repositories: a first publication into
an empty repository, an update, a deletion, and each refusal.

Usage: python code/publish.py -m "what changed" [--dry-run] [--yes] [--self-test]
"""

import argparse
import datetime
import io
import logging
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = "intertemporal-choice/intertemporal-choice.github.io"
PUBLIC_URL = f"https://github.com/{PUBLIC}.git"
STAT_LINES = 40


class PublishError(Exception):
    pass


def git(*args: str, cwd: Path) -> str:
    done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if done.returncode:
        raise PublishError(f"git {' '.join(args)} failed in {cwd}:\n{done.stderr.strip()}")
    return done.stdout


def same_repo(a: str, b: str) -> bool:
    def norm(url: str) -> str:
        return url.strip().rstrip("/").removesuffix(".git").lower()

    return norm(a) == norm(b)


def check_source(root: Path, public_url: str) -> str:
    """The commit to publish, once every refusal has been passed."""
    origin = git("remote", "get-url", "origin", cwd=root).strip()
    if same_repo(origin, public_url):
        raise PublishError(
            "this is a clone of the public repository; run publish.py from the source repository"
        )
    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=root).strip()
    if branch != "main":
        raise PublishError(f"on branch {branch}, not main")
    if git("status", "--porcelain", "--untracked-files=no", cwd=root).strip():
        raise PublishError("uncommitted changes to tracked files; commit or stash them first")
    git("fetch", "-q", "origin", "main", cwd=root)
    head = git("rev-parse", "HEAD", cwd=root).strip()
    if head != git("rev-parse", "origin/main", cwd=root).strip():
        raise PublishError(
            "HEAD is not origin/main; push or pull first, so that what is published is "
            "what was reviewed"
        )
    return head


def export(root: Path, dest: Path) -> None:
    """Unpack the committed tree of `root` into `dest`, leaving out what is export-ignore."""
    done = subprocess.run(
        ["git", "archive", "--format=tar", "HEAD"], cwd=root, capture_output=True
    )
    if done.returncode:
        raise PublishError(f"git archive failed:\n{done.stderr.decode().strip()}")
    with tarfile.open(fileobj=io.BytesIO(done.stdout)) as tar:
        tar.extractall(dest, filter="data")


def clone_public(public_url: str, into: Path) -> Path:
    clone = into / "public"
    git("clone", "-q", public_url, str(clone), cwd=into)
    # A repository with no commit yet (the first publication) gets its main branch here.
    has_commit = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", "HEAD"], cwd=clone, capture_output=True
    )
    if has_commit.returncode:
        git("symbolic-ref", "HEAD", "refs/heads/main", cwd=clone)
    elif git("rev-parse", "--abbrev-ref", "HEAD", cwd=clone).strip() != "main":
        git("checkout", "-q", "main", cwd=clone)
    return clone


def stage(root: Path, clone: Path) -> None:
    """Replace the clone's tracked files with the source's committed tree, staged."""
    if git("ls-files", cwd=clone).strip():
        git("rm", "-r", "-q", ".", cwd=clone)
    export(root, clone)
    git("add", "-A", cwd=clone)


def staged_summary(clone: Path) -> str:
    stat = git("diff", "--cached", "--stat=100", cwd=clone).rstrip().splitlines()
    if len(stat) > STAT_LINES:
        stat = stat[:STAT_LINES] + ["   ..."] + stat[-1:]
    return "\n".join(stat)


def confirm() -> bool:
    return input("Push this to the public repository? [y/N] ").strip().lower() == "y"


def publish(
    root: Path, public_url: str, message: str, *, dry_run: bool = False, yes: bool = False
) -> str | None:
    """Publish `root`'s main into `public_url`; the new commit, or None if nothing was pushed."""
    head = check_source(root, public_url)
    with tempfile.TemporaryDirectory() as tmp:
        clone = clone_public(public_url, Path(tmp))
        stage(root, clone)
        if not git("status", "--porcelain", cwd=clone).strip():
            log.info("nothing to publish: the public repository already matches %s", head[:12])
            return None
        log.info("to publish, from source commit %s:\n%s", head[:12], staged_summary(clone))
        if dry_run:
            log.info("dry run: nothing committed")
            return None
        if not yes and not confirm():
            log.info("not published")
            return None
        subject = f"Publish {datetime.date.today():%Y-%m-%d}: {message}"
        git("commit", "-q", "-m", subject, "-m", f"Source commit {head}.", cwd=clone)
        git("push", "-q", "-u", "origin", "main", cwd=clone)
        sha = git("rev-parse", "HEAD", cwd=clone).strip()
        log.info("published as %s: %s", sha[:12], subject)
        return sha


def watch_deploy(public_url: str, sha: str) -> None:
    """Follow the public repository's build of the pushed commit, if `gh` is available."""
    if "github.com/" not in public_url:
        return
    slug = public_url.split("github.com/", 1)[1].removesuffix(".git")
    actions = f"https://github.com/{slug}/actions"
    if not shutil.which("gh"):
        log.info("the site deploys when the build passes; watch it at %s", actions)
        return
    for _ in range(12):  # the run appears a few seconds after the push
        found = subprocess.run(
            ["gh", "run", "list", "--repo", slug, "--commit", sha, "--json", "databaseId",
             "--jq", ".[0].databaseId"],
            capture_output=True, text=True,
        ).stdout.strip()
        if found:
            break
        time.sleep(5)
    else:
        log.info("no workflow run found yet for %s; watch %s", sha[:12], actions)
        return
    log.info("watching the build and deploy of %s", sha[:12])
    subprocess.run(["gh", "run", "watch", found, "--repo", slug, "--exit-status"])


def self_test() -> bool:
    """The whole flow against throwaway repositories."""
    ok = True
    level = log.level
    log.setLevel(logging.WARNING)
    for var in ("GIT_AUTHOR_NAME", "GIT_COMMITTER_NAME"):
        os.environ.setdefault(var, "publish self-test")
    for var in ("GIT_AUTHOR_EMAIL", "GIT_COMMITTER_EMAIL"):
        os.environ.setdefault(var, "self-test@localhost")

    def expect(condition: bool, failure: str) -> None:
        nonlocal ok
        if not condition:
            log.error("SELF-TEST FAIL: %s", failure)
            ok = False

    def refuses(root: Path, public: str, why: str) -> None:
        try:
            publish(root, public, "should be refused", yes=True)
            expect(False, f"published although {why}")
        except PublishError:
            pass

    def write(path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit_and_push(src: Path, subject: str) -> None:
        git("add", "-A", cwd=src)
        git("commit", "-q", "-m", subject, cwd=src)
        git("push", "-q", "origin", "main", cwd=src)

    def published_files(public: Path) -> set[str]:
        return set(git("ls-tree", "-r", "--name-only", "main", cwd=public).split())

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        src = tmp / "source"
        src.mkdir()
        git("init", "-q", "-b", "main", cwd=src)
        write(src / "content/a.md", "# a\n")
        write(src / "code/x.py", "print(1)\n")
        write(src / "dev/private.py", "not for publication\n")
        write(src / ".gitattributes", "dev/** export-ignore\n")
        git("add", "-A", cwd=src)
        git("commit", "-q", "-m", "first", cwd=src)
        origin = tmp / "source-origin.git"
        git("init", "-q", "--bare", "-b", "main", str(origin), cwd=tmp)
        git("remote", "add", "origin", str(origin), cwd=src)
        git("push", "-q", "-u", "origin", "main", cwd=src)
        public = tmp / "public.git"
        git("init", "-q", "--bare", "-b", "main", str(public), cwd=tmp)

        sha = publish(src, str(public), "first publication", yes=True)
        expect(sha is not None, "the first publication pushed nothing")
        expect(
            published_files(public) == {"content/a.md", "code/x.py", ".gitattributes"},
            f"the public repository holds {published_files(public)}",
        )
        subject = git("log", "-1", "--format=%s", "main", cwd=public).strip()
        expect(
            subject.startswith("Publish ") and subject.endswith(": first publication"),
            f"unexpected commit subject {subject!r}",
        )
        expect(
            publish(src, str(public), "again", yes=True) is None,
            "an unchanged source was published again",
        )

        write(src / "content/a.md", "# a, revised\n")
        write(src / "content/b.md", "# b\n")
        commit_and_push(src, "revise a, add b")
        expect(
            publish(src, str(public), "revise", yes=True) is not None,
            "a revision was not published",
        )
        expect(
            git("show", "main:content/a.md", cwd=public) == "# a, revised\n"
            and "content/b.md" in published_files(public),
            "the revision did not reach the public repository",
        )

        (src / "code/x.py").unlink()
        commit_and_push(src, "remove x")
        publish(src, str(public), "remove", yes=True)
        expect("code/x.py" not in published_files(public), "a deletion did not propagate")
        expect(
            "dev/private.py" not in published_files(public), "dev/ reached the public repository"
        )

        write(src / "scratch.txt", "untracked\n")
        expect(
            publish(src, str(public), "noop", yes=True) is None,
            "an untracked file was treated as a change",
        )
        (src / "scratch.txt").unlink()

        write(src / "content/a.md", "dirty\n")
        refuses(src, str(public), "a tracked file had uncommitted changes")
        git("checkout", "-q", "--", "content/a.md", cwd=src)

        write(src / "content/c.md", "# c\n")
        git("add", "-A", cwd=src)
        git("commit", "-q", "-m", "unpushed", cwd=src)
        refuses(src, str(public), "HEAD was ahead of origin/main")
        git("push", "-q", "origin", "main", cwd=src)

        git("checkout", "-q", "-b", "topic", cwd=src)
        refuses(src, str(public), "the checkout was not on main")
        git("checkout", "-q", "main", cwd=src)

        pub_clone = tmp / "public-clone"
        git("clone", "-q", str(public), str(pub_clone), cwd=tmp)
        refuses(pub_clone, str(public), "it was run from a clone of the public repository")

    log.setLevel(level)
    log.info("self-test %s", "passed" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="what this publication changes")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true", help="push without asking")
    parser.add_argument("--public-url", default=PUBLIC_URL)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)
    if not args.message and not args.dry_run:
        parser.error("-m MESSAGE is required (what this publication changes)")

    try:
        sha = publish(ROOT, args.public_url, args.message or "", dry_run=args.dry_run, yes=args.yes)
    except PublishError as e:
        log.error("not published: %s", e)
        sys.exit(1)
    if sha:
        watch_deploy(args.public_url, sha)
