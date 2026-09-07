(sec:RiskAndPSPremia)=
# Risk Premia and Precautionary Premia

A consumer who faces a risk to future consumption suffers two distinct consequences, and it is easy to conflate them. The first is that the risk makes the consumer worse off; we would like to know how much the consumer would pay to be rid of it. The second is that the risk changes the consumer's behavior, inducing extra saving; we would like to know how much. The two questions have different answers, and each is governed by a different property of the utility function. This section defines the measure that answers each one.

Suppose the consumer would consume {math}`\bar{\cons}` in the absence of risk, and now faces an additive mean-zero shock {math}`\epsilon` that takes the value {math}`-\alpha` or {math}`+\alpha`, each with probability one half. The parameter {math}`\alpha>0` indexes the size of the risk.

## The Pratt-Arrow Risk Premium

The measure of how much the consumer dislikes the risk was introduced by {cite:t}`pratt:smallandlarge`. The risk premium {math}`\pi^{*}` is the amount by which certain consumption would have to be reduced to make the consumer exactly as badly off as the risk makes them:

```{math}
:label: eq:RiskPrem

\uFunc(\bar{\cons}-\pi^{*}) = \Ex[\uFunc(\bar{\cons}+\epsilon)].
```

In words, {math}`\pi^{*}` measures willingness to pay, in units of certain consumption, to have the risk removed.

{numref}`fig:RiskAndPSPremiaRisk` constructs {math}`\pi^{*}` geometrically. The two possible outcomes {math}`\bar{\cons}-\alpha` and {math}`\bar{\cons}+\alpha` are marked on the horizontal axis, and the dashed straight line joining the corresponding points on the utility function is the chord between them. Because each outcome occurs with probability one half, expected utility {math}`\Ex[\uFunc(\bar{\cons}+\epsilon)]` is the height of the midpoint of that chord, which sits directly above {math}`\bar{\cons}`. The figure shows this height lying strictly below {math}`\uFunc(\bar{\cons})`, the height of the curve itself at {math}`\bar{\cons}`; this is Jensen's inequality, and it holds for any mean-zero risk whenever {math}`\uFunc` is concave, {math}`\uPP<0`. Tracing that height horizontally back to the utility function locates the certainty-equivalent consumption level {math}`\bar{\cons}-\pi^{*}`, and the horizontal distance from there to {math}`\bar{\cons}` is the risk premium. Concavity of {math}`\uFunc` is therefore exactly what makes {math}`\pi^{*}` positive: risk aversion is what makes the risk unwelcome.

:::{figure} /content/figures/RiskAndPSPremia/RiskAndPSPremiaRisk.png
:name: fig:RiskAndPSPremiaRisk
:align: center

The Pratt-Arrow risk premium {math}`\pi^{*}`. Expected utility is the midpoint of the chord, which lies below the utility function because {math}`\uFunc` is concave.
:::

## The Kimball Precautionary Premium

Willingness to pay, however, is not what determines saving. Saving is chosen by comparing marginal utilities, so the object that matters for behavior is the effect of the risk on expected *marginal* utility. The corresponding measure comes from {cite:t}`kimball:smallandlarge`, who defines the precautionary premium {math}`\mu^{*}` as the reduction in certain consumption that would raise marginal utility by as much as the risk does:

```{math}
:label: eq:PrecPrem

\uP(\bar{\cons}-\mu^{*}) = \Ex[\uP(\bar{\cons}+\epsilon)].
```

The definition is {eq}`eq:RiskPrem` with {math}`\uP` written everywhere in place of {math}`\uFunc`. Its behavioral content is that a consumer facing the risk acts, at the margin, like a consumer with no risk whose consumption has been cut by {math}`\mu^{*}`; the extra saving that produces the cut is precautionary saving.

{numref}`fig:RiskAndPSPremiaPrec` repeats the geometry of the previous figure one derivative up. The chord now joins {math}`\uP(\bar{\cons}-\alpha)` to {math}`\uP(\bar{\cons}+\alpha)`, and its midpoint gives {math}`\Ex[\uP(\bar{\cons}+\epsilon)]`. The direction of the inequality reverses: because {math}`\uP` is a *convex* function, the chord lies *above* the curve, so the risk *raises* expected marginal utility. Convexity of {math}`\uP` means {math}`\uPPP>0`, the property Kimball named prudence. Since {math}`\uP` is downward sloping, reading the elevated marginal utility back to the curve locates a consumption level *below* {math}`\bar{\cons}`, namely {math}`\bar{\cons}-\mu^{*}`, so {math}`\mu^{*}>0`. Prudence, not risk aversion, is what generates precautionary saving.

