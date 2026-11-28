(sec:RamseyCassKoopmans)=
# The Ramsey/Cass-Koopmans (RCK) Model

{cite:t}`ramseySave`, followed much later by {cite:t}`cass:growth` and {cite:t}`koopmans:growth`, formulated the canonical model of optimal growth, presented here for an economy with exogenous "labor-augmenting" technological progress.

:::{margin}
For the facts the model is meant to explain, and the Solow model it builds on, see the undergraduate textbook of {cite:t}`ashrafWeilGrowth`. Graduate textbook treatments are in {cite:t}`blanchard&fischer:text`, chapter 2, {cite:t}`barro&salaimartin:book`, chapter 2, and {cite:t}`acemogluGrowth`, chapter 8. [Notation in Other Treatments](#sec:RCK-notationCrosswalk) translates the symbols of {cite:t}`romer:text` and {cite:t}`acemogluGrowth` into this chapter's.
:::

## The Budget Constraint

The economy has a perfectly competitive production sector that uses a constant-returns-to-scale Cobb-Douglas production function

:::{margin}
States and controls are functions of time; time subscripts appear only where clarity needs them.
:::

```{math}
\begin{gathered}\begin{aligned}
                   \YLvl & =  \FFunc(\KLvl,\PtyLab \LLvl) = \KLvl^{\kapShare}(\PtyLab \LLvl)^{1-\kapShare}
\end{aligned}\end{gathered}
```

:::{margin}
An important insight here is that all of output is absorbed by payments to labor and to capital; there is nothing left over (say, to fund corporate research to invent new technologies to augment productivity). [What Endogenous Growth Requires](#sec:Endogenous) starts from this point.
:::

to produce output using capital and labor. Under perfect competition firms must make zero profits in equilibrium, which means, by [Euler's theorem](#fact:eulerstheorem), that

```{math}
:label: eq:RCK-outputExhausted

\YLvl = \FFunc_{\KLvl}\KLvl + \FFunc_{\LLvl}\LLvl , \qquad \FFunc_{\KLvl} \equiv \partial\YLvl/\partial\KLvl , \quad \FFunc_{\LLvl} \equiv \partial\YLvl/\partial\LLvl .
```

Labor hours (the same as population) increase exogenously at a constant rate

:::{margin}
The population growth rate is written {math}`\PopnGroRte`: {math}`\PopnGroFac` is the population's growth factor and {math}`\lnat` is the natural log, so {math}`\PopnGroRte = \log \PopnGroFac`.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\LLvl}/\LLvl & =  \PopnGroRte ,
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

Lower case variables are the upper case version divided by efficiency units, so {math}`\yNrm = \YLvl/(\PtyLab \LLvl) = (\KLvl/(\PtyLab \LLvl))^{\kapShare} = \kNrm^{\kapShare}`. Since {math}`\kNrm = \KLvl/(\PtyLab \LLvl)`,

:::{margin}
NOT per capita; this makes the "[balanced growth](#sec:RCK-SteadyState)" path a steady state.
:::

```{math}
\dot{\kNrm}/\kNrm = \dot{\KLvl}/\KLvl - \dot{\PtyLab}/\PtyLab - \dot{\LLvl}/\LLvl = \dot{\KLvl}/\KLvl - (\PtyGroRte +\PopnGroRte),
```

so dividing {eq}`eq:Kdotlevel` by {math}`\PtyLab \LLvl` and using it gives

```{math}
:label: eq:RCK-kdot

\dot{\kNrm} = \fFunc(\kNrm) - \cNrm - (\PtyGroRte +\PopnGroRte+\deprRte) \kNrm .
```

A steady state is a point where {math}`\dot{\kNrm} = 0`, so that

```{math}
:label: eq:RCK-cSteadyState

\cNrm = \fFunc(\kNrm) - (\PtyGroRte +\PopnGroRte+\deprRte) \kNrm .
```

A first candidate for the best steady state is the one with the highest {math}`\cNrm`. Maximizing steady-state consumption with respect to {math}`\kNrm` requires

```{math}
\frac{d\cNrm}{d\kNrm} = \fFunc^{\prime}(\kNrm) - (\PtyGroRte +\PopnGroRte+\deprRte) = 0 ,
```

and since {math}`d^{2}\cNrm/d\kNrm^{2} = \fFunc^{\prime\prime}(\kNrm) < 0`, this is a maximum. The capital stock that satisfies it, {math}`\GoldRule{\kNrm}`, obeys the "golden rule" of {cite:t}`phelps:golden`:

:::{margin}
Phelps called it the "golden rule" on the grounds that every generation does unto its successors what it would want its ancestors to have done unto it. You might worry that the argument doesn't make sense, because what is really being equalized across generations is consumption per efficiency unit of labor, and no extant texts of the Christian New Testament quote Jesus as having said "do unto other efficiency units of labor as you, an efficiency unit of labor yourself, would have liked the ancestral efficiency units to have done unto you." Keep reading.
:::

```{math}
:label: eq:RCK-goldenRule

\fFunc^{\prime}(\GoldRule{\kNrm}) = \PtyGroRte +\PopnGroRte+\deprRte .
```

One more unit of {math}`\kNrm` adds {math}`\fFunc^{\prime}(\kNrm)` to output, but holding it steady as effective labor grows and capital depreciates takes {math}`\PtyGroRte +\PopnGroRte+\deprRte` more investment; consumption is highest where the two are equal. With the Cobb-Douglas {math}`\fFunc(\kNrm) = \kNrm^{\kapShare}`, the golden rule is

```{math}
:label: eq:RCK-goldenRuleCobbDouglas

\GoldRule{\kNrm} = \left(\kapShare/(\PtyGroRte +\PopnGroRte+\deprRte)\right)^{1/(1-\kapShare)} .
```

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
  \PtyLab _{t} & =  \PtyLab _{0}e^{\PtyGroRte t} ,
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
\dot{\kNrm} = \kNrm^{\kapShare}-\cNrm-(\PopnGroRte+\PtyGroRte+\deprRte)\kNrm,
```

whose current-value Hamiltonian is

:::{margin}
If the Hamiltonian is new to you, Peter Thompson's [lecture notes on optimal control](https://www.andrew.cmu.edu/course/88-737/optimal_control/optimal_control.pdf) derive the method from the economics of a firm's capital problem, and later work through this model. Wikipedia's [worked example of the RCK model](https://en.wikipedia.org/wiki/Hamiltonian_\(control_theory\)#Example:_Ramsey%E2%80%93Cass%E2%80%93Koopmans_model) uses the present-value Hamiltonian instead, whose costate is this one discounted to date zero.
:::

```{math}
\Ham(\kNrm,\cNrm,\vk) = \uFunc(\cNrm) + (\kNrm^{\kapShare} - \cNrm - (\PopnGroRte+\PtyGroRte+\deprRte)\kNrm)\vk.
```

The maximum principle gives the conditions that an optimal path satisfies. Here {math}`\kNrm` is the state variable, {math}`\cNrm` the control, {math}`\vk` the costate (the shadow value of capital, in units of utility), and {math}`\discRte-(1-\CRRA)\PtyGroRte` the rate at which the objective discounts. The conditions are:

:::{margin}
{cite:t}`acemogluGrowth`, chapter 7, states and proves the maximum principle, including its transversality condition.
:::

- optimization: the control maximizes the Hamiltonian at each date, {math}`\partial\Ham/\partial\cNrm = 0`;
- the costate equation: {math}`\dot{\vk} = (\discRte-(1-\CRRA)\PtyGroRte)\vk - \partial\Ham/\partial\kNrm`;
- the state equation: {math}`\dot{\kNrm} = \partial\Ham/\partial\vk`, which restates the constraint;
- transversality: {math}`\lim_{t\rightarrow\infty} e^{-(\discRte-(1-\CRRA)\PtyGroRte)t}\vk_{t}\kNrm_{t} = 0`.

Any problem with one state and one control has the same four conditions, with its own payoff, constraint and discount rate in place of these.

The [current-value Hamiltonian optimization condition](#eq:uceqvk) for consumption requires {math}`\partial 
 \Ham/\partial \cNrm = 0`:

```{math}
:label: eq:RCK-H1A

\cNrm^{-\CRRA} = \vk ,
```

which can be differentiated with respect to time to obtain

```{math}
:label: eq:RCK-margUtilDot

-\CRRA \cNrm^{-\CRRA-1}\dot{\cNrm} = \dot{\vk} .
```

The [current-value Hamiltonian optimization condition](#eq:lamgrow) for capital, the costate equation, requires:

:::{margin}
In the book's mathematical appendices, [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) derives the Hamiltonian's conditions for a version of this model without productivity growth and shows how each relates to the discrete-time Bellman approach.
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\vk} & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \partial \Ham/\partial \kNrm  \\
                & =  (\discRte-(1-\CRRA)\PtyGroRte)\vk - \vk (\fFunc^{\prime}(\kNrm) - (\PopnGroRte+\PtyGroRte+\deprRte))  \\
  \dot{\vk}/{\vk} & =  \discRte+\PopnGroRte+\deprRte+\CRRA \PtyGroRte-\fFunc^{\prime}(\kNrm) .
\end{aligned}\end{gathered}
```

Since {eq}`eq:RCK-H1A` and {eq}`eq:RCK-margUtilDot` give {math}`\dot{\vk}/\vk = -\CRRA\dot{\cNrm}/\cNrm`, this is

```{math}
:label: eq:cdotOc

\dot{\cNrm}/\cNrm = \CRRA^{-1}(\fFunc^{\prime}(\kNrm)-(\PopnGroRte+\deprRte)-\discRte - \CRRA \PtyGroRte),
```

or, with {math}`\rfree \equiv \fFunc^{\prime}(\kNrm) - \deprRte` the interest rate, {math}`\dot{\cNrm}/\cNrm = \CRRA^{-1}(\rfree - \discRte - \PopnGroRte) - \PtyGroRte`.

This Euler equation is called the "Keynes-Ramsey rule," because Ramsey derived it
with an explanation attributed to Keynes.
Apart from the {math}`-\PtyGroRte`, which comes from measuring consumption per efficiency unit, it is like [the Euler equation in the perfect foresight CRRA model](#eq:PFCRRA-cgrow) in continuous time, with two differences: the return that matters is {math}`\rfree-\PopnGroRte` rather than {math}`\rfree`, because population growth dilutes each person's capital, and that return varies over time as {math}`\fFunc^{\prime}(\kNrm)` does.

Since per capita consumption is {math}`\CLvl/\LLvl = \cNrm \PtyLab`, it grows at {math}`\dot{\cNrm}/\cNrm + \PtyGroRte = \CRRA^{-1}(\fFunc^{\prime}(\kNrm)-(\PopnGroRte+\deprRte)-\discRte)`: the same formula, as a function of {math}`\kNrm`, as in the model with no productivity growth, the [Euler equation](#eq:cdotOc) with {math}`\PtyGroRte=0`. Productivity growth matters only through {math}`\kNrm`.

(sec:RCK-SteadyState)=
## The Steady State

Technological progress is assumed to be labor-augmenting because then,
in the steady state, per capita consumption, income
and capital all grow at rate {math}`\PtyGroRte`.

:::{margin}
{cite:t}`ghosDespiteUzawa` discuss how realistic this requirement is.
:::

{math}`\dot{\cNrm}/\cNrm = 0` implies that at the steady-state value of {math}`\Steady{\kNrm}`,

```{math}
:label: eq:RCK-modGoldenRule

\fFunc^{\prime}(\Steady{\kNrm}) = \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte .
```

This is what {cite:t}`cassTurnpike` named the "modified golden rule." Comparing it with the [golden rule](#eq:RCK-goldenRule), {math}`\fFunc^{\prime}(\Steady{\kNrm}) - \fFunc^{\prime}(\GoldRule{\kNrm}) = \discRte - (1-\CRRA)\PtyGroRte`, so {math}`\Steady{\kNrm} < \GoldRule{\kNrm}` exactly when {math}`\discRte > (1-\CRRA)\PtyGroRte`: the assumption that keeps the planner's objective finite also rules out accumulating more capital than the golden rule.

:::{margin}
"Keep reading" might have given you hope that optimizing consumption per person, rather than per efficiency unit, would fix the "golden-rule-per-efficiency-unit" problem. Nope. The trouble is that we study only "balanced growth" equilibria, in which labor productivity grows at a constant rate forever. Suppose instead that AI brings a century of amazing technological progress, after which everything that conduces to growth *has* been discovered and {math}`\PtyLab` stops growing. The generations born a century from now and later will be enormously richer than we are, which would justify massive consumption now. Just sayin'.
:::

Using {math}`\fFunc^{\prime}(\kNrm) = \kapShare \kNrm^{\kapShare-1}`, the modified golden rule gives an analytical formula for the steady state:

```{math}
:label: eq:RCK-kSteadyCobbDouglas

\begin{gathered}\begin{aligned}
  \kapShare \Steady{\kNrm}^{\kapShare-1} & =  \discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte  \\
  \Steady{\kNrm} & =  \left(\frac{\kapShare}{\discRte +\PopnGroRte+\deprRte+\CRRA \PtyGroRte}\right)^{\frac{1}{1-\kapShare}} .
\end{aligned}\end{gathered}
```

Thus {math}`\Steady{\kNrm}` is higher when capital's share of output, {math}`\kapShare`, is higher, and lower when consumers are more impatient, population grows faster, capital depreciates faster, or productivity grows faster. Faster productivity growth lowers it for the reason behind the [growth impatience condition](#eq:PatWGroCond): consumers who know they will be richer in the future want to spend more today. When productivity grows, it is also lower when {math}`\CRRA` is higher: consumers who dislike differences in consumption over time save less when they expect their consumption to grow.

:::{margin}
Strictly, {math}`\Steady{\kNrm}` rises with {math}`\kapShare` when {math}`\kapShare/(\discRte+\PopnGroRte+\deprRte+\CRRA\PtyGroRte) > e^{-(1-\kapShare)/\kapShare}`, which holds for any plausible parameters: with the notebook's, the left side is 1.76 and the right 0.097.
:::

## A Phase Diagram

The RCK model's steady state has an analytical solution, but its transition
does not. The usual tool for analyzing it is a [phase diagram](https://en.wikipedia.org/wiki/Phase_portrait) in {math}`\cNrm` and {math}`\kNrm`.

The first step is to find where the system's differential equations are
zero. By {eq}`eq:RCK-kdot`, {math}`\dot{\kNrm}=0` implies

```{math}
:label: eq:RCK-kdotEq0

\begin{gathered}\begin{aligned}
  \cNrm & =  \fFunc(\kNrm) - (\PtyGroRte +\PopnGroRte+\deprRte) \kNrm ,
\end{aligned}\end{gathered}
```

and the {math}`\dot{\cNrm}/\cNrm=0` locus is the constant {math}`\Steady{\kNrm}` found above.
The two loci, drawn in {numref}`fig:RamseySSPlot` for two rates of productivity growth, divide the diagram into four regions, and the same two equations give the direction of motion in each. Above the {math}`\dot{\kNrm}=0` locus, consumption takes more than {eq}`eq:RCK-kdotEq0` leaves room for, so by {eq}`eq:RCK-kdot` {math}`\dot{\kNrm}<0`; below it, {math}`\dot{\kNrm}>0`. To the left of {math}`\Steady{\kNrm}`, {math}`\fFunc^{\prime}(\kNrm)` is above its steady-state value, because {math}`\fFunc^{\prime\prime}<0`, so by {eq}`eq:cdotOc` {math}`\dot{\cNrm}>0`; to the right of {math}`\Steady{\kNrm}`, {math}`\dot{\cNrm}<0`. So the economy moves:

- up and to the right, below the {math}`\dot{\kNrm}=0` locus and to the left of {math}`\Steady{\kNrm}`;
- up and to the left, above the locus and to the left of {math}`\Steady{\kNrm}`;
- down and to the left, above the locus and to the right of {math}`\Steady{\kNrm}`;
- down and to the right, below the locus and to the right of {math}`\Steady{\kNrm}`.

Only in the regions where it moves up and to the right, or down and to the left, does the economy head toward the steady state, and those are the regions the saddle path of {numref}`fig:RamseySaddlePlot` runs through.

:::{figure} figures/RamseySSPlot.png
:name: fig:RamseySSPlot

{math}`\dot{\cNrm}/\cNrm =0` and {math}`\dot{\kNrm}=0` Loci

Note: With {math}`\CRRA=2`, {math}`\kapShare=0.3`, {math}`\discRte=0.02`, {math}`\PopnGroRte=0.01` and {math}`\deprRte=0.08`, and productivity growth {math}`\PtyGroRte` of 0.03 (low) or 0.06 (high); the dotted line marks the golden rule when {math}`\PtyGroRte` is low. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::

## Transition

The two differential equations and {math}`\kNrm_{0}` don't pin down {math}`\cNrm_{0}`: every starting {math}`\cNrm_{0}` traces a path. Together with the requirement that capital stay positive, the transversality condition picks one:

:::{margin}
The transversality condition is an optimality condition, not the intertemporal budget constraint. The requirement that capital stay positive, {math}`\kNrm > 0`, rules out ending with negative wealth in present value; the transversality condition rules out ending with positive wealth in present value, capital that is never consumed. Together they make the intertemporal budget constraint hold with equality. [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) shows that the condition sets the present value of capital in the far future to zero, in discrete and in continuous time.
:::

```{math}
:label: eq:tvc

\begin{gathered}\begin{aligned}
  \lim_{t \rightarrow \infty} e^{-\int_{0}^{t} (\rfree_{\tau} -\PopnGroRte -\PtyGroRte)\,d\tau }\kNrm_{t} & =  0.
\end{aligned}\end{gathered}
```

This is the maximum principle's transversality condition, rewritten with the interest rate: integrating the costate equation gives {math}`e^{-(\discRte-(1-\CRRA)\PtyGroRte)t}\vk_{t} = \vk_{0}e^{-\int_{0}^{t}(\rfree_{\tau}-\PopnGroRte-\PtyGroRte)\,d\tau}`.

{numref}`fig:RamseySaddlePlot` shows three paths for {math}`\cNrm` and {math}`\kNrm` that satisfy the dynamic equations for consumption and assets, {eq}`eq:cdotOc` and {eq}`eq:RCK-kdot`, all from the same {math}`\kNrm_{0}`. The path that starts above the "saddle path" (the middle one) runs capital to zero in finite time, after which consumption would have to collapse, which the Euler equation forbids. The path that starts below it accumulates capital past the golden rule, toward the point where the {math}`\dot{\kNrm}=0` locus meets the {math}`\kNrm` axis, with consumption falling toward zero; there the interest rate is below {math}`\PopnGroRte+\PtyGroRte`, so the discount term grows without bound and the [transversality condition](#eq:tvc) fails. Only the saddle path satisfies all three conditions.

Why exactly one path? The steady state is a saddle point. Near it, the dynamics are those of the linearized system, whose Jacobian matrix, the derivatives of {math}`\dot{\kNrm}` and {math}`\dot{\cNrm}` with respect to {math}`\kNrm` and {math}`\cNrm` at the steady state, is

```{math}
:label: eq:RCK-Jacobian

\begin{pmatrix} \partial\dot{\kNrm}/\partial\kNrm & \partial\dot{\kNrm}/\partial\cNrm \\ \partial\dot{\cNrm}/\partial\kNrm & \partial\dot{\cNrm}/\partial\cNrm \end{pmatrix}
  = \begin{pmatrix} \discRte-(1-\CRRA)\PtyGroRte & -1 \\ \Steady{\cNrm}\fFunc^{\prime\prime}(\Steady{\kNrm})/\CRRA & 0 \end{pmatrix} .
```

The top left entry is {math}`\fFunc^{\prime}(\Steady{\kNrm})-(\PtyGroRte+\PopnGroRte+\deprRte)`, simplified with the [modified golden rule](#eq:RCK-modGoldenRule). The bottom right entry is zero because {math}`\dot{\cNrm}` is proportional to {math}`\fFunc^{\prime}(\kNrm)-(\discRte+\PopnGroRte+\deprRte+\CRRA\PtyGroRte)`, which is zero at the steady state. The determinant, the product of the two eigenvalues, is {math}`\Steady{\cNrm}\fFunc^{\prime\prime}(\Steady{\kNrm})/\CRRA<0`, so one eigenvalue is negative and the other positive. In the direction that belongs to the positive one, the economy moves away from the steady state; in the direction that belongs to the negative one, it converges. Capital cannot jump, but consumption can, so from each {math}`\kNrm_{0}` exactly one {math}`\cNrm_{0}` starts the economy in the converging direction: the saddle path.

On the saddle path near the steady state, the gap {math}`\kNrm-\Steady{\kNrm}` shrinks at a constant rate, the absolute value of the negative eigenvalue:

```{math}
:label: eq:RCK-convergenceSpeed

\frac{1}{2}\left(\sqrt{(\discRte-(1-\CRRA)\PtyGroRte)^{2}-4\Steady{\cNrm}\fFunc^{\prime\prime}(\Steady{\kNrm})/\CRRA}-(\discRte-(1-\CRRA)\PtyGroRte)\right) .
```

This is the model's speed of convergence. With the notebook's parameters it is 0.14: the gap closes at 14 percent a year, so half of it is gone in five years. {cite:t}`barro&salaimartin:book`, chapter 2, compare the speed with the roughly 2 percent a year that they estimate across countries and across regions within countries. With the notebook's other parameters, the model's speed is that low only if capital's share {math}`\kapShare` is about 0.8, far above the notebook's 0.3.

:::{figure} figures/RamseySaddlePlot.png
:name: fig:RamseySaddlePlot

Transition to the Steady State

Note: The same economy, with {math}`\PtyGroRte=0.03`. From {math}`\kNrm=0.5`, consumption 10 percent above the saddle path runs the capital stock down to zero, and consumption 10 percent below it accumulates capital past the golden rule, marked by the dotted line. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::


The saddle path has, in general, no analytical solution, so the transition must be computed. The [notebook](RamseyCassKoopmans.ipynb) computes it by the "time elimination" method {cite:p}`Mulligan&sm:transdynam`: along the path, {math}`d\cNrm/d\kNrm = \dot{\cNrm}/\dot{\kNrm}`, a differential equation in {math}`\kNrm` alone, which it solves outward from the steady state, starting along the saddle path's slope there. The notebook derives the method and draws the chapter's figures; run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb). {cite:t}`judd:book` covers numerical methods for saddle paths more generally.

How much of observed growth can the transition explain? Little, {cite:t}`king&rebelo:trans` argue: with plausible parameters, an economy far enough below its steady state for the transition to account for much of its growth would have implausibly high interest rates early on.

(sec:RCK-Experiment)=
## A Fall in the Time Preference Rate

The phase diagram's main use is to work out how the economy responds to a change. Suppose the economy is in its steady state when the time preference rate {math}`\discRte` falls, unexpectedly and permanently. By the [modified golden rule](#eq:RCK-modGoldenRule), {math}`\Steady{\kNrm}` rises, so the {math}`\dot{\cNrm}/\cNrm=0` locus moves to the right; the {math}`\dot{\kNrm}=0` locus, {eq}`eq:RCK-kdotEq0`, does not involve {math}`\discRte`, so it stays where it was.

Capital is accumulated, so {math}`\kNrm` cannot jump, but {math}`\cNrm` can, and it must jump onto the new saddle path, since every other path either fails the [transversality condition](#eq:tvc) or runs capital to zero. The old steady state is now to the left of the new {math}`\Steady{\kNrm}`, where the new saddle path lies below the {math}`\dot{\kNrm}=0` locus, so {math}`\cNrm` jumps down. From there the economy moves up and to the right along the new saddle path: {math}`\cNrm` and {math}`\kNrm` both rise, and the interest rate {math}`\rfree` falls as {math}`\kNrm` rises. The new steady state has more capital and, since the new {math}`\Steady{\kNrm}` is still below the golden rule, more consumption. {numref}`fig:RamseyTimePrefFall` shows the jump and the path that follows.

:::{figure} figures/RamseyTimePrefFall.png
:name: fig:RamseyTimePrefFall

Response to a Fall in the Time Preference Rate

Note: The same economy, with {math}`\PtyGroRte=0.03`, when {math}`\discRte` falls from 0.02 to 0.005; the view is enlarged around the two steady states. Consumption jumps down from the old steady state, the open circle, onto the new saddle path, and the economy then moves along it to the new steady state, still below the golden rule, marked by the dotted line. Drawn by the [notebook](RamseyCassKoopmans.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RamseyCassKoopmans.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RamseyCassKoopmans/RamseyCassKoopmans.ipynb).
:::

More patient households give up consumption now to build capital, and are repaid with more consumption later. Per capita consumption, {math}`\cNrm\PtyLab`, jumps down in the same proportion as {math}`\cNrm`, grows faster than {math}`\PtyGroRte` during the transition, and grows at {math}`\PtyGroRte` again once the economy reaches the new steady state.

[Decentralizing the Ramsey/Cass-Koopmans Model](#sec:decentralizingrck) shows that, under special conditions, competitive households and firms, taking prices as given, reproduce the planner's allocation, and [The Ramsey/Cass-Koopmans (RCK) Model with Government](#sec:RCKWithGov) adds government spending, taxes and debt.

(sec:RCK-notationCrosswalk)=
## Notation in Other Treatments

{cite:t}`romer:text`, chapter 2, and {cite:t}`acemogluGrowth`, chapter 8, write the model with different symbols. Both write {math}`\rho` for the time preference rate and {math}`\theta` for relative risk aversion, while this chapter writes variants of the same two letters the other way round: {math}`\discRte` for the time preference rate and {math}`\CRRA` for relative risk aversion.

| | This chapter | Romer | Acemoglu |
|---|:---:|:---:|:---:|
| time preference rate | {math}`\discRte` | {math}`\rho` | {math}`\rho` |
| relative risk aversion | {math}`\CRRA` | {math}`\theta` | {math}`\theta` |
| labor-augmenting productivity | {math}`\PtyLab` | {math}`A` | {math}`A` |
| productivity growth rate | {math}`\PtyGroRte` | {math}`g` | {math}`g` |
| population growth rate | {math}`\PopnGroRte` | {math}`n` | {math}`n` |
| depreciation rate | {math}`\deprRte` | none | {math}`\delta` |
| capital per efficiency unit | {math}`\kNrm` | {math}`k` | {math}`k` |
| consumption per efficiency unit | {math}`\cNrm` | {math}`c` | {math}`c` |
| consumption per person | {math}`\CLvl/\LLvl` | {math}`C` | {math}`\tilde{c}` |
| rate that discounts {math}`\uFunc(\cNrm)` | {math}`\discRte-(1-\CRRA)\PtyGroRte` | {math}`\rho-n-(1-\theta)g` | {math}`\rho-n-(1-\theta)g` |

Romer assumes no depreciation. The last row differs because both books weight each date's utility by the size of the population, which this chapter does not.
