(sec:UncertaintyRiskAversionAndPrudence)=
# Uncertainty, Risk Aversion, and Prudence

A consumer who faces a risk to future consumption suffers two distinct consequences, and it is easy to conflate them. The first is that the risk makes the consumer worse off; we would like to know how much the consumer would pay to be rid of it. The second is that the risk changes the consumer's behavior, inducing extra saving; we would like to know how much. The two questions have different answers, and each is governed by a different property of the utility function. The first part of this chapter defines the measure that answers each one. The rest follows the second question from a single decision about how much to save to the stock of wealth that such decisions build up, drawing on the theoretical parts of {cite:t}`CarrollKimballPSPW`.

Two terms are worth separating at the outset. *Precautionary saving* is a flow: the cut in current spending that a consumer makes because the future is uncertain, given the resources the consumer has now. The stock of extra wealth that past precautionary saving has piled up is better called *precautionary wealth* than "precautionary savings," a phrase too easily confused with the flow. Throughout, labor income is taken as given, so the only way to save more is to spend less; a consumer could also respond to risk by working more, a margin we leave aside.

## Risk Premia and Precautionary Premia

Suppose the consumer would consume {math}`\bar{\cons}` in the absence of risk, and now faces an additive mean-zero shock {math}`\epsilon` that takes the value {math}`-\alpha` or {math}`+\alpha`, each with probability one half. The parameter {math}`\alpha>0` indexes the size of the risk.

### The Pratt-Arrow Risk Premium

The measure of how much the consumer dislikes the risk was introduced by {cite:t}`pratt:smallandlarge`. The risk premium {math}`\pi^{*}` is the amount by which certain consumption would have to be reduced to make the consumer exactly as badly off as the risk makes them:

```{math}
:label: eq:RiskPrem

\uFunc(\bar{\cons}-\pi^{*}) = \Ex[\uFunc(\bar{\cons}+\epsilon)].
```

In words, {math}`\pi^{*}` measures willingness to pay, in units of certain consumption, to have the risk removed.

{numref}`fig:RiskPremium` constructs {math}`\pi^{*}` geometrically. The two possible outcomes {math}`\bar{\cons}-\alpha` and {math}`\bar{\cons}+\alpha` are marked on the horizontal axis, and the dotted straight line joining the corresponding points on the utility function is the chord between them. Because each outcome occurs with probability one half, expected utility {math}`\Ex[\uFunc(\bar{\cons}+\epsilon)]` is the height of the midpoint of that chord, which sits directly above {math}`\bar{\cons}`. The figure shows this height lying strictly below {math}`\uFunc(\bar{\cons})`, the height of the curve itself at {math}`\bar{\cons}`; this is Jensen's inequality, and it holds for any mean-zero risk whenever {math}`\uFunc` is concave, {math}`\uPP<0`. Tracing that height horizontally back to the utility function locates the certainty-equivalent consumption level {math}`\bar{\cons}-\pi^{*}`, and the horizontal distance from there to {math}`\bar{\cons}` is the risk premium. Concavity of {math}`\uFunc` is therefore exactly what makes {math}`\pi^{*}` positive: risk aversion is what makes the risk unwelcome.

:::{figure} figures/RiskPremium.png
:name: fig:RiskPremium
:align: center

The Pratt-Arrow risk premium {math}`\pi^{*}`, drawn for the numerical illustration below. Expected utility is the midpoint of the chord, which lies below the utility function because {math}`\uFunc` is concave.
:::

### The Kimball Precautionary Premium

Willingness to pay, however, is not what determines saving. Saving is chosen by comparing marginal utilities, so the object that matters for behavior is the effect of the risk on expected *marginal* utility. The corresponding measure comes from {cite:t}`kimball:smallandlarge`, who defines the precautionary premium {math}`\mu^{*}` as the reduction in certain consumption that would raise marginal utility by as much as the risk does:

