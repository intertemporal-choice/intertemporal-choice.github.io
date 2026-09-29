"""The manual pass over convert.py's output, recorded as exact edits so it can be replayed.

Usage: python manual_edits.py IN.md OUT.md
Every edit must match exactly once; a miss fails loudly rather than silently skipping.
"""

import re
import sys

src, dst = sys.argv[1:3]
md = open(src).read()


def rep(old, new, count=1):
    global md
    n = md.count(old)
    if n != count:
        raise SystemExit(f"expected {count} match(es), found {n}: {old[:90]!r}")
    md = md.replace(old, new)


def figure_block(suffix):
    m = re.search(r":::\{figure\} #nb-TractableBufferStock-" + suffix + r"\n.*?\n:::\n\n", md, re.S)
    if not m:
        raise SystemExit(f"figure {suffix} not found")
    return m.group(0)


def move_figure(suffix, after):
    """Move a figure block to just after the paragraph/footnote ending with `after`."""
    global md
    block = figure_block(suffix)
    md = md.replace(block, "", 1)
    i = md.index(after)
    j = md.index("\n\n", i + len(after)) + 2
    md = md[:j] + block + md[j:]


PFC = "[PerfForesightCRRA](#sec:PerfForesightCRRA)"
SEC = "the [perfect foresight CRRA](#sec:PerfForesightCRRA) section"

# ---- opening: companion material and the figure notebook
rep(
    "# A Tractable Model of Buffer Stock Saving\n\n## Introduction\n\nThis handout illustrates",
    "# A Tractable Model of Buffer Stock Saving\n\n"
    "A companion notebook in the Econ-ARK DemARK collection, "
    "[Tractable Buffer Stock (interactive)](https://econ-ark.org/materials/tractablebufferstock-interactive), "
    "lets you vary the model's parameters and watch the consumption function and target wealth respond. "
    "HARK solves the model as its "
    "[`TractableConsumerType`](https://github.com/econ-ark/HARK/blob/main/examples/TractableBufferStockModel/TractableConsumerType.ipynb), "
    "and this chapter's figures are drawn with that class by its [figure notebook](../notebooks/TractableBufferStock.md).\n\n"
    "## Introduction\n\nThis chapter illustrates",
)

# ---- links to other chapters (\handoutC / \handoutM)
rep(f"See {PFC} for a derivation", f"See {SEC} for a derivation")
rep(f"in the perfect foresight problem ({PFC}).", f"in the perfect foresight problem (see {SEC}).")
rep(f"For a perfect foresight consumer, {PFC} shows", f"For a perfect foresight consumer, {SEC} shows")
rep(f"The same solution methods used in {PFC} can be applied", f"The same solution methods used in {SEC} can be applied")
rep("use the [Envelope](#sec:Envelope) theorem", "use the [Envelope theorem](#sec:Envelope)")
rep(f"(again see {PFC})", f"(again see {SEC})")
rep(f"which, as in {PFC}, we call", f"which, as in {SEC}, we call")
rep(f"imposed earlier. {PFC} shows that the limit", f"imposed earlier. The [perfect foresight CRRA](#sec:PerfForesightCRRA) section shows that the limit")
rep(f"The handout {PFC} shows that in the perfect foresight context", "The [perfect foresight CRRA](#sec:PerfForesightCRRA) section shows that in the perfect foresight context")
rep(f"The appendix to {PFC} shows that", "The [appendix to the perfect foresight CRRA section](#sec:PFwhenFHWfails) shows that")

# ---- links to this chapter's appendices
rep("[Appendix](#sec:TBS-CGroApprox) shows that", "The [appendix on approximate consumption growth](#sec:TBS-CGroApprox) shows that")
rep("See [appendix](#sec:TBS-mTargExists) for a proof", "See the [appendix on conditions for a target](#sec:TBS-mTargExists) for a proof")
rep("[Appendix](#sec:TBS-mTargExists) demonstrates that", "The [appendix on conditions for a target](#sec:TBS-mTargExists) demonstrates that")
rep("[Appendix](#sec:TBS-mTargExact) solves for an explicit formula", "The [appendix on the exact target formula](#sec:TBS-mTargExact) solves for an explicit formula")
rep("the appendix shows that (under some strong assumptions)", "the [approximation appendix](#sec:TBS-mTargApprox) shows that (under some strong assumptions)")
rep("The appendix shows that, in the special case", "The [approximation appendix](#sec:TBS-mTargApprox) shows that, in the special case")
rep("(see the discussion below in [appendix section](#sec:TBS-PGroGEQRfree))",
    "(see the [appendix on the case where growth exceeds the interest factor](#sec:TBS-PGroGEQRfree) below)")

