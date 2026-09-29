# Porting a handout from LaTeX to MyST

Used for `content/consumption/TractableBufferStock.md` (PR #10, 2026-09-25), converted
from `TractableBufferStock.tex` in the public repository llorracc/TractableBufferStock.
Three scripts, run in this order:

1. `convert.py SRC.tex OUT.md REPORT.json`: a deterministic converter. It is a
   balanced-brace scanner rather than pandoc, because pandoc loses `\label`s inside
   `aligned`, renumbers and moves footnotes, and cannot handle a footnote that contains
   display math. It turns sections into headings with `(sec:TBS-...)=` anchors,
   `equation` environments into ```` ```{math} ```` blocks with `:label:`, `$...$` into
   `` {math}`...` ``, and `\eqref`, `\ref`, `\cite`, `\footnote` and `\handoutC` into
   their MyST forms; figures become `:::{figure} #nb-...` embeds of notebook cells; comments,
   margin notes and layout commands are dropped. `REPORT.json` records the label map, the
   margin notes dropped, unmapped references, and the counts the fidelity check uses.
   The source line ranges, the `TBS-` label prefix and the macro rewrites at the top are
   specific to that handout: adjust them for another.
2. `manual_edits_TractableBufferStock.py IN.md OUT.md`: the manual pass on the converter's
   output, recorded as exact replacements so the conversion can be replayed. Every edit
   must match exactly once; a miss fails loudly rather than skipping. Another handout
   needs its own such file.
3. `fidelity.py SRC.tex CHAPTER.md`: compares the finished chapter with its source: the
   counts of display equations, labels, references, citations, footnotes and figures;
   that labels and references map one to one; that every display equation is identical
   after the converter's normalisations; and that no LaTeX residue is left outside math.

The figure notebook (`content/notebooks/TractableBufferStock.md`) and the bibliography
entries were written by hand.
