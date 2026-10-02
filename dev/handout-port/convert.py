"""One-off converter: TractableBufferStock.tex (public repo) -> MyST chapter draft.

Deterministic; its output is then edited by hand (see manual_edits_TractableBufferStock.py)
and checked against the source (fidelity.py). Usage: python convert.py SRC.tex OUT.md REPORT.json
"""

import json
import re
import sys

SRC, OUT, REPORT = sys.argv[1:4]
lines = open(SRC).read().split("\n")
# Body lines 26-1602 and the post-\end{document} Appendix H (1609 up to the Emacs locals).
end_h = next(i for i, l in enumerate(lines) if l.startswith("% Local Variables"))
body = "\n".join(lines[25:1602]) + "\n\\TBSAPPENDIXH\n" + "\n".join(lines[1608:end_h])

report = {"margin_notes": [], "footnote_with_display": [], "labels": {}, "unmapped_refs": []}


# ---------------------------------------------------------------- helpers
def strip_comments(text):
    out = []
    for line in text.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        if m:
            line = line[: m.start()]
            if not line.strip():
                out.append(None)  # a comment-only line vanishes entirely
                continue
        out.append(line)
    return "\n".join(l for l in out if l is not None)


def balanced(text, start):
    """Given text[start] == '{', return index just past the matching '}'."""
    depth = 0
    for i in range(start, len(text)):
        c = text[i]
        if c == "\\":
            continue
        if c == "{" and (i == 0 or text[i - 1] != "\\"):
            depth += 1
        elif c == "}" and text[i - 1] != "\\":
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError("unbalanced braces at %d" % start)


def take_command(text, name, handler):
    """Replace every \\name{arg} (balanced) with handler(arg)."""
    out, i = [], 0
    pat = re.compile(r"\\" + name + r"\s*\{")
    while True:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:])
            return "".join(out)
        brace = m.end() - 1
        end = balanced(text, brace)
        out.append(text[i : m.start()])
        out.append(handler(text[brace + 1 : end - 1]))
        i = end


def new_label(old):
    for prefix in ("eq:", "fig:", "sec:", "subsec:", "subsubsec:"):
        if old.startswith(prefix):
            kind = {"eq:": "eq", "fig:": "fig"}.get(prefix, "sec")
            return f"{kind}:TBS-{old[len(prefix):]}"
    return f"eq:TBS-{old}"


# ---------------------------------------------------------------- stage 1: source cleanup
t = strip_comments(body)
t = re.sub(r"\\begin\{comment\}.*?\\end\{comment\}", "", t, flags=re.S)


def margin(arg):
    inner = re.sub(r"^\s*\\marginpar\s*\{\s*\\tiny\s*", "", arg).rstrip("} \n")
    report["margin_notes"].append(inner)
    return ""


# \opt{MarginNotes}{\marginpar{\tiny ...}}: record the note, drop the whole construct
while True:
    m = re.search(r"\\opt\{MarginNotes\}\s*\{", t)
    if not m:
        break
    end = balanced(t, m.end() - 1)
    margin(t[m.end() : end - 1])
    t = t[: m.start()] + t[end:]
t = re.sub(r"\\hypertarget\{[^}]*\}\{\}", "", t)
t = re.sub(r"\\label\{sec:PFwhenFHWfails\}", "", t)  # stray; the book's label lives elsewhere
t = re.sub(r"\\pagebreak|\\medskip|\\indent\b", "", t)
t = re.sub(r"\\centerline\\textbf\{\\LARGE Appendix\}", "", t)
t = re.sub(r"\\setcounter\{section\}\{0\}", "", t)
t = re.sub(r"\\input handoutBibMake\.tex", "", t)
t = t.replace("\\appendix", "\\TBSAPPENDIX")

