(sec:StickyExpectationsC)=

# Sticky Expectations and Consumption Dynamics

Consider a consumer subject to the dynamic budget constraint

```{math}
\bLev_{t+1} = (\bLev_{t}+\yLev_{t}-\cLev_{t})\Rfree
```

where {math}`\bLev_{t}` is beginning-of-period bank balances, {math}`\yLev_{t}` is current labor income, and {math}`\Rfree=(1+\rfree)` is the constant interest factor. Actual labor income {math}`\yLev` is permanent labor income {math}`\pLevBF` modified by a transitory shock factor {math}`\tShkEmp`:

```{math}
\yLev_{t+1} = \pLevBF_{t+1} \tShkEmp_{t+1}
```

where {math}`\Ex_{t}[\tShkEmp_{t+n}]=1~\forall~n>0`. Permanent labor income grows by a predictable factor {math}`\WGro` from period to period:

**PermShks=true:**

```{math}
\pLevBF_{t+1} = \WGro \pLevBF_{t}\psi_{t+1},
```

**PermShks=false:**

```{math}
\pLevBF_{t+1} = \WGro \pLevBF_{t},
```

so that the expected present discounted value of permanent labor income ("human wealth") for an infinite-horizon consumer is

```{math}
\hLev_{t} = \left(\frac{\pLevBF_{t}}{1-\WGro/\Rfree}\right).
```

We will assume that the consumer behaves according to the consumption rule

```{math}
:label: eq:DeatonPIH

\cLev_{t} = \underbrace{(\bLev_{t}+(\tShkEmp_{t}-1)\pLevBF_{t}+\hLev_{t})}_{\equiv \wAllLev_{t}}\underbrace{(\rfree/\Rfree)}_{\equiv \MPC},
```

where {math}`\MPC` is the "marginal propensity to consume" out of total wealth {math}`\wAllLev`.[^pih-derivation]

