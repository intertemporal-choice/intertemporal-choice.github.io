(sec:BlanchardFiniteHorizon)=
# The Blanchard (1985) Model of Perpetual Youth

The [Ramsey/Cass-Koopmans model](#sec:RamseyCassKoopmans) assumes that households live forever. {cite:t}`blanchardFinite` showed how to give them finite lives while keeping the model nearly as tractable: every consumer faces the same constant probability of death, whatever the consumer's age, so that someone who has lived a thousand years is no more likely to die in the next year than someone born yesterday. This chapter works out the model and three of its results. Finite horizons lower the steady-state capital stock below the RCK model's [modified golden rule](#eq:RCK-modGoldenRule). They break the Ricardian equivalence that holds in [the RCK model with government](#sec:RCKGov-Debt), so that government debt is net wealth and crowds out capital. And when income falls with age, they can make the interest rate negative and the economy dynamically inefficient, as the [Diamond OLG model](#sec:OLGModel) can be.

:::{margin}
[Decentralizing the Ramsey/Cass-Koopmans Model](#sec:decentralizingrck) lists finite lives among the reasons a market economy's allocation can differ from the RCK planner's. The appendix on [Aggregation](#sec:Aggregation) works through the population arithmetic of Blanchard's model in discrete as well as continuous time, and the same device keeps the distribution of income stationary in models whose income shocks are permanent, as the [Aiyagari chapter](#sec:Aiyagari) explains.
:::

(sec:BFH-Mortality)=
## Mortality and the Objective

Time is continuous, and every consumer dies with the same instantaneous probability {math}`\diePrb`, so the probability, as viewed by a consumer alive at date {math}`t`, of still being alive at a later date {math}`\tau` is

```{math}
:label: eq:BFH-living

\Alive_{t}^{\tau} = e^{-\diePrb(\tau-t)} .
```

Since {math}`\diePrb e^{-\diePrb(\tau-t)}` is the density of the date of death, the expected remaining life of a consumer of any age is

```{math}
\int_{t}^{\infty} (\tau-t)\,\diePrb e^{-\diePrb(\tau-t)}\,d\tau = 1/\diePrb ,
```

which we call the consumer's "horizon." If the chance of dying is {math}`\diePrb=1/50` a year, the horizon is 50 years.

At every instant a large cohort is born, whose size is normalized to {math}`\diePrb` per unit of time. Of the cohort born at date {math}`s`, the fraction {math}`\Alive_{s}^{t} = e^{-\diePrb(t-s)}` is still alive at {math}`t`. If the economy has existed forever, the population at {math}`t` is the sum of the survivors of every cohort born since {math}`s=-\infty`:

```{math}
:label: eq:BFH-totpop

\diePrb\int_{-\infty}^{t} \Alive_{s}^{t}\,ds = \int_{-\infty}^{t} \diePrb e^{-\diePrb(t-s)}\,ds = \Big[e^{-\diePrb(t-s)}\Big]_{s=-\infty}^{s=t} = 1 .
```

Births just offset deaths, and the population is constant at one.

Write {math}`x(s,t)` for the value at date {math}`t` of a variable {math}`x` for a consumer born at date {math}`s`, so that {math}`\cNrm(s,t)` is the consumption at {math}`t` of a consumer born at {math}`s`. A dot is a derivative with respect to the date {math}`t`, for a given date of birth.

Utility is logarithmic, {math}`\uFunc(\cNrm) = \lcNrm`, where {math}`\lnat` is the natural log, and the time preference rate is {math}`\discRte`. Mortality alone makes a consumer discount the future: even with a time preference rate of zero, utility at date {math}`\tau` would count only with the probability {math}`\Alive_{t}^{\tau}` of being alive to enjoy it. With time preference, the two discounts multiply, and at date {math}`t` a consumer born at {math}`s` maximizes

```{math}
:label: eq:BFH-objfunc

\int_{t}^{\infty} \lcNrm(s,\tau)\,\Alive_{t}^{\tau}e^{-\discRte(\tau-t)}\,d\tau = \int_{t}^{\infty} \lcNrm(s,\tau)\,e^{-\discRteEff(\tau-t)}\,d\tau ,
```

where {math}`\discRteEff \equiv \discRte+\diePrb` is the survival-inclusive time preference rate. The ring marks a rate that includes survival.

The same holds, approximately, in discrete time. Suppose {math}`t+1` is the last period of life, and that a consumer who dies before {math}`t+1` gets no utility then. With no chance of death, the value of the consumer's problem at {math}`t` would be {math}`\VFunc_{t} = \max \{\uFunc(\cNrm_{t}) + \uFunc(\cNrm_{t+1})/(1+\discRte)\}`; with a probability {math}`\diePrb` of dying between {math}`t` and {math}`t+1`, it is

```{math}
:label: eq:BFH-discreteApprox

\begin{gathered}\begin{aligned}
  \VFunc_{t} & = \max \left\{\uFunc(\cNrm_{t}) + \left(\frac{1}{1+\discRte}\right)\left[(1-\diePrb)\uFunc(\cNrm_{t+1}) + \diePrb \cdot 0\right]\right\}
\\ & = \max \left\{\uFunc(\cNrm_{t}) + \left(\frac{1-\diePrb}{1+\discRte}\right)\uFunc(\cNrm_{t+1})\right\}
\\ & \approx \max \left\{\uFunc(\cNrm_{t}) + \left(\frac{1}{1+\discRte+\diePrb}\right)\uFunc(\cNrm_{t+1})\right\} .
\end{aligned}\end{gathered}
```

The consumer behaves almost exactly like one who never dies but has the time preference rate {math}`\discRte+\diePrb`. The approximation drops terms of second order in the rates, {math}`\diePrb\discRte` and {math}`\diePrb^{2}`, which vanish relative to the rates themselves as the period shrinks; in continuous time, {eq}`eq:BFH-objfunc`, it is exact.

(sec:BFH-Insurance)=
## Insurance and the Budget Constraint

Consumers have no bequest motive: whatever they own when they die gives them no utility. So if someone offered to pay them, while they live, for the right to inherit their net worth when they die, they would gladly take the deal. For a consumer with net worth {math}`\netWorth(s,t)`, who dies at the rate {math}`\diePrb`, that right is worth a flow of {math}`\diePrb\netWorth(s,t)`. Suppose, then, that competitive insurance companies pay each living consumer {math}`\diePrb\netWorth(s,t)` per unit of time in exchange for the consumer's net worth at death: a [life annuity](https://en.wikipedia.org/wiki/Life_annuity). A company with many customers inherits, per unit of time, the net worth of the fraction {math}`\diePrb` of them who die, which pays exactly for its payments to the living, so it makes zero profits.

:::{margin}
The contract covers debt as well. A consumer with negative net worth pays the company {math}`\diePrb` times the debt, and the company repays the debt when the consumer dies, so lenders are always repaid, and the consumer borrows at {math}`\rfree+\diePrb`.
:::

From the consumer's standpoint, the insurance raises the interest rate on net worth by {math}`\diePrb`, to the survival-inclusive interest rate {math}`\rfreeEff \equiv \rfree+\diePrb`. A consumer born at {math}`s` receives noncapital (labor) income {math}`\wage(s,t)` at date {math}`t` and takes the path of the interest rate {math}`\rfree_{t}` as given, so, with the insurance, the consumer's net worth evolves as

```{math}
:label: eq:BFH-dbc

\dot{\netWorth}(s,t) = \rfreeEff_{t}\netWorth(s,t) + \wage(s,t) - \cNrm(s,t) .
```

(sec:BFH-Consumer)=
## The Consumer's Problem

The consumer's current-value Hamiltonian is

:::{margin}
These are [the decentralized RCK household's](#eq:cdotindiv) conditions, with logarithmic utility and the survival-inclusive rates. [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) derives them and relates each to its discrete-time counterpart.
:::

```{math}
\Ham(\netWorth,\cNrm,\vk) = \lcNrm(s,t) + (\rfreeEff_{t}\netWorth(s,t) + \wage(s,t) - \cNrm(s,t))\vk .
```

The [condition for optimal consumption](#eq:uceqvk), {math}`\partial\Ham/\partial\cNrm = 0`, and the [costate equation](#eq:lamgrow), with the survival-inclusive rates, are

```{math}
\begin{gathered}\begin{aligned}
  1/\cNrm(s,t) & = \vk ,
\\ \dot{\vk} & = \discRteEff\vk - \partial\Ham/\partial\netWorth = (\discRteEff-\rfreeEff_{t})\vk .
\end{aligned}\end{gathered}
```

Differentiating the first with respect to time gives {math}`\dot{\vk}/\vk = -\dot{\cNrm}(s,t)/\cNrm(s,t)`, so

```{math}
:label: eq:BFH-cdot

\dot{\cNrm}(s,t)/\cNrm(s,t) = \rfreeEff_{t}-\discRteEff = \rfree_{t}-\discRte .
```

Death raises the rate at which the consumer discounts the future and, through the annuity, the return on saving, by the same {math}`\diePrb`, and the two cancel. Each consumer's consumption grows at {math}`\rfree-\discRte`, as the infinitely lived household's does in [the decentralized RCK economy](#eq:cdotindiv) and as the [Keynes-Ramsey rule](#eq:cdotOc) has it, with logarithmic utility, {math}`\CRRA=1`, and without population or productivity growth. Finite horizons matter not for how any one consumer's consumption grows, but for how the economy's does, because consumers die and are replaced.

To find the level of consumption, write

```{math}
\PDVEff_{t}(\bullet) \equiv \int_{t}^{\infty} \bullet_{\tau}\,e^{-\int_{t}^{\tau}\rfreeEff_{\mu}\,d\mu}\,d\tau
```

for the present discounted value at date {math}`t` of a flow {math}`\bullet`, at the survival-inclusive interest rate; [the decentralized RCK economy's](#eq:DecRCK-ibc) {math}`\PDV` discounts at {math}`\rfree` instead. With a constant interest rate the discount factor is {math}`e^{-(\rfree+\diePrb)(\tau-t)}`: a payment at {math}`\tau` is discounted at {math}`\rfree+\diePrb`, because the consumer receives it only if still alive then. As in the decentralized economy, the no-Ponzi condition and the transversality condition, which together require {math}`\lim_{\tau\rightarrow\infty} e^{-\int_{t}^{\tau}\rfreeEff_{\mu}\,d\mu}\netWorth(s,\tau) = 0`, make the dynamic budget constraint {eq}`eq:BFH-dbc`, integrated forward, an intertemporal budget constraint that holds with equality,

```{math}
:label: eq:BFH-ibc

\PDVEff_{t}(\cNrm(s,\cdot)) = \netWorth(s,t) + \hNrm(s,t) :
```

the present discounted value of consumption equals net worth plus human wealth, {math}`\hNrm(s,t) = \PDVEff_{t}(\wage(s,\cdot))`, the present discounted value of noncapital income. This is the [perfect foresight model's human wealth](#eq:PFCRRA-yfin), at the survival-inclusive interest rate.

By {eq}`eq:BFH-cdot`, consumption at a later date is {math}`\cNrm(s,\tau) = \cNrm(s,t)e^{\int_{t}^{\tau}(\rfreeEff_{\mu}-\discRteEff)\,d\mu}`, so its present discounted value is

```{math}
\PDVEff_{t}(\cNrm(s,\cdot)) = \int_{t}^{\infty} \cNrm(s,t)e^{\int_{t}^{\tau}\rfreeEff_{\mu}\,d\mu}e^{-\discRteEff(\tau-t)}e^{-\int_{t}^{\tau}\rfreeEff_{\mu}\,d\mu}\,d\tau = \cNrm(s,t)\int_{t}^{\infty} e^{-\discRteEff(\tau-t)}\,d\tau = \cNrm(s,t)/\discRteEff ,
```

and the intertemporal budget constraint becomes the consumption function

```{math}
:label: eq:BFH-cFunc

\cNrm(s,t) = \discRteEff(\netWorth(s,t)+\hNrm(s,t)) .
```

:::{margin}
The interest rate still moves consumption, through human wealth: the [human wealth effect](#eq:dlogcdr) of the perfect foresight model.
:::

With logarithmic utility, the consumer spends a constant fraction of total wealth, net worth plus human wealth, whatever the path of interest rates, as in the [perfect foresight model](#eq:PFCRRA-cOfw) with logarithmic utility, whose marginal propensity to consume out of total wealth does not depend on the interest rate either. Here the fraction is the survival-inclusive time preference rate {math}`\discRteEff`: the shorter the horizon, the larger the share of wealth the consumer spends.

(sec:BFH-Aggregation)=
## Aggregation

An aggregate sums a variable over the cohorts alive. The cohort born at {math}`s` has {math}`\diePrb\Alive_{s}^{t} = \diePrb e^{-\diePrb(t-s)}` members left at {math}`t`, so aggregate consumption is

```{math}
\CNrm(t) = \int_{-\infty}^{t} \cNrm(s,t)\,\diePrb e^{-\diePrb(t-s)}\,ds ,
```

and aggregate net worth {math}`\NetWorth(t)`, human wealth {math}`\HNrm(t)` and noncapital income {math}`\Wage(t)` are defined in the same way. Since the population is one, each aggregate is also the average per person, and since nothing in this model grows, aggregates are not bold.

Every consumer spends the same fraction {math}`\discRteEff` of total wealth, so the consumption function {eq}`eq:BFH-cFunc` aggregates exactly:

```{math}
:label: eq:BFH-cagg

\CNrm(t) = \int_{-\infty}^{t} \discRteEff(\netWorth(s,t)+\hNrm(s,t))\,\diePrb e^{-\diePrb(t-s)}\,ds = \discRteEff(\NetWorth(t)+\HNrm(t)) .
```

Suppose that every consumer alive receives the same noncapital income, {math}`\wage(s,t) = \Wage(t)`; since the population is one, aggregate noncapital income is also {math}`\Wage(t)`. Every consumer then has the same human wealth, and aggregate human wealth,

```{math}
\HNrm(t) = \PDVEff_{t}(\Wage) = \int_{t}^{\infty} \Wage(\tau)\,e^{-\int_{t}^{\tau}\rfreeEff_{\mu}\,d\mu}\,d\tau ,
```

evolves as {math}`\dot{\HNrm} = \rfreeEff\HNrm - \Wage`. It discounts the economy's future noncapital income at {math}`\rfree+\diePrb`, not at {math}`\rfree`, because it counts only the income of the consumers alive now, not that of the generations not yet born.

Aggregate net worth changes for three reasons:

:::{margin}
This is [Leibniz's rule](https://en.wikipedia.org/wiki/Leibniz_integral_rule) for the derivative of an integral whose upper limit and integrand both depend on {math}`t`: the integrand at {math}`s=t`, plus the integral of the integrand's derivative, which includes the shrinking of each cohort as its members die.
:::

```{math}
:label: eq:BFH-Ndot

\dot{\NetWorth}(t) = \diePrb\netWorth(t,t) - \diePrb\NetWorth(t) + \int_{-\infty}^{t} \dot{\netWorth}(s,t)\,\diePrb e^{-\diePrb(t-s)}\,ds .
```

The first term is the net worth of the cohort being born, of size {math}`\diePrb`, which is zero, since consumers are born with none; the second is the net worth of the consumers dying at the moment, which passes to the insurance companies; and the last is the change in the net worth of everyone else. By {eq}`eq:BFH-dbc` the last is {math}`\rfreeEff\NetWorth + \Wage - \CNrm`, so {math}`\dot{\NetWorth} = \rfree\NetWorth + \Wage - \CNrm`: in the aggregate, the annuity payments to the living, {math}`\diePrb\NetWorth`, are exactly the net worth of the dying.

Collecting, and dropping the date arguments, the aggregate economy is described by

```{math}
:label: eq:BFH-aggregates

\begin{gathered}\begin{aligned}
  \CNrm & = \discRteEff(\NetWorth+\HNrm) ,
\\ \dot{\HNrm} & = \rfreeEff\HNrm - \Wage ,
\\ \dot{\NetWorth} & = \rfree\NetWorth + \Wage - \CNrm .
\end{aligned}\end{gathered}
```

Differentiating the first with respect to time, substituting the other two, and then substituting {math}`\HNrm = \CNrm/\discRteEff - \NetWorth` from the first gives

```{math}
\begin{gathered}\begin{aligned}
  \dot{\CNrm} & = \discRteEff(\rfree\NetWorth + \Wage - \CNrm + \rfreeEff\HNrm - \Wage)
\\ & = \discRteEff(\rfree\NetWorth + \rfreeEff(\CNrm/\discRteEff - \NetWorth) - \CNrm)
\\ & = (\rfreeEff-\discRteEff)\CNrm - \discRteEff(\rfreeEff-\rfree)\NetWorth ,
\end{aligned}\end{gathered}
```

and since {math}`\rfreeEff-\discRteEff = \rfree-\discRte` and {math}`\rfreeEff-\rfree = \diePrb`,

```{math}
:label: eq:BFH-aggCdot

\dot{\CNrm} = (\rfree-\discRte)\CNrm - \diePrb\discRteEff\NetWorth .
```

Each surviving consumer's consumption grows at {math}`\rfree-\discRte`, but aggregate consumption grows more slowly, because the population turns over. At each instant the dying, a fraction {math}`\diePrb` of the population drawn at random, consume {math}`\CNrm` on average, while the newborns who replace them, with the same human wealth but no net worth, consume only {math}`\discRteEff\HNrm = \CNrm - \discRteEff\NetWorth` each. The replacement lowers aggregate consumption by {math}`\diePrb\discRteEff\NetWorth` per unit of time: the last term.

:::{margin}
The same equation follows from aggregating consumption directly, as {eq}`eq:BFH-Ndot` aggregates net worth: {math}`\dot{\CNrm} = \diePrb\cNrm(t,t) - \diePrb\CNrm + (\rfree-\discRte)\CNrm`, with the newborns' consumption {math}`\cNrm(t,t) = \discRteEff\HNrm`.
:::

(sec:BFH-Phase)=
## The Phase Diagram

Production uses the RCK model's Cobb-Douglas technology, with no productivity growth and the one unit of labor the population supplies: output is {math}`\KNrm^{\kapShare}`, and capital depreciates at the rate {math}`\deprRte`. Factor markets are competitive, as in [the decentralized RCK economy](#eq:DecRCK-prices), so the interest rate is the net marginal product of capital and noncapital income is the wage:

```{math}
\rfree = \kapShare\KNrm^{\kapShare-1} - \deprRte, \qquad \Wage = (1-\kapShare)\KNrm^{\kapShare} .
```

Without a government, loans between consumers net out, so aggregate net worth is the capital stock, {math}`\NetWorth = \KNrm`, as in [the decentralized RCK economy](#eq:DecRCK-clear), where it reads {math}`\NetWorth = \kNrm`. The factor payments exhaust output net of depreciation, {math}`\rfree\KNrm + \Wage = \KNrm^{\kapShare} - \deprRte\KNrm`, so net worth accumulates as capital does in the RCK model,

```{math}
:label: eq:BFH-aggkdot

\dot{\KNrm} = \KNrm^{\kapShare} - \deprRte\KNrm - \CNrm ,
```

and {eq}`eq:BFH-aggCdot` becomes {math}`\dot{\CNrm} = (\kapShare\KNrm^{\kapShare-1} - \deprRte - \discRte)\CNrm - \diePrb\discRteEff\KNrm`. Consumption is constant where

```{math}
:label: eq:BFH-CdotEq0

\diePrb\discRteEff\KNrm = \CNrm(\kapShare\KNrm^{\kapShare-1} - \deprRte - \discRte) .
```

The left side is positive, so the {math}`\dot{\CNrm}=0` locus lies where the interest rate exceeds the time preference rate: to the left of the RCK model's steady state {math}`\Steady{\KNrm}_{\mathrm{RCK}}`, where {math}`\kapShare\KNrm^{\kapShare-1}-\deprRte = \discRte`, the [modified golden rule](#eq:RCK-modGoldenRule) without growth. Solved for consumption, the locus is {math}`\CNrm = \diePrb\discRteEff\KNrm/(\kapShare\KNrm^{\kapShare-1}-\deprRte-\discRte)`, which rises with {math}`\KNrm`: from the origin, where its numerator is zero and its denominator infinite, toward the vertical line at {math}`\Steady{\KNrm}_{\mathrm{RCK}}`, where its denominator is zero. So along the locus

```{math}
:label: eq:BFH-CdotEq0Limits

\lim_{\CNrm\rightarrow 0} \KNrm = 0, \qquad \lim_{\CNrm\rightarrow\infty} \KNrm = \Steady{\KNrm}_{\mathrm{RCK}} = \left(\frac{\kapShare}{\deprRte+\discRte}\right)^{\frac{1}{1-\kapShare}} .
```

As {math}`\diePrb \rightarrow 0`, the last term of {eq}`eq:BFH-aggCdot` vanishes, and the {math}`\dot{\CNrm}=0` locus becomes a vertical line at {math}`\Steady{\KNrm}_{\mathrm{RCK}}`, like the one in the RCK model's [phase diagram](#fig:RamseySSPlot). Finite horizons bend it to the left, the more so the shorter the horizon. The {math}`\dot{\KNrm}=0` locus, {math}`\CNrm = \KNrm^{\kapShare}-\deprRte\KNrm`, is [the RCK model's](#eq:RCK-kdotEq0) without growth: it rises to a peak at the [golden rule](#eq:RCK-goldenRule) {math}`\GoldRule{\KNrm}`, where {math}`\kapShare\KNrm^{\kapShare-1} = \deprRte` and the interest rate is zero, and falls after it.

{numref}`fig:BFH-Phase` shows the two loci. They cross at the steady state A, where the capital stock {math}`\Steady{\KNrm}` is below {math}`\Steady{\KNrm}_{\mathrm{RCK}}`, which is itself below the golden rule, and where the interest rate exceeds the time preference rate: by {eq}`eq:BFH-aggCdot`, {math}`(\Steady{\rfree}-\discRte)\Steady{\CNrm} = \diePrb\discRteEff\Steady{\KNrm} > 0`. The economy approaches A along the saddle path, as the RCK economy approaches its steady state along [its saddle path](#fig:RamseySaddlePlot).

:::{margin}
A is a saddle point. The slope of the {math}`\dot{\KNrm}=0` locus at A is the interest rate, {math}`\Steady{\rfree} = \kapShare\Steady{\KNrm}^{\kapShare-1}-\deprRte`. By {eq}`eq:BFH-CdotEq0`, the slope of the {math}`\dot{\CNrm}=0` locus is {math}`\CNrm/\KNrm - \rfree^{\prime}(\KNrm)\CNrm/(\rfree-\discRte)`, which exceeds {math}`\CNrm/\KNrm`, since {math}`\rfree^{\prime}(\KNrm) < 0`; and at A, {math}`\Steady{\CNrm}/\Steady{\KNrm} = \Steady{\KNrm}^{\kapShare-1}-\deprRte` exceeds {math}`\Steady{\rfree}`. The determinant of the system linearized at A, {math}`\Steady{\rfree}-\discRte` times the difference between the first slope and the second, is therefore negative, and its eigenvalues have opposite signs, as in [the RCK model](#fig:RamseySaddlePlot).
:::

Why does a finite horizon lower the capital stock? Finite-horizon consumers discount the future more than the infinitely lived household of the RCK model does, because they die and it does not. Within each life the annuity offsets the extra discounting, so each consumer's consumption grows at {math}`\rfree-\discRte`. But the consumers who hold the economy's net worth are continually replaced by newborns who hold none, and aggregate consumption can be constant only if each consumer's consumption rises, fast enough to offset that turnover. That takes an interest rate above the time preference rate, and so less capital than in the RCK model.

:::{figure} figures/BFHPhase.png
:name: fig:BFH-Phase

The Phase Diagram with Finite Horizons

Note: Aggregate consumption {math}`\CNrm` against the capital stock {math}`\KNrm`, with the values in [the RCK model's phase diagram](#fig:RamseySSPlot), {math}`\kapShare = 0.3`, {math}`\discRte = 0.02` and {math}`\deprRte = 0.08`, and {math}`\diePrb = 0.05`, a horizon of 20 years: with the 50-year horizon above, the steady state, {math}`\Steady{\KNrm} = 4.60`, would sit too close to {math}`\Steady{\KNrm}_{\mathrm{RCK}} = 4.80` for the gap to show. The {math}`\dot{\CNrm}=0` locus rises from the origin and bends up toward the dashed line at {math}`\Steady{\KNrm}_{\mathrm{RCK}}`, the {math}`\dot{\CNrm}=0` locus it becomes when {math}`\diePrb=0`. The hump-shaped {math}`\dot{\KNrm}=0` locus peaks at the golden rule, {math}`\GoldRule{\KNrm} = 6.61`. The loci cross at the steady state A, with capital {math}`\Steady{\KNrm} = 4.09` and consumption {math}`\Steady{\CNrm}`; the saddle path runs through A, and the gray arrows show the direction of motion in each region. The design is after {cite:t}`blanchardFinite`. Drawn by the [notebook](BlanchardFiniteHorizon.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=BlanchardFiniteHorizon.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb).
:::

(sec:BFH-Debt)=
## Government Debt

Now add a government, which spends {math}`\GovSpend` per unit of time and pays for it with lump-sum taxes of {math}`\TaxLev` per person or by issuing debt {math}`\Debt`, on which it pays the interest rate {math}`\rfree`. As in [the RCK model with government](#sec:RCKGov-Debt), its dynamic budget constraint is

```{math}
\dot{\Debt} = \GovSpend + \rfree\Debt - \TaxLev .
```

It cannot pay the interest on its debt by borrowing more forever, so it faces a no-Ponzi condition, {math}`\lim_{\tau\rightarrow\infty} e^{-\int_{t}^{\tau}\rfree_{\mu}\,d\mu}\Debt_{\tau} \leq 0` at any date {math}`t`; and it does not end with assets it never uses, so its no-Ponzi condition holds with equality:

```{math}
:label: eq:BFH-govDebtLimit

\lim_{\tau\rightarrow\infty} e^{-\int_{t}^{\tau}\rfree_{\mu}\,d\mu}\Debt_{\tau} = 0 .
```

Integrating the budget constraint forward with this condition gives the government's intertemporal budget constraint, as in [the RCK model with government](#eq:RCKGov-govibc): the present discounted value of its taxes, discounted at {math}`\rfree`, equals its debt plus the present discounted value of its spending.

Consider the following experiment. Until date 0 there is no government: {math}`\GovSpend=\Debt=\TaxLev=0`. At date 0, unexpectedly, the government issues debt {math}`\Debt` and rebates the proceeds to the public as a lump sum of {math}`\Debt` per person. It announces that from then on it will levy lump-sum taxes just large enough to pay the interest on the debt, {math}`\TaxLev = \rfree\Debt`, so that {math}`\dot{\Debt}=0` forever, and it never spends anything else.

The policy changes the consumers' side of the economy in two ways. Government bonds are a second asset, which must pay the same return as capital, so aggregate net worth now includes them, {math}`\NetWorth = \KNrm+\Debt`, as a household's does in [the RCK model with government](#sec:RCKGov-Debt). And net of taxes, noncapital income is {math}`\Wage-\TaxLev`, and human wealth is {math}`\HNrm - \PDVEff_{t}(\TaxLev)`: human wealth {math}`\HNrm = \PDVEff_{t}(\Wage)`, as before, less the present discounted value of the taxes the consumers alive will pay. The aggregate economy {eq}`eq:BFH-aggregates` becomes

```{math}
:label: eq:BFH-debtSystem

\begin{gathered}\begin{aligned}
  \CNrm & = \discRteEff(\KNrm + \Debt + \HNrm - \PDVEff_{t}(\TaxLev)) ,
\\ \frac{d}{dt}(\HNrm - \PDVEff_{t}(\TaxLev)) & = \rfreeEff(\HNrm - \PDVEff_{t}(\TaxLev)) - (\Wage-\TaxLev) ,
\\ \dot{\NetWorth} & = \rfree(\KNrm+\Debt) + \Wage - \TaxLev - \CNrm ,
\end{aligned}\end{gathered}
```

so net worth now accumulates out of income net of taxes, {math}`\rfree(\KNrm+\Debt) + \Wage - \TaxLev`, minus consumption. The steps that led to {eq}`eq:BFH-aggCdot`, with {math}`\KNrm+\Debt` for {math}`\NetWorth`, {math}`\Wage-\TaxLev` for {math}`\Wage` and {math}`\HNrm-\PDVEff_{t}(\TaxLev)` for {math}`\HNrm`, go through unchanged, the taxes canceling as noncapital income did. Since {math}`\dot{\Debt}=0`, capital accumulates as {math}`\dot{\KNrm} = \dot{\NetWorth} = \rfree\KNrm + \Wage - \CNrm + (\rfree\Debt - \TaxLev)`, and the last term is zero because the taxes pay exactly the interest on the debt. So

```{math}
:label: eq:BFH-debtDynamics

\begin{gathered}\begin{aligned}
  \dot{\CNrm} & = (\rfree-\discRte)\CNrm - \diePrb\discRteEff(\KNrm+\Debt) ,
\\ \dot{\KNrm} & = \KNrm^{\kapShare} - \deprRte\KNrm - \CNrm .
\end{aligned}\end{gathered}
```

The debt leaves the {math}`\dot{\KNrm}=0` locus where it was, but at every combination of capital and consumption it lowers {math}`\dot{\CNrm}` by {math}`\diePrb\discRteEff\Debt`: a point that was on the {math}`\dot{\CNrm}=0` locus now has {math}`\dot{\CNrm} = -\diePrb\discRteEff\Debt`. Since {math}`\dot{\CNrm}` rises with consumption wherever the interest rate exceeds {math}`\discRte`, restoring {math}`\dot{\CNrm}=0` at a given capital stock takes more consumption, so the locus shifts up, or equivalently to the left, as {numref}`fig:BFH-DebtPhase` shows. The new steady state A′, with capital {math}`\Steady{\KNrm}_{\Debt}` and consumption {math}`\Steady{\CNrm}_{\Debt}`, has less capital and a higher interest rate than A. Since A was below the golden rule, its interest rate being above {math}`\discRte`, which is positive, A′ also has less consumption.

:::{figure} figures/BFHDebtPhase.png
:name: fig:BFH-DebtPhase

Government Debt in the Phase Diagram

Note: The economy of {numref}`fig:BFH-Phase`, with {math}`\diePrb = 0.05`, zoomed on its steady states. Before the policy, the {math}`\dot{\CNrm}=0` locus (solid) crosses the {math}`\dot{\KNrm}=0` locus at the steady state A, with capital {math}`\Steady{\KNrm}` and consumption {math}`\Steady{\CNrm}`. A debt of half of output at A, {math}`\Debt = 0.76`, shifts the {math}`\dot{\CNrm}=0` locus up and to the left (dashed). At the new steady state A′, capital {math}`\Steady{\KNrm}_{\Debt}` is 2.5 percent below {math}`\Steady{\KNrm}`, consumption {math}`\Steady{\CNrm}_{\Debt}` is below {math}`\Steady{\CNrm}`, and the interest rate is 3.39 percent rather than 3.19. At date 0 consumption jumps from A up onto the saddle path with the debt, and capital and consumption then fall along it to A′ (purple). With the 50-year horizon, {math}`\diePrb = 0.02`, capital would fall only 0.7 percent. The design is after {cite:t}`blanchardFinite`. Drawn by the [notebook](BlanchardFiniteHorizon.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=BlanchardFiniteHorizon.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb).
:::

Why does the debt matter? Not because consumers hold the bonds: with {math}`\diePrb=0` they would hold them too, yet the term in {math}`\Debt` would vanish, and the debt would change nothing, as Ricardian equivalence says it must in [the RCK model with government](#sec:RCKGov-Debt). It matters because the consumers alive at date 0 will pay only part of the taxes that service it.

The government's intertemporal budget constraint makes the taxes worth the debt at the interest rate {math}`\rfree`, {math}`\PDV_{0}(\TaxLev) = \Debt`, with {math}`\PDV`, as in [the RCK model with government](#eq:RCKGov-govibc), the present discounted value at {math}`\rfree`. But the consumers alive discount the taxes at {math}`\rfree+\diePrb`, because they will pay them only while alive, so to them the taxes are worth less than the debt, {math}`\PDVEff_{0}(\TaxLev) < \PDV_{0}(\TaxLev) = \Debt`: with a constant interest rate, {math}`\PDVEff_{0}(\rfree\Debt) = \rfree\Debt/(\rfree+\diePrb)`. The bonds then raise their wealth, net of the taxes they will pay, by {math}`\diePrb\Debt/(\rfree+\diePrb)`, which is zero when {math}`\diePrb=0`. The rest of the taxes falls on generations not yet born, who will pay them without ever having held the bonds. That is the term {math}`-\diePrb\discRteEff\Debt` in {eq}`eq:BFH-debtDynamics`: the consumers who die hold bonds, while the newborns who replace them hold none but owe the same taxes. The policy transfers resources from future generations to the consumers alive today, and there are no altruistic links, such as bequests, that would lead today's consumers to offset the transfer by saving more on behalf of future generations. So government bonds are net wealth, unlike in [the RCK model with government](#eq:famibc), and Ricardian equivalence fails.

{numref}`fig:BFH-DebtConsumption` shows the path of aggregate consumption. Before date 0 the economy is in its steady state A, with consumption {math}`\Steady{\CNrm}`. At date 0 the capital stock cannot jump, but consumption can: it jumps up, onto the saddle path that leads to A′, because the policy transfers resources from future to current generations. The higher consumption runs the capital stock down and raises the interest rate, and consumption falls, below {math}`\Steady{\CNrm}`, approaching asymptotically the new, lower steady-state level {math}`\Steady{\CNrm}_{\Debt}`.

The generations alive at date 0 gain: they receive the bonds and will pay only part of the taxes that service them. The generations born later receive no bonds, pay the taxes all their lives, and work with less capital, at a lower wage.

:::{figure} figures/BFHDebtConsumption.png
:name: fig:BFH-DebtConsumption

Aggregate Consumption after the Debt Is Issued

Note: The economy and the debt of {numref}`fig:BFH-DebtPhase`. Consumption is at its steady-state level {math}`\Steady{\CNrm}`, at A, until the debt is issued at date 0. It then jumps up 1.2 percent, falls back through {math}`\Steady{\CNrm}` about 12 years later, and approaches the new steady-state level {math}`\Steady{\CNrm}_{\Debt}`, at A′, 0.28 percent below {math}`\Steady{\CNrm}`; the dashed lines mark the two levels. With the 50-year horizon, {math}`\diePrb = 0.02`, consumption would jump 0.34 percent, fall back through its old level about 15 years later, and settle 0.06 percent below it. Drawn by the [notebook](BlanchardFiniteHorizon.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=BlanchardFiniteHorizon.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb).
:::

(sec:BFH-FallingIncome)=
## Income That Falls with Age

Suppose instead that each consumer's noncapital income falls with age: it grows over a life at the rate {math}`\PermGroRte < 0`, so that a consumer born at {math}`s` earns, at date {math}`t`,

```{math}
\wage(s,t) = \left(\frac{\diePrb-\PermGroRte}{\diePrb}\right)\Wage(t)e^{\PermGroRte(t-s)} .
```

The factor in parentheses is a newborn's income relative to the average, and it keeps aggregate noncapital income at {math}`\Wage(t)`: aggregating over the cohorts alive, {math}`\int_{-\infty}^{t} \wage(s,t)\,\diePrb e^{-\diePrb(t-s)}\,ds = \Wage(t)`. A consumer's human wealth is then

```{math}
\hNrm(s,t) = \PDVEff_{t}(\wage(s,\cdot)) = \left(\frac{\diePrb-\PermGroRte}{\diePrb}\right)e^{\PermGroRte(t-s)}\int_{t}^{\infty} \Wage(\tau)\,e^{-\int_{t}^{\tau}(\rfreeEff_{\mu}-\PermGroRte)\,d\mu}\,d\tau ,
```

and aggregating it in the same way gives

```{math}
:label: eq:BFH-fallingH

\HNrm(t) = \int_{t}^{\infty} \Wage(\tau)\,e^{-\int_{t}^{\tau}(\rfreeEff_{\mu}-\PermGroRte)\,d\mu}\,d\tau, \qquad \dot{\HNrm} = (\rfree+\diePrb-\PermGroRte)\HNrm - \Wage .
```

As {cite:t}`blanchardFinite` shows, falling income is equivalent to discounting future noncapital income at a rate higher by {math}`-\PermGroRte`: at {math}`\rfree+\diePrb-\PermGroRte`, the perfect foresight model's {math}`\rfree-\PermGroRte` with death added. Human wealth is finite when {math}`\rfree+\diePrb > \PermGroRte`, the [finite human wealth condition](#eq:FHWCPF) with death added, which holds whenever {math}`\rfree+\diePrb > 0`, since {math}`\PermGroRte < 0`.

Every consumer still spends {math}`\discRteEff` of total wealth, and newborns still have no net worth, so the aggregate consumption function {eq}`eq:BFH-cagg` and the accumulation of net worth, {math}`\dot{\NetWorth} = \rfree\NetWorth + \Wage - \CNrm`, are unchanged; only {math}`\dot{\HNrm}` is different. The steps that led to {eq}`eq:BFH-aggCdot`, with {math}`\rfreeEff-\PermGroRte` for {math}`\rfreeEff` in {math}`\dot{\HNrm}`, and with {math}`\NetWorth = \KNrm`, now give

```{math}
:label: eq:BFH-fallingDynamics

\begin{gathered}\begin{aligned}
  \dot{\CNrm} & = (\kapShare\KNrm^{\kapShare-1}-\deprRte-\PermGroRte-\discRte)\CNrm - (\diePrb-\PermGroRte)\discRteEff\KNrm ,
\\ \dot{\KNrm} & = \KNrm^{\kapShare} - \deprRte\KNrm - \CNrm ,
\end{aligned}\end{gathered}
```

which, with {math}`\PermGroRte=0`, are {eq}`eq:BFH-aggCdot` and {eq}`eq:BFH-aggkdot`. Consumption is constant where

```{math}
:label: eq:BFH-fallingCdotEq0

(\kapShare\KNrm^{\kapShare-1}-\deprRte-\PermGroRte-\discRte)\CNrm = (\diePrb-\PermGroRte)\discRteEff\KNrm .
```

The right side is positive, so the locus lies where the interest rate exceeds {math}`\discRte+\PermGroRte`. The interest rate falls toward {math}`-\deprRte` as the capital stock grows, so if {math}`\discRte+\PermGroRte > -\deprRte`, some capital stock has the interest rate {math}`\discRte+\PermGroRte`, and as {math}`\CNrm \rightarrow \infty` along the locus the first factor on the left must go to zero: the locus approaches the vertical line where

```{math}
:label: eq:BFH-fallingAsymptote

\rfree = \kapShare\KNrm^{\kapShare-1}-\deprRte = \discRte+\PermGroRte .
```

If income falls faster still, the locus has no vertical asymptote and rises without bound only as the capital stock does.

The steady-state interest rate exceeds {math}`\discRte+\PermGroRte`, so it can be negative only if {math}`\PermGroRte < -\discRte`, a necessary condition but not a sufficient one. However fast income falls, the steady-state interest rate stays above {math}`\kapShare(\discRte+\diePrb)-(1-\kapShare)\deprRte`, which it approaches as {math}`\PermGroRte \rightarrow -\infty` and nearly all income arrives at birth. So it can be negative only if depreciation is large enough as well, {math}`(1-\kapShare)\deprRte > \kapShare(\discRte+\diePrb)`. With the values in [the RCK model's phase diagram](#fig:RamseySSPlot), {math}`\kapShare = 0.3`, {math}`\discRte = 0.02` and {math}`\deprRte = 0.08`, and the 50-year horizon above, {math}`\diePrb = 0.02`, it is: the bound is −4.4 percent, and the steady-state interest rate turns negative once income falls by about 3 percent a year with age. {numref}`fig:BFH-FallingIncome` shows such a case, with income falling 5 percent a year: the {math}`\dot{\CNrm}=0` locus crosses the {math}`\dot{\KNrm}=0` locus at the steady state A, to the right of its peak, the golden rule, where the interest rate is negative. Consumers save while young for the years when their income will be lower, a life-cycle motive for saving that the model with flat income lacks, and with income falling fast enough they can save so much that the capital stock exceeds not only {math}`\Steady{\KNrm}_{\mathrm{RCK}}` but the golden rule.

The economy is then dynamically inefficient, as the [Diamond OLG model](#sec:OLGModel) can be: its interest rate is below its growth rate, which in this model is zero. To the right of the peak, {math}`\rfree = \kapShare\KNrm^{\kapShare-1}-\deprRte < 0`, so output net of depreciation, {math}`\KNrm^{\kapShare}-\deprRte\KNrm`, rises as the capital stock falls: by holding less capital, the economy could consume more at every date, and so could make every generation better off. Falling income is a way to give this model the life-cycle motive for saving that drives the Diamond model, whose consumers earn nothing when old. In such an economy the debt experiment above is all the more interesting: debt still crowds out capital, so it could rescue an economy with too much capital from dynamic inefficiency. (With falling income, and the same tax on everyone, the debt's term in {math}`\dot{\CNrm}` is no longer the {math}`-\diePrb\discRteEff\Debt` of {eq}`eq:BFH-debtDynamics`; at a constant interest rate it is {math}`-\diePrb\discRteEff\Debt(\rfree+\diePrb-\PermGroRte)/(\rfree+\diePrb)`, still negative while {math}`\rfree+\diePrb > 0`.)

:::{margin}
While the interest rate is negative, the tax that pays the interest on the debt, {math}`\rfree\Debt`, is negative: a transfer. A constant debt satisfies the government's [condition on its debt at infinity](#eq:BFH-govDebtLimit) only if the new steady-state interest rate is positive, that is, only if the debt is large enough to bring the capital stock below the golden rule; otherwise its present discounted value grows without bound.
:::

:::{figure} figures/BFHFallingIncome.png
:name: fig:BFH-FallingIncome

The Phase Diagram When Income Falls with Age

Note: Aggregate consumption {math}`\CNrm` against the capital stock {math}`\KNrm`, with the 50-year horizon, {math}`\diePrb = 0.02`, the other values of {numref}`fig:BFH-Phase`, and income falling 5 percent a year with age, {math}`\PermGroRte = -0.05`, so that newborns earn 3.5 times the average. The {math}`\dot{\CNrm}=0` locus rises from the origin toward the dashed line where {math}`\rfree = \discRte+\PermGroRte = -0.03`, {eq}`eq:BFH-fallingAsymptote`, at {math}`\KNrm = 12.9`, and crosses the hump-shaped {math}`\dot{\KNrm}=0` locus at the steady state A, to the right of the hump's peak, the golden rule {math}`\GoldRule{\KNrm} = 6.61`. The interest rate is positive to the left of the golden rule and negative to its right: at A, with capital {math}`\Steady{\KNrm} = 8.20`, it is −1.1 percent. The RCK model's steady state, {math}`\Steady{\KNrm}_{\mathrm{RCK}} = 4.80`, is further left. The saddle path runs through A, and the gray arrows show the direction of motion in each region. The design is after {cite:t}`blanchardFinite`. Drawn by the [notebook](BlanchardFiniteHorizon.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=BlanchardFiniteHorizon.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/BlanchardFiniteHorizon/BlanchardFiniteHorizon.ipynb).
:::

