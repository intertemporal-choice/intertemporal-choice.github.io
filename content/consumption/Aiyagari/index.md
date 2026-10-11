(sec:Aiyagari)=
# Aiyagari: Precautionary Saving in GE

The [decentralization of the Ramsey/Cass-Koopmans model](#sec:decentralizingrck) showed that an economy of many households behaves exactly like a single representative household, provided every household is identical and faces no risk it cannot insure. Real households face large risks to their own incomes, risks that are mostly unrelated to what happens to everyone else and that no market lets them insure. The [buffer stock models](#sec:BufferStockAgeProfiles) of the preceding chapters show how a single household responds to such risk: it saves more, and its spending depends on how much wealth it has relative to its income. This chapter asks what happens when a whole economy is populated by such households, and the interest rate and the wage are set by the saving they do.

The question was posed in its now-standard form by {cite:t}`aiyagari:ge`: by how much does uninsurable idiosyncratic risk raise the economy's capital stock and its saving rate? His answer, for the parameter values he considered, was "not by much." Much of the interest of the model lies in why that answer came out as it did, and in what changes when the model is confronted with evidence on household income and wealth.

## From Friedman to Bewley to Aiyagari

{cite:t}`friedmanATheory` argued that consumption depends on permanent income, and that measured income is permanent income plus a transitory component that consumers largely save or dissave. The argument was verbal. {cite:t}`muthOptimal` supplied the statistics behind it: when income is a random walk plus serially uncorrelated noise, the best forecast of future income is an exponentially weighted average of past income, which is how Friedman had proposed to measure permanent income. {cite:t}`hallRandomWalk` later derived the implication that, under certainty equivalence, consumption follows a random walk (see the [random walk](#sec:RandomWalk) and [consumption function](#sec:ConsumptionFunction) sections).

Certainty equivalence rules out precautionary saving. Dropping it, as soon as income is risky and utility is not quadratic, leaves a problem with no closed-form solution. Rigorous treatments of that problem, for an infinitely lived consumer whose income fluctuates randomly and who cannot borrow against it, came in the mid-1970s. {cite:t}`schechtmanIncome` and {cite:t}`schechtmanEscudero` established when such a consumer's wealth stays bounded, and {cite:t}`bewleyPIH` gave the permanent income hypothesis a theoretical formulation in this setting, with income that fluctuates around a stable mean. Bewley then studied economies populated by many such consumers ({cite:t}`bewleyOptimumMoney`; {cite:t}`bewleyStationary`), and the whole class of models in which a continuum of prudent households, unable to insure their idiosyncratic risks, save against them in a single asset has since come to be called "Bewley models."

:::{margin}
The class also goes by "Bewley–Huggett–Aiyagari" models, after three of its early general-equilibrium applications, and by "standard incomplete markets" models.
:::

Bewley's framework established what such models could and could not deliver analytically. Quantitative answers had to wait for computers fast enough to solve them numerically. {cite:t}`zeldesStochastic` solved a life-cycle version with permanent and transitory shocks to income and showed how far optimal consumption departs from certainty equivalence. {cite:t}`deatonSaving` solved infinite-horizon versions with liquidity constraints under a variety of income processes. {cite:t}`carroll:brookings` calibrated such a model to the income dynamics of households in the Panel Study of Income Dynamics (PSID) and argued that precautionary motives help explain the behavior of aggregate consumption over the business cycle. Following Deaton, Carroll termed such behavior buffer stock saving.

The first general-equilibrium applications followed. {cite:t}`imrohorogluCost` computed the cost of business cycles in an economy whose households could not insure against unemployment. {cite:t}`huggettRiskFree` computed the interest rate on a bond in zero net supply in an endowment economy of Bewley households. {cite:t}`aiyagari:ge` put Bewley households into the neoclassical growth model, so that what they save becomes the economy's capital stock. Because the growth model, calibrated to aggregate data, was by then the standard framework of quantitative macroeconomics, his paper became the reference point for asking whether idiosyncratic risk matters for aggregates.

## The Household's Problem

Each of a continuum of households, of total mass one, maximizes expected discounted utility

```{math}
\max ~ \Ex_{0}\left[\sum_{t=0}^{\infty} \DiscFac^{t}\, \uFunc(\cRat_{t})\right], \qquad \uFunc(\cRat) = \frac{\cRat^{1-\CRRA}}{1-\CRRA},
```

with time preference factor {math}`\DiscFac = 1/(1+\timeRate)` and relative risk aversion {math}`\CRRA`. A household supplies an exogenous, random endowment of labor {math}`\labor_{t}` at the wage {math}`\Wage`, and holds assets that earn the interest rate {math}`\rfree`, with {math}`\Rfree = 1+\rfree`. Its market resources, the cash on hand it has after this period's wages and interest arrive, evolve as

```{math}
:label: eq:Aiyagari-mtp1

\mRat_{t+1} = \Rfree\aRat_{t} + \Wage\labor_{t+1}, \qquad \aRat_{t} = \mRat_{t} - \cRat_{t} \geq \aMin,
```

where {math}`\aRat_{t}` is the assets left at the end of period {math}`t` and {math}`\aMin \leq 0` is the most the household may borrow. Nothing in the household's problem changes over time, so in a steady state the wage and the interest rate are constants.

:::{margin}
Aiyagari writes {math}`\mu` for relative risk aversion, {math}`\rho` for the persistence of the endowment, {math}`\lambda` for the time preference rate, {math}`l` for the endowment and {math}`z` for resources; the translations here are {math}`\CRRA`, {math}`\corr`, {math}`\timeRate`, {math}`\labor` and {math}`\mRat`.
:::

The idiosyncratic labor productivity component is the only source of risk, and it is entirely idiosyncratic. Its logarithm follows a first-order autoregression,

```{math}
:label: eq:Aiyagari-AR1

\log \labor_{t+1} = \corr \log \labor_{t} + \sigma (1-\corr^{2})^{1/2}\, \epsilon_{t+1}, \qquad \epsilon_{t+1} \sim \mathcal{N}(0,1),
```

so that {math}`\sigma` is the unconditional standard deviation of {math}`\log\labor` and {math}`\corr` its persistence. For computation the process is replaced by a Markov chain with a finite number of states, following {cite:t}`tauchenFinite`, and the levels are scaled so that the average endowment, which is aggregate labor {math}`L`, equals one. Because the shocks are independent across households and there is a continuum of them, a law of large numbers holds: the cross-section distribution of endowments is always the chain's stationary distribution, even though each household's endowment keeps moving.

The first-order condition for consumption is the usual Euler equation, modified for the borrowing limit:

```{math}
:label: eq:Aiyagari-Euler

\uP(\cRat_{t}) \geq \DiscFac\Rfree\, \Ex_{t}\left[\uP(\cRat_{t+1})\right], \quad \text{with equality whenever } \aRat_{t} > \aMin.
```

A household that would like to bring consumption forward from the future but is at its limit consumes all its resources, {math}`\cRat_{t} = \mRat_{t} - \aMin`, and the marginal utility of its consumption exceeds the discounted expected marginal utility of next period's.

The solution is a consumption function for each level of the endowment, {math}`\cFunc(\mRat, \labor)`. [The consumption functions figure](#fig:ConsFuncByIncomeState) shows the seven functions for Aiyagari's baseline parameters at the equilibrium interest rate computed below. Each follows the 45-degree line, along which the household spends everything it has, until resources are large enough that the household prefers to save; from there on each is concave, as in the buffer stock models of earlier chapters. A household whose endowment is currently low spends less at any given {math}`\mRat` than one whose endowment is high, because with a persistent endowment a low wage today forecasts low wages to come. With {math}`\corr = 0.6` the forecast is short-lived, and the seven functions are close together.

:::{figure} figures/ConsFuncByIncomeState.png
:name: fig:ConsFuncByIncomeState
:align: center

The consumption function {math}`\cFunc(\mRat,\labor)` for each of the seven levels of the idiosyncratic labor productivity component, from lowest (dark) to highest (light), at the equilibrium interest rate for Aiyagari's baseline: {math}`\CRRA = 3`, {math}`\corr = 0.6`, {math}`\sigma = 0.2`, {math}`\DiscFac = 0.96`, and no borrowing.
:::

### How Much May a Household Borrow?

Whatever limit lenders impose, a household cannot be allowed to borrow more than it could repay for certain. With an endowment that can never fall below some {math}`\labor_{\min} > 0`, the most a household can be sure of repaying, if {math}`\rfree > 0`, is the present discounted value of the worst possible stream of wages.

:::{prf:definition} Natural borrowing limit
:label: res:aiyagari-natural-borrowing-limit
:enumerated: false

The natural borrowing limit is the largest debt a household can repay with certainty, the worst wage forever discounted at the interest rate; any limit tighter than it is imposed from outside the household's problem.

```{math}
:label: eq:Aiyagari-NaturalLimit

\aMin \geq -\frac{\Wage\labor_{\min}}{\rfree}.
```
:::

Aiyagari called this the "present value" borrowing constraint, and showed that it follows from the requirements that debts be repaid and that consumption never be negative. A household facing it never chooses to borrow all the way to the limit: doing so would leave it, after a run of the worst endowment, with nothing to consume, which CRRA utility makes infinitely costly. Any tighter limit, such as Aiyagari's baseline of no borrowing at all, {math}`\aMin = 0`, is "ad hoc" in the sense that it is imposed from outside the household's problem rather than derived from it. The distinction matters below, because the natural limit depends on {math}`\labor_{\min}`, a parameter that is easy to overlook.

### Why Wealth Stays Bounded

A household that faces no risk and is impatient, in the sense that {math}`\DiscFac\Rfree < 1`, runs its assets down to the borrowing limit and stays there. With risk, the same household holds a buffer of assets, and its assets move around a stationary distribution. What keeps that distribution from drifting off toward infinity is impatience, and the [perfect foresight](#sec:PerfForesightCRRA) chapter's conditions say which kind. The household's problem has a well-defined solution if it is return impatient, with a [return patience factor](#eq:PatR) {math}`\PatR = \Pat/\Rfree` below one; when {math}`\rfree > 0` this follows from the next condition. Wealth stays bounded relative to income if the household is growth impatient, with a [growth patience factor](#eq:PatWGroCond) {math}`\Pat/\WGro` below one. Here income does not grow, {math}`\WGro = 1`, so the condition is {math}`\Pat = (\Rfree\DiscFac)^{1/\CRRA} < 1`, which holds exactly when {math}`\rfree < \timeRate`; it coincides with absolute impatience only because income does not grow. With {math}`\rfree \leq 0`, as in Aiyagari's most extreme calibration, human wealth is infinite and only the borrowing limit keeps the problem well defined. If instead {math}`\DiscFac\Rfree \geq 1`, marginal utility discounted at the interest rate is a nonnegative supermartingale, and {cite:t}`chamberlainWilson` show that consumption and assets then grow without bound for almost every household. As {math}`\rfree` rises toward {math}`\timeRate` from below, the assets households want to hold rise steeply, and without bound in the limit.

## Firms and Factor Prices

Competitive firms rent capital and labor to produce output with the Cobb-Douglas technology {math}`Y = \KLev^{\kapShare}L^{1-\kapShare}`, and capital depreciates at rate {math}`\depr`. With aggregate labor equal to one (see the [aggregation](#sec:Aggregation) appendix for how a continuum of households adds up), profit maximization equates the rental rate to the marginal product of capital, net of depreciation, and the wage to the marginal product of labor:

```{math}
:label: eq:Aiyagari-Prices

\rfree = \kapShare\KLev^{\kapShare-1} - \depr, \qquad \Wage = (1-\kapShare)\KLev^{\kapShare}.
```

Inverting the first gives the capital that firms want at each interest rate,

```{math}
:label: eq:Aiyagari-CapitalDemand

\KLev(\rfree) = \left(\frac{\kapShare}{\rfree+\depr}\right)^{1/(1-\kapShare)},
```

a demand curve that slopes down, tends to infinity as {math}`\rfree` falls toward {math}`-\depr`, and tends to zero as {math}`\rfree` rises. The wage is pinned down by the interest rate too, {math}`\Wage(\rfree) = (1-\kapShare)\KLev(\rfree)^{\kapShare}`, so households' saving depends on {math}`\rfree` both directly and through the wage.

## Stationary Equilibrium

A steady state of this economy is a situation in which the interest rate, the wage and the cross-section distribution of households over assets and endowments are all constant, although every individual household's circumstances keep changing.

:::{prf:definition} Stationary equilibrium with uninsured idiosyncratic risk
:label: res:aiyagari-stationary-equilibrium
:enumerated: false

A stationary equilibrium is an interest rate, a wage, consumption functions and a distribution of households over assets and endowments such that households optimize, firms optimize, the distribution reproduces itself, and the capital households hold is the capital firms use.

1. Given {math}`\rfree` and {math}`\Wage`, the consumption functions {math}`\cFunc(\mRat,\labor)` solve the household's problem.
2. {math}`\rfree` and {math}`\Wage` satisfy the [firms' first-order conditions](#eq:Aiyagari-Prices) at the capital stock {math}`\KLev` and labor {math}`L = 1`.
3. The distribution of households over {math}`(\aRat,\labor)` is the stationary distribution generated by the consumption functions, the [budget constraint](#eq:Aiyagari-mtp1) and the Markov chain for {math}`\labor`.
4. Aggregate assets equal the capital stock: {math}`\KLev = \Ex[\aRat]`, the mean of end-of-period assets under that distribution.
:::

With capital and labor markets clearing, the goods market clears too, so the last condition is the only one that requires a search. Write {math}`\Ex\aRat(\rfree)` for the mean assets households hold in the stationary distribution that arises when they face the interest rate {math}`\rfree` and the wage {math}`\Wage(\rfree)`. Equilibrium then comes down to one equation in one unknown.

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

If households could insure their endowment risk, or if there were none, the economy would behave like the representative household of the [Ramsey/Cass-Koopmans model](#sec:RamseyCassKoopmans). In a steady state its consumption is constant, so its Euler equation requires {math}`\DiscFac\Rfree = 1`: the interest rate must equal the time preference rate, {math}`\rfree = \timeRate`. At that interest rate households are willing to hold any amount of wealth, and at any lower rate they would run their wealth down to the borrowing limit. The supply of capital is therefore a horizontal line at {math}`\timeRate`, infinitely elastic, and the capital stock is whatever firms demand at {math}`\timeRate`, the modified golden rule {math}`\KLev^{\timeRate} = \KLev(\timeRate)`. How wealth is distributed across households is not determined.

### The Interest Rate Is Below the Time Preference Rate

With uninsurable risk, the supply of capital is no longer horizontal. The argument above shows that households would accumulate without limit if {math}`\rfree \geq \timeRate`, so a steady state requires {math}`\rfree < \timeRate`. There is also a simple way to see the same thing from the households' first-order conditions.

:::{prf:proposition} Interest rate below time preference
:label: res:aiyagari-r-below-time-preference
:enumerated: false

When some households are at the borrowing limit with positive probability, averaging their Euler equations over the stationary distribution shows that the steady-state interest rate must be below the time preference rate.

```{math}
:label: eq:Aiyagari-AggregatedEuler

\Ex[\uP(\cRat)] = \DiscFac\Rfree\, \Ex[\uP(\cRat)] + \Ex[\nu] \quad \Longrightarrow \quad \DiscFac\Rfree = 1 - \frac{\Ex[\nu]}{\Ex[\uP(\cRat)]} < 1.
```
:::

Here {math}`\nu_{t} = \uP(\cRat_{t}) - \DiscFac\Rfree\Ex_{t}[\uP(\cRat_{t+1})] \geq 0` is the amount by which the [Euler equation](#eq:Aiyagari-Euler) holds as an inequality, positive only for households at the limit. In a stationary distribution the average of {math}`\uP(\cRat_{t+1})` across households is the same as the average of {math}`\uP(\cRat_{t})`, which gives the equation. If no household were ever constrained, the interest rate would have to equal the time preference rate; it is the possibility of hitting the limit, however rarely it happens, that forces it below.

[The capital supply and demand figure](#fig:CapitalSupplyDemand) draws Aiyagari's picture of the equilibrium, for his baseline parameters. The households' supply curve {math}`\Ex\aRat(\rfree)` is upward sloping and tends to infinity as {math}`\rfree` approaches {math}`\timeRate`; the firms' demand curve is the one derived above. The complete-markets steady state is where demand crosses the horizontal line at {math}`\timeRate`; the steady state with uninsured risk is where it crosses the supply curve, at a lower interest rate and a higher capital stock {math}`\KLev^{*}`.

:::{figure} figures/CapitalSupplyDemand.png
:name: fig:CapitalSupplyDemand
:align: center

Steady-state supply and demand for capital. The supply curve {math}`\Ex\aRat(\rfree)` lets the wage move with the interest rate, as it does in equilibrium. With complete markets the supply of capital is horizontal at the time preference rate {math}`\timeRate`, and the capital stock is {math}`\KLev^{\timeRate}`; with uninsured idiosyncratic risk it is {math}`\KLev^{*}`. Baseline parameters as in [the consumption functions figure](#fig:ConsFuncByIncomeState).
:::

The figure also shows why general equilibrium limits the effect of precautionary saving. At a given interest rate close to {math}`\timeRate`, precautionary saving can be made arbitrarily large; but the extra capital drives the interest rate down, and a lower interest rate makes saving less attractive. How far the interest rate falls, and how much capital rises, is a quantitative question that depends on the slopes of both curves.

Nothing in the argument guarantees that the supply curve slopes up everywhere, and so nothing guarantees a unique equilibrium; Aiyagari noted as much. {cite:t}`lightUniqueness` and {cite:t}`achdouHACT` prove uniqueness under conditions that include relative risk aversion no greater than one (Achdou and coauthors also require that borrowing not be allowed), and {cite:t}`acikgozExistence` constructs an example with several equilibria, though only for parameter values far from those used in practice. In the baseline computed here the supply curve slopes upward throughout the range shown and crosses demand once.

### The Saving Rate

Aiyagari reported his results as saving rates. In a steady state with no growth, gross saving just replaces depreciated capital, so the saving rate is investment over output, and the [firms' first-order condition](#eq:Aiyagari-Prices) turns it into a function of the interest rate alone.

:::{prf:proposition} Saving rate in a no-growth Cobb-Douglas steady state
:label: res:aiyagari-saving-rate
:enumerated: false

In a steady state with no growth the saving rate is replacement investment over output, which the Cobb-Douglas technology makes a decreasing function of the interest rate alone.

```{math}
:label: eq:Aiyagari-SavingRate

s = \frac{\depr\KLev}{Y} = \frac{\depr\kapShare}{\rfree+\depr}.
```
:::

The saving rate therefore carries no information beyond the interest rate: a lower interest rate means more capital per unit of output, and so more replacement investment.

## Computing the Equilibrium

Each step of the computation solves a problem from an earlier chapter, and the steps are repeated until the interest rate settles down:

1. Guess an interest rate {math}`\rfree < \timeRate`, and compute the wage {math}`\Wage(\rfree)` from the [firms' first-order conditions](#eq:Aiyagari-Prices).
2. Solve the household's problem for the consumption functions. The method of endogenous gridpoints ({cite:t}`carrollEGM`; {cite:t}`SolvingMicroDSOPs`) does this quickly and accurately by inverting the [Euler equation](#eq:Aiyagari-Euler) on a grid of end-of-period assets.
3. Find the stationary distribution of households over assets and endowments, and its mean {math}`\Ex\aRat(\rfree)`. Aiyagari simulated one household for 10,000 periods and averaged its assets; a deterministic alternative tracks the mass of households on a fine grid of assets, splitting the mass that lands between two gridpoints in proportion to distance ({cite:t}`youngNonStochastic`), and avoids simulation noise.
4. If {math}`\Ex\aRat(\rfree)` exceeds {math}`\KLev(\rfree)`, households want to hold more capital than firms want to use, so the interest rate is too high; if it falls short, too low. Adjust the guess, by bisection or a faster root-finder, and return to step 2.

The chapter's [notebook](Aiyagari.ipynb) carries out these steps and draws the figures. Its interest rate agrees with Aiyagari's to two decimal places at the baseline and to within about a quarter of a percentage point across all of his calibrations, and its household solution agrees with that of the Econ-ARK toolkit's `MarkovConsumerType`. The Econ-ARK replication [`Aiyagari1994QJE`](https://github.com/econ-ark/Aiyagari1994QJE) reproduces the paper's results with that toolkit by simulation.

## Calibration and Results

A period is a year. Aiyagari set the time preference factor to {math}`\DiscFac = 0.96`, the capital share to {math}`\kapShare = 0.36` and depreciation to {math}`\depr = 0.08`, values standard in the growth literature of the time ({cite:t}`prescottTheoryAhead`). With complete markets they imply an interest rate of {math}`\timeRate = 4.17` percent, a capital-output ratio of about 3, and a saving rate of 23.67 percent. For income risk he considered {math}`\sigma` of 0.2 and 0.4 and persistence {math}`\corr` from 0 to 0.9, approximated by a seven-state Markov chain, with relative risk aversion {math}`\CRRA` of 1, 3 or 5, and no borrowing.

The table reports the steady-state interest rate, in percent, for each combination (Aiyagari's Table II); the saving rate follows from the [saving rate in a no-growth Cobb-Douglas steady state](#eq:Aiyagari-SavingRate).

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

In the baseline, {math}`\sigma = 0.2`, {math}`\corr = 0.6` and {math}`\CRRA = 3`, uninsured risk lowers the interest rate from 4.17 to 3.88 percent, raises the capital stock by 3.8 percent, and raises the saving rate from 23.67 to 24.25 percent. Aiyagari concluded that for moderate values of risk aversion, variability and persistence, idiosyncratic risk raises the aggregate saving rate by no more than about three percentage points, though when the endowment is both volatile and persistent the increase can reach seven to fourteen points: with {math}`\sigma = 0.4`, {math}`\corr = 0.9` and {math}`\CRRA = 5`, the interest rate is negative and the saving rate is 37.6 percent. The interest rate falls with every one of the three parameters, and most of all when they are high together, because it is a persistent and volatile income stream, held by a household that dislikes risk, that makes a buffer of wealth valuable.

The model got some things right. Wealth is more unequal than income, and income more unequal than consumption, as in the data, and being able to trade assets roughly halves the variability of consumption compared with holding a fixed stock of them, a benefit Aiyagari valued at about 14 percent of consumption. Other things it got wrong, and several of them bear directly on the size of the effect it measured.

## What the Calibration Leaves Out

### The Income Process

The persistence Aiyagari considered, up to 0.9 and with 0.6 as a central value, drew on estimates of first-order autoregressions for individual earnings, among them a working-paper version of {cite:t}`heatonLucas`, which put {math}`\corr` between about 0.2 and 0.5. A separate literature in labor economics had by then studied the dynamics of individual earnings in panel data, chiefly the PSID, with a different specification. {cite:t}`lillardWillis` decomposed earnings into a component that persists over a career and a transitory one. {cite:t}`macurdyErrorStructure` and {cite:t}`abowdCard` found that year-to-year changes in log earnings follow a low-order moving average, the pattern implied by Muth's formalization of Friedman's idea, a permanent component that follows a random walk plus a transitory component that does not persist; autoregressive specifications were rejected. Using total family income rather than the earnings of the household head, {cite:t}`carroll:brookings` estimated standard deviations of about 0.16 for the annual transitory shock and 0.13 for the annual permanent shock, along with a small probability, about half a percent a year, that family income falls nearly to zero.

The two descriptions of income are not as far apart as they look; an autoregression fitted to income generated by permanent and transitory shocks simply misreads it. Suppose the logarithm of income {math}`\YLev_{t}` is {math}`\log \YLev_{t} = p_{t} + \tranShkInd_{t}`, where the persistent component {math}`p_{t} = \corr\, p_{t-1} + \permShkInd_{t}` has persistence {math}`\corr` (a random walk when {math}`\corr = 1`) and {math}`\tranShkInd_{t}` is white noise, and an econometrician fits {math}`\log \YLev_{t} = \hat{\corr} \log \YLev_{t-1} + e_{t}` across households.

:::{prf:proposition} Persistence estimated by an autoregression
:label: res:aiyagari-ar1-attenuation
:enumerated: false

An autoregression fitted to the sum of a persistent component and a transitory shock estimates a persistence equal to the persistence of the persistent component, weighted by its share of the variance of income, so the transitory shock pulls the estimate toward zero.

```{math}
:label: eq:Aiyagari-AR1Attenuation

\operatorname{plim} \hat{\corr} = \frac{\operatorname{cov}(\log \YLev_{t},\log \YLev_{t-1})}{\operatorname{var}(\log \YLev_{t-1})} = \corr\, \frac{\operatorname{var}(p_{t-1})}{\operatorname{var}(p_{t-1}) + \operatorname{var}(\tranShkInd)}.
```
:::

Here {math}`\operatorname{var}(p_{t-1})` is the cross-section variance of the persistent component at {math}`t-1`, which need not be constant: it grows over time when {math}`p` is a random walk. The estimate is a weighted average of the persistence of the two components, {math}`\corr` for the persistent one and zero for the transitory one, with weights equal to their shares of the variance; the transitory shock plays the role of measurement error. Aiyagari's values of {math}`\corr` were themselves estimates of this kind. In a household's own history, which is what an individual-level autoregression describes, the permanent component does not wander far enough over a decade or two to dominate the transitory variance, and allowing each household its own mean adds a further downward bias in short samples; the persistence of income is badly understated. In the chapter's notebook, income histories simulated from a pure random walk plus white noise, with Carroll's standard deviations, give autoregressive coefficients of 0.19, 0.44 and 0.63 when each household's history is 10, 20 or 40 years long, although every permanent shock lasts forever.

Allowing for the transitory component removes most of the bias. If income is modeled as an autoregression with a moving-average error of order one, the persistence is identified from the ratio of the covariance of income two periods apart to its covariance one period apart, which the transitory shock does not affect; in the same simulated histories this estimate is 0.83 at 20 years and 0.92 at 40, and the remaining gap reflects only the short samples. In actual panel data, studies that allow for a transitory component find the persistent component close to a random walk: {cite:t}`storeslettenTelmerYaron` estimate its autocorrelation at between 0.98 and one, and {cite:t}`heathcoteStoreslettenViolante` describe a very persistent autoregressive component plus a transitory one as the leading view, attributing the low persistence found in some early studies to the omission of the transitory shock.

The point matters because the effect of risk on saving rises steeply with persistence. Aiyagari himself observed that earnings with a unit root could be approximated by letting {math}`\corr` approach one while {math}`\sigma` rises, and that his results suggested this would lower the interest rate and raise saving enormously. He kept the endowment stationary because, with infinitely lived households and permanent shocks, the cross-section distribution of income would spread out without limit and never settle down. {cite:t}`cstwMPC` resolve that problem by giving households a constant probability of death, with each household replaced by a newborn, which keeps the cross-section stationary while each household's income has permanent and transitory components of the sizes the evidence suggests.

### The Lowest Income Level

With an endowment bounded away from zero, the [natural borrowing limit](#eq:Aiyagari-NaturalLimit) lets households borrow against the present value of the worst possible stream of wages. That limit, and so the amount of borrowing, depends on {math}`\labor_{\min}`, the bottom of the endowment's range: a parameter that is a by-product of the discretization rather than something estimated, and to which the results can be sensitive. Aiyagari showed that permitting more borrowing lowers the capital stock, so a small effect of risk under no borrowing becomes smaller still when borrowing is allowed.

If instead there is a small probability that income falls to zero, as in the PSID evidence above, the natural limit is zero: no household will borrow if it might have to repay out of nothing. The no-borrowing outcome then follows from the household's own preferences rather than from an arbitrary restriction, and the results no longer depend on how far the worst state lies above zero.

### The Distribution of Wealth

In the model, the distribution of wealth is far more equal than in the data. Aiyagari reported Gini coefficients of 0.12 for income and 0.32 for wealth in one of his calibrations, against about 0.4 and 0.8 in U.S. data. In the baseline computed here, households at the 10th and 90th percentiles of wealth hold 1.3 and 11.2, around a mean of 5.7; the wealth Gini is 0.39, the richest one percent hold 4 percent of wealth, and the richest ten percent hold 26 percent. In U.S. data the richest one percent hold about 30 percent ({cite:t}`ksHetero`, Table 1). [The Lorenz curve figure](#fig:WealthLorenz) compares the model's distribution with the U.S. data. {cite:t}`stachurskiTodaImpossibility` show that the shortfall at the top is no accident of calibration: when households are infinitely lived, save only in a risk-free asset and share a constant discount factor, the upper tail of the wealth distribution can be no thicker than that of income.

:::{figure} figures/WealthLorenz.png
:name: fig:WealthLorenz
:align: center

Lorenz curves for wealth: in the baseline Aiyagari economy, and the shares held by the richest 1, 5, 10, 20 and 30 percent of U.S. households as reported by {cite:t}`ksHetero`.
:::

The equality has a cause and a consequence. The cause is that infinitely lived, identical households all have enough time to accumulate wealth near the level that their common preferences and income risk make optimal; Aiyagari himself pointed to the dynastic household and to the single source of inequality as reasons the model could not match the data. The consequence is for spending. Almost no household in the baseline economy is anywhere near the borrowing limit (0.3 percent of households are at it), and the [consumption functions](#fig:ConsFuncByIncomeState) are close to linear over the range where most households live. The average annual marginal propensity to consume out of a small windfall is 0.055, not far above the 0.038 of a perfect foresight consumer with the same preferences facing the same interest rate, which is one minus the [return patience factor](#eq:PatR), {math}`1-\PatR`. Empirical estimates of the annual marginal propensity to consume are several times larger, and {cite:t}`cstwMPC` show that a model which matches the observed distribution of wealth, with its many households holding little wealth, delivers a marginal propensity to consume close to those estimates; {cite:t}`kaplanViolanteJEP` document the same gap between the marginal propensity to consume in models of this kind and the evidence. Since the aggregate marginal propensity to consume governs how strongly spending responds to transfers and to changes in income, a model that understates it will understate the force of any mechanism that runs through spending.

### Only a Steady State

The model describes a stationary equilibrium and nothing else. It has no aggregate shocks, so it says nothing about business cycles, and as stated it cannot describe how the economy moves from one steady state to another after a change in policy.

## Why the Answer Came Out as It Did

Aiyagari's quantitative conclusion, that uninsured idiosyncratic risk changes aggregate saving only modestly, was widely read as evidence that heterogeneity can be set aside when the questions are about aggregates. The model shows why the conclusion follows from its assumptions. Infinitely lived households with a stationary, moderately persistent income process all end up holding several years' income in wealth; households that rich hold a buffer large enough that a bad year barely moves their spending, and behave much as a representative household would. Each of the features of the calibration discussed above, the low persistence of income, the bounded-away-from-zero worst outcome, the dynastic horizon, pushes in that direction. Models that take the evidence on income dynamics and the distribution of wealth as targets, such as those of {cite:t}`cstwMPC` and {cite:t}`kaplanMollViolante`, find that the distribution of wealth matters a great deal for aggregate spending.

## Beyond the Steady State

{cite:t}`ksHetero` added aggregate productivity shocks to an economy of Aiyagari households. Households then need to forecast future interest rates and wages, which depend on the whole distribution of wealth, an object of infinite dimension. Krusell and Smith's solution was to suppose that households forecast next period's aggregate capital using only its current mean, and to search for the forecasting rule that is consistent with the outcomes it produces. The rule turned out to be almost perfectly accurate, a property known as approximate aggregation, and the economy's aggregate dynamics were close to those of a representative-agent economy. The near-equivalence has the same source as Aiyagari's result: in their calibration, too, almost every household is wealthy enough to behave like the representative household.

More recent methods linearize the economy's response to aggregate shocks around its steady state, computing how the paths of aggregate variables respond to a small perturbation in the sequence of prices households face ({cite:t}`auclertSSJ`). Such methods make it practical to embed realistic household heterogeneity in models with nominal rigidities, as in the heterogeneous-agent New Keynesian models of {cite:t}`kaplanMollViolante`. Because the approximation is built around a given steady state, it is most reliable for shocks that leave the steady state unchanged; a policy change that permanently alters the risks households face, such as a lasting change in the generosity of unemployment insurance, also changes the steady state that the approximation takes as its anchor.
