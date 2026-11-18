(sec:RamseyCassKoopmans)=
# The Ramsey/Cass-Koopmans (RCK) Model

{cite:t}`ramseySave`, followed much later by {cite:t}`cass:growth` and {cite:t}`koopmans:growth`, formulated the canonical model of optimal growth for an economy with exogenous "labor-augmenting" technological progress. For the facts the model is meant to explain, and the Solow model it builds on, see the undergraduate textbook of {cite:t}`ashrafWeilGrowth`.

:::{margin}
Graduate textbook treatments are in {cite:t}`blanchard&fischer:text`, chapter 2, {cite:t}`barro&salaimartin:book`, chapter 2, and {cite:t}`acemogluGrowth`, chapter 8.
:::

## The Budget Constraint

The economy has a perfectly competitive production sector that uses a constant-returns-to-scale Cobb-Douglas production function

:::{margin}
States and controls are functions of time; time subscripts appear only where clarity needs them.
:::

```{math}
\begin{gathered}\begin{aligned}
                   \YLvl & =  \FFunc(\KLvl,\LLvl) = \KLvl^{\kapShare}(\PtyLab \LLvl)^{1-\kapShare}
\end{aligned}\end{gathered}
```

to produce output using capital and labor. Under perfect competition firms must make zero profits in equilibrium, which means, by [Euler's theorem](#fact:eulerstheorem), that

:::{margin}
An important insight here is that all of output is absorbed by payments to labor and to capital; there is nothing left over (say, to fund corporate research to invent new technologies to augment productivity).
:::

```{math}
:label: eq:RCK-outputExhausted

\YLvl = \FFunc_{\KLvl}\KLvl + \FFunc_{\LLvl}\LLvl .
```

Labor hours (the same as population) increase exogenously at a constant rate

:::{margin}
The population growth rate is written {math}`\PopnGroRte`: {math}`\PopnGroFac` is the population's growth factor and {math}`\lnat` is the natural log, so {math}`\PopnGroRte = \log \PopnGroFac`.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\LLvl}/\LLvl & =  \PopnGroRte
\end{aligned}\end{gathered}
```

and {math}`\PtyLab` is an index of labor productivity that grows at rate

:::{margin}
This is "labor-augmenting" (Harrod-neutral) productivity growth: {math}`\PtyLab` multiplies labor, {math}`\FFunc(\KLvl,\PtyLab \LLvl)`. The alternative is productivity {math}`\PtyAgg` that multiplies total output, {math}`\PtyAgg \FFunc(\KLvl,\LLvl)` ("Hicks-neutral"). With any production function other than Cobb-Douglas, a steady state with constant growth rates requires progress to be labor-augmenting {cite:p}`uzawaNeutral`.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\PtyLab }/\PtyLab  & =  \PtyGroRte. 
\end{aligned}\end{gathered}
```

Technological progress thus lets each worker produce ever more with the same physical capital.

The quantity {math}`\PtyLab \LLvl` is the number of "efficiency units" of labor.

Aggregate capital accumulates according to

```{math}
:label: eq:Kdotlevel

\begin{gathered}\begin{aligned}
  \dot{\KLvl} & =  \YLvl - \CLvl - \deprRte \KLvl .
\end{aligned}\end{gathered}
```

Lower case variables are the upper case version divided by efficiency units, so {math}`\yNrm = \YLvl/(\PtyLab \LLvl) = (\KLvl/(\PtyLab \LLvl))^{\kapShare} = \kap^{\kapShare}`. Since {math}`\kap = \KLvl/(\PtyLab \LLvl)`,

:::{margin}
NOT per-capita; this is required for '[balanced growth](#sec:RCK-SteadyState)'.
:::

```{math}
\dot{\kap}/\kap = \dot{\KLvl}/\KLvl - \dot{\PtyLab}/\PtyLab - \dot{\LLvl}/\LLvl = \dot{\KLvl}/\KLvl - (\PtyGroRte +\PopnGroRte),
```

so dividing {eq}`eq:Kdotlevel` by {math}`\PtyLab \LLvl` and using it gives

```{math}
:label: eq:RCK-kdot

\dot{\kap} = \fFunc(\kap) - \cNrm - (\PtyGroRte +\PopnGroRte+\deprRte) \kap .
```

A steady state is a point where {math}`\dot{\kap} = 0`, so that

```{math}
:label: eq:RCK-cSteadyState

\cNrm = \fFunc(\kap) - (\PtyGroRte +\PopnGroRte+\deprRte) \kap .
```

A first candidate for the best steady state is the one with the highest {math}`\cNrm`. Maximizing steady-state consumption with respect to {math}`\kap` requires

```{math}
\frac{d\cNrm}{d\kap} = \fFunc^{\prime}(\kap) - (\PtyGroRte +\PopnGroRte+\deprRte) = 0 ,
```

and since {math}`d^{2}\cNrm/d\kap^{2} = \fFunc^{\prime\prime}(\kap) < 0`, this is a maximum. The capital stock that satisfies it, {math}`\GoldRule{\kap}`, obeys the "golden rule" of {cite:t}`phelps:golden`, an article well worth reading:

```{math}
:label: eq:RCK-goldenRule

\fFunc^{\prime}(\GoldRule{\kap}) = \PtyGroRte +\PopnGroRte+\deprRte .
```

One more unit of {math}`\kap` adds {math}`\fFunc^{\prime}(\kap)` to output, but holding it steady as effective labor grows and capital depreciates takes {math}`\PtyGroRte +\PopnGroRte+\deprRte` more investment; consumption is highest where the two are equal. With the Cobb-Douglas {math}`\fFunc(\kap) = \kap^{\kapShare}`, the golden rule is {math}`\GoldRule{\kap} = \left(\kapShare/(\PtyGroRte +\PopnGroRte+\deprRte)\right)^{1/(1-\kapShare)}`.

## The Social Planner's Problem

Now suppose a social planner maximizes the discounted
sum of CRRA utility from per capita consumption, with time preference rate {math}`\discRte`:

:::{margin}
This objective counts each date's per capita utility once, as {cite:t}`blanchard&fischer:text` do. {cite:t}`romer:text` weights it by the size of the population, which replaces {math}`\discRte` with {math}`\discRte-\PopnGroRte` below, and takes {math}`\PopnGroRte` out of the steady-state condition.
:::

```{math}
:label: eq:RCK-maxprob

\max \int_{0}^{\infty} \left(\frac{(\CLvl/\LLvl)^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}\,dt .
```

But {math}`\CLvl/\LLvl = \PtyLab (\CLvl/(\PtyLab \LLvl))= \PtyLab \cNrm`. Recall that for a variable growing at rate {math}`\PtyGroRte`,

```{math}
\begin{gathered}\begin{aligned}
  \PtyLab _{t} & =  \PtyLab _{0}e^{\PtyGroRte t}
\end{aligned}\end{gathered}
```

so if productivity at date 0 is {math}`\PtyLab_{0}`, at date {math}`t`

```{math}
:label: eq:cRat

\begin{gathered}\begin{aligned}
  \CLvl/\LLvl & =  \cNrm\PtyLab   \\
               & =  \cNrm\PtyLab _{0}e^{\PtyGroRte t}. 
\end{aligned}\end{gathered}
```

Since {math}`\PtyLab_{0}` multiplies consumption at every date, it only scales the objective, by the positive constant {math}`\PtyLab_{0}^{1-\CRRA}`, so we can impose {math}`\PtyLab_{0}=1` without loss of generality.

Using {eq}`eq:cRat`, and writing {math}`\uFunc(\cNrm) = \cNrm^{1-\CRRA}/(1-\CRRA)`, with {math}`\CRRA` the coefficient of relative risk aversion, rewrite the social planner's objective function as

```{math}
:label: eq:maxprobmod

\begin{gathered}\begin{aligned}
  \int_{0}^{\infty} \left(\frac{(\PtyLab \cNrm)^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}\,dt & =  
                                                                                               \int_{0}^{\infty} \left(\frac{\cNrm^{1-\CRRA}}{1-\CRRA}\right) e^{-\discRte  t}e^{(1-\CRRA)\PtyGroRte  t}\,dt 
  \\ & =  \int_{0}^{\infty} \uFunc(\cNrm) e^{\left((1-\CRRA)\PtyGroRte -\discRte \right) t}\,dt
           .
\end{aligned}\end{gathered}
```

Thus, assuming {math}`\discRte > (1-\CRRA) \PtyGroRte`, so that the objective is finite (that is, imposing the [finite value of autarky condition](https://llorracc.github.io/BufferStockTheory/#pffvac)), the complete optimization problem
is

```{math}
\max \int_{0}^{\infty} \uFunc(\cNrm) e^{-(\discRte - (1-\CRRA)\PtyGroRte) t}\,dt
```

subject to

```{math}
\dot{\kap} = \kap^{\kapShare}-\cNrm-(\PopnGroRte+\PtyGroRte+\deprRte)\kap,
```

whose current-value Hamiltonian is

:::{margin}
If the Hamiltonian is new to you, Peter Thompson's [lecture notes on optimal control](https://www.andrew.cmu.edu/course/88-737/optimal_control/optimal_control.pdf) derive the method from the economics of a firm's capital problem, and later work through this model. Wikipedia's [worked example of the RCK model](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model), linked from the two optimization conditions, uses the present-value Hamiltonian instead, whose costate is this one discounted to date zero.
:::

```{math}
\Ham(\kap,\cNrm,\vk) = \uFunc(\cNrm) + (\kap^{\kapShare} - \cNrm - (\PopnGroRte+\PtyGroRte+\deprRte)\kap)\vk.
```

The [current-value Hamiltonian optimization condition](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model) for consumption requires {math}`\partial 
 \Ham/\partial \cNrm = 0`:

```{math}
:label: eq:RCK-H1A

\begin{gathered}\begin{aligned}
  \cNrm^{-\CRRA} & =  \vk   \\
  -\CRRA \cNrm^{-\CRRA-1}\dot{\cNrm} & =  \dot{\vk} 
                                       .
\end{aligned}\end{gathered}
```

The [current-value Hamiltonian optimization condition](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model) for capital, the costate equation, requires:

:::{margin}
In the book's mathematical appendices, [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) derives the Hamiltonian's conditions for a version of this model without productivity growth and shows how each relates to the discrete-time Bellman approach.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\vk} & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \partial \Ham/\partial \kap  \\
                & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \vk (\fFunc^{\prime}(\kap) - (\PopnGroRte+\PtyGroRte+\deprRte))  \\
  \dot{\vk}/{\vk} & =  \discRte+\PopnGroRte+\deprRte+\CRRA \PtyGroRte-\fFunc^{\prime}(\kap) .
\end{aligned}\end{gathered}
```

Since {eq}`eq:RCK-H1A` gives {math}`\dot{\vk}/\vk = -\CRRA\dot{\cNrm}/\cNrm`, this is

```{math}
:label: eq:cdotOc

\dot{\cNrm}/\cNrm = \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\PopnGroRte+\deprRte)-\discRte - \CRRA \PtyGroRte),
```

or, with {math}`\rfree \equiv \fFunc^{\prime}(\kap) - \deprRte` the interest rate, {math}`\dot{\cNrm}/\cNrm = \CRRA^{-1}(\rfree - \discRte - \PopnGroRte) - \PtyGroRte`.

This Euler equation is called the "Keynes-Ramsey rule," because Ramsey derived it
with an explanation attributed to Keynes.
Apart from the {math}`-\PtyGroRte`, which comes from measuring consumption per efficiency unit, it is like [the Euler equation in the perfect foresight CRRA model](#eq:PFCRRA-cgrow) in continuous time, with two differences: the return that matters is {math}`\rfree-\PopnGroRte` rather than {math}`\rfree`, because population growth dilutes each person's capital, and that return varies over time as {math}`\fFunc^{\prime}(\kap)` does.

Since per capita consumption is {math}`\CLvl/\LLvl = \cNrm \PtyLab`, it grows at {math}`\dot{\cNrm}/\cNrm + \PtyGroRte = \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\PopnGroRte+\deprRte)-\discRte)`: the same formula, as a function of {math}`\kap`, as in the model with no productivity growth, the [Euler equation](#eq:cdotOc) with {math}`\PtyGroRte=0`. Productivity growth matters only through {math}`\kap`.

(sec:RCK-SteadyState)=
## The Steady State

Technological progress is assumed to be labor-augmenting because then,
in the steady state, per capita consumption, income
and capital all grow at rate {math}`\PtyGroRte`.

:::{margin}
{cite:t}`ghosDespiteUzawa` discuss how realistic this requirement is.
:::

{math}`\dot{\cNrm}/\cNrm = 0` implies that at the steady-state value of {math}`\Steady{\kap}`,

```{math}
:label: eq:RCK-modGoldenRule

