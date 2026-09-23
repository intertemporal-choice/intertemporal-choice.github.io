"""Reconcile sources/ against Carroll's website and report every gap.

sources/ mirrors the per-handout source zips published alongside the lecture notes at
econ2.jhu.edu. Each handout's zip holds the real LaTeX; the PDF is only the rendering.
This lists every handout on every section index, says whether the mirror has it and
whether a source zip exists, and exits non-zero when anything is missing. --fetch
downloads and extracts what is absent.

Two constraints the enumeration has to respect, both learned by getting them wrong:

  Enumerate BOTH href="...pdf" and href="...zip". Swapping the .pdf suffix for .zip
  finds most handouts but not RamseyNumericSolve, which is linked only as a zip.
  Never skip a stem with no existing sources/<part>/<Handout>/ directory. Doing so
  can refresh what the mirror already has and can never add anything new.

Usage: uv run python code/mirror_check.py [--fetch]
"""

import argparse
import io
import itertools
import logging
import re
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

BASE = "https://www.econ2.jhu.edu/people/ccarroll/public/LectureNotes"
# Website section -> the sources/ subdirectory it maps to.
SECTIONS = {
    "Consumption": "consumption",
    "AssetPricing": "asset_pricing",
    "Investment": "investment",
    "Growth": "growth",
    "DSGEModels": "dsge",
    "MathFacts": "appendix",
}
# Handouts that are on the site but deliberately outside the book. Each needs a
# reason, so that "not mirrored" never quietly becomes "forgotten".
EXCLUDED = {
    "TractableBufferStock": "Carroll and Toche paper, not a handout",
    "PalgravePrecautionary": "Palgrave entry under /papers/, not a handout",
    "AggImplications": "IMF minicourse, syllabus and slides only",
    "AggImplicationsSyllabus": "minicourse syllabus",
    "AggGimplicationsSlides": "minicourse slides (404 on Carroll's own index)",
}
ARTIFACT_EXT = {
    ".aux",
    ".log",
    ".out",
    ".bbl",
    ".blg",
    ".toc",
    ".lof",
    ".lot",
    ".fls",
    ".fdb_latexmk",
    ".synctex.gz",
    ".xbb",
    ".def",
    ".vrb",
    ".upa",
    ".upb",
    ".cuts",
    ".dep",
    ".idx",
    ".ilg",
    ".ind",
    ".nav",
    ".snm",
    ".4ht",
    ".4ct",
    ".4tc",
    ".mk4",
    ".idv",
    ".lg",
    ".xref",
    ".tmp",
    ".dvi",
    ".ps",
    ".svg",
    ".html",
    ".htm",
    ".css",
    ".sty",
    ".cls",
    ".bst",
    ".cnf",
    ".cfg",
    ".texmf",
    ".el",
    ".title",
    ".zip",
    ".db",
    ".webloc",
    ".old",
    ".bat",
    ".rel",
    ".fff",
    ".txsprofile",
}


def curl(url, binary=False):
    # -f and check=True: a failed or 404 fetch must raise, since an empty index reads
    # as "nothing missing" and a 404 page would be saved as the handout's PDF.
    out = subprocess.run(
        ["curl", "-fsSL", "--max-time", "90", url],
        capture_output=True,
        text=not binary,
        check=True,
    )
    return out.stdout


def head_status(url):
    out = subprocess.run(
        ["curl", "-sSI", "-L", "--max-time", "30", url],
        capture_output=True,
        text=True,
        check=False,
    ).stdout
    codes = re.findall(r"^HTTP/[\d.]+ (\d+)", out, re.MULTILINE)
    return int(codes[-1]) if codes else 0


def handouts_on_site(section):
    """Every handout stem linked from a section index, however it is linked.

    Both .pdf and .zip hrefs count. Taking only .pdf was the original defect.
    """
    html = curl(f"{BASE}/{section}/")
    stems = set()
    for href in re.findall(r'href="([^"]+)"', html):
        m = re.search(rf"/{section}/([A-Za-z0-9_-]+)\.(pdf|zip)$", href)
        if m:
            stems.add(m.group(1))
    return sorted(stems)


def excluded_from_zip(path, stem):
    parts = [p.lower() for p in path.parts]
    if "web" in parts:
        return True
    if any(p.startswith("texmf") for p in parts):
        return True
    if any(a == b for a, b in itertools.pairwise(parts)):
        return True
    if path.suffix.lower() in ARTIFACT_EXT:
        return True
    return path.name.lower() == f"{stem.lower()}.pdf"


def extract(stem, blob, dest):
    written = 0
    with zipfile.ZipFile(io.BytesIO(blob)) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            rel = PurePosixPath(info.filename)
            if ".." in rel.parts or rel.is_absolute() or excluded_from_zip(rel, stem):
                continue
            out = dest.joinpath(*rel.parts)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(zf.read(info.filename))
            written += 1
    return written


ap = argparse.ArgumentParser()
ap.add_argument("--fetch", action="store_true", help="download what is missing")
args = ap.parse_args()

sources = Path("sources")
missing, pdf_only, ok = [], [], 0

for section, part in SECTIONS.items():
    for stem in handouts_on_site(section):
        if stem in EXCLUDED:
            continue
        local = sources / part / stem
        if local.is_dir():
            ok += 1
            continue
        zip_url = f"{BASE}/{section}/{stem}.zip"
        if head_status(zip_url) == 200:
            missing.append((section, part, stem, zip_url))
        else:
            pdf_only.append((section, part, stem))

log.info("mirrored and present: %d", ok)
log.info("")
if missing:
    log.info("=== MISSING from the mirror, source zip available ===")
    for section, part, stem, url in missing:
        log.info("  %-12s %-26s %s", section, stem, url)
if pdf_only:
    log.info("=== on the site with NO source zip (PDF only) ===")
    for section, part, stem in pdf_only:
        log.info("  %-12s %-26s %s/%s/%s.pdf", section, stem, BASE, section, stem)
log.info("")
for stem, why in sorted(EXCLUDED.items()):
    log.info("excluded by policy: %-26s %s", stem, why)

if args.fetch:
    log.info("")
    for section, part, stem, url in missing:
        dest = sources / part / stem
        n = extract(stem, curl(url, binary=True), dest)
        log.info("fetched %s -> %s (%d files)", stem, dest, n)
    # For a handout with no zip the compiled PDF is the only source there is, so the
    # usual "drop the compiled PDF" rule does not apply; without it the mirror holds
    # nothing at all for a handout the book may already draw a chapter from.
    for section, part, stem in pdf_only:
        dest = sources / part / stem
        dest.mkdir(parents=True, exist_ok=True)
        out = dest / f"{stem}.pdf"
        out.write_bytes(curl(f"{BASE}/{section}/{stem}.pdf", binary=True))
        log.info(
            "fetched %s -> %s (%d bytes, PDF is the source)",
            stem,
            out,
            out.stat().st_size,
        )

raise SystemExit(1 if missing else 0)
