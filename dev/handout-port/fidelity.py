"""Compare the ported chapter against TractableBufferStock.tex: counts, labels and references,
display math block by block, and LaTeX residue outside math. Usage: fidelity.py SRC.tex CHAPTER.md"""
import re, sys
from collections import Counter

src_path, md_path = sys.argv[1:3]
lines = open(src_path).read().split("\n")
end_h = next(i for i, l in enumerate(lines) if l.startswith("% Local Variables"))
body = "\n".join(lines[25:1602]) + "\n" + "\n".join(lines[1608:end_h])
body = "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in body.split("\n"))
body = re.sub(r"\\begin\{comment\}.*?\\end\{comment\}", "", body, flags=re.S)
md = open(md_path).read()
problems = []

# 1. counts
src_display = re.findall(r"\\begin\{(equation\*?)\}(.*?)\\end\{\1\}", body, re.S)
md_display = re.findall(r"```\{math\}\n(.*?)```", md, re.S)
src_eqlabels = [l for _, b in src_display for l in re.findall(r"\\label\{(eq:[^}]+)\}", b)]
src_eqlabels += [l for l in re.findall(r"\\label\{(eq:[^}]+)\}", body) if l not in src_eqlabels]
md_eqlabels = re.findall(r":label: (eq:\S+)", md)
src_eqrefs = re.findall(r"\\eqref\{([^}]+)\}", body)
md_eqrefs = re.findall(r"\{eq\}`([^`]+)`", md)
src_cites = re.findall(r"\\cite[pt]?\*?(?:\[[^]]*\])?\{([^}]+)\}", body)
md_cites = re.findall(r"\{cite:[pt]\}`([^`]+)`", md)
src_fn = len(re.findall(r"\\footnote\{", body))
md_fn = len(re.findall(r"^\[\^[^\]]+\]:", md, re.M))
src_fig = len(re.findall(r"\\begin\{figure\}", body))
md_fig = len(re.findall(r":::\{figure\} #nb-", md))
print(f"{'':12}{'source':>8}{'chapter':>9}")
for name, a, b in [("display", len(src_display), len(md_display)), ("eq labels", len(set(src_eqlabels)), len(md_eqlabels)),
                   ("eq refs", len(src_eqrefs), len(md_eqrefs)), ("citations", len(src_cites), len(md_cites)),
                   ("footnotes", src_fn, md_fn), ("figures", src_fig, md_fig)]:
    print(f"{name:12}{a:>8}{b:>9}")

# 2. labels and references map one to one (source label X -> chapter eq:TBS-X, one renamed)
renamed = {"eq:Metp1": "eq:TBS-MLevtp1"}
def mapped(x): return renamed.get(x, "eq:TBS-" + x.split(":", 1)[1])
missing = [l for l in set(src_eqlabels) if mapped(l) not in md_eqlabels]
extra = [l for l in md_eqlabels if l not in {mapped(x) for x in src_eqlabels}]
dangling = sorted({r for r in md_eqrefs if r not in md_eqlabels and not r.startswith("eq:") is False})
dangling = sorted({r for r in md_eqrefs if r.startswith("eq:TBS-") and r not in md_eqlabels})
src_ref_counts = Counter(mapped(r) if r.startswith("eq:") else r for r in src_eqrefs)
md_ref_counts = Counter(md_eqrefs)
ref_diff = {k: (src_ref_counts[k], md_ref_counts[k]) for k in set(src_ref_counts) | set(md_ref_counts) if src_ref_counts[k] != md_ref_counts[k]}
for name, v in [("labels missing from chapter", missing), ("labels not in source", extra), ("dangling refs", dangling), ("ref count differences", ref_diff)]:
    print(f"{name}: {v if v else 'none'}")

# 3. display math, normalised by the converter's substitutions
def norm(b):
    b = re.sub(r":label: \S+|\\label\{[^}]+\}|\\notag|\\nonumber", "", b)
    b = re.sub(r"\\(begin|end)\{(gathered|split|aligned)\}", "", b)
    b = b.replace("^{\\hideSup}", "").replace("_{\\tSS}", "").replace("\\MPCU", "\\MPC").replace("\\GPFacRaw", "\\PatPGro")
    b = b.replace("\\dddot{\\star}", "\\overset{\\dots}{\\star}")
    return re.sub(r"\s+|&", "", b)
S = [norm(b) for _, b in src_display]
M = [norm(b) for b in md_display]
unmatched_src = [i for i, s in enumerate(S) if s not in M]
unmatched_md = [i for i, m in enumerate(M) if m not in S]
order_ok = [s for s in S if s in M] == [m for m in M if m in S]
print(f"display blocks matching after normalisation: {sum(s in M for s in S)}/{len(S)}; same order: {order_ok}")
for i in unmatched_src:
    lab = re.findall(r"\\label\{([^}]+)\}", src_display[i][1])
    print(f"  source block {i} {lab} has no identical chapter block")

# 4. residue outside math, code and directives
text = re.sub(r"```.*?```", "", md, flags=re.S)
text = re.sub(r"\{[a-z:]+\}`[^`]*`", "", text)
text = re.sub(r"`[^`]*`", "", text)
residue = [(n + 1, l.strip()[:90]) for n, l in enumerate(text.split("\n")) if re.search(r"\\|\$|~|--", l)]
print(f"residue lines: {residue if residue else 'none'}")