\fFunc^{\prime}(\Steady{\kap}) = \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte .
```

This is the "modified golden rule" of {cite:t}`blanchard&fischer:text`, chapter 2. Comparing it with the [golden rule](#eq:RCK-goldenRule), {math}`\fFunc^{\prime}(\Steady{\kap}) - \fFunc^{\prime}(\GoldRule{\kap}) = \discRte - (1-\CRRA)\PtyGroRte`, so {math}`\Steady{\kap} < \GoldRule{\kap}` exactly when {math}`\discRte > (1-\CRRA)\PtyGroRte`: the assumption that keeps the planner's objective finite also rules out accumulating more capital than the golden rule.

Using {math}`\fFunc^{\prime}(\kap) = \kapShare \kap^{\kapShare-1}`, the modified golden rule gives an analytical formula for the steady state:

```{math}
:label: eq:RCK-kSteadyCobbDouglas

\begin{gathered}\begin{aligned}
  \kapShare \Steady{\kap}^{\kapShare-1} & =  \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte  \\
  \Steady{\kap} & =  \left(\frac{\kapShare}{\discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte}\right)^{\frac{1}{1-\kapShare}} .
\end{aligned}\end{gathered}
```

Thus {math}`\Steady{\kap}` is higher when capital's share of output, {math}`\kapShare`, is higher, and lower when consumers are more impatient, population grows faster, capital depreciates faster, or productivity grows faster. Faster productivity growth lowers it for the reason behind the [growth impatience condition](#eq:PatWGroCond): consumers who know they will be richer in the future want to spend more today. When productivity grows, it is also lower when {math}`\CRRA` is higher: consumers who dislike differences in consumption over time save less when they expect their consumption to grow.

:::{margin}
Strictly, {math}`\Steady{\kap}` rises with {math}`\kapShare` when {math}`\kapShare/(\discRte+\PopnGroRte+\deprRte+\CRRA\PtyGroRte) > e^{-(1-\kapShare)/\kapShare}`, which holds for any plausible parameters: with the notebook's, the left side is 1.76 and the right 0.097.
:::

## A Phase Diagram

The RCK model's steady state has an analytical solution, but its transition
does not. The usual tool for analyzing it is a [phase diagram](https://en.wikipedia.org/wiki/Phase_portrait) in {math}`\cNrm` and {math}`\kap`.

The first step is to find where the system's differential equations are
zero. By {eq}`eq:RCK-kdot`, {math}`\dot{\kap}=0` implies

```{math}
:label: eq:RCK-kdotEq0

