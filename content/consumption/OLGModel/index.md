(sec:OLGModel)=
# The Diamond OLG Model

This chapter and its [notebook](OLGModel.ipynb) present a canonical overlapping generations (OLG) model, like the one originally proposed by {cite:t}`diamond:olg`, building on {cite:t}`samuelsonOLG`.[^olg-references]

[^olg-references]: For a remarkably clear statement of the questions addressed by OLG models, see {cite:t}`jeffersonOLG`. For a review of the influence of {cite:t}`samuelsonOLG`'s model, see {cite:t}`weilSamuelson`.

## Setup

The economy has the following features:

1. Two generations are alive at any point in time, the young (age 1) and old (age 2). A period is a generation, about 30 years, so annual rates compound: a discount factor of 0.96 a year is {math}`0.96^{30} \approx 0.29` a period.

2. The size of the *young* generation in period {math}`t` is given by {math}`\PopLev_{t}=\PopLev_{0}\PopGro^{t}` (note that {math}`\PopLev` denotes only the young population, not the entire population, and this formula assumes constant population growth since time 0).

3. Households work only in the first period of life, earning the wage {math}`\Wage_{1,t}`. They earn no income in the second period of life ({math}`\Wage_{2,t+1}=0`).

4. They consume part of their first-period income and save the rest to finance their consumption when old.

5. The assets of the young at the end of period {math}`t` are the source of the capital used for aggregate production in period {math}`t+1`, {math}`\KLev_{t+1} = \PopLev_{t}{\aLev}_{1,t}` where {math}`{\aLev}_{1,t}` is the assets per young household *after* their consumption in period 1. (For convenience, we assume that there is no depreciation). Note that lower-case letters denote per-capita quantities, a convention used throughout.

6. The old in period {math}`t` own the entire capital stock and (because they have no bequest motive) will consume it all, so dissaving by the old in period {math}`t` will be {math}`\PopLev_{t-1}{\aLev}_{1,t-1} = \KLev_{t}` (it is {math}`\PopLev_{t-1}` because the old in {math}`t` were young in {math}`t-1`). The old do receive interest on their capital, so their consumption will be {math}`\KLev_{t}` plus the interest income {math}`\rfree \KLev_{t}`, but the {math}`\rfree \KLev_{t}` component does not affect saving because it is part of both income and consumption.