# Macro conflicts: rewrite so the book's macros.yml need not change (see the plan).
t = re.sub(r"\^\{\\hideSup\}", "", t)
t = re.sub(r"\\hideSup\b", "", t)
t = re.sub(r"_\{\\tSS\}", "", t)
t = re.sub(r"\\tSS\b", "", t)
t = re.sub(r"\\MPCU(?![A-Za-z])", r"\\MPC", t)
t = re.sub(r"\\GPFacRaw(?![A-Za-z])", r"\\PatPGro", t)
t = t.replace("\\cite{carrollBSTheory}", "\\cite{BufferStockTheory}")

# ---------------------------------------------------------------- stage 2: labels
all_labels = re.findall(r"\\label\{([^}]+)\}", t)
for old in all_labels:
    report["labels"][old] = new_label(old)


def ref_target(old):
    if old in report["labels"]:
        return report["labels"][old]
    report["unmapped_refs"].append(old)
    return new_label(old)


# ---------------------------------------------------------------- stage 3: inline conversion
def convert_math(m):
    body = " ".join(m.split())
    return "{math}`" + body + "`"


TEXT_MATH_MACROS = ["GICPGro", "GICWGro", "FHWCPGro", "FHWCWGro", "FHWC"]


def convert_text(s):
    """Convert a text-mode run (no display math) to MyST."""
    # references first (they contain braces)
    s = re.sub(
        r"Figures~\\ref\{([^}]+)\}\s+and\s+\\ref\{([^}]+)\}",
        lambda m: "{numref}`" + ref_target(m.group(1)) + "` and {numref}`" + ref_target(m.group(2)) + "`",
        s,
    )
    s = re.sub(r"[Ff]igures?[~ ]?\s*\\ref\{([^}]+)\}", lambda m: "{numref}`" + ref_target(m.group(1)) + "`", s)
    s = re.sub(r"\\eqref\{([^}]+)\}", lambda m: "{eq}`" + ref_target(m.group(1)) + "`", s)
    s = re.sub(
        r"(appendix section|[Aa]ppendix)~?\s*\\ref\{([^}]+)\}",
        lambda m: f"[{m.group(1)}](#{ref_target(m.group(2))})",
        s,
    )
    s = re.sub(r"\\ref\{([^}]+)\}", lambda m: "{numref}`" + ref_target(m.group(1)) + "`", s)
    # citations: parenthetical when alone in parentheses
    s = re.sub(r"\(\\cite\{([^}]+)\}\)", lambda m: "({cite:p}`" + m.group(1) + "`)", s)
    s = re.sub(r"\\cite\{([^}]+)\}", lambda m: "{cite:t}`" + m.group(1) + "`", s)
    # links to other handouts
    s = re.sub(r"\\handout[CM]\{([^}]+)\}", lambda m: f"[{m.group(1)}](#sec:{m.group(1)})", s)
    s = s.replace("\\MathFactsList", "[Math Facts](#fact:mathfactslist)")
    s = s.replace("\\TaylorOne", "[TaylorOne](#fact:taylorone)")
    s = s.replace("\\TaylorTwo", "[TaylorTwo](#fact:taylortwo)")
    s = re.sub(r"\\Mma~?", "*Mathematica* ", s)
    # text-mode macros that typeset math, only outside $...$
    parts = re.split(r"(\$[^$]+\$)", s)
    for k in range(0, len(parts), 2):
        for name in TEXT_MATH_MACROS:
            parts[k] = re.sub(
                r"\\" + name + r"(?![A-Za-z])(~?)",
                lambda m, n=name: "{math}`\\" + n + "`" + (" " if m.group(1) else ""),
                parts[k],
            )
    s = "".join(parts)
    # inline math
    s = re.sub(r"\$([^$]+)\$", lambda m: convert_math(m.group(1)), s)
    # emphasis
    s = re.sub(r"\{\\it\s+([^{}]*)\}", r"*\1*", s)
    s = take_command(s, "textbf", lambda a: "**" + a + "**")
    s = take_command(s, "emph", lambda a: "*" + a + "*")
    # quotes: ``x'' and `x'
    s = re.sub(r"``(.*?)''", r'"\1"', s, flags=re.S)
    s = re.sub(r"`([^`']{1,80}?)'(?![A-Za-z])", r'"\1"', s)
    s = s.replace("\\^{o}", "ô").replace('\\^o', "ô")
    # spacing and escapes
    s = s.replace("\\ ", " ").replace("~", " ").replace("\\%", "%").replace("\\&", "&")
    s = re.sub(r"(i\.e|e\.g|cf|eq)\.\\?\s", r"\1. ", s)
    return s