\begin{gathered}\begin{aligned}
  \cNrm & =  \fFunc(\kap) - (\PtyGroRte +\PopnGroRte+\deprRte) \kap 
\end{aligned}\end{gathered}
```

and the {math}`\dot{\cNrm}/\cNrm=0` locus is the constant {math}`\Steady{\kap}` found above.
The two loci divide the diagram into its phases, as {numref}`fig:RamseySSPlot` shows.

:::{figure} figures/RamseySSPlot.png
:name: fig:RamseySSPlot

{math}`\dot{\cNrm}/\cNrm =0` and {math}`\dot{\kap}=0` Loci

Note: With {math}`\CRRA=2`, {math}`\kapShare=0.3`, {math}`\discRte=0.02`, {math}`\PopnGroRte=0.01` and {math}`\deprRte=0.08`, and productivity growth {math}`\PtyGroRte` of 0.03 (low) or 0.06 (high); the dotted line marks the golden rule when {math}`\PtyGroRte` is low. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::

## Transition

The two differential equations and {math}`\kap_{0}` don't pin down {math}`\cNrm_{0}`: every starting {math}`\cNrm_{0}` traces a path. Together with the requirement that capital stay positive, the transversality condition picks one:

:::{margin}
The transversality condition is an optimality condition, not the intertemporal budget constraint. The requirement that capital stay positive, {math}`\kap > 0`, rules out ending with negative wealth in present value; the transversality condition rules out ending with positive wealth in present value, capital that is never consumed. Together they make the intertemporal budget constraint hold with equality. [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) shows that the condition sets the present value of capital in the far future to zero, in discrete and in continuous time.
:::

```{math}
:label: eq:tvc