```{math}
:label: eq:PrecPrem

\uP(\bar{\cons}-\mu^{*}) = \Ex[\uP(\bar{\cons}+\epsilon)].
```

The definition is {eq}`eq:RiskPrem` with {math}`\uP` written everywhere in place of {math}`\uFunc`. Its behavioral content is that a consumer facing the risk acts, at the margin, like a consumer with no risk whose consumption has been cut by {math}`\mu^{*}`; the extra saving that produces the cut is precautionary saving.

{numref}`fig:PrecautionaryPremium` repeats the geometry of the previous figure one derivative up. The chord now joins {math}`\uP(\bar{\cons}-\alpha)` to {math}`\uP(\bar{\cons}+\alpha)`, and its midpoint gives {math}`\Ex[\uP(\bar{\cons}+\epsilon)]`. The direction of the inequality reverses: because {math}`\uP` is a *convex* function, the chord lies *above* the curve, so the risk *raises* expected marginal utility. Convexity of {math}`\uP` means {math}`\uPPP>0`, the property Kimball named prudence. Since {math}`\uP` is downward sloping, reading the elevated marginal utility back to the curve locates a consumption level *below* {math}`\bar{\cons}`, namely {math}`\bar{\cons}-\mu^{*}`, so {math}`\mu^{*}>0`. Prudence, not risk aversion, is what generates precautionary saving.

:::{figure} figures/PrecautionaryPremium.png
:name: fig:PrecautionaryPremium
:align: center

The Kimball precautionary premium {math}`\mu^{*}`, drawn for the numerical illustration below. Expected marginal utility is the midpoint of the chord, which lies above {math}`\uP` because {math}`\uP` is convex.
:::

### Absolute Risk Aversion and Absolute Prudence

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