# ---- dashes (the book uses none)
rep("small open economy -- there is a constant interest factor", "small open economy, so there is a constant interest factor")
rep("{math}`\\MPC > 0` -- the consumer must not be", "{math}`\\MPC > 0`: the consumer must not be")
rep("boosts consumption growth[^tbs-least-continuing-employed] -- in the logarithmic case,", "boosts consumption growth;[^tbs-least-continuing-employed] in the logarithmic case,")
rep("A different future -- with the consumer unemployed -- does occur;", "A different future (with the consumer unemployed) does occur;")
rep("remains in employment -- a condition whose probability", "remains in employment, a condition whose probability")
rep("resources - he will always leave", "resources; he will always leave")

# ---- the footnote that held display math: promote it into the text
rep(
    "so long as {math}`\\straight > 0`.[^tbs-will-hold-true]",
    "so long as {math}`\\straight > 0`. That holds if and only if the numerator on the LHS of {eq}`eq:TBS-straightDef` is a positive finite number, which requires",
)
rep(
    "[^tbs-will-hold-true]: This will hold true iff the numerator on the LHS of {eq}`eq:TBS-straightDef` is a positive finite number; for this, we we need the condition:\n\n",
    "",
)

# ---- margin notes with substance, folded in
rep(
    "(which is the proportion by which consumption would be greater next period for an employed than for an unemployed person), and define",
    "(which is the proportion by which consumption would be greater next period for an employed than for an unemployed person),[^tbs-nabla-mnemonic] and define",
)
rep(
    "and define an \"excess prudence\" factor\n\n",
    "and define an \"excess prudence\" factor\n\n"
    "[^tbs-nabla-mnemonic]: Mnemonic: {math}`\\nabla` is like {math}`\\Delta`, a change, but it points down, because it measures the fall in consumption if unemployment strikes.\n\n",
)
rep(
    "will be the point of intersection between the {math}`\\dcEqZero` and {math}`\\dmEqZero` loci.",
    "will be the point of intersection between the {math}`\\dcEqZero` and {math}`\\dmEqZero` loci. Here and below, a variable without a time subscript denotes its steady-state value.",
)
rep(
    "(which comes from {eq}`eq:TBS-cDelEqZero`) is a bit subtler.",
    "(which comes from {eq}`eq:TBS-cDelEqZero`) is a bit subtler, because it reflects preferences: it comes from the Euler equation, not from the budget constraint, which gives the {math}`\\Delta \\mRatE = 0` locus.",
)

# ---- figures: refer by number, and place each after the paragraph that first cites it
rep("The next figure shows the optimal consumption function", "{numref}`fig:TBS-cFunc` shows the optimal consumption function")
move_figure("cFunc", "[^tbs-limiting-result-requires]: This limiting result")
rep("The next figure (\"the growth diagram\") illustrates", "{numref}`fig:TBS-GrowthA` (\"the growth diagram\") illustrates")
move_figure("GrowthB", "as would be expected on intuitive grounds.")
rep(
    "The next exercise is an increase in the risk of unemployment {math}`\\urate.`",
    "The next exercise, shown in {numref}`fig:TBS-cGroIncreaseMhoPlot`, is an increase in the risk of unemployment {math}`\\urate`.",
)
move_figure("DecreaseTheta", "[^tbs-could-also-analyze]: We could also analyze")
rep(
    "The final figures depict the time paths of consumption, market wealth, and the marginal propensity to consume",
    "{numref}`fig:TBS-cPathAfterThetaDrop`, {numref}`fig:TBS-mPathAfterThetaDrop` and {numref}`fig:TBS-MPCPathAfterThetaDrop` depict the time paths of consumption, market wealth, and the marginal propensity to consume",
)
rep("the dots in these two new diagrams are spread out", "the dots in these three diagrams are spread out")

# ---- code references: the public repository, and what the book uses instead
rep(
    "A notebook {cite:t}`When-FHWC-Holds` (see references for details) in the code archive associated with these lecture notes shows how this works for alternative values of {math}`\\Discount.`",
    "A *Mathematica* notebook in the handout's repository, "
    "[`When-FHWC-Holds.nb`](https://github.com/llorracc/TractableBufferStock/blob/main/Code/Mathematica/Examples/ManipulateParameters/When-FHWC-Holds.nb) "
    "({cite:t}`When-FHWC-Holds`), shows how this works for alternative values of {math}`\\Discount`.",
)
rep(
    "The *Mathematica* code constructs this derivative and solves the quadratic equation analytically; the Matlab code simply copies the analytical formula generated by *Mathematica* .",
    "The *Mathematica* code in the handout's [repository](https://github.com/llorracc/TractableBufferStock) constructs this derivative and solves the quadratic equation analytically; its Matlab code simply copies the analytical formula generated by *Mathematica*. This chapter's figures instead use HARK's `TractableConsumerType`, which solves the model by the same reverse shooting.",
)
rep("*Mathematica* permits the convenient", "*Mathematica* permits the convenient")  # (kept; asserts presence)

