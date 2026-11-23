---
math:
  # The chapter's own four, as in content/consumption/TractableBufferStock/index.md: two symbols that wait on
  # Chris (Pi's face, the check) and the two loci's labels, which have no registry row.
  '\GPRteAdj': '\check{\APRte}_{\WGroRtehFix}'
  '\dcEqZero': '\Delta\cNrmE=0'
  '\dmEqZero': '\Delta\mNrmE=0'
  '\straight': '\Pi'
---
(sec:TractableBufferStock-Appendix)=
# Appendix: A Tractable Model of Buffer Stock Saving

This is the appendix to the chapter [A Tractable Model of Buffer Stock Saving](#sec:TractableBufferStock), which [states its results](#sec:TractableBufferStock-AppendixResults) without proof. The chapter's [notebook](../../consumption/TractableBufferStock/TractableBufferStock.ipynb) solves the model numerically, by reverse shooting, and draws its figures; the equations it uses are derived here.

(sec:TBS-CGroApprox)=
## Approximate Formula for Consumption Growth

Using the second-order and then the first-order Taylor approximations from [Math Facts](#fact:mathfactslist), [TaylorTwo](#fact:taylortwo) {math}`(1+\epsilon)^{\zeta} \approx 1 + \zeta \epsilon + (1/2)\zeta(\zeta-1) \epsilon^{2}` and [TaylorOne](#fact:taylorone) {math}`(1+\epsilon)^{\zeta} \approx 1 + \zeta \epsilon`, and the chapter's prudence term {math}`\prudEx = (\CRRA-1)/2`, the expression in braces in the chapter's [normalized Euler equation](#eq:TBS-BeforePFStep) can be rewritten

```{math}
\begin{aligned}
        \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA} & =  \left\{1+\urate\left[\left(\frac{\cNrmU_{t+1}+{\cNrm}^{\EmpLbl}_{t+1}-\cNrmU_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\      & =  \left\{1+\urate\left[\left(1+\cGap _{t+1}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\      & \approx       \left\{1+\urate\left[1+\CRRA \cGap _{t+1}+ \CRRA (\cGap _{t+1})^{2}\prudEx-1\right]\right\}^{1/\CRRA}
\\ & =          \left\{1+ \CRRA \urate (\cGap _{t+1}+ (\cGap _{t+1})^{2}\prudEx)\right\}^{1/\CRRA}
\\ & \approx  1+ \urate  \left(1+\cGap _{t+1}\prudEx\right)\cGap _{t+1},
\end{aligned}
```

which leads directly to the chapter's [approximation to consumption growth](#eq:TBS-cedelapprox).

(sec:TBS-mTargExists)=
## A Target Exists If and Only If the {math}`\GIChFix` Holds

Given the RIC, the employed consumer has a target {math}`\mTrgNrm^{\EmpLbl}` if and only if the {math}`\GIChFix` holds. This is proved from [the two loci](#sec:TractableBufferStock-LociCross), and again through the two cases of the {math}`\FHWChFix`, [where it fails](#sec:TractableBufferStock-TargetWhenFHWChFixFails) and [where it holds](#sec:TractableBufferStock-TargetWhenFHWChFixHolds), which also give the bound on {math}`\DiscFac`. [The subsection on the {math}`\dcEqZero` locus](#sec:TractableBufferStock-cLocusExists) shows that the locus exists under a weaker condition, the GIC-TBS, and that the consumption function exists, given the RIC, for {math}`\CRRA > 1`, and for {math}`\CRRA < 1` when {math}`\DiscFac \WGroFachFix^{1-\CRRA} \erate < 1`, even when the GIC-TBS fails.

(sec:TractableBufferStock-LociCross)=
### The Loci Cross If and Only If the {math}`\GIChFix` Holds

At a steady-state value of {math}`\mNrmE`, both {math}`\dcEqZero` and {math}`\dmEqZero` hold (the chapter's [{math}`\dcEqZero` locus](#eq:TBS-cDelEqZero) and [{math}`\dmEqZero` locus](#eq:TBS-mDelEqZero)); for convenience defining {math}`\cLocusSlope \equiv \RNrmByG \MPC \straight`,

```{math}
{\cNrm}^{\EmpLbl} = \overbrace{\left(\frac{\cLocusSlope}{1+\cLocusSlope}\right) \mNrmE}^{\dcEqZero} = \overbrace{\left(\frac{\RNrmByG-1}{\RNrmByG}\right)\mNrmE + \RNrmByG^{-1}}^{\dmEqZero} .
```

Since {math}`\RNrmByG^{-1}` is positive, at {math}`\mNrmE=0` the {math}`\dmEqZero` locus's value is {math}`\RNrmByG^{-1}` while the {math}`\dcEqZero` locus's is zero, so the two loci intersect at a positive {math}`\mNrmE` if and only if the {math}`\dcEqZero` locus is the steeper:

:::{margin}
The equivalence uses {math}`1+\cLocusSlope > 0`, which holds because {math}`\cLocusSlope > 0` when the RIC holds and {math}`\straight > 0`.
:::

```{math}
:label: eq:TBS-cDelEq0SlopeCond

\left(\frac{\cLocusSlope}{1+\cLocusSlope}\right) > \left(\frac{\RNrmByG-1}{\RNrmByG}\right)
```

which is equivalent to

```{math}
:label: eq:TBS-cDelEq0SlopeCondAlt

\overbrace{\RNrmByG \MPC \straight}^{= \cLocusSlope} > \RNrmByG-1
```

where the left-hand side is (proportional to) the slope of {math}`\dcEqZero` and the right-hand side is (proportional to) the slope of {math}`\dmEqZero`.

Since {math}`\MPC = 1-\RPFac` and {math}`\RNrmByG\RPFac = \GPFachFix`, {math}`\RNrmByG\MPC = \RNrmByG-\GPFachFix`, so

```{math}
\cLocusSlope-(\RNrmByG-1) = \RNrmByG\MPC(\straight-1)+(1-\GPFachFix) .
```

At {math}`\GPFachFix=1` both terms are zero: the two loci are parallel, and no target exists. More generally, {math}`\straight-1` has the sign of {math}`1-\GPFachFix` (from the chapter's [definition of {math}`\straight`](#eq:TBS-straightDef)), and the RIC makes {math}`\RNrmByG\MPC` positive, so both terms have the sign of {math}`1-\GPFachFix`; if the chapter's [GIC-TBS](#eq:TBS-GICExistsSoln) fails, there is no {math}`\dcEqZero` locus, and the {math}`\GIChFix` fails too. Given the RIC, then, {eq}`eq:TBS-cDelEq0SlopeCondAlt` holds, and a target exists, if and only if {math}`\GPFachFix < 1`, the {math}`\GIChFix`.

For any fixed {math}`\urate` and {math}`\WGroFac` and {math}`\Rfree` we can find some {math}`\WGroShortfall` for which {math}`\WGroFac = \Rfree (1-\WGroShortfall \urate)`, and using this {math}`\WGroShortfall` it turns out to be useful to rewrite

```{math}
:label: eq:TBS-RnormFromAlpha

\begin{aligned}
  \RNrmByG^{-1} & =  \WGroFachFix/\Rfree
\\ & =  \frac{\WGroFac}{\Rfree(1-\urate)}
\\ & =  \frac{\Rfree(1-\WGroShortfall \urate)}{\Rfree(1-\urate)}
\\ & =  (1-\WGroShortfall \urate + \urate - \urate)/(1-\urate)
\\ & =  (1-\urate+(1-\WGroShortfall) \urate)/(1-\urate)
\\ & =  1+(1-\WGroShortfall)\urate/(1-\urate)
.
\end{aligned}
```

Note for future use that {eq}`eq:TBS-RnormFromAlpha` implies that whenever {math}`\WGroShortfall \leq 1`, the {math}`\FHWChFix` fails because {math}`\RNrmByG^{-1} \geq 1 \Rightarrow \Rfree/\WGroFachFix = \RNrmByG \leq 1 \Rightarrow \Rfree \leq \WGroFachFix`. (Human wealth {math}`\hNrm` itself is infinite if and only if {math}`\WGroShortfall \leq 0`, that is, if {math}`\WGroFac \geq \Rfree`.)

Multiplying both sides of {eq}`eq:TBS-cDelEq0SlopeCondAlt` by {math}`\RNrmByG^{-1}` then substituting the expression for {math}`\RNrmByG^{-1}` from {eq}`eq:TBS-RnormFromAlpha` gives

```{math}
:label: eq:TBS-alphaReq

\begin{aligned}
  1- \RNrmByG^{-1} & <  \MPC \straight
\\ - (1-\WGroShortfall)\urate/(1-\urate) & <  \MPC \straight
\end{aligned}
```

(sec:TractableBufferStock-TargetWhenFHWChFixFails)=
### A Target Always Exists When the {math}`\FHWChFix` Fails

Since {math}`0 < \urate < 1` and {math}`\MPC>0` (as guaranteed by the RIC), {eq}`eq:TBS-alphaReq` is satisfied whenever the {math}`\FHWChFix` fails ({math}`\WGroShortfall \leq 1`) and {math}`\straight > 0`. We now show that under these conditions, {math}`\straight>0`.

{math}`\straight`, from the chapter's [definition of {math}`\straight`](#eq:TBS-straightDef), is:

```{math}
\straight = \left(1+\urate^{-1}(\GPFachFix^{-\CRRA}-1)\right)^{1/\CRRA}
```

but note that

```{math}
\GPFachFix = \RPFac \overbrace{(\Rfree/\WGroFachFix)}^{=\RNrmByG}
```

so when the {math}`\FHWChFix` fails, {math}`\RNrmByG \leq 1` and {math}`\GPFachFix \leq \RPFac < 1` by the RIC: the {math}`\GIChFix` holds, {math}`\GPFachFix^{-\CRRA} > 1`, and hence {math}`\straight > 1 > 0`. At {math}`\WGroShortfall=1`, {math}`\RNrmByG = 1` and {math}`\GPFachFix = \RPFac`; at {math}`\WGroShortfall=0`, so that {math}`\WGroFac=\Rfree`, {math}`\RNrmByG=\Rfree(1-\urate)/\WGroFac=1-\urate<1`, so {math}`\GPFachFix < \RPFac` and {math}`\straight` is further above 1.

Thus, when the {math}`\FHWChFix` fails (that is, if {math}`\WGroShortfall \leq 1`), a target {math}`\TargetNrm{\mNrm}^{\EmpLbl}` exists: given the RIC, the failure of the {math}`\FHWChFix` implies the {math}`\GIChFix`.

(sec:TractableBufferStock-TargetWhenFHWChFixHolds)=
### When the {math}`\FHWChFix` Holds, a Target Exists If and Only If {math}`\DiscFac < \WGroFachFix^{\CRRA}/\Rfree`

In the case where the {math}`\FHWChFix` holds ({math}`\WGroShortfall > 1`), we need the right-hand side of {eq}`eq:TBS-alphaReq` not merely to be positive, but to exceed a specific positive number, {math}`(\WGroShortfall-1)\urate/(1-\urate)`:

```{math}
:label: eq:TBS-GPFacRawReqForTarget

\begin{aligned}
    \MPC \straight & >  (\WGroShortfall-1)\urate/(1-\urate)
\\   \straight & >  \left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)
\\   \straight^{\CRRA} & >  \left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}
\\  (\GPFachFix^{-\CRRA}-1)\urate^{-1} = \straight^{\CRRA}-1 & >  \left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1
\\  (\GPFachFix^{-\CRRA}-1) & >  \urate \left[\left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right]
\\  \GPFachFix^{-\CRRA} & >  1  + \urate \left[\left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right]
\\  \GPFachFix & <  \left\{1  + \urate \left[\left(\frac{(\WGroShortfall-1)\urate}{\MPC (1-\urate)}\right)^{\CRRA}-1\right] \right\}^{-1/\CRRA}
\end{aligned}
```

and the boundary will be the point at which this expression holds with equality.

An increase in impatience caused by an increase in the pure time preference rate {math}`\discRte` (equivalently, a reduction in {math}`\DiscFac`) has the effect of reducing growth-patience (the left-hand side of {eq}`eq:TBS-GPFacRawReqForTarget`) and of increasing the right-hand side. Since the condition holds when {math}`\DiscFac` is small enough, there is a threshold {math}`\DiscFacMaxGICWhenFHWCTBSHolds` at which its two sides are equal, and {eq}`eq:TBS-GPFacRawReqForTarget` is satisfied by every {math}`\DiscFac` below it:

```{math}
:label: eq:TBS-DiscountMaxGICWhenFHWCTBSHolds

\DiscFac < \DiscFacMaxGICWhenFHWCTBSHolds .
```

Since we have assumed the RIC (so that {math}`\MPC > 0`), as {math}`\urate \downarrow 0`, {eq}`eq:TBS-GPFacRawReqForTarget` asymptotes to the {math}`\GIChFix` for any given value of {math}`\DiscFac`. (As {math}`\WGroShortfall \downarrow 1`, {math}`\RNrmByG \rightarrow 1` and {math}`\GPFachFix \rightarrow \RPFac < 1`, so under the RIC the requirement holds automatically, as it does when {math}`\WGroShortfall \leq 1`; the [bound on {math}`\DiscFac`](#eq:TBS-DiscountMaxGICWhenFHWCTBSHoldsAndGICPGroIsExactlySatisfied) approaches the RIC's, {math}`\Rfree^{\CRRA-1}`.)

The apparently harder case is when {math}`\WGroShortfall>1` and {math}`\urate > 0`. But note that we will have found {math}`\DiscFacMaxGICWhenFHWCTBSHolds` if we can find the corresponding {math}`\MPC` at which the first term in the square brackets of [the requirement for a target](#eq:TBS-GPFacRawReqForTarget) reaches 1:

```{math}
:label: eq:TBS-DiscountMaxGICWhenFHWCTBSHoldsAndGICPGroIsExactlySatisfied

\begin{aligned}
    \left(\frac{(\WGroShortfall-1)\urate}{(1-\RPFac) (1-\urate)}\right)^{\CRRA} & =  1
\\  \left(\frac{(\WGroShortfall-1)\urate}{(1-\RPFac) (1-\urate)}\right) & =  1
\\  \left(\frac{(\WGroShortfall-1)\urate}{ (1-\urate)}\right) & =  1-\RPFac
\\  1-\left(\frac{(\WGroShortfall-1)\urate}{ (1-\urate)}\right) & =  \RPFac
\\                  \left[1-\left(\frac{(\WGroShortfall-1)\urate}{ (1-\urate)}\right)\right] & =  (\Rfree \DiscFac)^{1/\CRRA}/\Rfree
\\  \Rfree^{\CRRA}  \left[1-\left(\frac{(\WGroShortfall-1)\urate}{ (1-\urate)}\right)\right]^{\CRRA} & =  (\Rfree \DiscFac)
\\  \Rfree^{\CRRA-1}\left[1-\left(\frac{(\WGroShortfall-1)\urate}{ (1-\urate)}\right)\right]^{\CRRA} & =  \DiscFacMaxGICWhenFHWCTBSHolds
.\end{aligned}
```

At this value of {math}`\DiscFac` the bracketed term is 0, so the right-hand side of {eq}`eq:TBS-GPFacRawReqForTarget` is 1. By {eq}`eq:TBS-RnormFromAlpha`, the expression {math}`1-(\WGroShortfall-1)\urate/(1-\urate)` in {eq}`eq:TBS-DiscountMaxGICWhenFHWCTBSHoldsAndGICPGroIsExactlySatisfied` equals {math}`\RNrmByG^{-1}`, so {math}`\DiscFacMaxGICWhenFHWCTBSHolds = \Rfree^{\CRRA-1}\RNrmByG^{-\CRRA} = \WGroFachFix^{\CRRA}/\Rfree`, at which {math}`\GPFachFix = 1`: the requirement's two sides are equal, and {math}`\DiscFacMaxGICWhenFHWCTBSHolds=\DiscFacMaxGIChFix`. So the {math}`\GIChFix` is the definitive boundary, as the loci showed directly: a finite target {math}`\mNrmE` exists so long as {math}`\DiscFac < \DiscFacMaxGIChFix = \WGroFachFix^{\CRRA}/\Rfree`.

(sec:TractableBufferStock-cLocusExists)=
### The {math}`\dcEqZero` Locus Exists Under the Weaker GIC-TBS

We have shown that, given the RIC, the {math}`\GIChFix` is necessary and sufficient for a target {math}`\mTrgNrm^{\EmpLbl}` to exist. A weaker condition, the chapter's [GIC-TBS](#eq:TBS-GICExistsSoln), is necessary and sufficient for the {math}`\dcEqZero` locus to exist ({math}`\straight > 0`) and slope upward.

This can be understood as follows. Rewrite the requirement for existence of a target, {eq}`eq:TBS-cDelEq0SlopeCondAlt`, as

```{math}
:label: eq:TBS-cDelEq0SlopeCondAltAlt

\RNrmByG \MPC \straight+1 > \RNrmByG ,
```

or taking logs we have approximately

```{math}
:label: eq:TBS-cDelEq0SlopeCondLog

\MPC \straight > \rfree-\WGroRtehFix .
```

The left-hand side captures the slope of the {math}`\dcEqZero` locus, which is {math}`\MPC` modified by {math}`\straight`, whose difference from 1 captures the degree of growth (im)patience. The right-hand side captures the slope of the {math}`\dmEqZero` locus. Recall that the inequality captures the fact that a target {math}`\mTrgNrm^{\EmpLbl}` exists if these two loci intersect, which happens if and only if the slope of {math}`\dcEqZero` exceeds that of {math}`\dmEqZero`.

:::{margin}
"Captures" does not mean "is equal to." The chapter's [{math}`\dcEqZero` locus](#eq:TBS-cDelEqZero) gives the actual formula for the slope.
:::

If the consumer is "growth patience poised" (that is, {math}`\GPFachFix = 1`), then {math}`\straight = 1` and the left-hand side of {eq}`eq:TBS-cDelEq0SlopeCondLog` is the {math}`\MPC` that characterizes the perfect foresight consumption function. As the [subsection on when the loci cross](#sec:TractableBufferStock-LociCross) showed from the exact condition, the two loci are then parallel, and no target exists.

As noted above, if the consumer is growth-impatient ({math}`\GPFachFix < 1`) then {math}`\straight > 1` and the slope of {math}`\dcEqZero` is monotonically increased as the degree of growth-impatience increases (so that target {math}`\TargetNrm{\mNrm}^{\EmpLbl}` is diminished).

But if the consumer is growth-patient ({math}`\GPFachFix > 1`) then {math}`\straight < 1` and the slope of {math}`\dcEqZero` is diminished (which reflects the fact that the greater the degree of patience, the lower will consumption be for any given {math}`\mNrmE`). The lower bound is defined by the point at which the degree of growth patience becomes so strong that the slope of {math}`\dcEqZero` reaches zero (when {math}`\straight=0`). This restricts the degree of growth patience for which the {math}`\dcEqZero` locus exists, because {math}`\straight > 0` requires (rewriting the chapter's [GIC-TBS](#eq:TBS-GICExistsSoln)):

:::{margin}
Note that if the {math}`\GIChFix` fails so that {math}`\straight < 1`, the slope of the {math}`\dcEqZero` locus is shallower than the slope of the perfect foresight consumption function. The fact that the {math}`\dcEqZero` and {math}`\dmEqZero` loci then never intersect reflects the fact that the consumer will accumulate {math}`\mNrmE` forever.
:::

```{math}
\left(\frac{(\Rfree \DiscFac (1-\urate))^{1/\CRRA}}{\WGroFac/(1-\urate)}\right) = \left(\frac{(\Rfree \DiscFac (1-\urate))^{1/\CRRA}}{\WGroFachFix}\right) < 1 .
```

Expanding on the chapter's [discussion of why unemployment risk increases growth impatience](#sec:TBS-URiskGrowthImpatience), the numerator in the leftmost expression reflects the sense in which the unemployment risk acts in a manner similar to the effect of an extra degree of discounting (reflecting the fact that the relevant condition applies only so long as the consumer remains in employment, a condition whose probability is {math}`(1-\urate)`), while the denominator reflects the mechanical effect in which the relevant measure of growth is boosted by the adjustment that preserves human wealth. Writing the perfect foresight version of the growth patience factor as {math}`\APFac_{\WGroFac}` (which is just the limit as {math}`\urate \downarrow 0`), we can see that the expression on the left-hand side is just {math}`\APFac_{\WGroFac}(1-\urate)^{1+1/\CRRA}` which is smaller than {math}`\APFac_{\WGroFac}` because {math}`\urate>0` and {math}`1+\CRRA^{-1} > 0`. So, the GIC-TBS holds whenever the plain-vanilla {math}`\GICWGro` holds, but not vice-versa; there are parametric configurations in which a perfect-foresight consumer with income growth rate {math}`\WGroFac` would not satisfy the relevant {math}`\GICWGro` (so, their wealth-to-income ratio would go to infinity), but the same consumer facing the same human wealth but with an unemployment risk {math}`\urate` would have an upward-sloping {math}`\dcEqZero` locus, and a finite target wealth-to-income ratio so long as the {math}`\GIChFix` holds, as it can even when the {math}`\GICWGro` fails, because {math}`\WGroFachFix = \WGroFac/(1-\urate) > \WGroFac`.

Unlike the {math}`\dcEqZero` locus, the employed consumer's consumption function exists, given the RIC, for {math}`\CRRA > 1`, and for {math}`\CRRA < 1` when {math}`\DiscFac \WGroFachFix^{1-\CRRA} \erate < 1`, whether or not the GIC-TBS holds. Solve the problem for a finite horizon, at the end of which the consumer spends everything, and let the horizon lengthen. Because utility is negative when {math}`\CRRA > 1`, each period added to the horizon lowers value. But at every horizon the employed consumer's value is at least that of an unemployed consumer with the same resources, since the employed consumer could always spend what the unemployed one would. And as the horizon lengthens, the unemployed consumer's value falls toward {math}`\uFunc(\MPC\mNrm)/\MPC`, its [value with no end to the horizon](#sec:TractableBufferStock-ValueFunction), which the RIC keeps finite. So the employed consumer's value functions, falling and bounded below, converge; since they are concave, so do their slopes (the limit is differentiable, since it solves the Bellman equation with spending strictly between zero and resources), and with them, through the envelope condition, the consumption functions. The limiting consumption function is neither zero nor infinite: it is at least {math}`\MPC\mNrm`, what an unemployed consumer with the same resources spends, because the employed consumer's future income is never less than an unemployed consumer's, and at most {math}`\mNrm`, because the consumer never borrows. None of this uses the GIC-TBS. {cite:t}`BufferStockTheory` proves the analogous result for {math}`\CRRA > 1`, by a contraction mapping, in a model whose zero-income events are transitory; there the RIC can be weakened to a weak return impatience condition together with a finite value of autarky, because a consumer with no income today can expect income tomorrow.

When {math}`\CRRA < 1`, utility is positive, and the value functions rise as the horizon lengthens instead. The argument then needs them bounded above, which requires {math}`\DiscFac \WGroFachFix^{1-\CRRA} \erate < 1`, the condition that [the derivation of the value function](#sec:TractableBufferStock-ValueFunction) assumes when {math}`\CRRA < 1`: otherwise an employed consumer who spent each period's income as it arrived would already have infinite value. The RIC alone does not ensure it: with {math}`\CRRA = 0.5`, {math}`\DiscFac = 0.96`, {math}`\Rfree = 1.04`, {math}`\WGroFac = 1.1` and {math}`\urate = 0.01`, the RIC holds, and the loci cross, but {math}`\DiscFac \WGroFachFix^{1-\CRRA} \erate \approx 1.0018`, so the employed consumer's value is infinite. But the condition is also enough: spending never exceeds resources, which after {math}`t` periods of employment are at most {math}`(\mNrm+t)\max\{\Rfree,\WGroFachFix\}^{t}` times current income and, once the consumer is unemployed, grow at most by the factor {math}`\Rfree` a period, so value is bounded by a series that converges because {math}`\DiscFac \erate \max\{\Rfree,\WGroFachFix\}^{1-\CRRA} < 1`, by the condition and the RIC, and {math}`\DiscFac \Rfree^{1-\CRRA} < 1`, which is equivalent to the RIC.

(sec:TBS-mTargExact)=
## The Exact Formula for Target {math}`\mNrm`

To simplify the expressions in the derivations below, we use {math}`\cLocusSlope \equiv \RNrmByG \MPC \straight` so that {math}`\Rfree \MPC \straight = \cLocusSlope \WGroFachFix` and we drop the {math}`\EmpLbl` superscripts, allowing the chapter's [{math}`\dcEqZero` locus](#eq:TBS-cDelEqZero) to be rewritten as

```{math}
\cNrm = \left(\frac{\cLocusSlope }{1+\cLocusSlope}\right)\mNrm .
```

If a target value {math}`\mTrgNrm` exists it will be at the point of intersection between the {math}`\dcEqZero` and the {math}`\dmEqZero` loci:

```{math}
:label: eq:TBS-mTarget

\begin{aligned}
  \left(\frac{\cLocusSlope}{1+\cLocusSlope}\right)\mTrgNrm & =  (1-\RNrmByG^{-1})\mTrgNrm+\RNrmByG^{-1}
\\  \left(\RNrmByG\frac{\cLocusSlope}{1+\cLocusSlope}\right)\mTrgNrm & =  (\RNrmByG-1)\mTrgNrm+1
\\  \left(\RNrmByG\left\{\frac{\cLocusSlope}{1+\cLocusSlope}-1\right\}+1\right)\mTrgNrm & =  1
\\  \left(\RNrmByG\left\{\frac{\cLocusSlope-(1+\cLocusSlope)}{1+\cLocusSlope}\right\}+\frac{1+\cLocusSlope}{1+\cLocusSlope}\right)\mTrgNrm & =  1
\\  \left(\frac{1+\cLocusSlope-\RNrmByG}{1+\cLocusSlope}\right)\mTrgNrm & =  1
\\  \mTrgNrm & =  \left(\frac{1+\cLocusSlope}{1+\cLocusSlope-\RNrmByG}\right)
\\  \mTrgNrm & =  \left(\frac{1+\cLocusSlope+\RNrmByG-\RNrmByG}{1+\cLocusSlope-\RNrmByG}\right)
\\ & =  1 + \left(\frac{\RNrmByG}{1+\cLocusSlope-\RNrmByG}\right)
\\ & =  1 + \left(\frac{\Rfree}{\WGroFachFix+\cLocusSlope\WGroFachFix-\Rfree}\right)
.
\end{aligned}
```

A first point about this formula is suggested by the fact that

```{math}
\cLocusSlope\WGroFachFix = \Rfree \MPC \left(1+\left(\frac{\GPFachFix^{-\CRRA} - 1}{\urate}\right)\right)^{1/\CRRA}
```

which is likely to increase as {math}`\urate` approaches zero. When the perfect foresight {math}`\GICWGro` holds ({math}`\APFac_{\WGroFac} < 1`), its limit as {math}`\urate \rightarrow 0` is infinity, which implies that {math}`\lim_{\urate \rightarrow 0} \mTrgNrm = 1`. (When {math}`\APFac_{\WGroFac} = 1`, {math}`(\GPFachFix^{-\CRRA}-1)/\urate` approaches {math}`\CRRA` instead, and the target approaches a finite value above 1.) This is precisely what would be expected from this model in which consumers are impatient but self-constrained to have {math}`\mNrmE > 1`: As the risk gets infinitesimally small, the amount by which target {math}`\mNrmE` exceeds its minimum possible value shrinks to zero.

:::{margin}
"Likely" but not certain because of the fact that {math}`\urate` affects {math}`\GPFachFix` as well as appearing in the denominator of {eq}`eq:TBS-mTarget`; however, for plausible calibrations the effect of the denominator predominates.
:::

We now show that the RIC and {math}`\GIChFix` ensure that the denominator of the fraction in {eq}`eq:TBS-mTarget` is positive:

```{math}
\begin{aligned}
\WGroFachFix + \cLocusSlope \WGroFachFix - \Rfree & =  \WGroFachFix + \Rfree \MPC \straight - \Rfree
 \\& =  \WGroFachFix + \Rfree \left(1- \frac{(\Rfree \DiscFac)^{1/\CRRA}}{\Rfree}\right) \left(\frac{(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\WGroFachFix})^{-\CRRA}-1}{\urate}+1\right)^{1/\CRRA}-\Rfree
 \\& >   \WGroFachFix+\Rfree \left(1-\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)
\left(\frac{(\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\WGroFachFix})^{-\CRRA}-1}{1}+1\right)^{1/\CRRA}-\Rfree
 \\& =  \WGroFachFix+\Rfree\left(1-\frac{(\Rfree\DiscFac)^{1/\CRRA}}{\Rfree}\right)\frac{\WGroFachFix}{(\Rfree\DiscFac)^{1/\CRRA}}-\Rfree
 \\& =  \WGroFachFix+\Rfree \frac{\WGroFachFix}{(\Rfree\DiscFac)^{1/\CRRA}}- \WGroFachFix - \Rfree
 \\& =  \Rfree \left(\frac{\WGroFachFix}{(\Rfree\DiscFac)^{1/\CRRA}}-1\right)
 \\& >  0.
\end{aligned}
```

The bound replaces {math}`\urate` by 1 only where it divides {math}`\GPFachFix^{-\CRRA}-1`; since {math}`\WGroFachFix` and {math}`\GPFachFix` also depend on {math}`\urate`, it says nothing about how the denominator changes with {math}`\urate`.

(sec:TBS-mTargApprox)=
## Approximate Formulas for Target {math}`\mNrm`

Now noting that

```{math}
\straight^{\CRRA}-1 = \left(\frac{\GPFachFix^{-\CRRA} - 1}{\urate}\right),
```

under certain conditions we can obtain further insight into {eq}`eq:TBS-mTarget` using a judicious mix of first- and second-order Taylor expansions (along with {math}`\MPC = -\RPRte`):

:::{margin}
See below for caveats.
:::

```{math}
:label: eq:TBS-zetaExp

\begin{aligned}
  \cLocusSlope\WGroFachFix & =  \Rfree \MPC \left(1+(\straight^{\CRRA}-1)\right)^{1/\CRRA}
\\ & \approx  -\Rfree \RPRte \left(1+\CRRA^{-1}(\straight^{\CRRA}-1)+(\CRRA^{-1})(\CRRA^{-1}-1)((\straight^{\CRRA}-1)^{2}/2)\right)
\\ & =  -\Rfree \RPRte \left(1+\CRRA^{-1}(\straight^{\CRRA}-1)\left\{1+\left(\frac{1-\CRRA}{\CRRA}\right)((\straight^{\CRRA}-1)/2)\right\}\right)
.
\end{aligned}
```

But

```{math}
:label: eq:TBS-hatpi

\begin{aligned}
  \straight^{\CRRA}-1 & \approx  \left(\frac{(1+\GPRtehFix)^{-\CRRA}-1}{\urate}\right)
\\ & \approx  \left(\frac{1- \CRRA \GPRtehFix-1}{\urate}\right)
\\ & \approx  -\left(\frac{\CRRA \GPRtehFix}{\urate}\right)
\end{aligned}
```

which is guaranteed to be positive by the {math}`\GIChFix`, but which can take any value in the interval {math}`(0,\infty)`. Note, however, that the approximations above are valid only if {math}`\straight` is close to 1 (except under logarithmic utility, where the expansion in {eq}`eq:TBS-zetaExp` is exact), which requires that the degree of growth impatience be small relative to the size of the unemployment risk. Thus, the formulas derived above (and used below) are reliable only in rather special circumstances, in particular when the consumer is only very slightly growth-impatient. Under these circumstances, this approximation can be substituted into {eq}`eq:TBS-zetaExp` to obtain

:::{margin}
Other approximations are better for consumers who are highly impatient, relative to their unemployment risk; in this case a better approximation to {eq}`eq:TBS-zetaExp` is obtained by rewriting it as {math}`\cLocusSlope\WGroFachFix = \Rfree \MPC (\straight^{\CRRA}-1)^{1/\CRRA} \left(1+(\straight^{\CRRA}-1)^{-1}\right)^{1/\CRRA}` and approximating using {math}`(1+(\straight^{\CRRA}-1)^{-1})^{1/\CRRA} \approx 1 + \CRRA^{-1}(\straight^{\CRRA}-1)^{-1}+\CRRA^{-1}(\CRRA^{-1}-1)(\straight^{\CRRA}-1)^{-2}/2`.
:::

```{math}
:label: eq:TBS-zetaGammaApprox

\begin{aligned}
  \cLocusSlope\WGroFachFix & \approx   -\Rfree \RPRte \left(1-(\GPRtehFix/\urate)(1+(1-\CRRA)(-\GPRtehFix/\urate)/2)\right)
\\ & \approx  \underbrace{-\Rfree \RPRte}_{>0} \left\{1\underbrace{-(\GPRtehFix/\urate)}_{>0}\left(1+\underbrace{(1-\CRRA)}_{<0}\underbrace{(-\GPRtehFix/\urate)}_{>0}/2\right)\right\}
.
\end{aligned}
```

and inspired by {cite:t}`kimball:smallandlarge` defining a term related to the excess of prudence over the logarithmic case,

```{math}
\prudEx = \left(\frac{\CRRA-1}{2}\right),
```

{eq}`eq:TBS-mTarget` can be approximated by

```{math}
:label: eq:TBS-mTargetApprox

\begin{aligned}
 \mTrgNrm & \approx  1 + \left(\frac{1}{\WGroFachFix/\Rfree-\RPRte \left(1-(\GPRtehFix/\urate)(1-(-\GPRtehFix/\urate)\prudEx) \right)-1}\right)
\\ & \approx  1 + \left(\frac{1}{(\WGroRtehFix-\rfree)+(-\RPRte) \left(1+(-\GPRtehFix/\urate)(1-(-\GPRtehFix/\urate)\prudEx)\right)}\right)
\end{aligned}
```

where negative signs have been preserved in front of the {math}`\RPRte` and {math}`\GPRtehFix` terms as a reminder that the {math}`\GIChFix` and the RIC imply these terms are themselves negative (so that {math}`-\RPRte` and {math}`-\GPRtehFix` are positive). *Ceteris paribus*, an increase in relative risk aversion {math}`\CRRA` will increase {math}`\prudEx` and thereby decrease the denominator of {eq}`eq:TBS-mTargetApprox`. This suggests that greater risk aversion will result in a larger target level of wealth.

:::{margin}
"Suggests" because this derivation used some dubious approximations; the suggestion is verified, however, for plausible numerical calibrations.
:::

The formula also provides insight about how the human wealth effect works in equilibrium. All else equal, the human wealth effect is captured by the {math}`(\WGroRtehFix-\rfree)` term in the denominator of {eq}`eq:TBS-mTargetApprox`, and it is obvious that a larger value of {math}`\WGroRtehFix` will result in a smaller target value for {math}`\mNrm`. But it is also clear that the size of the human wealth effect will depend on the magnitude of the patience and prudence contributions to the denominator, and that those terms can easily dominate the human wealth effect. This reduction in the human wealth effect is interesting because practitioners have known at least since {cite:t}`summersCapTax` that the human wealth effect is implausibly large in the perfect foresight model.

For {eq}`eq:TBS-mTargetApprox` to make sense, we need the denominator of the fraction to be a positive number; defining

```{math}
\GPRteAdj = \GPRtehFix(1-(-\GPRtehFix/\urate)\prudEx),
```

this means that we need:

```{math}
:label: eq:TBS-newDenom

\begin{aligned}
    (\WGroRtehFix - \rfree) & >  \RPRte - \RPRte\GPRteAdj/\urate
\\   & \approx  \left(\CRRA^{-1}(\rfree-\discRte)-\rfree\right)-  \RPRte\GPRteAdj/\urate
\\ \WGroRtehFix & >  \CRRA^{-1}(\rfree-\discRte)-  \RPRte\GPRteAdj/\urate
\\ 0 & >  \underbrace{\CRRA^{-1}(\rfree-\discRte) - \WGroRtehFix}_{\GPRtehFix} -  \RPRte(\GPRteAdj/\urate)
\\ 0 & >  \GPRtehFix -  \RPRte(\GPRteAdj/\urate)
.
\end{aligned}
```

But since the RIC guarantees {math}`\RPRte<0` and the {math}`\GIChFix` guarantees {math}`\GPRtehFix<0` (which, so long as {math}`(-\GPRtehFix/\urate)\prudEx < 1`, in turn guarantees {math}`\GPRteAdj < 0`), this condition must hold.

:::{margin}
In more detail: the second-order Taylor approximation in {eq}`eq:TBS-zetaExp` assumes that the second-order term is smaller in absolute value than the first-order one, {math}`|\CRRA^{-1} (\straight^{\CRRA}-1) | > |(\CRRA^{-1})(\CRRA^{-1}-1)((\straight^{\CRRA}-1)^{2}/2)|`. For {math}`\CRRA \geq 1`, substituting {eq}`eq:TBS-hatpi` turns this into {math}`(-\GPRtehFix/\urate)\prudEx < 1`, which with the {math}`\GIChFix` gives {math}`\GPRteAdj < 0`. The exact denominator, in {eq}`eq:TBS-mTarget`, is positive under the RIC and the {math}`\GIChFix` alone.
:::

The same set of derivations imply that we can replace the denominator in {eq}`eq:TBS-mTargetApprox` with the negative of the right-hand side of {eq}`eq:TBS-newDenom`, yielding a more compact expression for the target level of resources,

```{math}
:label: eq:TBS-mTargetCompact

\begin{aligned}
 \mTrgNrm & \approx  1 + \left(\frac{1}{\RPRte(\GPRteAdj/\urate) - \GPRtehFix }\right)
\\ & =  1 + \left(\frac{1/(-\GPRtehFix)}{1+(-\RPRte/\urate)(1-(-\GPRtehFix/\urate)\prudEx)  }\right)
.
\end{aligned}
```

This formula makes plain the fact that an increase in return impatience, by increasing the denominator of the fraction in {eq}`eq:TBS-mTargetCompact`, will reduce the target level of assets. An increase in growth impatience does the same so long as {math}`2(-\GPRtehFix/\urate)\prudEx < 1+\urate/(-\RPRte)`, which always holds under logarithmic utility ({math}`\prudEx=0`).

We are now in position to discuss {eq}`eq:TBS-mTargetApprox`, understanding that the impatience conditions, with {math}`(-\GPRtehFix/\urate)\prudEx < 1`, guarantee that its denominator is a positive number.

Two specializations of the formula are particularly useful. The first is the case where {math}`\CRRA = 1` (logarithmic utility). In this case

```{math}
\begin{aligned}
    \RPRte & =  -\discRte
\\  \GPRtehFix & =  \rfree-\discRte-\WGroRtehFix
\\  \prudEx & =  0
\end{aligned}
```

and the approximation becomes

```{math}
\mTrgNrm \approx 1 + \left(\frac{1}{(\WGroRtehFix-\rfree)+\discRte(1+(\WGroRtehFix+\discRte-\rfree)/\urate)}\right)
```

which neatly captures the effect of an increase in human wealth (via either increased {math}`\WGroRtehFix` or reduced {math}`\rfree`), the effect of increased impatience {math}`\discRte`, or the effect of a reduction in unemployment risk {math}`\urate` in reducing target wealth (holding {math}`\WGroRtehFix` fixed; see the condition after the chapter's [target under logarithmic utility](#eq:TBS-mTargetLogCase)).

The other useful case to consider is where {math}`\rfree = \discRte` but {math}`\CRRA>1`. In this case, we have

```{math}
\begin{aligned}
    \RPRte & =  -\discRte
\\  \GPRtehFix & =  -\WGroRtehFix
\\  \GPRteAdj & =  -\WGroRtehFix (1-(\WGroRtehFix/\urate)\prudEx)
\end{aligned}
```

so that

```{math}
\mTrgNrm \approx 1 + \left(\frac{1}{(\WGroRtehFix-\rfree)+\discRte(1+(\WGroRtehFix/\urate)(1-(\WGroRtehFix/\urate)\prudEx))}\right)
```

where the additional term involving {math}`\prudEx` in this equation captures the fact that an increase in the prudence term {math}`\prudEx` shrinks the denominator and thereby boosts the target level of wealth.

:::{margin}
It would be inappropriate to use the equation to consider the effect of an increase in {math}`\rfree` because the equation was derived under the assumption {math}`\discRte=\rfree` so {math}`\rfree` is not free to vary.
:::

How good are these approximations? The table compares each with the exact target from {eq}`eq:TBS-mTarget`, evaluating the patience rates as the logs of the patience factors, with {math}`\rfree = \Rfree-1` and {math}`\discRte = 1/\DiscFac-1`; parameters not listed are at the benchmark calibration. The approximations are close under logarithmic utility, where the expansion in {eq}`eq:TBS-zetaExp` is exact, rough when {math}`\discRte = \rfree`, and useless at the benchmark itself, where {math}`(-\GPRtehFix/\urate)\prudEx \approx 3.8` violates the condition {math}`(-\GPRtehFix/\urate)\prudEx < 1` on which {eq}`eq:TBS-mTargetCompact` rests.

| Calibration | {math}`\straight` | Exact {math}`\mTrgNrm` | Approximation | Approximate {math}`\mTrgNrm` |
|---|---|---|---|---|
| {math}`\CRRA = 1` | 15.7 | 1.71 | log utility | 1.64 |
| {math}`\CRRA = 1`, {math}`\urate = 0.05` | 3.48 | 3.95 | log utility | 3.75 |
| {math}`\CRRA = 2`, {math}`\discRte = \rfree = 0.03` | 1.74 | 39.0 | {math}`\discRte = \rfree` | 51.0 |
| benchmark ({math}`\CRRA = 2`, {math}`\discRte = 0.10`) | 4.09 | 5.48 | {eq}`eq:TBS-mTargetCompact` | 0.22 |

(sec:TBS-NumericalSolution)=
## The Mathematics of the Numerical Solution

The chapter's notebook solves the model by *reverse shooting*: it starts at the target and runs the model's dynamics backward. This section derives the equations it uses.

(sec:TractableBufferStock-ReverseShooting)=
### The Reverse-Shooting Equations

To solve the model by the method of *reverse shooting*, we need {math}`{\cNrm}^{\EmpLbl}_{t}` as a function of {math}`{\cNrm}^{\EmpLbl}_{t+1}`. Starting with the chapter's [normalized Euler equation](#eq:TBS-BeforePFStep):

:::{margin}
See {cite:t}`judd:book` for a presentation of shooting methods of solution for numerical difference and differential equations.
:::

```{math}
:label: eq:TBS-cReverse

\begin{aligned}
         \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{{\cNrm}^{\EmpLbl}_{t}}\right) & =  \WGroFachFix^{-1} (\Rfree\DiscFac)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\cNrmU_{t+1}}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA}
\\       {\cNrm}^{\EmpLbl}_{t} & =  \left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\WGroFachFix^{-1} (\Rfree\DiscFac)^{1/\CRRA} \left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\MPC (\mNrmE_{t+1}-1)}\right)^{\CRRA}-1\right]\right\}^{1/\CRRA} }  \right)
\\        & =  \WGroFachFix (\Rfree\DiscFac)^{-1/\CRRA} {\cNrm}^{\EmpLbl}_{t+1}\left\{1+\urate\left[\left(\frac{{\cNrm}^{\EmpLbl}_{t+1}}{\MPC (\mNrmE_{t+1}-1)}\right)^{\CRRA}-1\right]\right\}^{-1/\CRRA}        .
\end{aligned}
```

Inverting the chapter's [normalized budget constraint](#eq:TBS-metp1), the reverse shooting equation for {math}`\mNrmE_{t}` is

```{math}
:label: eq:TBS-mReverse

\mNrmE_{t} = \RNrmByG^{-1} (\mNrmE_{t+1}-1)+{\cNrm}^{\EmpLbl}_{t} .
```

(sec:TractableBufferStock-MPC)=
### The MPC at the Target and as {math}`\mNrm` Approaches Zero

Reverse shooting is more accurate when it tracks the marginal propensity to consume as well as consumption. The MPC's recursion comes from differentiating the consumption Euler equation with respect to {math}`\mNrm_{t}`:

```{math}
:label: eq:TBS-dEuler

\begin{aligned}
  \uP(\cFunc^{\EmpLbl}(\mNrm_{t})) & = \overbrace{\RNrmByG \DiscFac \WGroFachFix^{1-\CRRA}}^{\DiscFacAlt} \Ex_{t}[\uP(\cFunc^{\bullet}(\mNrm_{t+1}))]
\\  \uFunc^{\prime\prime}(\cFunc^{\EmpLbl}(\mNrm_{t}))\MPCFunc^{\EmpLbl}(\mNrm_{t}) & = \DiscFacAlt  \RNrmByG (1-\MPCFunc^{\EmpLbl}(\mNrm_{t}))\Ex_{t}[\uFunc^{\prime\prime}(\cFunc^{\bullet}(\mNrm_{t+1}))\MPCFunc^{\bullet}(\mNrm_{t+1})]
\end{aligned}
```

so that defining, e.g., {math}`\MPCE_{t} = \MPCFunc^{\EmpLbl}(\mNrm_{t})` we have

```{math}
:label: eq:TBS-naturalMPC

\begin{aligned}
 \MPCE_{t} & =  (1-\MPCE_{t}) \underbrace{\DiscFacAlt \RNrmByG (1/\uPP({\cNrm}^{\EmpLbl}_{t}))\Ex_{t}\left[\uPP(\cNrm^{\bullet}_{t+1})\MPC^{\bullet}_{t+1}\right]}_{\equiv \natural_{t+1}}
\\ (1+\natural_{t+1})\MPCE_{t} & = \natural_{t+1}
\\ \MPCE_{t} & = \left(\frac{\natural_{t+1}}{1+\natural_{t+1}}\right)
.
\end{aligned}
```

At the target level of {math}`\mNrmE`, write {math}`\cTrgNrm^{\UnempLbl} \equiv \MPC\RNrmByG(\mTrgNrm-\cTrgNrm^{\EmpLbl})` for what a consumer at the target would consume next period after becoming unemployed, so that {math}`\cTrgNrm^{\EmpLbl}/\cTrgNrm^{\UnempLbl} = \straight` by the chapter's [ratio of employed to unemployed consumption](#eq:TBS-cRatEtfmcRatUtp1). Then

```{math}
\overbrace{(1/\uPP(\cTrgNrm^{\EmpLbl}))\Ex_{t}\left[\uPP(\cNrm^{\bullet})\MPC^{\bullet}\right]}^{\natural / \RNrmByG \DiscFacAlt} = \erate \overbrace{(\uPP(\cTrgNrm^{\EmpLbl})/\uPP(\cTrgNrm^{\EmpLbl}))}^{=1}\MPCE+\urate (\uPP(\cTrgNrm^{\UnempLbl})/\uPP(\cTrgNrm^{\EmpLbl}))\MPC
```

so that

```{math}
\natural = \DiscFacAlt \RNrmByG (\erate \MPCE + \urate (\cTrgNrm^{\UnempLbl}/\cTrgNrm^{\EmpLbl})^{-\CRRA-1} \MPC)
```

yielding from {eq}`eq:TBS-naturalMPC` a quadratic equation in {math}`\MPCE`:

```{math}
:label: eq:TBS-quadraticForTargetMPC

\left(1+\DiscFacAlt \RNrmByG (\erate \MPCE + \urate (\cTrgNrm^{\UnempLbl}/\cTrgNrm^{\EmpLbl})^{-\CRRA-1} \MPC) \right)\MPCE = \DiscFacAlt \RNrmByG (\erate \MPCE + \urate (\cTrgNrm^{\UnempLbl}/\cTrgNrm^{\EmpLbl})^{-\CRRA-1} \MPC)
```

which has exactly one solution for {math}`\MPCE` in the interval {math}`(0,1)`, which is the MPC at target wealth; its other solution is negative.

:::{margin}
The chapter's figures come from its notebook, which computes this solution by {eq}`eq:TBS-MPCatTarget` and then constructs the consumption function by reverse shooting. Its results have been checked against those of HARK's `TractableConsumerType`, which solves the model by the same method.
:::

To see this, and to solve the equation, write {math}`\natural = \natural^{\EmpLbl}\MPCE+\natural^{\UnempLbl}`, where {math}`\natural^{\EmpLbl} \equiv \DiscFacAlt\RNrmByG\erate` and {math}`\natural^{\UnempLbl} \equiv \DiscFacAlt\RNrmByG\urate\straight^{\CRRA+1}\MPC` are both positive. Then {eq}`eq:TBS-quadraticForTargetMPC` is

```{math}
\natural^{\EmpLbl}(\MPCE)^{2}+(1+\natural^{\UnempLbl}-\natural^{\EmpLbl})\MPCE-\natural^{\UnempLbl} = 0 ,
```

whose left-hand side is {math}`-\natural^{\UnempLbl} < 0` at {math}`\MPCE = 0` and {math}`1` at {math}`\MPCE = 1`, and whose two solutions have the negative product {math}`-\natural^{\UnempLbl}/\natural^{\EmpLbl}`. The solution in {math}`(0,1)` is

```{math}
:label: eq:TBS-MPCatTarget

\MPCE = \left(\frac{\natural^{\EmpLbl}-1-\natural^{\UnempLbl}+\sqrt{(1+\natural^{\UnempLbl}-\natural^{\EmpLbl})^{2}+4\natural^{\EmpLbl}\natural^{\UnempLbl}}}{2\natural^{\EmpLbl}}\right) .
```

The limiting MPC as consumption approaches zero, {math}`\bar{\MPC}^{\EmpLbl},` will also be useful. As {math}`{\cNrm}^{\EmpLbl}_{t}` approaches zero, the term for the employed state in {math}`\natural_{t+1}` vanishes, because consumption next period if still employed stays above zero ({math}`\mNrmE_{t+1}` exceeds 1); and {math}`{\cNrm}^{\EmpLbl}_{t}/\mNrmE_{t}` approaches {math}`\bar{\MPC}^{\EmpLbl}`, so {math}`\aNrmE_{t}/{\cNrm}^{\EmpLbl}_{t}` approaches {math}`(1-\bar{\MPC}^{\EmpLbl})/\bar{\MPC}^{\EmpLbl}`. Since {math}`\cNrmU_{t+1} = \MPC\RNrmByG\aNrmE_{t}`,

```{math}
\begin{aligned}
& \lim_{{\cNrm}^{\EmpLbl}_{t} \rightarrow 0}  \overbrace{ \DiscFacAlt \RNrmByG \left(\erate ({\cNrm}^{\EmpLbl}_{t+1}/{\cNrm}^{\EmpLbl}_{t})^{-\CRRA-1}\MPCE_{t+1}  + \urate (\cNrmU_{t+1}/{\cNrm}^{\EmpLbl}_{t})^{-\CRRA-1}\MPC\right)}^{\natural_{t+1}}
\\ & \quad =  \lim_{{\cNrm}^{\EmpLbl}_{t} \rightarrow 0} \DiscFacAlt \RNrmByG \urate (\cNrmU_{t+1}/{\cNrm}^{\EmpLbl}_{t})^{-\CRRA-1}\MPC
\\ & \quad =  \lim_{{\cNrm}^{\EmpLbl}_{t} \rightarrow 0} \DiscFacAlt \RNrmByG \urate \left(\MPC \RNrmByG \aNrmE_{t}/{\cNrm}^{\EmpLbl}_{t}\right)^{-\CRRA-1}\MPC
\\ & \quad =  \DiscFacAlt \RNrmByG \urate (\MPC \RNrmByG ((1-\bar{\MPC}^{\EmpLbl})/\bar{\MPC}^{\EmpLbl}))^{-\CRRA-1}\MPC
\end{aligned}
```

so that from {eq}`eq:TBS-naturalMPC` we have

```{math}
:label: eq:TBS-MPCat0

\bar{\MPC}^{\EmpLbl} \equiv \lim_{\mNrm_{t} \rightarrow 0} \MPCFunc^{\EmpLbl}(\mNrm_{t}) = \left(\frac{ \DiscFacAlt \RNrmByG \urate (\MPC \RNrmByG ((1-\bar{\MPC}^{\EmpLbl})/\bar{\MPC}^{\EmpLbl}))^{-\CRRA-1}\MPC }{1+ \DiscFacAlt \RNrmByG \urate (\MPC \RNrmByG ((1-\bar{\MPC}^{\EmpLbl})/\bar{\MPC}^{\EmpLbl}))^{-\CRRA-1}\MPC }\right)
```

which implicitly defines {math}`\bar{\MPC}^{\EmpLbl}`. It can also be solved explicitly: {eq}`eq:TBS-MPCat0` says that {math}`\bar{\MPC}^{\EmpLbl}/(1-\bar{\MPC}^{\EmpLbl}) = \DiscFacAlt \RNrmByG \urate \MPC (\MPC \RNrmByG (1-\bar{\MPC}^{\EmpLbl})/\bar{\MPC}^{\EmpLbl})^{-\CRRA-1}`, whose solution is {math}`\bar{\MPC}^{\EmpLbl}/(1-\bar{\MPC}^{\EmpLbl}) = \MPC \RNrmByG (\DiscFacAlt \urate)^{-1/\CRRA}`. Since {math}`\DiscFacAlt = \Rfree \DiscFac \WGroFachFix^{-\CRRA}` and {math}`(\Rfree\DiscFac)^{1/\CRRA}/\Rfree = \RPFac`, this gives

```{math}
\bar{\MPC}^{\EmpLbl} = \left(\frac{\MPC}{\MPC+\RPFac\urate^{1/\CRRA}}\right) ,
```

which approaches 1 as {math}`\urate \downarrow 0` and, since {math}`\RPFac = 1-\MPC`, approaches {math}`\MPC` as {math}`\urate \uparrow 1`.

(sec:TractableBufferStock-MPCDerivatives)=
### The MPC's Derivatives at the Target

The curvature (second derivative) of the consumption function is obtained by a procedure analogous to the one used to obtain the MPC: differentiate the differentiated Euler equation {eq}`eq:TBS-dEuler` again. Noting that {math}`\MPC^{\UnempLbl\prime}=0` we can obtain:

```{math}
:label: eq:TBS-kappaPExpr

\begin{aligned}
(\MPC^{\EmpLbl}_{t})^{2} \uPPP(\cNrm^{\EmpLbl}_{t}) +\MPC_{t}^{\EmpLbl\prime}\uPP(\cNrm^{\EmpLbl}_{t}) & = \DiscFacAlt \RNrmByG \Big\{(-\MPC_{t}^{\EmpLbl\prime}) \Ex_{t}[\uPP(\cNrm^{\bullet}_{t+1})\MPC^{\bullet}_{t+1}]
\\ & \quad +  \RNrmByG (1-\MPC^{\EmpLbl}_{t})^{2}\left(\Ex_{t}[(\MPC_{t+1}^{\bullet})^{2}\uPPP(\cNrm^{\bullet}_{t+1})]+\erate  \uPP(\cNrm^{\EmpLbl}_{t+1})\MPC_{t+1}^{\EmpLbl\prime}\right)\Big\}
\end{aligned}
```

so that

```{math}
:label: eq:TBS-kappaPReverse

\MPC^{\EmpLbl\prime}_{t} = \left(\frac{\DiscFacAlt \RNrmByG^{2} (1-\MPC^{\EmpLbl}_{t})^{2} \left( \Ex_{t}[(\MPC_{t+1}^{\bullet})^{2}\uPPP(\cNrm^{\bullet}_{t+1})] +\erate \uPP(\cNrm^{\EmpLbl}_{t+1}) \MPC^{\EmpLbl \prime}_{t+1}\right)-(\MPC^{\EmpLbl}_{t})^{2} \uPPP(\cNrm^{\EmpLbl}_{t})}{\uPP(\cNrm^{\EmpLbl}_{t})+\DiscFacAlt \RNrmByG \Ex_{t}[\uPP(\cNrm^{\bullet}_{t+1})\MPC^{\bullet}_{t+1}] }\right)
```

which can be further simplified at the target because {math}`\MPCFunc^{\EmpLbl \prime}_{t}(\mTrgNrm) = \MPCFunc^{\EmpLbl \prime}_{t+1}(\mTrgNrm) = \MPC^{\EmpLbl \prime}` so that

```{math}
:label: eq:TBS-MPCPrimeSS

\MPC^{\EmpLbl\prime} = \left(\frac{\DiscFacAlt \RNrmByG^{2} (1-\MPCE)^{2}\Ex_{t}[(\MPC^{\bullet})^{2} \uPPP(\cNrm^{\bullet})] -(\MPCE)^{2} \uPPP(\cTrgNrm^{\EmpLbl})}{\uPP(\cTrgNrm^{\EmpLbl}) + \DiscFacAlt \RNrmByG \Ex_{t}[\uPP(\cNrm^{\bullet})\MPC^{\bullet}]- \DiscFacAlt \RNrmByG^{2} (1-\MPCE)^{2}\erate \uPP(\cTrgNrm^{\EmpLbl})}\right) .
```

Differentiating {eq}`eq:TBS-kappaPExpr` once more, and using {math}`\MPC^{\EmpLbl\prime\prime}_{t}=\MPC^{\EmpLbl\prime\prime}_{t+1}=\MPC^{\EmpLbl\prime\prime}` at the target, gives an equation linear in {math}`\MPC^{\EmpLbl\prime\prime}`:

```{math}
:label: eq:TBS-MPCPrimePrimeSS

\begin{aligned}
& \MPC^{\EmpLbl\prime\prime}\left(\uPP(\cTrgNrm^{\EmpLbl})+\DiscFacAlt \RNrmByG \Ex_{t}[\uPP(\cNrm^{\bullet})\MPC^{\bullet}]-\DiscFacAlt \RNrmByG^{3} (1-\MPCE)^{3}\erate \uPP(\cTrgNrm^{\EmpLbl})\right)
\\ & \quad = \DiscFacAlt \RNrmByG^{3} (1-\MPCE)^{3}\left(\Ex_{t}[(\MPC^{\bullet})^{3}\uFunc^{\prime\prime\prime\prime}(\cNrm^{\bullet})]+3\erate\MPCE\MPC^{\EmpLbl\prime}\uPPP(\cTrgNrm^{\EmpLbl})\right)
\\ & \qquad -3\DiscFacAlt\RNrmByG^{2}(1-\MPCE)\MPC^{\EmpLbl\prime}\left(\Ex_{t}[(\MPC^{\bullet})^{2}\uPPP(\cNrm^{\bullet})]+\erate\uPP(\cTrgNrm^{\EmpLbl})\MPC^{\EmpLbl\prime}\right)
\\ & \qquad -3\MPCE\MPC^{\EmpLbl\prime}\uPPP(\cTrgNrm^{\EmpLbl})-(\MPCE)^{3}\uFunc^{\prime\prime\prime\prime}(\cTrgNrm^{\EmpLbl}) ,
\end{aligned}
```

where {math}`\Ex_{t}[(\MPC^{\bullet})^{3}\uFunc^{\prime\prime\prime\prime}(\cNrm^{\bullet})] = \erate(\MPCE)^{3}\uFunc^{\prime\prime\prime\prime}(\cTrgNrm^{\EmpLbl})+\urate\MPC^{3}\uFunc^{\prime\prime\prime\prime}(\cTrgNrm^{\UnempLbl})`; in principle, any number of derivatives can be constructed in this manner.

:::{margin}
Once the lower derivatives are known, each further derivative at the target enters the equation from one more differentiation linearly, so, like {eq}`eq:TBS-MPCPrimeSS`, it has an explicit formula and needs no numerical search. The chapter's notebook computes {math}`\MPC^{\EmpLbl\prime}` and {math}`\MPC^{\EmpLbl\prime\prime}` from {eq}`eq:TBS-MPCPrimeSS` and {eq}`eq:TBS-MPCPrimePrimeSS`.
:::

With the steady-state {math}`\MPCE`, {math}`\MPC^{\EmpLbl\prime}` and {math}`\MPC^{\EmpLbl\prime\prime}`, the consumption function a step {math}`\blacktriangle` from the target is, to third order,

```{math}
:label: eq:TBS-revshootmstart

\begin{aligned}
  \mNrmE_{\Alt{t}} & = \mTrgNrm + \blacktriangle
\\ \tilde{\mathbf{c}}(\blacktriangle) & = \cTrgNrm^{\EmpLbl} + \blacktriangle \MPCE+ (\blacktriangle^{2}/2) \MPC^{\EmpLbl\prime}+ (\blacktriangle^{3}/6) \MPC^{\EmpLbl\prime\prime}
\end{aligned}
```

From such a point on each side of the target, the chapter's notebook runs {eq}`eq:TBS-cReverse` and {eq}`eq:TBS-mReverse`, with {eq}`eq:TBS-naturalMPC` for the MPC, backward to trace the consumption function.

(sec:TractableBufferStock-ValueFunction)=
### The Value Function

As a preliminary, note that since {math}`\uFunc(xy)=\uFunc(x)y^{1-\CRRA}` (for {math}`\CRRA \neq 1`), value for an unemployed consumer is

```{math}
\begin{aligned}
  \vLvl_{t}^{\UnempLbl} & =  \uFunc(\cLvl_{t}^{\UnempLbl})+\DiscFac \uFunc(\cLvl_{t+1}^{\UnempLbl}) + \DiscFac^{2} \uFunc(\cLvl_{t+2}^{\UnempLbl})+...
\\ & =  \uFunc(\cLvl_{t}^{\UnempLbl})\left(1+\DiscFac \{(\Rfree \DiscFac)^{1/\CRRA}\}^{1-\CRRA} + \DiscFac^{2}\left\{(\Rfree \DiscFac)^{2/\CRRA}\right\}^{1-\CRRA}+...\right)
\\ & =  \uFunc(\cLvl_{t}^{\UnempLbl})\underbrace{\left(\frac{1}{1-\DiscFac (\Rfree \DiscFac)^{(1/\CRRA)-1}}\right)}_{\equiv \vMultUnemp}
\end{aligned}
```

where the RIC guarantees that the denominator in the fraction is a positive number. Since {math}`\DiscFac(\Rfree\DiscFac)^{(1/\CRRA)-1} = (\Rfree\DiscFac)^{1/\CRRA}/\Rfree = \RPFac`, the multiplier is {math}`\vMultUnemp = 1/(1-\RPFac) = 1/\MPC`: value is current utility times the inverse of the MPC, as in the [perfect foresight model](#sec:PerfForesightCRRA-ValueClosedForm).

From this we can see that value for the normalized problem is similarly:

```{math}
\vFunc^{\UnempLbl}(\mNrm_{t}) = \uFunc(\MPC \mNrm_{t}) \vMultUnemp .
```

Turning to the problem of the employed consumer, we have

```{math}
\vFunc^{\EmpLbl}(\mNrm_{t}) = \uFunc({\cNrm}^{\EmpLbl}_{t})+\DiscFac \WGroFachFix^{1-\CRRA} \Ex_{t}[\vFunc^{\bullet}(\mNrm_{t+1})]
```

and at the target level of market resources this will be unchanging for a consumer who remains employed so that

```{math}
\begin{aligned}
  \vTrgNrm^{\EmpLbl} & =  \uFunc(\cTrgNrm^{\EmpLbl})+\DiscFac \WGroFachFix^{1-\CRRA} \left(\erate \vTrgNrm^{\EmpLbl} + \urate \vFunc^{\UnempLbl}(\TargetNrm{\aNrm}^{\EmpLbl} \RNrmByG)\right)
\\ (1-\DiscFac \WGroFachFix^{1-\CRRA} \erate) \vTrgNrm^{\EmpLbl} & =  \uFunc(\cTrgNrm^{\EmpLbl})+\DiscFac \WGroFachFix^{1-\CRRA} \urate \vFunc^{\UnempLbl}(\TargetNrm{\aNrm}^{\EmpLbl} \RNrmByG)
\\ \vTrgNrm^{\EmpLbl} & =  \left(\frac{\uFunc(\cTrgNrm^{\EmpLbl})+\DiscFac \WGroFachFix^{1-\CRRA} \urate \vFunc^{\UnempLbl}(\TargetNrm{\aNrm}^{\EmpLbl} \RNrmByG)}{(1-\DiscFac \WGroFachFix^{1-\CRRA} \erate) }\right)
.
\end{aligned}
```

The denominator is positive so long as {math}`\DiscFac \WGroFachFix^{1-\CRRA} \erate < 1`; the RIC and the {math}`\GIChFix` imply this when {math}`\CRRA \geq 1`, but it must be assumed when {math}`\CRRA < 1`.

Given these facts, our recursion for generating a sequence of points on the consumption function can be used at the same time to generate corresponding points on the value function from

```{math}
\vNrmE_{t} = \uFunc({\cNrm}^{\EmpLbl}_{t})+\DiscFac \WGroFachFix^{1-\CRRA} \left(\erate \vNrmE_{t+1} + \urate \vFunc^{\UnempLbl}(\aNrmE_{t} \RNrmByG)\right)
```

with the first iteration point generated by numerical integration from

```{math}
\vNrm^{\EmpLbl}_{\Alt{t}} = \vTrgNrm^{\EmpLbl}+\int_{0}^{\blacktriangle} \uP(\tilde{\mathbf{c}}(\bullet)) d\bullet
```

(sec:TBS-PGroGEQRfree)=
## The Consumption Function as Wealth Grows Large

The chapter asserts that, as wealth grows, the employed consumer's consumption function approaches the perfect foresight function {math}`\bar{\cFunc}(\mNrm) = \MPC(\mNrm-1+\hNrm)`:

```{math}
\lim_{\mNrm \uparrow \infty} \bar{\cFunc}(\mNrm) - \cFunc(\mNrm) = 0 .
```

This holds whenever human wealth is finite, that is, under the {math}`\FHWCWGro` ({math}`\WGroFac < \Rfree`); the stronger {math}`\FHWChFix` is not needed. To see why, write {math}`\cFunc(\mNrm) = \MPC(\mNrm+x)`. For large {math}`\mNrm`, the chapter's [normalized Euler equation](#eq:TBS-BeforePFStep) and [normalized budget constraint](#eq:TBS-metp1) give, to first order in {math}`1/\mNrm`,

```{math}
x_{t} = (\WGroFac/\Rfree)(1+x_{t+1}) ,
```

in which the unemployment risk has dropped out, because {math}`(1-\urate)\RNrmByG^{-1} = \WGroFac/\Rfree`. As wealth grows, {math}`x` therefore approaches the fixed point {math}`(\WGroFac/\Rfree)/(1-\WGroFac/\Rfree) = \hNrm-1` when {math}`\WGroFac < \Rfree`, and {math}`\cFunc(\mNrm)` approaches {math}`\bar{\cFunc}(\mNrm)`: the proportion of consumption financed out of (uncertain) labor income approaches zero, and the precautionary effect, which is proportional to the square of that proportion, vanishes. {math}`\WGroFachFix` sets only the speed of convergence. Since {math}`\mNrm_{t+1} \approx \GPFachFix\mNrm_{t}` at large {math}`\mNrm`, {math}`\bar{\cFunc}(\mNrm)-\cFunc(\mNrm)` falls like {math}`\mNrm` raised to the power {math}`-\min\{1, \log(\Rfree/\WGroFac)/\log(\WGroFachFix/\APFac)\}` when the {math}`\GIChFix` holds, and like {math}`1/\mNrm` when it fails, as numerical solutions confirm; when {math}`\WGroFac < \Rfree \leq \WGroFachFix` that power can be close to zero, and the convergence very slow.

When {math}`\WGroFac \geq \Rfree`, human wealth is infinite and {math}`\bar{\cFunc}` is not defined. The consumption function then approaches the unemployed consumer's {math}`\MPC\mNrm` only in ratio: {math}`\cFunc(\mNrm)/(\MPC\mNrm) \rightarrow 1`, but {math}`\cFunc(\mNrm)-\MPC\mNrm` grows without bound, like {math}`\mNrm` raised to the power {math}`\log(\WGroFac/\Rfree)/\log(\WGroFachFix/\APFac)` (like {math}`\log \mNrm` when {math}`\WGroFac = \Rfree`). The solution of the perfect foresight problem with liquidity constraints, which {cite:t}`parkLiqConstrContinuous` treats in continuous time, shares that limit in ratio, but differs from {math}`\cFunc(\mNrm)` by an amount that also grows without bound.