:::{figure} /content/figures/RiskAndPSPremia/RiskAndPSPremiaPrec.png
:name: fig:RiskAndPSPremiaPrec
:align: center

The Kimball precautionary premium {math}`\mu^{*}`. Expected marginal utility is the midpoint of the chord, which lies above {math}`\uP` because {math}`\uP` is convex.
:::

## Absolute Risk Aversion and Absolute Prudence

The parallel between the two definitions carries over to the parallel between the two measures of curvature that govern them. Writing {math}`\sigma^{2}=\Ex[\epsilon^{2}]=\alpha^{2}` for the variance of the risk, a second-order expansion of each side of {eq}`eq:RiskPrem` around {math}`\bar{\cons}` gives

```{math}
:label: eq:RiskPremApprox

\pi^{*} \approx \left(\frac{\sigma^{2}}{2}\right)\left(\frac{-\uPP(\bar{\cons})}{\uP(\bar{\cons})}\right),
```

in which the second factor is the coefficient of absolute risk aversion. The identical calculation applied to {eq}`eq:PrecPrem`, with {math}`\uP` in place of {math}`\uFunc`, gives

```{math}
:label: eq:PrecPremApprox

\mu^{*} \approx \left(\frac{\sigma^{2}}{2}\right)\left(\frac{-\uPPP(\bar{\cons})}{\uPP(\bar{\cons})}\right),
```

in which the second factor is what Kimball calls the coefficient of absolute prudence. Absolute prudence therefore stands to the precautionary premium exactly as absolute risk aversion stands to the risk premium.[^kimball-relative]

[^kimball-relative]: Multiplying each coefficient by {math}`\bar{\cons}` yields the relative measures, relative risk aversion {math}`-\bar{\cons}\uPP/\uP` and relative prudence {math}`-\bar{\cons}\uPPP/\uPP`.

For the CRRA utility function used throughout these notes, absolute risk aversion is {math}`\CRRA/\bar{\cons}` while absolute prudence is {math}`(\CRRA+1)/\bar{\cons}`. Two things follow. First, prudence is implied by risk aversion in this family, so any CRRA consumer who dislikes risk also saves against it. Second, prudence strictly exceeds risk aversion, so {math}`\mu^{*}>\pi^{*}`: the risk moves behavior by more than it moves welfare. That the two coefficients differ by exactly one unit of relative curvature is a special feature of CRRA, not a general result.

Logarithmic utility makes the gap concrete. Setting {math}`\CRRA=1` gives relative risk aversion of one but relative prudence of two, so the log consumer's precautionary saving is governed by a curvature twice as large as the curvature that governs their distaste for the risk. Quoting a coefficient of relative risk aversion therefore does not by itself pin down how much precautionary saving a risk will induce.

## A Numerical Illustration

Take relative risk aversion {math}`\CRRA=6`, baseline consumption {math}`\bar{\cons}=3`, and a risk of {math}`\alpha=0.75`, so consumption is either {math}`2.25` or {math}`3.75` with equal probability. Solving {eq}`eq:RiskPrem` and {eq}`eq:PrecPrem` exactly gives {math}`\pi^{*}\approx 0.454` and {math}`\mu^{*}\approx 0.494`, confirming {math}`\mu^{*}>\pi^{*}`.

The approximations are less impressive. Equations {eq}`eq:RiskPremApprox` and {eq}`eq:PrecPremApprox` return {math}`0.563` and {math}`0.656`, overstating both premia by more than twenty percent. The discrepancy is what a local approximation should be expected to produce when the risk is a shock of {math}`\pm 25` percent of consumption. The approximations are reliable guides to how the premia depend on preferences and on the scale of the risk, and unreliable guides to their level when the risk is large.

Prudence is the engine of the buffer stock saving behavior taken up in the sections that follow, and {cite:t}`CarrollKimballPSPW` survey how precautionary motives translate into accumulated wealth.
