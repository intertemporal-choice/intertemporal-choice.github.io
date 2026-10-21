(sec:Aiyagari)=
# Aiyagari: Precautionary Saving in GE

The [decentralization of the Ramsey/Cass-Koopmans model](#sec:decentralizingrck) showed that an economy of many households behaves exactly like a single representative household, provided every household is identical and can insure any risk at an actuarially fair rate. Real households face large uninsurable risks to their own incomes, that are mostly unrelated to what happens to everyone else in the economy.[^cohort-insurance] A [prudent](#sec:RiskAndPSPremia) household facing such risk saves for precautionary reasons, and [buffer stock models](#sec:BufferStockAgeProfiles) show how much. This chapter asks what happens when a whole economy consists of such households, and their saving sets the interest rate and the wage.

[^cohort-insurance]: Graduate students might consider whether anyone has offered them an insurance contract offering them a guarantee that they will receive the mean average income of the members of their cohort of economics PhD students.

{cite:t}`aiyagari:ge` asked by how much uninsurable idiosyncratic risk raises the capital stock and the saving rate. For his parameter values, the answer was "not by much." The interest of the model lies in why.

## From Friedman to Bewley to Aiyagari

{cite:t}`friedmanATheory` argued that consumption depends on permanent income, and that measured income is permanent income plus a transitory component that consumers largely save or dissave. The argument was in words, not in math. {cite:t}`muthOptimal` mathematized it: when income is a random walk plus serially uncorrelated noise, the best forecast of future income is an exponentially weighted average of past income, which is actually exactly how Friedman had proposed to measure permanent income. {cite:t}`hallRandomWalk` later showed that, under certainty equivalence, consumption follows a random walk (see [random walk](#sec:RandomWalk) and [consumption function](#sec:ConsumptionFunction)).

Certainty equivalence rules out precautionary saving. Dropping it, when utility is not quadratic, leaves a problem with no closed-form solution. {cite:t}`bewleyPIH` formulated the permanent income hypothesis for a single infinitely lived consumer who cannot borrow against random income, and {cite:t}`bewleyStationary` placed a continuum of such consumers, with independent shocks, in a general-equilibrium exchange economy. {cite:t}`zeldesStochastic` and {cite:t}`deatonSaving` solved such problems numerically, and {cite:t}`carroll:brookings` calibrated one to household income in the Panel Study of Income Dynamics (PSID) and argued that precautionary motives quantitatively explain the behavior of aggregate consumption over the business cycle. Following Deaton, Carroll termed such behavior buffer stock saving.

{cite:t}`huggettRiskFree` used such households to determine the interest rate on a bond in zero net supply. {cite:t}`aiyagari:ge` put them into the neoclassical growth model, so that their saving becomes the capital stock. Models of this kind are now called "Aiyagari models," and his paper is the reference point for whether idiosyncratic risk matters for aggregates.

## The Household's Problem

Each of a continuum of households, of total mass one, maximizes

```{math}
\max ~ \Ex_{0}\left[\sum_{t=0}^{\infty} \DiscFac^{t}\, \uFunc(\cRat_{t})\right], \qquad \uFunc(\cRat) = \frac{\cRat^{1-\CRRA}}{1-\CRRA},
```

with {math}`\DiscFac = 1/(1+\timeRate)`. It supplies an exogenous, random endowment of labor {math}`\labor_{t}` at the wage {math}`\Wage` and holds assets earning the interest rate {math}`\rfree`, so its market resources evolve as

```{math}
:label: eq:Aiyagari-mtp1

\mRat_{t+1} = \Rfree\aRat_{t} + \Wage\labor_{t+1}, \qquad \aRat_{t} = \mRat_{t} - \cRat_{t} \geq \aMin,
```

where {math}`\aRat_{t}` is end-of-period assets and {math}`\aMin \leq 0` is the borrowing limit.

:::{margin}
Aiyagari's {math}`\mu`, {math}`\rho`, {math}`\lambda`, {math}`l` and {math}`z` (risk aversion, persistence, time preference rate, endowment, resources) are here {math}`\CRRA`, {math}`\tau`, {math}`\timeRate`, {math}`\labor` and {math}`\mRat`.
:::

The idiosyncratic labor productivity component is the only source of risk. Its logarithm follows a first-order autoregression with persistence {math}`\tau`,

```{math}
:label: eq:Aiyagari-AR1

\log \labor_{t+1} = \tau \log \labor_{t} + \sigma (1-\tau^{2})^{1/2}\, \epsilon_{t+1}, \qquad \epsilon_{t+1} \sim \mathcal{N}(0,1),
```

so {math}`\sigma` is the unconditional standard deviation of {math}`\log\labor`. For computation the process becomes a finite Markov chain ({cite:t}`tauchenFinite`). With a continuum of households, the cross-section distribution of endowments is always the chain's stationary distribution, though each household's endowment keeps moving.

The [Euler equation](#eq:uPEuler) now holds with equality only when the household is not at its borrowing limit:

```{math}
:label: eq:Aiyagari-Euler

\uP(\cRat_{t}) \geq \DiscFac\Rfree\, \Ex_{t}\left[\uP(\cRat_{t+1})\right], \quad \text{with equality whenever } \aRat_{t} > \aMin.
```

The solution is a consumption function for each level of the endowment, {math}`\cFunc(\mRat, \labor)`. In [the consumption functions figure](#fig:ConsFuncByIncomeState), each follows the 45-degree line until the household prefers to save, and is concave beyond. A household with a low endowment spends less at a given {math}`\mRat`, because a low wage today forecasts low wages to come.

:::{figure} figures/ConsFuncByIncomeState.png
:name: fig:ConsFuncByIncomeState
:align: center

The consumption function {math}`\cFunc(\mRat,\labor)` for each of the seven levels of the idiosyncratic labor productivity component, from lowest (dark) to highest (light), at the equilibrium interest rate for Aiyagari's baseline: {math}`\CRRA = 3`, {math}`\tau = 0.6`, {math}`\sigma = 0.2`, {math}`\DiscFac = 0.96`, and no borrowing. Drawn by the chapter's [notebook](Aiyagari.ipynb); open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/Aiyagari/Aiyagari.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/Aiyagari/Aiyagari.ipynb) to run it without installing anything.
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

A household never borrows all the way to this limit: a run of the worst endowment would leave it nothing to consume, which CRRA utility makes infinitely costly. Aiyagari's baseline of no borrowing, {math}`\aMin = 0`, is tighter.

### Why Wealth Stays Bounded

The [perfect foresight](#sec:PerfForesightCRRA) conditions carry over. [Return impatience](#eq:PatR) makes the household's problem well defined, and [growth impatience](#eq:PatWGroCond) keeps wealth bounded relative to income. Income does not grow here, so growth impatience is {math}`(\Rfree\DiscFac)^{1/\CRRA} < 1`, or {math}`\rfree < \timeRate`; it coincides with absolute impatience only for that reason. With {math}`\rfree \leq 0`, as in Aiyagari's most extreme calibration, human wealth is [infinite](#sec:PFwhenFHWfails) and only the borrowing limit keeps the problem well defined. If {math}`\DiscFac\Rfree \geq 1`, consumption and assets grow without bound for almost every household ({cite:t}`chamberlainWilson`).

## Firms and Factor Prices

Competitive firms produce with {math}`Y = \KLev^{\kapShare}L^{1-\kapShare}`, and capital depreciates at rate {math}`\depr`. As in the [decentralized Ramsey model](#sec:decentralizingrck), the interest rate households earn is the marginal product of capital net of depreciation, and the wage is the [marginal product](#eq:rEqfp) of labor; with [aggregate](#sec:Aggregation) labor {math}`L`,

```{math}
:label: eq:Aiyagari-Prices

\rfree = \kapShare(\KLev/L)^{\kapShare-1} - \depr, \qquad \Wage = (1-\kapShare)(\KLev/L)^{\kapShare}.
```

Inverting the first gives the capital firms want at each interest rate,

```{math}
:label: eq:Aiyagari-CapitalDemand

\KLev(\rfree) = L\left(\frac{\kapShare}{\rfree+\depr}\right)^{1/(1-\kapShare)},
```

a downward-sloping demand curve. The wage moves with the interest rate, so the interest rate affects saving both directly and through the wage.

## Stationary Equilibrium

:::{prf:definition} Stationary equilibrium with uninsured idiosyncratic risk
:label: res:aiyagari-stationary-equilibrium
:enumerated: false

A stationary equilibrium is an interest rate, a wage, consumption functions and a distribution of households over assets and endowments such that households optimize, firms optimize, the distribution reproduces itself, and the capital households hold is the capital firms use.

1. Given {math}`\rfree` and {math}`\Wage`, the consumption functions {math}`\cFunc(\mRat,\labor)` solve the household's problem.
2. {math}`\rfree` and {math}`\Wage` satisfy the [firms' first-order conditions](#eq:Aiyagari-Prices).
3. The distribution of households over {math}`(\aRat,\labor)` is stationary under the consumption functions, the [budget constraint](#eq:Aiyagari-mtp1) and the Markov chain for {math}`\labor`.
4. Aggregate assets equal the capital stock: {math}`\KLev = \Ex[\aRat]`.
:::

Each household's circumstances keep changing; only the distribution is constant. Write {math}`\Ex\aRat(\rfree)` for mean assets in the stationary distribution at the interest rate {math}`\rfree` and the wage it implies.

:::{prf:proposition} Capital market clearing with uninsured idiosyncratic risk
:label: res:aiyagari-market-clearing
:enumerated: false

The steady-state interest rate equates the capital that households supply to the capital that firms demand at that interest rate.

```{math}
:label: eq:Aiyagari-Equilibrium

\Ex\aRat(\rfree) = \KLev(\rfree).
```
:::

With complete markets, the economy would have the [Ramsey/Cass-Koopmans](#sec:RamseyCassKoopmans) steady state: {math}`\rfree = \timeRate`, a horizontal supply of capital at that rate, and an indeterminate distribution of wealth across households. With uninsurable risk, households would accumulate without limit at {math}`\rfree \geq \timeRate`, so the interest rate must be lower. Averaging the Euler equations shows this directly.

:::{prf:proposition} Interest rate below time preference
:label: res:aiyagari-r-below-time-preference
:enumerated: false

When some households are at the borrowing limit with positive probability, averaging their Euler equations over the stationary distribution shows that the steady-state interest rate must be below the time preference rate.

```{math}
:label: eq:Aiyagari-AggregatedEuler

\Ex[\uP(\cRat)] = \DiscFac\Rfree\, \Ex[\uP(\cRat)] + \Ex[\nu] \quad \Longrightarrow \quad \DiscFac\Rfree = 1 - \frac{\Ex[\nu]}{\Ex[\uP(\cRat)]} < 1.
```
:::

Here {math}`\nu_{t} = \uP(\cRat_{t}) - \DiscFac\Rfree\Ex_{t}[\uP(\cRat_{t+1})] \geq 0` is the slack in the [Euler equation](#eq:Aiyagari-Euler), positive only at the limit, and in a stationary distribution the average of {math}`\uP(\cRat_{t+1})` equals that of {math}`\uP(\cRat_{t})`.

In [the capital supply and demand figure](#fig:CapitalSupplyDemand), supply rises without bound as {math}`\rfree` approaches {math}`\timeRate`, and crosses demand at a lower interest rate and a higher capital stock than complete markets give. General equilibrium limits the effect: the extra capital drives the interest rate down, which makes saving less attractive.

:::{figure} figures/CapitalSupplyDemand.png
:name: fig:CapitalSupplyDemand
:align: center

Steady-state supply and demand for capital, with the wage moving with the interest rate. With complete markets the supply of capital is horizontal at the time preference rate {math}`\timeRate`, and the capital stock is {math}`\KLev^{\timeRate}`; with uninsured idiosyncratic risk it is {math}`\KLev^{*}`. Baseline parameters as in [the consumption functions figure](#fig:ConsFuncByIncomeState). Drawn by the chapter's [notebook](Aiyagari.ipynb); open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/Aiyagari/Aiyagari.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/Aiyagari/Aiyagari.ipynb) to run it without installing anything.
:::

Nothing guarantees that supply slopes up everywhere, so the equilibrium need not be unique ({cite:t}`acikgozExistence`); {cite:t}`lightUniqueness` and {cite:t}`achdouHACT` prove uniqueness only under conditions that include relative risk aversion no greater than one.

## Gross Saving and Net Saving

Aiyagari measured saving gross. Investment, including the replacement of worn-out capital, is divided by output measured before depreciation, so capital's income in the denominator is {math}`(\rfree+\depr)\KLev`. In a steady state without growth, investment just replaces depreciation:

:::{prf:proposition} Saving rate in a no-growth Cobb-Douglas steady state
:label: res:aiyagari-saving-rate
:enumerated: false

In a steady state with no growth the saving rate is replacement investment over output, which the Cobb-Douglas technology makes a decreasing function of the interest rate alone.

```{math}
:label: eq:Aiyagari-SavingRate

s = \frac{\depr\KLev}{Y} = \frac{\depr\kapShare}{\rfree+\depr}.
```
:::

This is the [gross saving rate](#eq:grossavrate) of the growth model. The consumption chapters of this book instead study [net saving](#sec:PerfForesightCRRA): the household's income includes interest at {math}`\rfree`, already net of depreciation ({math}`\Rfree = 1+\rfree`), and saving is that income minus consumption. In Aiyagari's steady state net saving is zero, in the aggregate and for the average household: the saving of households building their buffers is matched by the dissaving of households drawing them down. Precautionary motives raise the capital stock, and a larger capital stock needs more replacement investment, which is why they raise the gross saving rate.

## Computing the Equilibrium

Aiyagari's algorithm repeats three steps until the interest rate settles down:

1. Guess an interest rate {math}`\rfree < \timeRate`, and compute the wage from the [firms' first-order conditions](#eq:Aiyagari-Prices).
2. Solve the household's problem at those prices, and simulate one household for many periods (Aiyagari used 10,000) to find mean assets {math}`\Ex\aRat(\rfree)`.
3. If {math}`\Ex\aRat(\rfree)` exceeds {math}`\KLev(\rfree)`, lower the guess; if it falls short, raise it.

The [notebook](Aiyagari.ipynb) carries out these steps with the code of the Aiyagari1994QJE REMARK, which builds the households with HARK and, like Aiyagari, simulates them; open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/Aiyagari/Aiyagari.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/Aiyagari/Aiyagari.ipynb) to run it without installing anything.

## Results

A period is a year; Aiyagari set {math}`\DiscFac = 0.96`, {math}`\kapShare = 0.36` and {math}`\depr = 0.08` ({cite:t}`prescottTheoryAhead`), so that with complete markets {math}`\timeRate = 4.17` percent and the saving rate is 23.67 percent. He varied {math}`\sigma` (0.2, 0.4), {math}`\tau` (0 to 0.9) and {math}`\CRRA` (1, 3, 5), with no borrowing. In the baseline ({math}`\sigma = 0.2`, {math}`\tau = 0.6`, {math}`\CRRA = 3`), uninsured risk lowers the interest rate to 3.86 percent (Aiyagari found 3.88), raises capital by 4.0 percent and the saving rate to 24.28 percent. Aiyagari concluded that for moderate risk aversion, variability and persistence the saving rate rises by at most about three percentage points; only when income is both volatile and persistent is the effect large ({math}`\sigma = 0.4`, {math}`\tau = 0.9`, {math}`\CRRA = 5`: a negative interest rate and a saving rate of 37.6 percent).

## What the Calibration Leaves Out

### The Income Process

Aiyagari's values of {math}`\tau` came from first-order autoregressions for individual earnings, such as a working-paper version of {cite:t}`heatonLucas`, which put it at about 0.2 to 0.5. Panel studies of earnings found a different structure: {cite:t}`abowdCard` showed that year-to-year changes in log earnings follow a low-order moving average, as Muth's random walk plus transitory noise implies, and using total family income {cite:t}`carroll:brookings` estimated standard deviations of about 0.16 for the annual transitory shock and 0.13 for the permanent one, with a probability of about half a percent a year that family income falls nearly to zero. An autoregression fitted to income of that kind misreads it: the transitory shock acts as measurement error and biases the estimated persistence toward zero. Allowing for it, with an autoregression plus a first-order moving-average error, gives persistence near one: {cite:t}`storeslettenTelmerYaron` estimate 0.98 to one, and {cite:t}`heathcoteStoreslettenViolante` attribute the low estimates of some early studies to the omitted transitory shock.

This matters because the effect of risk on saving rises steeply with persistence; Aiyagari noted that a unit root would lower the interest rate and raise saving enormously. He kept the endowment stationary because, with infinitely lived households and permanent shocks, the cross-section distribution of income would spread out without limit. A constant probability of death, as in [Blanchard's model](#sec:BlanchardFiniteHorizon), keeps it stationary; {cite:t}`cstwMPC` use it to give households permanent and transitory shocks of the sizes the evidence suggests.

### The Lowest Income Level

With an endowment bounded away from zero, the [natural borrowing limit](#eq:Aiyagari-NaturalLimit) depends on {math}`\labor_{\min}`, a by-product of the discretization rather than an estimate; Aiyagari showed that permitting more borrowing lowers the capital stock. If income can fall to zero with a small probability, as in the PSID, the natural limit is zero: no household borrows if it might have to repay out of nothing, so no borrowing follows from preferences rather than from an arbitrary restriction.

### The Distribution of Wealth

The model's wealth distribution is far more equal than the data's, across the whole range of [the Lorenz curve figure](#fig:WealthLorenz). In the 2004 Survey of Consumer Finances the poorest 40 percent of households hold about 1 percent of net worth, and the poorest fifth slightly less than nothing; in the model the poorest 40 percent hold 15 percent. At the top, the richest 1 percent hold about 32 percent of U.S. net worth but 4 percent in the model, and the Gini coefficients are 0.80 and 0.38. {cite:t}`stachurskiTodaImpossibility` show that this is no accident of calibration: when infinitely lived households save only in a risk-free asset and share a discount factor, the upper tail of wealth can be no thicker than that of income.

:::{figure} figures/WealthLorenz.png
:name: fig:WealthLorenz
:align: center

Lorenz curves for wealth: in the baseline Aiyagari economy, and for U.S. net worth in the 2004 Survey of Consumer Finances, the data used by {cite:t}`cstwMPC`. Drawn by the chapter's [notebook](Aiyagari.ipynb); open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/Aiyagari/Aiyagari.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/Aiyagari/Aiyagari.ipynb) to run it without installing anything.
:::

Identical, infinitely lived households all have time to accumulate a large buffer, and that matters for spending. Only about a quarter of one percent of households are at the borrowing limit, and the average annual marginal propensity to consume is 0.054, not far above the [perfect foresight](#eq:PFCRRA-cOfw) value of 0.038 at the same interest rate. Empirical estimates are several times larger; {cite:t}`cstwMPC` show that matching the observed wealth distribution, with its many households holding little, brings the model close to them.

## Why the Answer Came Out as It Did

Aiyagari's conclusion was widely read as evidence that heterogeneity can be set aside for questions about aggregates. But it follows from his assumptions: households with stationary, moderately persistent income and infinite horizons all hold several years' income in wealth, a buffer large enough that a bad year barely moves their spending, so they behave much like a representative household. Models that match the evidence on income dynamics and wealth ({cite:t}`cstwMPC`; {cite:t}`kaplanMollViolante`) find that the distribution of wealth matters a great deal for aggregate spending.

## Beyond the Steady State

The model has no aggregate shocks. {cite:t}`ksHetero` added them, and found that households forecasting aggregate capital from its mean alone were almost exactly right ("approximate aggregation"), for the same reason as Aiyagari's result. More recent methods linearize the economy's response to aggregate shocks around its steady state ({cite:t}`auclertSSJ`), making realistic heterogeneity practical in heterogeneous-agent New Keynesian models ({cite:t}`kaplanMollViolante`).

## Replication

Econ-ARK's replication of {cite:t}`aiyagari:ge` is the [Aiyagari1994QJE REMARK](https://econ-ark.github.io/Aiyagari1994QJE/); its [econ-ark.org page](https://econ-ark.org/materials/aiyagari1994qje/) launches its notebooks in the browser.