[^pih-derivation]: This is the optimal consumption function for a utility-maximizing consumer with {math}`\Rfree \Discount = 1` if that consumer has quadratic utility ({cite:t}`hallRandomWalk`) or if the consumer has CRRA utility and perfect foresight and anticipates {math}`\tShkEmp_{t+n}=\pShk_{t+n}=1~\forall~n>0`. See the [](#sec:ConsumptionFunction) for a derivation of this consumption function under quadratic utility, and [](#sec:PerfForesightCRRA) for the derivation in the perfect foresight CRRA case. {cite:t}`deatonUnderstandingC` argues that the "Permanent Income Hypothesis" should be **defined** as the hypothesis that consumption is determined according to {eq}`eq:DeatonPIH`; but this differs sharply from {cite:t}`friedmanATheory`'s definition, and has not become universally accepted.

Under these circumstances, the [](#sec:RandomWalk) shows that consumption will follow a random walk,

```{math}
:label: eq:StickyE-rwc

\Delta \cLev_{t+1} = \error_{t+1}, \quad \Ex_{t}[\error_{t+n}] = 0 ~\forall~n>0.
```

Now assume that the economy is populated by a set of measure one of consumers indexed by a superscript {math}`i` distributed uniformly along the unit interval. Per capita values of all variables, designated by the upper case, are the integral over all individuals in the economy, as in the [](#sec:Aggregation), so that

```{math}
\CLev_{t} = \int_{0}^{1} \cLev_{t}^{i} di = \int_{0}^{1} (\rfree/\Rfree)  \wAllLev_{t}^{i} di = \WAllLev_{t} \MPC.
```

This equation implies that an aggregate version of equation {eq}`eq:StickyE-rwc` holds,[^aggregation-linearity]

[^aggregation-linearity]: The crucial feature of the model that allows us to aggregate analytically is the linearity of the consumption rule in {math}`p, b,` and {math}`\TShkEmp`.

```{math}
\Delta \CLev_{t+1} = \error_{t+1}.
```

In principle, we could allow each individual in this economy to experience a different transitory shock (and, **PermShks=true:** permanent shock) from every other individual in each period. However, for our purposes it is useful to assume that everyone experiences the same shocks in a given period; that is {math}`\tShkEmp_{t}^{i}=\TShkEmp_{t}~\forall~t` (**PermShks=true:** and {math}`\psi_{t}^{i} = \Psi_{t}~\forall~t`).

Assuming (here and henceforth) that the growth factor for permanent income is {math}`\WGro=1`, the figures below show the path of consumption and bank balances (the solid dots) for an economy populated by omniscient consumers who in periods {math}`t-n` for {math}`n>0` had experienced {math}`\TShkEmp_{t-n}=1` (**PermShks=true:** {math}`=\Psi_{t-n}`); that is, this economy has had no shocks to income in the past. (For convenience, the consumer is assumed to have arrived in period {math}`t` with {math}`\BLev_{t}=0`). In period {math}`t` the consumer draws {math}`\TShkEmp_{t}=2` (**PermShks=true:** and {math}`\Psi_{t}=1`); thereafter {math}`\TShkEmp_{t+n}=1` (**PermShks=true:** {math}`\Psi_{t+n}=`). The figures show {math}`\CLev_{t-2},\CLev_{t-1},\CLev_{t},\Ex_{t}[\CLev_{t+1}],\Ex_{t}[\CLev_{t+2}],\ldots` and the corresponding values for {math}`\BLev`.

:::{figure} /sources/consumption/StickyExpectationsC/LaTeX/Figures/cPlot.png
:name: fig:aftershock

Path of {math}`\CLev` after a shock {math}`\TShkEmp_{t}=2`, Omniscient Consumers
:::

:::{figure} /sources/consumption/StickyExpectationsC/LaTeX/Figures/bPlot.png
:name: fig:epidshock

Path of {math}`\BLev` after a shock {math}`\TShkEmp_{t}=2`, Omniscient Consumers
:::

Now suppose that not every consumer updates expectations in every period. Instead, expectations are "sticky": each consumer updates with probability {math}`\Pi` in each period. Whether the consumer at location {math}`i` updates in period {math}`t` is determined by the realization of the dichotomous random variable

```{math}
\pi^{i}_{t} =
\begin{cases}
   1 & \text{if consumer $i$ updates in period $t$}
\\ 0 & \text{if consumer $i$ does not update in period $t$}  ,
\end{cases}
```

and each period's updaters are chosen randomly such that a constant proportion {math}`\Pi` update in each period:

```{math}
\Ex_{t}^{i}[\pi^{i}_{t+1}] = \Pi~\forall~t, \quad
\int_{0}^{1} \pi^{i}_{\tau} di = \Pi ~\forall~\tau.
```

It will also be convenient to define the date of consumer {math}`i`'s most recent update; we call this object {math}`\tau^{i}_{t}`. We designate the value of a variable {math}`\bullet` at date {math}`t` for a consumer who last updated his expectations at date {math}`t-n` by {math}`\bullet_{t|=t-n}`, where the part of the subscript following {math}`|` indicates criteria that must be matched by the consumer's (or group's) {math}`\tau`. To illustrate, consider a consumer who updated his expectations most recently in period {math}`t-3` so that {math}`n(i)=3`. This consumer's actual consumption in period {math}`t` will be {math}`\cLev^{i}_{t} = \cLev_{t-3|=t-3}`, the level of consumption that was chosen in period {math}`t-3` given beliefs at that time.

We are assuming that the probability of adjusting one's expectations is independent of the level of income or wealth; therefore, the average levels of wealth and income among those consumers who adjust their expectations this period will be the same as the average levels of wealth and income in the economy as a whole. This independence assumption is crucial for aggregation: it ensures that the subset of consumers who update in any period is representative of the population.

We need a notation to represent sets of consumers defined by the period of their most recent update. We denote such a set by the condition on {math}`\tau^{i}_{t}`; for example, the set of consumers whose most recent update, as of date {math}`t`, was prior to period {math}`t-1` would be {math}`\mathcal{T} = \{\tau^{i}_{t} < t-1\}`. We denote the per-capita value of a variable {math}`\bullet`, among consumers in a set {math}`\mathcal{T}` as of date {math}`t`, by {math}`\bullet_{t|\mathcal{T}}`. Dropping the {math}`i` superscripts to reduce clutter, per-capita consumption among households who have updated in period {math}`t` is therefore

```{math}
\CLev_{t|\tau_{t}=t} = \Pi^{-1} \int_{0}^{1} \pi_{t} \cLev_{t} di.
```

Dropping the {math}`i` superscript for notational simplicity, the level of consumption per capita that would prevail if all consumers were to update in period {math}`t` is {math}`\CLev_{t|=t} = \int_{0}^{1} \cLev_{t|=t} di`. But since the set of consumers who updated was randomly selected from the population, the average level of consumption-per-capita for the updaters must equal the average level of consumption-per-capita that would characterize the population as a whole if everyone in the economy were to update. This is the key step that allows aggregation to work analytically.

In periods when expectations are not updated, the consumer continues to spend the same amount as in the most recent period when his expectations **were** updated.[^random-walk-assumption] If the economy is large the proportion of consumers who update their expectations every period will be {math}`\Pi`.[^non-updaters-integral] Average consumption among those who are not updating in the current period (for whom {math}`1-\pi_{t}=1`) is then

[^random-walk-assumption]: This makes sense because under the {cite:t}`hallRandomWalk` assumptions the expected change in consumption is zero under our assumption that {math}`\Rfree \Discount=1`.

[^non-updaters-integral]: For consumers who are not updating at date {math}`t`, {math}`\cLev_{t} > 0` but {math}`\pi_{t} = 0`, so the integral produces the sum of consumption among only those {math}`i` who are updating in period {math}`t`.

```{math}
\CLev_{t|\tau_{t} < t} = (1-\Pi)^{-1} \int_{0}^{1} (1-\pi_{t}) \cLev_{t} di = \CLev_{t-1}
```

because consumption per capita among those who are not updating in the current period is (by assumption) identical to their consumption per capita in the prior period, which must match aggregate consumption per capita in the prior period because the set who do **not** update today is randomly selected from the {math}`t-1` population.

Now note that

```{math}
:label: eq:DCtp1

\CLev_{t+1} = \Pi \CLev_{t+1|\tau_{t+1}=t+1} + (1-\Pi) \overbrace{\CLev_{t+1|\tau_{t+1}<t+1}}^{=\CLev_{t}}, \quad
\Delta \CLev_{t+1} = \Pi (\CLev_{t+1|\tau_{t+1}=t+1}-\CLev_{t|\tau_{t}=t}) + (1-\Pi) \Delta \CLev_{t}
```

and

```{math}
:label: eq:DCvsCmC

\CLev_{t} = \Pi \CLev_{t|\tau_{t}=t} + (1-\Pi) \CLev_{t-1}, \quad
\Delta \CLev_{t} = \Pi (\CLev_{t|\tau_{t}=t}-\CLev_{t-1}) = \Pi (\CLev_{t|\tau_{t}=t}-\CLev_{t}+\CLev_{t}-\CLev_{t-1}), \quad
(1-\Pi) \Delta \CLev_{t} = \Pi (\CLev_{t|\tau_{t}=t}-\CLev_{t})
```

while, defining {math}`\hat{\TShkEmp}=\TShkEmp-1` (**PermShks=true:** and {math}`\hat{\Psi}=\Psi-1`),

**PermShks=true:**

```{math}
:label: eq:DCtp1Gtp1

\begin{aligned}
\CLev_{t+1|\tau_{t+1}=t+1} & = \left(\overbrace{(\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t})\Rfree}^{=\BLev_{t+1}}+\hat{\TShkEmp}_{t+1}\right)\MPC+1+\hat{\Psi}_{t+1}
\\ \CLev_{t+1|\tau_{t+1}=t+1} & = \left((\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t}+\CLev_{t|\tau_{t}=t}-\CLev_{t|\tau_{t}=t})\Rfree+\hat{\TShkEmp}_{t+1}\right)\MPC+1+\hat{\Psi}_{t+1}
\\ & = \underbrace{\left((\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t|\tau_{t}=t})\Rfree+\hat{\TShkEmp}_{t+1}\right)\MPC+1+\hat{\Psi}_{t+1}}_{=\Ex_{t}[\CLev_{t+1|\tau_{t}=t}]+\hat{\TShkEmp}_{t+1}\MPC+\hat{\Psi}_{t+1}}+(\CLev_{t|\tau_{t}=t}-\CLev_{t})\Rfree\MPC
\\ & = \CLev_{t|\tau_{t}=t}+\hat{\TShkEmp}_{t+1}\MPC+\hat{\Psi}_{t+1}+(\CLev_{t|\tau_{t}=t}-\CLev_{t})\MPC \Rfree
\end{aligned}
```

**PermShks=false:**

```{math}
\begin{aligned}
\CLev_{t+1|\tau_{t+1}=t+1} & = \left(\overbrace{(\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t})\Rfree}^{=\BLev_{t+1}}+\hat{\TShkEmp}_{t+1}\right)\MPC+1
\\ \CLev_{t+1|\tau_{t+1}=t+1} & = \left((\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t}+\CLev_{t|\tau_{t}=t}-\CLev_{t|\tau_{t}=t})\Rfree+\hat{\TShkEmp}_{t+1}\right)\MPC+1
\\ & = \underbrace{\left((\BLev_{t}+\hat{\TShkEmp}_{t}-\CLev_{t|\tau_{t}=t})\Rfree+\hat{\TShkEmp}_{t+1}\right)\MPC+1}_{=\Ex_{t}[\CLev_{t+1|\tau_{t}=t}]+\hat{\TShkEmp}_{t+1}\MPC}+(\CLev_{t|\tau_{t}=t}-\CLev_{t})\Rfree\MPC
\\ & = \CLev_{t|\tau_{t}=t}+\hat{\TShkEmp}_{t+1}\MPC+(\CLev_{t|\tau_{t}=t}-\CLev_{t})\MPC \Rfree
\end{aligned}
```

where {eq}`eq:DCtp1Gtp1` follows its predecessor since, among consumers who have updated in period {math}`t`, the random walk proposition says that {math}`\Ex_{t}[\CLev_{t+1|\tau_{t}=t}]=\CLev_{t,\tau_{t}=t}`. Subtracting {math}`\CLev_{t|\tau_{t}=t}` from both sides of {eq}`eq:DCtp1Gtp1` and substituting the result into {eq}`eq:DCtp1`, and using {eq}`eq:DCvsCmC` to substitute for {math}`\Pi(\CLev_{t|\tau_{t}=t}-\CLev_{t})`, yields

**PermShks=true:**

```{math}
\begin{aligned}
\Delta \CLev_{t+1} & = (1-\Pi) \Delta \CLev_{t}+
\underbrace{\Pi (\CLev_{t|\tau_{t}=t}-\CLev_{t})}_{=(1-\Pi)\Delta \CLev_{t}}\underbrace{\Rfree\MPC}_{=\rfree} + \underbrace{\Pi\left(\hat{\TShkEmp}_{t+1}\MPC+\hat{\Psi}_{t+1}\right)}_{\equiv \xi_{t+1}}
\\ & = (1-\Pi) \Delta \CLev_{t}+ (1-\Pi) \rfree \Delta \CLev_{t} + \xi_{t+1}
\\ & = (1-\Pi) \Rfree \Delta \CLev_{t} + \xi_{t+1}
\end{aligned}
```

**PermShks=false:**

```{math}
\begin{aligned}
\Delta \CLev_{t+1} & = (1-\Pi) \Delta \CLev_{t}+
\underbrace{\Pi (\CLev_{t|\tau_{t}=t}-\CLev_{t})}_{=(1-\Pi)\Delta \CLev_{t}}\underbrace{\Rfree\MPC}_{=\rfree} + \underbrace{\Pi\left(\hat{\TShkEmp}_{t+1}\MPC\right)}_{\equiv \xi_{t+1}}
\\ & = (1-\Pi) \Delta \CLev_{t}+ (1-\Pi) \rfree \Delta \CLev_{t} + \xi_{t+1}
\\ & = (1-\Pi) \Rfree \Delta \CLev_{t} + \xi_{t+1}
\end{aligned}
```

where {math}`\xi` is a white noise variable ({math}`\Ex_{t}[\xi_{t+n}]=0~\forall~n>0`).

We are finally in position to show how aggregate consumption and wealth would respond in this economy to a transitory positive shock to aggregate labor income like the one considered above for the omniscient model.

Consider the case of a positive shock of size {math}`\hat{\TShkEmp}_{t}=1`, as before. In the first period consumption rises only by {math}`\Pi \MPC`, rather than the full amount corresponding to the permanent income associated with the new level of wealth. Therefore aggregate wealth in period {math}`t+1` will be greater than it would have been in the omniscient model. Similarly for all subsequent periods. Thus, in contrast with the omniscient model, the sluggish adjustment of consumption to the shock means that the shock has a permanent effect on the level of aggregate wealth, and therefore on the level of aggregate consumption. (The figures below depict the results.)

:::{figure} /sources/consumption/StickyExpectationsC/LaTeX/Figures/StickyExpectationsCc.png
:name: fig:StickyExpectationsCc

Path of {math}`\CLev` after a shock {math}`\TShkEmp_{t}=2`; Sticky Expectations in Red/Gray
:::

:::{figure} /sources/consumption/StickyExpectationsC/LaTeX/Figures/StickyExpectationsCb.png
:name: fig:StickyExpectationsCb

Path of {math}`\BLev` after a shock {math}`\TShkEmp_{t}=2`; Sticky Expectations in Red/Gray
:::

The sticky expectations model says that consumption growth today can be statistically related to any variable that is related to lagged consumption growth. In particular, if lagged consumption growth is related to lagged income growth (as it certainly will be), then there **should** be a statistically significant effect of lagged income growth on current consumption growth if expectations are sticky.

If the model derived here could be taken literally, it would suggest estimating an equation of the form

```{math}
:label: eq:eststick

\Delta \CLev_{t+1} = \alpha_{0}+\alpha_{1} \Delta \CLev_{t} + \varepsilon_{t+1}
```

and interpreting the coefficient {math}`\alpha_{1}` as a measure of {math}`\Rfree (1-\Pi)`.

However, if there is potential measurement error in {math}`\CLev_{t}` the coefficient obtained from estimating {eq}`eq:eststick` would be biased toward zero for standard errors-in-variables reasons (just as regressing consumption on actual income yields a downward-biased estimate of the response of consumption to permanent income), which means that the estimate of {math}`\Pi` would be biased toward 1 (i.e. the omniscient model in which everyone adjusts all the time). Under these circumstances, direct estimation of {eq}`eq:eststick` would not be a reliable way to estimate {math}`\Pi`.

For estimation methods that get around this problem see {cite:t}`som07`, {cite:t}`cssIntlStickyC`, {cite:t}`cosHousingWealth`. Those papers consistently find that the proportion of updaters is about {math}`\Pi=0.25` per quarter, so that the serial correlation of "true" consumption growth is about {math}`(1-\Pi)=0.75` per quarter.

## Appendix

This appendix provides additional derivations and notation useful for simulating the model. One way of interpreting consumers' behavior in this model is to attribute to them the beliefs that would rationalize their actions. Define {math}`\WAllLev` as the level of wealth (human and nonhuman) that the consumer perceives. Then the Deaton definition of the permanent income hypothesis is that

```{math}
\CLevBF_{t} = \WAllLev_{t} \MPC
```

and the reason consumption follows a random walk is that {math}`\MPC=(\rfree/\Rfree)` is precisely the amount that ensures that {math}`\Ex_{t}[\WAllLev_{t+1}] = \WAllLev_{t}`.

Writing the "believed" level of wealth as {math}`\bar{\WAllLev}`, we could then interpret the failure of the sticky expectations consumer to change his consumption during the period of nonupdating as reflecting his optimal forecast that, in the absence of further information, {math}`\bar{\WAllLev}_{t+1} = \bar{\WAllLev}_{t+2} + ... = \WAllLev_{t}`.

To pursue this interpretation, it is useful to write the budget constraint more explicitly, as before; start with the constraint in levels, then decompose variables into ratios to permanent income (nonbold variables) and the level of permanent income:

```{math}
\begin{aligned}
\BLevBF_{t+1} & = \ALevBF_{t} \Rfree_{t+1}
\\  \BRat_{t+1}P_{t+1} & = \ARat_{t}P_{t} \Rfree_{t+1}
\\  \BRat_{t+1} & = \ARat_{t} \underbrace{(\Rfree_{t+1}/\WGro_{t+1})}_{\equiv \Rnorm_{t+1}}
\end{aligned}
```

where we permit a time subscript on {math}`\Rfree` and {math}`\WGro` because we want to allow for the possibility that beliefs about the interest rate or growth rate might change over time. (**PermShks=false:** We also allow henceforth for the existence of permanent shocks to income, {math}`\Psi_{t}`.)

Consider an economy that comes into existence in period {math}`0` with a population of consumers who are identical in every respect, including their beliefs about current and future values of the economy's variables.

First we examine the case where neither {math}`\Rfree` nor {math}`\WGro` can change after date {math}`0`. In that case, we can track the dynamics of believed and actual variables as follows.

```{math}
\begin{aligned}
\bar{\BLevBF}_{t+1} & = \Pi \BLevBF_{t+1} + (1-\Pi) \bar{\ALevBF}_{t} \Rfree
\\ \bar{\BRat}_{t+1}\bar{P}_{t+1} & = \Pi \BRat_{t+1}P_{t+1} + (1-\Pi) \bar{\ARat}_{t}\bar{P}_{t} \Rfree
\\ \bar{\BRat}_{t+1} & = \Pi \BRat_{t+1}\underbrace{(P_{t+1}/\bar{P}_{t+1})}_{\equiv Q_{t+1}} + (1-\Pi)\bar{\ARat}_{t} \underbrace{(\Rfree/\WGro \bar{\hat{\Psi}}_{t+1})}_{\equiv \bar{\Rnorm}_{t+1}}
\end{aligned}
```

where capturing the dynamics of the ratio of true permanent income to believed permanent income {math}`Q_{t+1}` requires us to compute

```{math}
\begin{aligned}
\bar{P}_{t+1} & = \left(\Pi \Psi_{t+1} P_{t} + (1-\Pi) \bar{P}_{t}\right)\WGro
\\ \bar{\Psi}_{t+1} & \equiv \bar{P}_{t+1}/(\bar{P}_{t} \WGro)
\\ Q_{t+1} & = (\Psi_{t+1}/\bar{\Psi}_{t+1}) Q_{t}
\end{aligned}
```

and so

```{math}
\begin{aligned}
(\bar{\TShkEmp}_{t+1}-1)\bar{P}_{t+1} & = \Pi (\TShkEmp_{t+1}-1) P_{t+1} + (1-\Pi) (1-1) \bar{P}_{t} \WGro
\\  \bar{\TShkEmp}_{t+1}-1 & = \Pi (\TShkEmp_{t+1}-1) Q_{t+1}
\end{aligned}
```

with the crucially useful fact that since by assumption neither {math}`\Rfree` nor {math}`\WGro` is changing, normalized human wealth does not change from

```{math}
\hRat = \left(\frac{1}{1-\WGro/\Rfree}\right)
```

so that

```{math}
\begin{aligned}
\bar{\HLev}_{t} & = \hRat \bar{P}_{t}
\\ \HLev_{t} & = \hRat P_{t}
\\ \bar{\HLev}_{t+1} & = \left(\Pi Q_{t+1} + (1-\Pi)/\bar{\Psi}_{t+1} \right) \hRat \bar{P}_{t+1}
\end{aligned}
```

so that perceived wealth and consumption will be

```{math}
\begin{aligned}
\bar{\WAllRat}_{t+1} & = \bar{\BRat}_{t+1}+(\bar{\TShkEmp}_{t+1}-1)+\bar{\HRat}_{t+1}
\\ \bar{\CRat}_{t+1} & = \bar{\WAllRat}_{t+1} \MPC
\\ \bar{\ARat}_{t+1} & = \bar{\BRat}_{t+1}+\bar{\TShkEmp}_{t+1}-\bar{\CRat}_{t+1}.
\end{aligned}
```

Matters are more complex if expectations about {math}`\Rfree` and {math}`\WGro` are allowed to change over time.

Suppose again that we begin our economy in period {math}`0` with population with homogeneous views: Everyone believes {math}`\Rfree=\Rfree^{0}` and {math}`\WGro=\WGro^{0}`; so long as these views are universally held in the population, aggregate dynamics are captured by the foregoing analysis.

Suppose, however, that in some period {math}`n>0` the economy's "true" values of {math}`\Rfree` or {math}`\WGro` change. Updating consumers see this change immediately. But nonupdaters will not discover the changed nature of the economy's dynamics until they update again.

We capture this modification to the model by keeping track of the aggregate values of the variables for the set of consumers who adhere to each differing opinion, along with the population mass associated with the different opinions. Specifically, suppose there are {math}`J` different opinions in the population, each of whom constitutes population mass {math}`\mathcal{L}^{j}_{t}` such that {math}`\sum_{j} \mathcal{L}^{j}_{t} = 1~\forall~t`. Then for each such population, it will be necessary to keep track of their average beliefs about macroeconomic variables.

Suppose, for example, that through period {math}`x` there have been only {math}`j-1` different opinion groups in the population. In period {math}`x+1` either {math}`\WGro` or {math}`\Rfree` changes. We need then to define group {math}`j` by {math}`\Rfree^{j}=\Rfree_{x}` and {math}`\WGro^{j}=\WGro_{x}` and to define {math}`\bar{\ARat}^{j}_{x} \equiv \ARat_{x}`, {math}`\bar{P}^{j}_{x}=P_{x}`, and so on. We will henceforth need to keep track of dynamics of the consumers who remain in belief group {math}`j` by, e.g.,

```{math}
\begin{aligned}
\bar{\BLevBF}^{j}_{t+1} & = \ALevBF^{j}_{t} \Rfree^{j}
\\ \bar{\BRat}^{j}_{t+1}\bar{P}^{j}_{t+1} & = \bar{\ARat}^{j}_{t}\bar{P}^{j}_{t} \Rfree^{j}
\\ \bar{\BRat}^{j}_{t+1} & = \bar{\ARat}^{j}_{t} \underbrace{(\Rfree^{j}/\WGro^{j} \bar{\Psi}^{j}_{t+1})}^{j}_{\equiv \bar{\Rnorm}^{j}}
\\ \bar{P}^{j}_{t+1} & = \bar{P}^{j} \WGro^{j}
\end{aligned}
```

while we need to keep track of the populations of the differing groups by, e.g.,

```{math}
\begin{aligned}
\mathcal{L}^{j}_{t} & = \Pi
\\  \mathcal{L}^{j}_{t+1} & = \Pi(1-\Pi)
\\  \mathcal{L}^{j}_{t+2} & = \Pi(1-\Pi)^{2}
\end{aligned}
```

and so on. These population dynamics continue forever, but the population of households continuing to hold any specific belief configuration dwindles toward zero as time progresses.

Aggregate variables for the population as a whole can be constructed as the population-weighted sums across all the differing belief groups, weighted by their masses:

```{math}
\bar{P}_{t} = \Pi P_{t} + (1-\Pi) \sum_{j} \mathcal{L}^{j}_{t} \bar{P}^{j}_{t}
```

and note that if beliefs change back to a configuration that has been seen before it is possible to add the population mass and aggregate values of the variables associated with the new population with that belief configuration to the corresponding figures for the old population that holds the same beliefs. This reduces the number of groups that the simulations must track in the case where beliefs switch between a limited number of distinct values.
