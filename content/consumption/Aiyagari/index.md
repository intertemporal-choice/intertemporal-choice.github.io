(sec:Aiyagari)=
# Aiyagari: Precautionary Saving in GE

The [decentralization of the Ramsey/Cass-Koopmans model](#sec:decentralizingrck) showed that an economy of many households behaves exactly like a single representative household, provided every household is identical and can insure any risk at an actuarially fair rate. Real households face large uninsurable risks to their own incomes, that are mostly unrelated to what happens to everyone else in the economy.[^cohort-insurance] [Buffer stock models](#sec:BufferStockAgeProfiles) show how one household responds: it saves more, and its spending depends on its wealth relative to its income. This chapter asks what happens when a whole economy consists of such households, and their saving sets the interest rate and the wage.

[^cohort-insurance]: Graduate students might consider whether anyone has offered them an insurance contract offering them a guarantee that they will receive the mean average income of the members of their cohort of economics PhD students.

{cite:t}`aiyagari:ge` posed the question in its standard form: by how much does uninsurable idiosyncratic risk raise the capital stock and the saving rate? For his parameter values, the answer was "not by much." The interest of the model lies in why.

## From Friedman to Bewley to Aiyagari

{cite:t}`friedmanATheory` argued that consumption depends on permanent income, and that measured income is permanent income plus a transitory component that consumers largely save or dissave. The argument was in words, not in math. {cite:t}`muthOptimal` mathematized it: when income is a random walk plus serially uncorrelated noise, the best forecast of future income is an exponentially weighted average of past income, which is actually exactly how Friedman had proposed to measure permanent income. {cite:t}`hallRandomWalk` later showed that, under certainty equivalence, consumption follows a random walk (see [random walk](#sec:RandomWalk) and [consumption function](#sec:ConsumptionFunction)).

Certainty equivalence rules out precautionary saving. Dropping it, when utility is not quadratic, leaves a problem with no closed-form solution. In the mid-1970s {cite:t}`schechtmanIncome` and {cite:t}`schechtmanEscudero` established when the wealth of an infinitely lived consumer who cannot borrow against random income stays bounded, and {cite:t}`bewleyPIH` formulated the permanent income hypothesis for that setting. Bewley then studied economies of many such consumers ({cite:t}`bewleyOptimumMoney`; {cite:t}`bewleyStationary`); models in which a continuum of prudent households, unable to insure their idiosyncratic risks, save against them in a single asset are now called "Bewley models."

Quantitative answers needed fast computers. {cite:t}`zeldesStochastic` solved a life-cycle version with permanent and transitory income shocks and showed how far optimal consumption departs from certainty equivalence; {cite:t}`deatonSaving` solved infinite-horizon versions with liquidity constraints; and {cite:t}`carroll:brookings` calibrated such a model to household income dynamics in the Panel Study of Income Dynamics (PSID) and argued that precautionary motives quantitatively explain the behavior of aggregate consumption over the business cycle. Following Deaton, Carroll termed such behavior buffer stock saving.

General-equilibrium applications followed: {cite:t}`imrohorogluCost` on the cost of business cycles when unemployment cannot be insured, {cite:t}`huggettRiskFree` on the risk-free rate in an endowment economy, and {cite:t}`aiyagari:ge`, who put Bewley households into the neoclassical growth model, so that their saving becomes the capital stock. Because that model was the standard framework of quantitative macroeconomics, his paper became the reference point for whether idiosyncratic risk matters for aggregates.

## The Household's Problem

Each of a continuum of households, of total mass one, maximizes

```{math}
\max ~ \Ex_{0}\left[\sum_{t=0}^{\infty} \DiscFac^{t}\, \uFunc(\cRat_{t})\right], \qquad \uFunc(\cRat) = \frac{\cRat^{1-\CRRA}}{1-\CRRA},
```

with {math}`\DiscFac = 1/(1+\timeRate)`. It supplies an exogenous, random endowment of labor {math}`\labor_{t}` at the wage {math}`\Wage` and holds assets earning the interest rate {math}`\rfree`, with {math}`\Rfree = 1+\rfree`, so its market resources evolve as

```{math}
:label: eq:Aiyagari-mtp1

\mRat_{t+1} = \Rfree\aRat_{t} + \Wage\labor_{t+1}, \qquad \aRat_{t} = \mRat_{t} - \cRat_{t} \geq \aMin,
```

where {math}`\aRat_{t}` is end-of-period assets and {math}`\aMin \leq 0` is the borrowing limit.

:::{margin}
Aiyagari's {math}`\mu`, {math}`\rho`, {math}`\lambda`, {math}`l` and {math}`z` (risk aversion, persistence, time preference rate, endowment, resources) are here {math}`\CRRA`, {math}`\corr`, {math}`\timeRate`, {math}`\labor` and {math}`\mRat`.
:::

The idiosyncratic labor productivity component is the only source of risk. Its logarithm follows a first-order autoregression,

```{math}
:label: eq:Aiyagari-AR1

\log \labor_{t+1} = \corr \log \labor_{t} + \sigma (1-\corr^{2})^{1/2}\, \epsilon_{t+1}, \qquad \epsilon_{t+1} \sim \mathcal{N}(0,1),
```

so {math}`\sigma` is the unconditional standard deviation of {math}`\log\labor` and {math}`\corr` its persistence. For computation the process becomes a finite Markov chain ({cite:t}`tauchenFinite`), scaled so that aggregate labor {math}`L` is one. With a continuum of households, the cross-section distribution of endowments is always the chain's stationary distribution, though each household's endowment keeps moving.

The Euler equation holds with equality except at the borrowing limit:

```{math}
:label: eq:Aiyagari-Euler

\uP(\cRat_{t}) \geq \DiscFac\Rfree\, \Ex_{t}\left[\uP(\cRat_{t+1})\right], \quad \text{with equality whenever } \aRat_{t} > \aMin.
```

The solution is a consumption function for each level of the endowment, {math}`\cFunc(\mRat, \labor)`, shown in [the consumption functions figure](#fig:ConsFuncByIncomeState) for Aiyagari's baseline at the equilibrium interest rate. Each follows the 45-degree line until the household prefers to save, and is concave from there on. A household with a low endowment spends less at a given {math}`\mRat`, because a low wage today forecasts low wages to come; with {math}`\corr = 0.6` that forecast fades fast, so the functions are close together.

:::{figure} figures/ConsFuncByIncomeState.png
:name: fig:ConsFuncByIncomeState
:align: center

The consumption function {math}`\cFunc(\mRat,\labor)` for each of the seven levels of the idiosyncratic labor productivity component, from lowest (dark) to highest (light), at the equilibrium interest rate for Aiyagari's baseline: {math}`\CRRA = 3`, {math}`\corr = 0.6`, {math}`\sigma = 0.2`, {math}`\DiscFac = 0.96`, and no borrowing.
:::

### How Much May a Household Borrow?

If the endowment never falls below some {math}`\labor_{\min} > 0` and {math}`\rfree > 0`, the most a household can repay for certain is the present discounted value of the worst possible stream of wages.

:::{prf:definition} Natural borrowing limit
:label: res:aiyagari-natural-borrowing-limit
:enumerated: false

The natural borrowing limit is the largest debt a household can repay with certainty, the worst wage forever discounted at the interest rate; any tighter limit is imposed from outside the household's problem.

```{math}
:label: eq:Aiyagari-NaturalLimit

\aMin \geq -\frac{\Wage\labor_{\min}}{\rfree}.
```
:::

A household never borrows all the way to this limit: a run of the worst endowment would leave it nothing to consume, which CRRA utility makes infinitely costly. Aiyagari's baseline of no borrowing, {math}`\aMin = 0`, is tighter, and so is imposed on the household's problem rather than derived from it. The natural limit depends on {math}`\labor_{\min}`, a parameter that is easy to overlook.

### Why Wealth Stays Bounded

Without risk, a household with {math}`\DiscFac\Rfree < 1` runs its assets down to the borrowing limit; with risk, it holds a buffer, and its assets move around a stationary distribution. The [perfect foresight](#sec:PerfForesightCRRA) conditions say what keeps that distribution from drifting off. Return impatience, a [return patience factor](#eq:PatR) {math}`\PatR = \Pat/\Rfree` below one, makes the household's problem well defined. Growth impatience, a [growth patience factor](#eq:PatWGroCond) {math}`\Pat/\WGro` below one, keeps wealth bounded relative to income. Income does not grow here, {math}`\WGro = 1`, so growth impatience is {math}`\Pat = (\Rfree\DiscFac)^{1/\CRRA} < 1`, which holds exactly when {math}`\rfree < \timeRate`; it coincides with absolute impatience only because income does not grow, and when {math}`\rfree > 0` it implies return impatience. With {math}`\rfree \leq 0`, as in Aiyagari's most extreme calibration, human wealth is infinite and only the borrowing limit keeps the problem well defined. If instead {math}`\DiscFac\Rfree \geq 1`, consumption and assets grow without bound for almost every household ({cite:t}`chamberlainWilson`), and as {math}`\rfree` rises toward {math}`\timeRate`, desired assets rise steeply.

## Firms and Factor Prices

Competitive firms produce with the Cobb-Douglas technology {math}`Y = \KLev^{\kapShare}L^{1-\kapShare}`, capital depreciates at rate {math}`\depr`, and [aggregate](#sec:Aggregation) labor is one. The interest rate is the marginal product of capital net of depreciation, and the wage is the marginal product of labor:

```{math}
:label: eq:Aiyagari-Prices

\rfree = \kapShare\KLev^{\kapShare-1} - \depr, \qquad \Wage = (1-\kapShare)\KLev^{\kapShare}.
```

Inverting the first gives the capital that firms want at each interest rate,

```{math}
:label: eq:Aiyagari-CapitalDemand

\KLev(\rfree) = \left(\frac{\kapShare}{\rfree+\depr}\right)^{1/(1-\kapShare)},
```

a downward-sloping demand curve. The interest rate also pins down the wage, {math}`\Wage(\rfree) = (1-\kapShare)\KLev(\rfree)^{\kapShare}`, so it affects saving both directly and through the wage.

## Stationary Equilibrium

In a steady state the interest rate, the wage and the cross-section distribution of households are constant, though each household's circumstances keep changing.

:::{prf:definition} Stationary equilibrium with uninsured idiosyncratic risk
:label: res:aiyagari-stationary-equilibrium
:enumerated: false

A stationary equilibrium is an interest rate, a wage, consumption functions and a distribution of households over assets and endowments such that households optimize, firms optimize, the distribution reproduces itself, and the capital households hold is the capital firms use.

1. Given {math}`\rfree` and {math}`\Wage`, the consumption functions {math}`\cFunc(\mRat,\labor)` solve the household's problem.
2. {math}`\rfree` and {math}`\Wage` satisfy the [firms' first-order conditions](#eq:Aiyagari-Prices) at the capital stock {math}`\KLev` and labor {math}`L = 1`.
3. The distribution of households over {math}`(\aRat,\labor)` is stationary under the consumption functions, the [budget constraint](#eq:Aiyagari-mtp1) and the Markov chain for {math}`\labor`.
4. Aggregate assets equal the capital stock: {math}`\KLev = \Ex[\aRat]`.
:::

The goods market then clears too, so only the last condition requires a search. With {math}`\Ex\aRat(\rfree)` for households' mean assets in the stationary distribution at the interest rate {math}`\rfree` and the wage {math}`\Wage(\rfree)`, equilibrium is one equation in one unknown.

:::{prf:proposition} Capital market clearing with uninsured idiosyncratic risk
:label: res:aiyagari-market-clearing
:enumerated: false

The steady-state interest rate equates the capital that households supply to the capital that firms demand at that interest rate.

```{math}
:label: eq:Aiyagari-Equilibrium

\Ex\aRat(\rfree) = \KLev(\rfree).
```
:::

### The Complete-Markets Benchmark

If households could insure their endowment risk, or faced none, the economy would behave like the representative household of the [Ramsey/Cass-Koopmans model](#sec:RamseyCassKoopmans): constant consumption requires {math}`\DiscFac\Rfree = 1`, so {math}`\rfree = \timeRate`. At that rate households will hold any amount of wealth, so the supply of capital is horizontal at {math}`\timeRate`, and the capital stock is the modified golden rule {math}`\KLev^{\timeRate} = \KLev(\timeRate)`. How wealth is distributed across households is indeterminate.

### The Interest Rate Is Below the Time Preference Rate

With uninsurable risk, households would accumulate without limit if {math}`\rfree \geq \timeRate`, so a steady state requires {math}`\rfree < \timeRate`. Averaging the Euler equations shows the same thing directly.

:::{prf:proposition} Interest rate below time preference
:label: res:aiyagari-r-below-time-preference
:enumerated: false

When some households are at the borrowing limit with positive probability, averaging their Euler equations over the stationary distribution shows that the steady-state interest rate must be below the time preference rate.

```{math}
:label: eq:Aiyagari-AggregatedEuler

\Ex[\uP(\cRat)] = \DiscFac\Rfree\, \Ex[\uP(\cRat)] + \Ex[\nu] \quad \Longrightarrow \quad \DiscFac\Rfree = 1 - \frac{\Ex[\nu]}{\Ex[\uP(\cRat)]} < 1.
```
:::

Here {math}`\nu_{t} = \uP(\cRat_{t}) - \DiscFac\Rfree\Ex_{t}[\uP(\cRat_{t+1})] \geq 0` is the slack in the [Euler equation](#eq:Aiyagari-Euler), positive only at the limit, and in a stationary distribution the average of {math}`\uP(\cRat_{t+1})` equals that of {math}`\uP(\cRat_{t})`. Without any chance of hitting the limit, the interest rate would equal the time preference rate.

[The capital supply and demand figure](#fig:CapitalSupplyDemand) draws Aiyagari's picture for his baseline. Supply {math}`\Ex\aRat(\rfree)` rises without bound as {math}`\rfree` approaches {math}`\timeRate`, so it crosses demand at a lower interest rate and a higher capital stock, {math}`\KLev^{*}`, than complete markets give. General equilibrium limits the effect: near {math}`\timeRate` precautionary saving can be arbitrarily large, but the extra capital drives the interest rate down, which makes saving less attractive.

:::{figure} figures/CapitalSupplyDemand.png
:name: fig:CapitalSupplyDemand
:align: center

Steady-state supply and demand for capital, with the wage moving with the interest rate. With complete markets the supply of capital is horizontal at the time preference rate {math}`\timeRate`, and the capital stock is {math}`\KLev^{\timeRate}`; with uninsured idiosyncratic risk it is {math}`\KLev^{*}`. Baseline parameters as in [the consumption functions figure](#fig:ConsFuncByIncomeState).
:::

Nothing guarantees that supply slopes up everywhere, so the equilibrium need not be unique: {cite:t}`lightUniqueness` and {cite:t}`achdouHACT` prove uniqueness only under conditions that include relative risk aversion no greater than one, and {cite:t}`acikgozExistence` constructs several equilibria, though for unusual parameter values. In the baseline, supply crosses demand once.

### The Saving Rate

Aiyagari reported his results as saving rates. With no growth, gross saving just replaces depreciated capital.

:::{prf:proposition} Saving rate in a no-growth Cobb-Douglas steady state
:label: res:aiyagari-saving-rate
:enumerated: false

In a steady state with no growth the saving rate is replacement investment over output, which the Cobb-Douglas technology makes a decreasing function of the interest rate alone.

```{math}
:label: eq:Aiyagari-SavingRate

s = \frac{\depr\KLev}{Y} = \frac{\depr\kapShare}{\rfree+\depr}.
```
:::

The saving rate therefore carries no information beyond the interest rate.

## Computing the Equilibrium

The steps repeat until the interest rate settles down:

1. Guess an interest rate {math}`\rfree < \timeRate`, and compute the wage {math}`\Wage(\rfree)` from the [firms' first-order conditions](#eq:Aiyagari-Prices).
2. Solve for the consumption functions by the method of endogenous gridpoints ({cite:t}`carrollEGM`; {cite:t}`SolvingMicroDSOPs`), which inverts the [Euler equation](#eq:Aiyagari-Euler) on a grid of end-of-period assets.
3. Find the stationary distribution and its mean {math}`\Ex\aRat(\rfree)`. Aiyagari simulated one household for 10,000 periods; tracking the mass of households on a fine grid of assets, splitting the mass that lands between two gridpoints in proportion to distance ({cite:t}`youngNonStochastic`), avoids simulation noise.
4. If {math}`\Ex\aRat(\rfree)` exceeds {math}`\KLev(\rfree)`, lower the guess; if it falls short, raise it; then solve the household's problem again.

The [notebook](Aiyagari.ipynb) carries out these steps and draws the figures; open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/Aiyagari/Aiyagari.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/Aiyagari/Aiyagari.ipynb) to run it without installing anything. Its interest rates match Aiyagari's to within a quarter of a percentage point, and its household solution matches Econ-ARK's `MarkovConsumerType`; the Econ-ARK replication [`Aiyagari1994QJE`](https://github.com/econ-ark/Aiyagari1994QJE) reproduces the paper by simulation.

## Calibration and Results

A period is a year. Aiyagari set {math}`\DiscFac = 0.96`, the capital share {math}`\kapShare = 0.36` and depreciation {math}`\depr = 0.08`, standard values at the time ({cite:t}`prescottTheoryAhead`); with complete markets they imply {math}`\timeRate = 4.17` percent, a capital-output ratio of about 3, and a saving rate of 23.67 percent. For income risk he used {math}`\sigma` of 0.2 or 0.4 and {math}`\corr` from 0 to 0.9, on a seven-state chain, with relative risk aversion {math}`\CRRA` of 1, 3 or 5 and no borrowing. The table gives the steady-state interest rate, in percent, for each combination (Aiyagari's Table II).

| {math}`\sigma` | {math}`\corr` | {math}`\CRRA = 1` | {math}`\CRRA = 3` | {math}`\CRRA = 5` |
|:---:|:---:|:---:|:---:|:---:|
| 0.2 | 0   | 4.17 | 4.15 | 4.09 |
| 0.2 | 0.3 | 4.14 | 4.04 | 3.91 |
| 0.2 | 0.6 | 4.09 | 3.88 | 3.59 |
| 0.2 | 0.9 | 3.93 | 3.29 | 2.53 |
| 0.4 | 0   | 4.06 | 3.78 | 3.42 |
| 0.4 | 0.3 | 3.96 | 3.42 | 2.80 |
| 0.4 | 0.6 | 3.76 | 2.78 | 1.81 |
| 0.4 | 0.9 | 3.31 | 1.29 | −0.35 |

In the baseline ({math}`\sigma = 0.2`, {math}`\corr = 0.6`, {math}`\CRRA = 3`), uninsured risk lowers the interest rate from 4.17 to 3.88 percent, raises the capital stock by 3.8 percent, and raises the saving rate from 23.67 to 24.25 percent. Aiyagari concluded that for moderate risk aversion, variability and persistence, idiosyncratic risk raises the saving rate by at most about three percentage points, but by seven to fourteen when income is both volatile and persistent: with {math}`\sigma = 0.4`, {math}`\corr = 0.9` and {math}`\CRRA = 5`, the interest rate is negative and the saving rate is 37.6 percent.

The model gets the ranking of inequality right: wealth is more unequal than income, and income more unequal than consumption. Several things it gets wrong bear directly on the size of the effect it measured.

## What the Calibration Leaves Out

### The Income Process

Aiyagari's persistence values, up to 0.9 with 0.6 as a central case, drew on first-order autoregressions for individual earnings, among them a working-paper version of {cite:t}`heatonLucas`, which put {math}`\corr` at about 0.2 to 0.5. Panel studies of earnings, chiefly in the PSID, used a different specification. {cite:t}`lillardWillis` separated a component that persists over a career from a transitory one, and {cite:t}`macurdyErrorStructure` and {cite:t}`abowdCard` found that year-to-year changes in log earnings follow a low-order moving average, the pattern implied by Muth's random walk plus transitory noise, and rejected autoregressive specifications. Using total family income rather than the earnings of the household head, {cite:t}`carroll:brookings` estimated standard deviations of about 0.16 for the annual transitory shock and 0.13 for the annual permanent shock, and a probability of about half a percent a year that family income falls nearly to zero.

An autoregression fitted to such income misreads it. Suppose the logarithm of income {math}`\YLev_{t}` is {math}`\log \YLev_{t} = p_{t} + \tranShkInd_{t}`, where the persistent component {math}`p_{t} = \corr\, p_{t-1} + \permShkInd_{t}` has persistence {math}`\corr` (a random walk when {math}`\corr = 1`) and {math}`\tranShkInd_{t}` is white noise, and an econometrician fits {math}`\log \YLev_{t} = \hat{\corr} \log \YLev_{t-1} + e_{t}` across households.

:::{prf:proposition} Persistence estimated by an autoregression
:label: res:aiyagari-ar1-attenuation
:enumerated: false

An autoregression fitted to a persistent component plus a transitory shock estimates the persistence of the persistent component times its share of the variance of income, so the transitory shock pulls the estimate toward zero.

```{math}
:label: eq:Aiyagari-AR1Attenuation

\operatorname{plim} \hat{\corr} = \frac{\operatorname{cov}(\log \YLev_{t},\log \YLev_{t-1})}{\operatorname{var}(\log \YLev_{t-1})} = \corr\, \frac{\operatorname{var}(p_{t-1})}{\operatorname{var}(p_{t-1}) + \operatorname{var}(\tranShkInd)}.
```
:::

Here {math}`\operatorname{var}(p_{t-1})` is the cross-section variance of the persistent component at {math}`t-1`, which grows over time when {math}`p` is a random walk; the transitory shock acts as measurement error. Aiyagari's values of {math}`\corr` were estimates of this kind. Within a household's own history, the permanent component does not wander far enough in a decade or two to dominate the transitory variance, and giving each household its own mean adds a further downward bias in short samples. In the [notebook](Aiyagari.ipynb), histories simulated from a random walk plus white noise, with Carroll's standard deviations, give autoregressive coefficients of 0.19, 0.44 and 0.63 over 10, 20 and 40 years, although every permanent shock lasts forever.

Allowing for the transitory component removes most of the bias. With an autoregression plus a moving-average error of order one, persistence is identified by the ratio of the covariance of income two periods apart to its covariance one period apart, which the transitory shock does not affect; in the same simulated histories this estimate is 0.83 at 20 years and 0.92 at 40. Panel-data studies that allow for a transitory component find the persistent component close to a random walk: {cite:t}`storeslettenTelmerYaron` estimate its autocorrelation at 0.98 to one, and {cite:t}`heathcoteStoreslettenViolante` attribute the low persistence in some early studies to the omission of the transitory shock.

This matters because the effect of risk on saving rises steeply with persistence; Aiyagari noted that his results suggested a unit root would lower the interest rate and raise saving enormously. He kept the endowment stationary because, with infinitely lived households and permanent shocks, the cross-section distribution of income would spread out without limit. {cite:t}`cstwMPC` resolve that problem with a constant probability of death, each household being replaced by a newborn, which keeps the cross-section stationary while income has permanent and transitory components of the sizes the evidence suggests.

### The Lowest Income Level

With an endowment bounded away from zero, the [natural borrowing limit](#eq:Aiyagari-NaturalLimit) depends on {math}`\labor_{\min}`, a by-product of the discretization rather than an estimate, to which the results can be sensitive; Aiyagari showed that permitting more borrowing lowers the capital stock, so a small effect of risk becomes smaller still. If instead income can fall to zero with a small probability, as in the PSID evidence, the natural limit is zero: no household borrows if it might have to repay out of nothing. No borrowing then follows from the household's own preferences, and the results no longer depend on how far the worst state lies above zero.

### The Distribution of Wealth

The model's wealth distribution is far more equal than the data's. Aiyagari reported Gini coefficients of 0.12 for income and 0.32 for wealth in one of his calibrations, against about 0.4 and 0.8 in U.S. data. In the baseline here the wealth Gini is 0.39, and the richest one percent hold 4 percent of wealth, against about 30 percent in U.S. data ({cite:t}`ksHetero`, Table 1); [the Lorenz curve figure](#fig:WealthLorenz) compares the two. {cite:t}`stachurskiTodaImpossibility` show that the shortfall at the top is no accident of calibration: when infinitely lived households save only in a risk-free asset and share a constant discount factor, the upper tail of wealth can be no thicker than that of income.

:::{figure} figures/WealthLorenz.png
:name: fig:WealthLorenz
:align: center

Lorenz curves for wealth: in the baseline Aiyagari economy, and the shares held by the richest 1, 5, 10, 20 and 30 percent of U.S. households as reported by {cite:t}`ksHetero`.
:::

Infinitely lived, identical households all have time to accumulate wealth near the level their common preferences and income risk make optimal, and that matters for spending. Almost no household is near the borrowing limit (0.3 percent are at it), so the average annual marginal propensity to consume is 0.055, not far above the 0.038, {math}`1-\PatR`, of a perfect foresight consumer with the same preferences. Empirical estimates are several times larger; {cite:t}`cstwMPC` show that matching the observed distribution of wealth, with its many households holding little wealth, brings the model close to them. A model that understates the marginal propensity to consume understates any mechanism that runs through spending.

## Why the Answer Came Out as It Did

Aiyagari's conclusion, that uninsured idiosyncratic risk changes aggregate saving only modestly, was widely read as evidence that heterogeneity can be set aside for questions about aggregates. But it follows from his assumptions. Infinitely lived households with stationary, moderately persistent income all end up holding several years' income in wealth, a buffer large enough that a bad year barely moves their spending, so they behave much as a representative household would. The low persistence of income, a worst outcome bounded away from zero and the dynastic horizon all push that way. Models that target the evidence on income dynamics and wealth ({cite:t}`cstwMPC`; {cite:t}`kaplanMollViolante`) find that the distribution of wealth matters a great deal for aggregate spending.

## Beyond the Steady State

The model describes a stationary equilibrium only: it has no aggregate shocks, and as stated it cannot describe the transition between steady states after a change in policy. {cite:t}`ksHetero` added aggregate productivity shocks, which require households to forecast prices that depend on the whole distribution of wealth, an object of infinite dimension. They found that forecasting next period's aggregate capital from its current mean alone was almost perfectly accurate ("approximate aggregation"), and that aggregate dynamics were close to those of a representative-agent economy, for the same reason as Aiyagari's result: almost every household is wealthy enough to behave like the representative household.

More recent methods linearize the economy's response to aggregate shocks around its steady state ({cite:t}`auclertSSJ`), making it practical to put realistic heterogeneity into heterogeneous-agent New Keynesian models ({cite:t}`kaplanMollViolante`). Being built around a given steady state, the approximation is least reliable for a policy change, such as a lasting change in unemployment insurance, that moves the steady state itself.

## Replication

Econ-ARK's replication of {cite:t}`aiyagari:ge` is the [Aiyagari1994QJE REMARK](https://econ-ark.github.io/Aiyagari1994QJE/); its [econ-ark.org page](https://econ-ark.org/materials/aiyagari1994qje/) launches its notebooks in the browser.