# ---------------------------------------------------------------- stage 4: blocks
def display_math(env_body):
    labels = re.findall(r"\\label\{([^}]+)\}", env_body)
    if len(labels) > 1:
        raise ValueError(f"display block with labels {labels}")
    b = re.sub(r"\\label\{[^}]+\}", "", env_body)
    b = re.sub(r"\\notag|\\nonumber", "", b)
    b = re.sub(r"\\begin\{gathered\}|\\end\{gathered\}", "", b)
    b = b.replace("\\begin{split}", "\\begin{aligned}").replace("\\end{split}", "\\end{aligned}")
    b = "\n".join(l.rstrip() for l in b.strip().split("\n") if l.strip())
    inner = re.sub(r"\\begin\{aligned\}|\\end\{aligned\}", "", b).strip()
    single_row = "\\\\" not in inner
    if single_row and b.startswith("\\begin{aligned}"):
        b = inner.replace("&", "").strip()  # one-row aligned: unwrap
        b = re.sub(r"\s+", " ", b)
    head = "```{math}\n" + (f":label: {new_label(labels[0])}\n\n" if labels else "")
    return head + b + "\n```", labels


footnotes = []  # (slug, text)
used_slugs = set()


def slug_for(text):
    plain = re.sub(r"\]\([^)]*\)", "]", text)  # link targets are not words of the note
    plain = re.sub(r"\{math\}`[^`]*`|\{[a-z:]+\}`[^`]*`|```.*?```", " ", plain, flags=re.S)
    words = re.findall(r"[A-Za-z]{3,}", plain)
    stop = {"the", "and", "for", "that", "this", "with", "are", "not", "see", "which", "from", "its", "has", "have"}
    words = [w.lower() for w in words if w.lower() not in stop][:3] or ["note"]
    slug = "tbs-" + "-".join(words)
    base, n = slug, 2
    while slug in used_slugs:
        slug, n = f"{base}-{n}", n + 1
    used_slugs.add(slug)
    return slug


def convert_footnote(arg):
    if "\\begin{equation" in arg:
        report["footnote_with_display"].append(arg[:80])
        # keep the display math as a block inside the footnote for the manual pass
        parts = re.split(r"(\\begin\{equation\*?\}.*?\\end\{equation\*?\})", arg, flags=re.S)
        conv = []
        for p in parts:
            if p.startswith("\\begin{equation"):
                env = re.match(r"\\begin\{(equation\*?)\}(.*)\\end\{\1\}", p, re.S)
                block, _ = display_math(env.group(2))
                conv.append("\n\n" + block + "\n\n")
            else:
                conv.append(" ".join(convert_text(p).split()))
        text = "".join(conv).strip()
    else:
        text = " ".join(convert_text(arg).split())
    slug = slug_for(text)
    footnotes.append((slug, text))
    return f"[^{slug}]"


t = take_command(t, "footnote", convert_footnote)

# figures -> directive placeholders
figs = []


def figure(m):
    inner = m.group(1)
    cap_start = inner.index("\\caption")
    brace = inner.index("{", cap_start)
    caption = inner[brace + 1 : balanced(inner, brace) - 1]
    label = re.search(r"\\label\{([^}]+)\}", inner).group(1)
    suffix = label.split(":", 1)[1]
    figs.append(suffix)
    cap = " ".join(convert_text(caption).split())
    return (
        f"\n\n:::{{figure}} #nb-TractableBufferStock-{suffix}\n:name: {new_label(label)}\n\n{cap}\n:::\n\n"
    )