For the CRRA utility function used throughout these notes, absolute risk aversion is {math}`\CRRA/\bar{\cons}` while absolute prudence is {math}`(\CRRA+1)/\bar{\cons}`. Two things follow. First, prudence is implied by risk aversion in this family, so any CRRA consumer who dislikes risk also saves against it. Second, prudence strictly exceeds risk aversion, so {math}`\mu^{*}>\pi^{*}`: the risk moves behavior by more than it moves welfare. That the two coefficients differ by exactly one unit of relative curvature is a special feature of CRRA; a [later section](#sec:UR-PrudenceExceedsRiskAversion) shows when prudence exceeds risk aversion more generally.

Logarithmic utility makes the gap concrete. Setting {math}`\CRRA=1` gives relative risk aversion of one but relative prudence of two, so the log consumer's precautionary saving is governed by a curvature twice as large as the curvature that governs their distaste for the risk. Quoting a coefficient of relative risk aversion therefore does not by itself pin down how much precautionary saving a risk will induce.

### A Numerical Illustration

Take relative risk aversion {math}`\CRRA=6`, baseline consumption {math}`\bar{\cons}=3`, and a risk of {math}`\alpha=0.75`, so consumption is either {math}`2.25` or {math}`3.75` with equal probability. Solving {eq}`eq:RiskPrem` and {eq}`eq:PrecPrem` exactly gives {math}`\pi^{*}\approx 0.454` and {math}`\mu^{*}\approx 0.494`, confirming {math}`\mu^{*}>\pi^{*}`. These are the premia marked in {numref}`fig:RiskPremium` and {numref}`fig:PrecautionaryPremium`.

The approximations are less impressive. Equations {eq}`eq:RiskPremApprox` and {eq}`eq:PrecPremApprox` return {math}`0.5625` and {math}`0.65625`, overstating both premia by more than twenty percent. The discrepancy is what a local approximation should be expected to produce when the risk is a shock of {math}`\pm 25` percent of consumption. The approximations are reliable guides to how the premia depend on preferences and on the scale of the risk, and unreliable guides to their level when the risk is large. The chapter's [figure notebook](UncertaintyRiskAversionAndPrudence.ipynb) computes these numbers and draws all four figures; its parameters can be changed and the figures redrawn.

## Precautionary Saving in the Consumer's Problem

The premia describe a consumer whose consumption is simply handed over. A real consumer chooses how much to spend and how much to carry into the future, and precautionary saving is the part of that choice that responds to risk. The analysis of this choice began with a two-period model by {cite:t}`LelandPrecaution`, which {cite:t}`SibleyPIH` and {cite:t}`MillerPIH` extended to many periods. Interest in it grew after {cite:t}`zeldesStochastic` solved a benchmark version numerically and {cite:t}`barskymankiwzeldes:aer` traced its implications for the effects of government debt. Preferences here are the same in every period, which leaves aside the questions of time consistency raised by {cite:t}`laibson:goldeneggs` and others.

The problem has two parts: how resources carry over from one period to the next, and how they are divided within a period. Assets {math}`\aRat_{t}` held at the close of period {math}`t` earn interest at the rate {math}`\rfree`, so the resources available in period {math}`t+1`, called *market resources* or "cash on hand," are

```{math}
:label: eq:UR-mtp1

\mRat_{t+1} = \Rfree\aRat_{t} + \yRat_{t+1},
```

where {math}`\Rfree \equiv 1+\rfree` is the interest *factor* and {math}`\yRat_{t+1}` is labor income. Think of {math}`\mRat` as the balance in the consumer's bank account just after the paycheck and the interest have arrived. Spending in period {math}`t` is paid for out of {math}`\mRat_{t}`, so the assets left at the end of the period are {math}`\aRat_{t} = \mRat_{t}-\cRat_{t}`.

A good choice today requires knowing what each possible level of resources tomorrow is worth. The value function {math}`\vFunc_{t+1}(\mRat_{t+1})` records exactly that; for now we take it as given. With time preference factor {math}`\DiscFac` and beliefs about next period's income captured by the expectations operator {math}`\Ex_{t}`, the value of ending period {math}`t` with assets {math}`\aRat` is

```{math}
:label: eq:UR-vEnd

\vEndFunc_{t}(\aRat) = \DiscFac\,\Ex_{t}[\vFunc_{t+1}(\Rfree\aRat+\tilde{\yRat}_{t+1})],
```

where the tilde marks income that is not yet known in period {math}`t`. The value function for period {math}`t` is the value of the best division of {math}`\mRat_{t}` between consumption and assets,

```{math}
\vFunc_{t}(\mRat_{t}) = \max_{\cRat}\left\{\uFunc(\cRat)+\vEndFunc_{t}(\mRat_{t}-\cRat)\right\},
```

and under standard assumptions the best division equates the marginal utility of consumption to the marginal value of assets:

```{math}
:label: eq:UR-FOC

\uP(\mRat_{t}-\aRat_{t}) = \vEndFunc_{t}^{\prime}(\aRat_{t}).
```

If the two sides differed, moving a little of the resources from consumption to assets, or back, would raise value.

{numref}`fig:EquateMargUtils` draws the two sides of {eq}`eq:UR-FOC` against {math}`\aRat` for a given {math}`\mRat_{t}`. Marginal utility {math}`\uP(\mRat_{t}-\aRat)` rises with {math}`\aRat`, because saving more leaves less to consume. The marginal value of assets falls with {math}`\aRat`, and the figure shows it twice: the lower curve for a consumer who is sure to receive next period's mean income, {math}`\Ex_{t}[\tilde{\yRat}_{t+1}]`, and the upper curve for a consumer whose income is risky. Adding the risk moves the optimal choice of assets from {math}`\aRat^{*}` to {math}`\aRat^{**}`. Since {math}`\cRat_{t}=\mRat_{t}-\aRat_{t}`, the consumer spends {math}`\aRat^{**}-\aRat^{*}` less, and that cut in spending is the precautionary saving the risk induces. Repeating the construction for every {math}`\mRat_{t}` traces out the consumption function {math}`\cFunc_{t}(\mRat_{t})`.

:::{figure} figures/EquateMargUtils.png
:name: fig:EquateMargUtils
:align: center

Marginal utility of consumption and marginal value of end-of-period assets. With risky income, {math}`\vEndFunc_{t}^{\prime}(\aRat) = \DiscFac\Rfree\,\Ex_{t}[\vFunc_{t+1}^{\prime}(\Rfree\aRat+\tilde{\yRat}_{t+1})]`; with income certain at its mean, it is {math}`\DiscFac\Rfree\,\vFunc_{t+1}^{\prime}(\Rfree\aRat+\Ex_{t}[\tilde{\yRat}_{t+1}])`. Drawn for a consumer for whom period {math}`t+1` is the last, so that {math}`\vFunc_{t+1}=\uFunc`, with {math}`\CRRA=2`, {math}`\DiscFac=\Rfree=1`, {math}`\mRat_{t}=3`, and next period's income {math}`1-0.75` or {math}`1+0.75`.
:::

Why does the risk raise the marginal value of assets? Differentiating {eq}`eq:UR-vEnd` gives

```{math}
\vEndFunc_{t}^{\prime}(\aRat) = \DiscFac\Rfree\,\Ex_{t}[\vFunc_{t+1}^{\prime}(\Rfree\aRat+\tilde{\yRat}_{t+1})],
```

an expectation of a marginal value, which is exactly the kind of object the precautionary premium was built from. If {math}`\vFunc_{t+1}^{\prime}` is convex, that is, if the value function is prudent, a mean-zero risk raises the expectation, and the whole curve shifts up and to the right. {cite:t}`kimball:smallandlarge` shows that the value function's absolute prudence, {math}`-\vFunc_{t+1}^{\prime\prime\prime}/\vFunc_{t+1}^{\prime\prime}`, and its relative prudence, {math}`-\mRat\vFunc_{t+1}^{\prime\prime\prime}/\vFunc_{t+1}^{\prime\prime}`, measure how far a risk of a given size shifts the curve. When the value function has constant relative risk aversion, its relative prudence is relative risk aversion plus one, as for CRRA utility above.

### Separating Risk Aversion from Intertemporal Substitution

Under time-separable expected utility a single parameter does two jobs: {math}`\CRRA` measures relative risk aversion, and its inverse is the elasticity of intertemporal substitution, {math}`\varsigma = 1/\CRRA`. Preferences of the kind proposed by {cite:t}`KrepsPorteus:Prefs` give each its own parameter. {cite:t}`KimballWeil:Poss` work out how strong the precautionary motive is for such preferences: the counterpart of relative prudence becomes

```{math}
:label: eq:UR-PrudenceKW

\mathcal{P} = (1 + \varsigma\varepsilon)\,\CRRA,
```

where {math}`\varepsilon` measures how fast absolute risk tolerance grows with wealth: it is the elasticity of absolute risk tolerance with respect to wealth, which equals minus the elasticity of absolute risk aversion. Time-separable CRRA utility is the case {math}`\varsigma = 1/\CRRA` and {math}`\varepsilon = 1`, which gives back {math}`\mathcal{P} = \CRRA+1`. More generally, since {math}`\varsigma` and {math}`\CRRA` are positive, any risk tolerance that rises with wealth ({math}`\varepsilon>0`) makes the precautionary motive stronger than risk aversion: {math}`\mathcal{P}>\CRRA`.

(sec:UR-PrudenceExceedsRiskAversion)=
### When Prudence Must Exceed Risk Aversion

The inequality {math}`\mathcal{P}>\CRRA` is one instance of a far more general result, first suggested by {cite:t}`DrezeModigliani`. Suppose that a small forced cut in consumption, which leaves the consumer with more assets, would lead an optimizing investor to take on more risk; Drèze and Modigliani call this property "endogenously decreasing absolute risk aversion." Then, however unusual the objective function, the precautionary saving motive is stronger than risk aversion.

The argument runs through complementarity. If the extra assets that come from consuming less make the consumer willing to accept risks that were previously a matter of indifference, then lower consumption and the bearing of such risks are complements. Complementarity is symmetric, so taking on one of those risks makes lower consumption more attractive: given a free choice, a consumer who is induced to accept such a risk responds by consuming less. Risk aversion determines how much the consumer has to be paid to accept the risk, but that payment does not cancel the extra saving the risk induces.

Additive habit formation provides an example (in contrast to the multiplicative habits of {cite:t}`carroll:solvinghabits`). For a consumer with additive habits, consuming less today both raises assets and lowers the habit against which future consumption will be judged, so it unambiguously raises the consumer's willingness to bear risk. By the principle above, such a consumer is more prudent than risk averse.

## From Precautionary Saving to Precautionary Wealth

The analysis so far weighed the present against the future for a given level of resources {math}`\mRat_{t}`. It cannot address what is perhaps the central question: by how much does precaution raise the resources that consumers hold? A framework that takes {math}`\mRat` as given has nothing to say about that. Answering it requires a horizon long enough that {math}`\vFunc` and {math}`\vEndFunc` capture the value of all future periods, and assumptions under which optimal behavior is the same in every period, so that a single consumption function describes the relation between resources and spending.

The assumption that makes this work is impatience, understood as a condition on preferences that keeps wealth, or the ratio of wealth to income, from growing without bound. The [perfect foresight CRRA](#sec:PerfForesightCRRA) section defines the absolute patience factor {math}`\Pat \equiv (\Rfree\DiscFac)^{1/\CRRA}`, the factor by which a perfect foresight consumer's consumption grows. When labor income grows by the factor {math}`\PGro`, the condition required is a growth impatience condition (GIC), which in its simplest form requires {math}`\Pat` to be less than {math}`\PGro`; {cite:t}`BufferStockTheory` gives the precise conditions. With no income growth, the GIC comes down to {math}`\Pat < 1`, which holds exactly when {math}`\Rfree\DiscFac < 1`.

Given impatience, the exact nature of the income risk matters less. A particularly simple case adapts a model of {cite:t}`toche:urisk`. A consumer is either a worker or a retiree. Retirees receive no labor income and consume out of their wealth. Workers are paid a steady wage, but each period carries the same probability {math}`\urate` that they will be forced to retire, and that is the only risk in the model. With CRRA utility a retiree faces no risk at all, and behaves very simply: they spend a constant fraction of {math}`\mRat` every period, a fraction set by the degree of impatience and by the elasticity of intertemporal substitution {math}`1/\CRRA`. The worker's problem is more interesting. It is the subject of the chapter on a tractable model of buffer stock saving, and {numref}`fig:ConsFuncTarget` shows its solution, with everything measured relative to the worker's permanent labor income.

:::{figure} figures/ConsFuncTarget.png
:name: fig:ConsFuncTarget
:align: center

The consumption function {math}`\cFunc(\mRat)` of a worker who faces a risk of forced retirement, the consumption function {math}`\cFuncAbove(\mRat)` of the same worker without the risk, and the level of consumption that would leave a worker who stays employed with unchanged {math}`\mRat`. The first and the last meet at the target {math}`\mTarg`. Drawn for the benchmark parameters of the tractable buffer stock model: {math}`\urate=0.005`, {math}`\DiscFac=1/1.10`, {math}`\Rfree=1.03`, {math}`\PGro=1` and {math}`\CRRA=2`.
:::

Start with the straight black line. For any {math}`\mRat`, it gives the spending at which a worker who keeps the job would start next period with the same {math}`\mRat`: labor income plus the interest earned on assets. It slopes upward because more resources earn more interest.

The upper line, {math}`\cFuncAbove(\mRat)`, is the consumption function the worker would follow if the risk did not exist, with labor income adjusted so that removing the risk does not raise its expected growth. Impatience shows in the fact that this line lies everywhere above the black one: an impatient consumer who faced no risk would choose to spend more than could be sustained indefinitely. The lower curve is the consumption function {math}`\cFunc(\mRat)` when the risk is present. Because the only difference between the two is the risk, the gap {math}`\cFuncAbove(\mRat)-\cFunc(\mRat)` is the precautionary saving of a worker with resources {math}`\mRat`.

Under standard assumptions about preferences and risk, the consumption function crosses the black line, and {cite:t}`BufferStockTheory` proves that it crosses it only once. The crossing defines a *target* level of resources, {math}`\mTarg`: a worker who has {math}`\mTarg` today, and stays employed, will have {math}`\mTarg` again next period. The target is stable. Below it, consumption is less than labor income plus interest, so {math}`\mRat` rises, and consumption climbs along {math}`\cFunc(\mRat)` toward the target; above it, consumption exceeds labor income plus interest, and {math}`\mRat` falls. The worker holds a *buffer stock* of wealth, and aims at the target.

Three properties of {numref}`fig:ConsFuncTarget` summarize the effect of uncertainty:

1. {math}`\cFunc(\mRat) < \cFuncAbove(\mRat)`: consumption is lower when the future is uncertain.
2. {math}`\lim_{\mRat\to\infty}\left(\cFuncAbove(\mRat)-\cFunc(\mRat)\right) = 0`: as resources grow without bound, the effect of the labor income risk vanishes. (The approach is slow, and the figure's range does not show it.)
3. {math}`\cFunc(\mRat)` is strictly concave, so {math}`\cFunc^{\prime}(\mRat)`, the share of an unexpected extra dollar that is spent, is larger for poorer consumers than for richer ones.

The concavity has an intuition close to that of liquidity constraints. When a consumer's liquidity constraint binds, a little extra cash is spent in full, an MPC of one; after a large windfall the constraint no longer binds, and the MPC falls below one. With a precautionary motive, each extra unit of wealth eases the restraint that the risk places on spending, and the relief is greater for a consumer with few resources, living close to the edge, than for one with plenty. Liquidity constraints, precautionary motives, or both together therefore make the consumption function concave ({cite:t}`carroll&kimball:concavity`; {cite:t}`carrollHolmKimball:liquidity`), and {cite:t}`huggett:higherW` shows that concavity of the consumption function in turn means higher wealth in equilibrium.

### Consumption Growth at the Target

A target has a consequence that is surprising at first sight: at the target, the expected growth rate of a worker's consumption equals the predictable growth rate of labor income, {math}`\gamma \equiv \log\PGro`, whatever the interest rate and however impatient the worker is:

```{math}
:label: eq:UR-CGrowTarget

\Ex_{t}[\Delta\log\cRat^{e}_{t+1}] \approx \gamma,
```

where the superscript {math}`e` denotes a worker who stays employed. That consumption grows with income may seem natural, but it seems at odds with the usual way of studying consumption growth, through an approximation to the first order condition, or Euler equation:

```{math}
:label: eq:UR-CGrowEuler

\Ex_{t}[\Delta\log\cRat^{e}_{t+1}] \approx \CRRA^{-1}(\rfree-\timeRate) + \phi,
```

in which {math}`\timeRate` is the time preference rate and {math}`\phi` is the contribution of the precautionary motive to consumption growth. There is no contradiction, because {math}`\phi` is not a fixed number: it depends on where the consumer is relative to the target. Equating {eq}`eq:UR-CGrowTarget` and {eq}`eq:UR-CGrowEuler` gives its value at the target,

```{math}
:label: eq:UR-phi

\phi \approx \gamma - \CRRA^{-1}(\rfree-\timeRate).
```

At the target, the precautionary contribution takes whatever value is needed to make consumption grow with income. Prudence is thus the engine of buffer stock saving: it determines how strongly a consumer cuts spending in response to risk, and through the target it determines how much precautionary wealth the consumer ends up holding.