\begin{gathered}\begin{aligned}
  \lim_{t \rightarrow \infty} e^{-\int_{0}^{t} (\rfree_{\tau} -\PopnGroRte -\PtyGroRte)\,d\tau }\kap_{t} & =  0.
\end{aligned}\end{gathered}
```

{numref}`fig:RamseySaddlePlot` shows three paths for {math}`\cNrm` and {math}`\kap` that satisfy the dynamic equations for consumption and assets, {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot`, all from the same {math}`\kap_{0}`. The path that starts above the middle one, the "saddle path," runs capital to zero in finite time, after which consumption would have to collapse, which the Euler equation forbids. The path that starts below it accumulates capital past the golden rule, toward the point where the {math}`\dot{\kap}=0` locus meets the {math}`\kap` axis, with consumption falling toward zero; there the interest rate is below {math}`\PopnGroRte+\PtyGroRte`, so the discount term grows without bound and the [transversality condition](#eq:tvc) fails. Only the saddle path satisfies all three conditions.

:::{figure} figures/RamseySaddlePlot.png
:name: fig:RamseySaddlePlot

Transition to the Steady State

Note: The same economy, with {math}`\PtyGroRte=0.03`. From {math}`\kap=0.5`, consumption 10 percent above the saddle path runs the capital stock down to zero, and consumption 10 percent below it accumulates capital past the golden rule, marked by the dotted line. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::

:::{margin}
The steady state is a saddle point. Linearize the system there: its Jacobian matrix, the derivatives of {math}`\dot{\kap}` and {math}`\dot{\cNrm}` with respect to {math}`\kap` and {math}`\cNrm`, has {math}`\partial\dot{\kap}/\partial\cNrm = -1` and {math}`\partial\dot{\cNrm}/\partial\cNrm = 0`, so its determinant is {math}`\partial\dot{\cNrm}/\partial\kap = \Steady{\cNrm}\fFunc^{\prime\prime}(\Steady{\kap})/\CRRA < 0`, and its two eigenvalues have opposite signs: one direction converges to the steady state, and the other diverges. The saddle path is the converging one; the stable eigenvalue, in absolute value, is the model's speed of convergence, which {cite:t}`barro&salaimartin:book`, chapter 2, compare with the speed observed across countries and regions.
:::

How much of observed growth can the transition explain? Little, {cite:t}`king&rebelo:trans` argue: with plausible parameters, an economy far enough below its steady state for the transition to account for much of its growth would have implausibly high interest rates early on.

[Decentralizing the Ramsey/Cass-Koopmans Model](#sec:decentralizingrck) shows that, under special conditions, competitive households and firms, taking prices as given, reproduce the planner's allocation, and [The Ramsey/Cass-Koopmans (RCK) Model with Government](#sec:RCKWithGov) adds government spending, taxes and debt.

## Appendix: Numerical Solution

Since the transition has, in general, no analytical solution, its quantitative implications must be computed. This appendix shows how, for students beginning research on growth models.

The most straightforward numerical method for perfect foresight
models of this kind is the
"time elimination" method {cite:p}`Mulligan&sm:transdynam`. It starts from

```{math}
\begin{gathered}\begin{aligned}
    \left(\frac{d\cNrm/dt}{d\kap/dt}\right) &=  d\cNrm/d\kap.
  \end{aligned}\end{gathered}
```

By {eq}`eq:cdotOc`,

```{math}
:label: eq:cdot

\begin{gathered}\begin{aligned}
    \dot{\cNrm} & =   \CRRA^{-1}(\fFunc^{\prime}(\kap)-\discRte -(\PopnGroRte+\deprRte)-\CRRA \PtyGroRte)\cNrm ,
  \end{aligned}\end{gathered}
```

so

```{math}
\begin{gathered}\begin{aligned}
    d\cNrm/d\kap & =  \left(\frac{(\kapShare \kap^{\kapShare-1}-\discRte -(\PopnGroRte+\deprRte)-\CRRA \PtyGroRte)\cNrm}
                       {\CRRA(\kap^{\kapShare} - \cNrm - (\PtyGroRte +\PopnGroRte+\deprRte) \kap)}\right)
  \end{aligned}\end{gathered}
```

which is a differential equation with, in general, no analytical solution. Many numerical math packages can solve it, yielding a numerical version of the {math}`\cFunc(\kap)` function.

One problem: at the steady state both {math}`\dot{\cNrm}` and {math}`\dot{\kap}` are zero, so the right-hand side of this equation is {math}`0/0`, and the solution cannot start there. It starts instead a small step {math}`\epsilon` away from the steady state on each side, along the saddle path's slope there, and integrates the equation outward, away from the steady state: once down toward {math}`\kap=0`, yielding {math}`\cFunc_{-}(\kap)`, and once up to some large value of {math}`\kap`, yielding {math}`\cFunc_{+}(\kap)`. The slope comes from the system linearized at the steady state: it is the direction of the eigenvector with the negative eigenvalue, the one direction from which the economy converges. Within {math}`\epsilon` of the steady state, the consumption function is the straight line along that slope.

{cite:t}`judd:book` covers numerical methods for saddle paths more generally. The [notebook](RamseyCassKoopmans.ipynb) solves the model this way and draws both figures; run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