t = re.sub(r"\\begin\{figure\}(.*?)\\end\{figure\}", figure, t, flags=re.S)
report["figures"] = figs

# display math
display_labels = []


def display(m):
    block, labels = display_math(m.group(2))
    display_labels.extend(labels)
    return "\n\n" + block + "\n\n"


t = re.sub(r"\\begin\{(equation\*?)\}(.*?)\\end\{\1\}", display, t, flags=re.S)

# headings
in_appendix = False
section_titles = {}


def heading(m):
    global in_appendix
    level = {"section": 2, "subsection": 3, "subsubsection": 4}[m.group(1)]
    if in_appendix:
        level += 1
    title_tex = m.group(2)
    label = m.group(3)
    title = " ".join(convert_text(title_tex).split())
    anchor = f"({new_label(label)})=\n" if label else ""
    if label:
        section_titles[label] = title
    return f"\n\n{anchor}{'#' * level} {title}\n\n"


def heading_pass(text):
    global in_appendix
    out = []
    for chunk in re.split(r"(\\TBSAPPENDIXH|\\TBSAPPENDIX)", text):
        if chunk == "\\TBSAPPENDIX":
            in_appendix = True
            out.append("\n\n## Appendix\n\n")
            continue
        if chunk == "\\TBSAPPENDIXH":
            out.append("\n\n<!-- APPENDIX H FOLLOWS (after \\end{document} in the source) -->\n\n")
            continue
        out.append(
            re.sub(
                r"\\(section|subsection|subsubsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}\s*(?:\\label\{([^}]+)\})?",
                heading,
                chunk,
            )
        )
    return "".join(out)


t = heading_pass(t)

# ---------------------------------------------------------------- stage 5: paragraphs
blocks = re.split(r"(```\{math\}.*?```|:::\{figure\}.*?:::)", t, flags=re.S)
out = []
for b in blocks:
    if b.startswith("```{math}") or b.startswith(":::{figure}"):
        out.append(b)
        continue
    paras = re.split(r"\n\s*\n", b)
    conv = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if p.startswith("#") or re.match(r"\(sec:[^)]+\)=", p) or p.startswith("<!--"):
            conv.append(p)
            continue
        conv.append(" ".join(convert_text(p).split()))
    out.append("\n\n".join(conv))
md = "\n\n".join(x.strip() for x in out if x.strip())

# footnote definitions after the paragraph that first cites them
paras = md.split("\n\n")
result = []
fn = dict(footnotes)
for p in paras:
    result.append(p)
    for slug in re.findall(r"\[\^([^\]]+)\](?!:)", p):
        if slug in fn:
            result.append(f"[^{slug}]: {fn.pop(slug)}")
if fn:
    report["unplaced_footnotes"] = list(fn)
md = "\n\n".join(result)

header = "(sec:TractableBufferStock)=\n# A Tractable Model of Buffer Stock Saving\n\n"
open(OUT, "w").write(header + md.strip() + "\n")

# residue outside math and code spans
plain = re.sub(r"```\{math\}.*?```", "", md, flags=re.S)
plain = re.sub(r"\{[a-z:]+\}`[^`]*`", "", plain)
residue = {
    k: len(re.findall(p, plain))
    for k, p in {"backslash": r"\\", "dollar": r"\$", "tilde": r"~", "dash": r"--", "backtick": r"`"}.items()
}
report["residue"] = residue
report["display_blocks"] = md.count("```{math}")
report["eq_labels"] = len(re.findall(r":label: eq:TBS-", md))
report["eq_refs"] = len(re.findall(r"\{eq\}`", md))
report["cites"] = len(re.findall(r"\{cite:[tp]\}`", md))
report["footnote_defs"] = len(re.findall(r"^\[\^[^\]]+\]:", md, re.M))
report["section_titles"] = section_titles
json.dump(report, open(REPORT, "w"), indent=1)
print(json.dumps({k: v for k, v in report.items() if k not in ("labels", "section_titles", "margin_notes")}, indent=1))
print("margin notes:", len(report["margin_notes"]))