7. Labor and capital markets are perfectly competitive and the aggregate production technology is CRS, {math}`\YLev=\FFunc(\KLev,\LLev)` (recall that this implies that {math}`\FFunc(\KLev,\LLev) = \FFunc_{L}\LLev + \FFunc_{K}\KLev`, which is ["Euler's Theorem"](#fact:eulerstheorem)).

## Analysis

Let's normalize everything by the period-{math}`t` young population {math}`\PopLev_{t}`, writing normalized variables in lower case. Thus the per-young-capita aggregate production function becomes

```{math}
:label: eq:fFromF

\fFunc(\kLev_{t}) \equiv \FFunc(\KLev_{t},\PopLev_{t})/\PopLev_{t} = \FFunc(\KLev_{t}/\PopLev_{t},1).
```

The perfect competition assumption implies that wages and net interest rates are equal to the marginal products of labor and capital, respectively:

```{math}
:label: eq:rEqfp

\begin{aligned}
\Wage_{t} & = \fFunc(\kLev_{t}) - \kLev_{t}\fFunc^{\prime}(\kLev_{t}), \\
\rfree_{t} & = \fFunc^{\prime}(\kLev_{t}).
\end{aligned}
```

To make further progress, we need to make specific assumptions about the utility function and the aggregate production function. Assume that utility is CRRA, {math}`\uFunc(\bullet) = \bullet^{1-\CRRA}/(1-\CRRA)` and assume a Cobb-Douglas aggregate production function {math}`\FFunc(\KLev,\LLev) = \KLev^{\kapShare}\LLev^{1-\kapShare} \Rightarrow \fFunc(\kLev) = \kLev^{\kapShare}`.

In this case we can solve for wages and interest rates:

```{math}
\begin{aligned}
\Wage_{t} & = (1-\kapShare) \kLev^{\kapShare}_{t} \\
\rfree_{t} & = \kapShare \kLev^{\kapShare-1}_{t}.
\end{aligned}
```

The individual's maximization problem yields the Euler equation ({math}`\Rfree = 1+\rfree`; despite its lower case, {math}`\rfree` is not a per-capita quantity):

```{math}
\uFunc^{\prime}(\cLev_{1,t}) = \Discount \Rfree_{t+1} \uFunc^{\prime}(\cLev_{2,t+1}).
```

Now let's assume that utility is logarithmic, {math}`\CRRA = 1`. With no income when old, a change in the interest rate does not revalue the young's human wealth, all of which is their current wage, and with logarithmic utility its income and substitution effects cancel (see [the Fisher two-period model](#sec:2PeriodLCModel)); so the young save the same share of their wage, {math}`\Wage_{1,t} = \Wage_{t}`, whatever the interest rate. (With {math}`\CRRA \neq 1`, saving would depend on {math}`\Rfree_{t+1}`, which depends on {math}`\kLev_{t+1}` itself, and the accumulation equation would be implicit.) Beginning with consumption in levels and then moving to per-capita, this implies

```{math}
:label: eq:ktp1

\begin{aligned}
\cLev_{1,t} & = \frac{\Wage_{1,t} + \overbrace{\Wage_{2,t+1}}^{=0}/\Rfree_{t+1}}{1+\Discount} \\
\cLev_{1,t} & = \frac{\Wage_{1,t}}{1+\Discount} \\
{\aLev}_{1,t} & = \Wage_{1,t}-\cLev_{1,t} \\
& = \Wage_{1,t}(1-1/(1+\Discount)) \\
& = \Wage_{1,t}(\Discount/(1+\Discount)) \\
& = (1-\kapShare) \kLev_{t}^{\kapShare}\left(\frac{\Discount}{1+\Discount}\right) \\
\overbrace{\kLev_{t+1}}^{={\aLev}_{1,t}/\PopGro} & = \kLev_{t}^{\kapShare}\left[\frac{(1-\kapShare)\Discount}{\PopGro(1+\Discount)}\right] \\
\frac{d\kLev_{t+1}}{d\kLev_{t}} & = \kLev_{t}^{\kapShare-1}\left[\frac{\kapShare (1-\kapShare) \Discount}{\PopGro(1+\Discount)}\right].
\end{aligned}
```

The steady-state will be the point where {math}`\kLev_{t+1}=\kLev_{t}`. For convenience, define a constant

```{math}
\mathcal{Q} = \frac{(1-\kapShare) \Discount}{\PopGro(1+\Discount)},
```

allowing us to rewrite {eq}`eq:ktp1` as

```{math}
\kLev_{t+1} = \mathcal{Q} \kLev_{t}^{\kapShare}.
```

Then the steady-state will be the point where {math}`\kLev_{t+1}=\kLev_{t}=\bar{\kLev}`

```{math}
\begin{aligned}
\bar{\kLev} & = \mathcal{Q} \bar{\kLev}^{\kapShare} \\
\bar{\kLev} & = \mathcal{Q}^{1/(1-\kapShare)}.
\end{aligned}
```

Dynamics of the model can be analyzed using a simple figure relating the capital stock per capita in period {math}`t+1` to that in period {math}`t`. The solid locus is a graph of equation {eq}`eq:ktp1`. We depict the 45 degree line because it indicates the set of "steady-state" points where {math}`\kLev_{t+1}=\kLev_{t}` and thus any intersection of the 45 degree line with the {math}`\kLev_{t+1}(\kLev_{t})` function indicates a steady-state of the model. One is at {math}`\kLev = 0`: an economy with no capital stays there, but any positive amount of capital grows away from it.

:::{figure} figures/OLGModelDynamics.png
:name: fig:OLGModelDynamics

Convergence of OLG Economy to Steady State, with a capital share of a third, a discount factor of 0.96 a year and population growth of 1 percent a year, a generation being 30 years. Drawn by the chapter's [notebook](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=OLGModel.ipynb), which runs in your browser.
:::

The experiment traced out in the figure is as follows. We start the economy in period {math}`t=0` with capital per capita of {math}`\kLev_{0}`, which, from {eq}`eq:ktp1`, implies a certain value {math}`\kLev_{1}` for capital in period {math}`t+1=1`. Now think about period 1 becoming {math}`t` and period 2 becoming {math}`t+1`. To find the level of capital the model implies for period {math}`t+1=2`, we find the point on the 45 degree line that corresponds to {math}`\kLev_{1}`, then go vertically up from there to the curve, which gives {math}`\kLev_{t+1}=\kLev_{2}`. When the same set of gyrations is repeated the result is that the level of capital converges to the steady-state level {math}`\bar{\kLev}`.

The steady state is stable: there the slope of the accumulation curve, the last line of {eq}`eq:ktp1`, is {math}`\kapShare`, less than one. In logs, {math}`\log \kLev_{t+1} - \log \bar{\kLev} = \kapShare(\log \kLev_{t} - \log \bar{\kLev})`, so each generation closes the fraction {math}`1-\kapShare` of the remaining gap: two thirds, with a capital share of a third, so that two generations take the economy most of the way to its steady state.

## Social Optimum

We have determined the outcome that will arise in a perfectly competitive economy in which households optimally choose their behavior given market prices with no government intervention.

Often in macroeconomic analysis this constellation of assumptions yields a conclusion that the steady state is optimal (and dynamics are also optimal) according to some plausible criteria. We now examine the optimality properties of the OLG model outcome.

As a preliminary, let's define the lifetime utility experienced by the young generation at time {math}`t` as

```{math}
:label: eq:lifeUtil

\vLev_{t} = \uFunc(\cLev_{1,t})+\Discount \uFunc(\cLev_{2,t+1}).
```

Suppose our definition of optimality reflects the choices that would be made by a benevolent social planner who maximizes a social welfare function of the form[^time-inconsistency]

[^time-inconsistency]: The old at time {math}`t` are generation {math}`t-1`, so the planner weights their old-age utility by their own {math}`\Discount` and, as an earlier generation, by {math}`\beth^{-1}`. With any other weight the planner at {math}`t` would value the old relative to the young differently than the planner at {math}`t-1` did, and would revise that planner's plan: the problem would be time inconsistent.

```{math}
\VLev_{t} = \beth^{-1}\Discount \uFunc(\cLev_{2,t}) + \sum_{n=0}^{\infty} \beth^{n} \vLev_{t+n}
```

subject to the economy's aggregate resource constraint

```{math}
:label: eq:Bud

\underbrace{\KLev_{t} + \FFunc(\KLev_{t},\PopLev_{t})}_{\text{Sources}} = \underbrace{\KLev_{t+1} + \PopLev_{t} \cLev_{1,t} + \PopLev_{t-1} \cLev_{2,t}}_{\text{Uses}}
```

where the Hebrew letter {math}`\beth` reflects the social planner's discount factor and the planner must allocate the society's resources ("Sources") between consumption of the two generations alive at time {math}`t` and the capital stock in period {math}`t+1` ("Uses").

The idea is that the social planner cares about every generation's lifetime happiness, but discounts the happiness of future generations. (Without discounting, the sum over infinitely many generations would not converge, and the planner's problem would not be well defined.)

It is possible to show (using methods not described in this section; see {cite:t}`blanchard&fischer:text` for details) that the socially optimal steady state is characterized by the equation

```{math}
1+\fFunc^{\prime}(\bar{\kLev}^{*}) = \PopGro \beth^{-1}
```

In the case of our Cobb-Douglas production function, this becomes

```{math}
:label: eq:OLG-planner-steady-state

\begin{aligned}
(\bar{\kLev}^{*})^{\kapShare-1}\kapShare & = \PopGro \beth^{-1} - 1 \\
\bar{\kLev}^{*} & = \left(\frac{\PopGro \beth^{-1} - 1}{\kapShare}\right)^{1/(\kapShare-1)}.
\end{aligned}
```

Comparing this to the outcome that will actually arise,

```{math}
\bar{\kLev} = \left(\frac{\PopGro(1+\Discount)}{(1-\kapShare) \Discount}\right)^{1/(\kapShare-1)},
```

our point is that there is no particular relationship between the socially optimal outcome and the actual equilibrium outcome that will arise if the social planner is not involved. The actual outcome could have too little capital or too much, and there is no reason to expect it to be the "right" amount.

You might respond by saying that our definition of optimality here is too strong; we might hope that the economy would at least be able to avoid a Pareto inefficient outcome, even if we can't expect perfect optimality according to the preferences of some mythical Godlike "social planner."

It turns out, however, that even Pareto efficiency is not guaranteed. (In this context, Pareto efficiency must be defined across generations: The economy is Pareto efficient if there is no way to make one generation better off without making another generation worse off).

To examine Pareto efficiency, start by dividing the aggregate resource constraint, {eq}`eq:Bud`, by the size of the labor force at time {math}`t`:

```{math}
:label: eq:OLG-resources-per-worker

\kLev_{t} + \fFunc(\kLev_{t}) = \PopGro \kLev_{t+1} + \cLev_{1,t} + \cLev_{2,t}/\PopGro
```

Define an index of aggregate per capita consumption as

```{math}
:label: eq:OLG-consumption-index

\cLev_{t} = \cLev_{1,t} + \cLev_{2,t}/\PopGro
```

In steady state, {math}`\kLev_{t+1}=\kLev_{t}=\bar{\kLev}`, so if {math}`\bar{\cLev}` is the steady-state level of {math}`\cLev_{t}` then the resource constraint implies

```{math}
\begin{aligned}
\bar{\kLev} + \fFunc(\bar{\kLev}) & = \PopGro \bar{\kLev} + \bar{\cLev} \\
\fFunc(\bar{\kLev}) & = \underbrace{(\PopGro-1)}_{\popGro}\bar{\kLev}+\bar{\cLev} \\
\fFunc(\bar{\kLev})-\popGro \bar{\kLev} & = \bar{\cLev}
\end{aligned}
```

Now consider the effects of a change in {math}`\bar{\kLev}` on {math}`\bar{\cLev}`:

```{math}
\left(\frac{d \bar{\cLev}}{d \bar{\kLev}}\right) = \fFunc^{\prime}(\bar{\kLev})-\popGro.
```

There exists a {math}`\bar{\kLev}` which maximizes per-capita steady-state consumption:

```{math}
\max_{\bar{\kLev}} ~ \fFunc(\bar{\kLev}) - \popGro \bar{\kLev}
```

whose solution is obtained from the FOC

```{math}
\begin{aligned}
\kapShare \bar{\kLev}^{\kapShare-1} & = \popGro \\
\bar{\kLev}^{**} & = (\popGro/\kapShare)^{1/(\kapShare-1)},
\end{aligned}
```

and note that this means that for {math}`\bar{\kLev} > \bar{\kLev}^{**}` an extra bit of capital actually requires a *decline* in steady-state consumption. An economy in this circumstance of excessive saving is called "dynamically inefficient." It is Pareto inefficient: it can cut capital per worker to {math}`\bar{\kLev}^{**}` once, giving the capital released to the generations alive at the time, and every later generation then consumes more, because {math}`d\bar{\cLev}/d\bar{\kLev} < 0` beyond {math}`\bar{\kLev}^{**}`. Every generation can be made better off.

Since {math}`\rfree = \fFunc^{\prime}(\bar{\kLev})`, the economy is dynamically inefficient exactly when its interest rate is below the population growth rate, {math}`\rfree < \popGro`. In this model {math}`\fFunc^{\prime}(\bar{\kLev}) = \kapShare\bar{\kLev}^{\kapShare-1} = \kapShare/\mathcal{Q}`, so the steady-state interest rate is

```{math}
:label: eq:OLG-steady-state-interest-rate

\bar{\rfree} = \frac{\kapShare\PopGro(1+\Discount)}{(1-\kapShare)\Discount}.
```

With the calibration of {numref}`fig:OLGModelDynamics`, it is 4.7 percent a year, against population growth of 1 percent: the economy is dynamically efficient by a wide margin, with capital only 4 percent of the golden rule's. Inefficiency takes very patient households, a low capital share and fast population growth together, and {cite:t}`amszDynamicEfficiency` find that actual economies are dynamically efficient. Dynamic inefficiency is the condition under which pay-as-you-go [Social Security](#sec:SocSecAndKAccum) can make every generation better off, and under which [bubbles](#sec:Bubbles) can last.

Note further that there is actually a {math}`\bar{\kLev}` so large that consumption would have to be zero:

```{math}
\begin{aligned}
\bar{\kLev}^{\kapShare} & = \popGro \bar{\kLev} \\
\bar{\kLev}^{\kapShare-1} & = \popGro \\
\bar{\kLev} & = \popGro^{1/(\kapShare-1)}.
\end{aligned}
```

The figure of gross and net output, {numref}`fig:fnkBoth`, illustrates both points.

:::{figure} figures/fnkBoth.png
:name: fig:fnkBoth

Gross and Net Per Capita Output as a Function of {math}`\kLev`, with the same calibration: net output, steady-state consumption per capita, is highest at the golden rule {math}`\bar{\kLev}^{**}`. Drawn by the chapter's [notebook](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=OLGModel.ipynb), which runs in your browser.
:::

Both figures are drawn by this chapter's [figure notebook](OLGModel.ipynb), which also redraws them with sliders for the capital share, patience and population growth, and adds the introduction of a pay-as-you-go [Social Security](#sec:SocSecAndKAccum) system; run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=OLGModel.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/consumption/OLGModel/OLGModel.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/consumption/OLGModel/OLGModel.ipynb).