# ---- equations that need restructuring
rep(
    "\\begin{aligned}\n"
    "\\lefteqn{  (\\MPCFunc^{e}_{t})^{2} \\uPPP(\\cFunc^{e}_{t}) +\\MPCFunc_{t}^{e\\prime}\\uPP(\\cFunc^{e}_{t}) = } &    \\\\\n"
    "&  \\beth \\Rnorm \\left\\{(-\\MPCFunc_{t}^{e\\prime}) \\Ex_{t}[\\uPP(\\cFunc^{\\bullet}_{t+1})\\MPCFunc^{\\bullet}_{t+1}]\n"
    "+  \\Rnorm (1-\\MPCFunc^{e}_{t})^{2}\\left(\\Ex_{t}[(\\MPCFunc_{t+1}^{\\bullet})^{2}\\uPPP(\\cFunc^{\\bullet}_{t+1})]+\\erate  \\uPP(\\cFunc^{e}_{t+1})\\MPCFunc_{t+1}^{e\\prime}\\right)\\right\\}  \\\\\n"
    "\\end{aligned}",
    "\\begin{aligned}\n"
    "(\\MPCFunc^{e}_{t})^{2} \\uPPP(\\cFunc^{e}_{t}) +\\MPCFunc_{t}^{e\\prime}\\uPP(\\cFunc^{e}_{t}) & = \\beth \\Rnorm \\Big\\{(-\\MPCFunc_{t}^{e\\prime}) \\Ex_{t}[\\uPP(\\cFunc^{\\bullet}_{t+1})\\MPCFunc^{\\bullet}_{t+1}]\n"
    "\\\\ & \\quad +  \\Rnorm (1-\\MPCFunc^{e}_{t})^{2}\\left(\\Ex_{t}[(\\MPCFunc_{t+1}^{\\bullet})^{2}\\uPPP(\\cFunc^{\\bullet}_{t+1})]+\\erate  \\uPP(\\cFunc^{e}_{t+1})\\MPCFunc_{t+1}^{e\\prime}\\right)\\Big\\}\n"
    "\\end{aligned}",
)
m = re.search(r"(:label: eq:TBS-kappaPReverse\n\n)\\begin\{aligned\}\n(.*?)\\\\\n\\end\{aligned\}", md, re.S)
if not m:
    raise SystemExit("kappaPReverse not found")
row = " ".join(m.group(2).replace(" & ", " ").split())
md = md[: m.start()] + m.group(1) + row + md[m.end():]

# ---- appendix anchors for the unlabelled appendices
rep("### Approximating Target {math}`m`", "(sec:TBS-mTargApprox)=\n### Approximating Target {math}`m`")
rep("### Numerical Solution", "(sec:TBS-NumericalSolution)=\n### Numerical Solution")
rep("### The Algorithm", "(sec:TBS-Algorithm)=\n### The Algorithm")

# ---- Appendix H: kept for reference, marked superseded
rep(
    "<!-- APPENDIX H FOLLOWS (after \\end{document} in the source) -->\n\n### The Marginal Propensity to Consume at Target Wealth\n\n",
    "(sec:TBS-MPCatTarget)=\n### The Marginal Propensity to Consume at Target Wealth\n\n"
    "This appendix is kept for reference. It is not part of the published handout: in the source it follows the end "
    "of the document, marked as superseded by the reverse-shooting derivation in the "
    "[numerical solution appendix](#sec:TBS-NumericalSolution), and preserved because its derivations are useful for checking.\n\n",
)
rep(
    "Differentiating {eq}`eq:TBS-naturalMPC`, dropping arguments, and evaluating at the steady state yields",
    "Differentiating {eq}`eq:TBS-naturalMPC`, dropping arguments, and evaluating at the steady state yields[^tbs-eta-undefined]",
)
rep(
    "Differentiating {eq}`eq:TBS-naturalMPC`, dropping arguments, and evaluating at the steady state yields[^tbs-eta-undefined]\n\n",
    "Differentiating {eq}`eq:TBS-naturalMPC`, dropping arguments, and evaluating at the steady state yields[^tbs-eta-undefined]\n\n"
    "[^tbs-eta-undefined]: The source does not define {math}`\\eta`; the derivation is reproduced as it stands there.\n\n",
)

# ---- typos in the source
rep("corresonding", "corresponding")
rep("arrow orginating", "arrow originating")
rep("illustate", "illustrate")
rep("and everywhere drop {math}`e` the superscripts", "and everywhere drop the {math}`e` superscripts")
rep("continuous-time treatement", "continuous-time treatment")

# ---- found by the strict build
# MyST lowercases identifiers, so the source's eq:Metp1 (levels) and eq:metp1 (ratios) collide.
rep(":label: eq:TBS-Metp1\n", ":label: eq:TBS-MLevtp1\n")
rep("{eq}`eq:TBS-Metp1`", "{eq}`eq:TBS-MLevtp1`")
# KaTeX has no \dddot, and amsmath already defines it, so a macros.yml entry would break the PDF.
rep("\\dddot{\\star}", "\\overset{\\dots}{\\star}", count=10)

open(dst, "w").write(md)
print("manual edits applied")
