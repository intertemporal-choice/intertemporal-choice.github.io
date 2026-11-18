(sec:HamiltonianVSDiscrete)=
# Ramsey Growth in Discrete and Continuous Time

This section derives the optimality conditions of a continuous-time version of the Ramsey/Cass-Koopmans (RCK) model, without productivity growth, using the Hamiltonian, and maps each to its counterpart in the discrete-time (Bellman) solution. It ends with the equation that unites the two methods, the Hamilton-Jacobi-Bellman (HJB) equation, the form in which modern macroeconomics usually writes continuous-time problems.

## The Problem, in Continuous and Discrete Time

The problem is to choose a path of consumption per capita {math}`\cons` from the present moment (arbitrarily called date 0) into the infinite future, {math}`\{\cons\}_{0}^{\infty}`, that solves the problem

:::{margin}
The objective counts each date's per capita utility once, as [the RCK chapter's planner](#eq:RCK-maxprob) does; a note there says what changes when it is weighted by the size of the population.
:::

```{math}
:label: eq:HVD-maxprob

\max_{\{\cons\}_{0}^{\infty}} \int_{0}^{\infty} \uFunc(\cons) e^{-\timeRate t}\,dt
```

subject to

```{math}
\begin{gathered}\begin{aligned}
        \dot{\kap} & =  \fFunc(\kap) - \cons - (\popGro+\depr)\kap
\\      \kap & >  0 ~\forall~t
\end{aligned}\end{gathered}
```

where {math}`\timeRate` is the time preference rate, {math}`\popGro` is the population growth rate, and {math}`\depr` is the depreciation rate. Every variable is a function of time; the argument {math}`t` is omitted. Capital at date 0, {math}`\kap(0)`, is given. Write {math}`\rfree \equiv \fFunc^{\prime}(\kap)-\depr` for the net return on capital, so that {math}`\rfree-\popGro` is its return per person, net of the dilution that population growth brings. All of these rates are measured at an annual rate.

:::{margin}
The population growth rate is written {math}`\PopnGroRte`: {math}`\PopnGroFac` is the population's growth factor and {math}`\lnat` is the natural log, so {math}`\PopnGroRte = \log \PopnGroFac`. In discrete time, where the population grows by the factor {math}`\PopnGroFac` a period, {math}`\PopnGroRte` stands for the net rate {math}`\PopnGroFac-1`, which it approximates when growth is slow.
:::

The discrete-time version of the problem measures the state at the start of period {math}`t` by market resources, {math}`\mNrm_{t} = \fFunc(\kap_{t}) + (1-\depr)\kap_{t}`. What is not consumed becomes the next period's capital, shared among a population larger by the factor {math}`1+\popGro`, and the value function {math}`\VFunc` satisfies the Bellman equation:

```{math}
:label: eq:HVD-bellman

\begin{gathered}\begin{aligned}
        \kap_{t+1} & =  (\mNrm_{t}-\cons_{t})/(1+\popGro)
\\      \VFunc(\mNrm_{t}) & =  \max_{\cons_{t}} \{\uFunc(\cons_{t}) + \Discount \VFunc(\mNrm_{t+1})\} .
\end{aligned}\end{gathered}
```

Its first-order condition and the envelope theorem give

```{math}
:label: eq:HVD-discFOC

\uFunc^{\prime}(\cons_{t}) = \VFunc^{\prime}(\mNrm_{t})
```

and

```{math}
:label: eq:HVD-discEuler

\VFunc^{\prime}(\mNrm_{t}) = \Discount \Rfree_{t+1} \VFunc^{\prime}(\mNrm_{t+1}), \qquad \Rfree_{t+1} \equiv (1+\fFunc^{\prime}(\kap_{t+1})-\depr)/(1+\popGro),
```

where {math}`\Rfree_{t+1}` is the gross return, per person, on a unit of resources saved in period {math}`t`.

## The Hamiltonian's Conditions

The value of the continuous-time problem as a function of initial capital is {math}`\VFuncCts(\kap)`, a curly V to parallel the roman {math}`\VFunc` of the discrete-time value function.

The current-value Hamiltonian is

```{math}
:label: eq:hamilt

\Ham(\kap,\cons,\vk) = \uFunc(\cons) + (\fFunc(\kap)-\cons-(\popGro+\depr)\kap)\vk
```

where {math}`\kap` is the state variable, {math}`\cons` is the control variable, and
{math}`\vk` is the costate variable.

{math}`\vk` is the continuous-time equivalent of a Lagrange
multiplier, so its value should be equivalent to the value of relaxing
the corresponding constraint by an infinitesimal amount. But the
constraint in question is the capital-accumulation constraint. Thus
{math}`\vk` should be equal to the value of having a tiny bit more
capital, {math}`\frac{\VFuncCts(\kap+\Delta \kap)-\VFuncCts(\kap)}{\Delta \kap}`. In other words,
you can think of {math}`\vk=\VFuncCts'(\kap)`.

The condition for optimal consumption is

```{math}
:label: eq:uceqvk

\begin{gathered}\begin{aligned}
        \frac{\partial \Ham}{\partial \cons} & =  0  \\
        \uFunc^{\prime}(\cons) & =  \vk
\\  \uFunc^{\prime}(\cons) & =  \VFuncCts'(\kap) .
\end{aligned}\end{gathered}
```

This is the counterpart of the discrete-time [first-order condition](#eq:HVD-discFOC), {math}`\uFunc^{\prime}(\cons_{t})=\VFunc^{\prime}(\mNrm_{t})`, so the intuition for why the marginal utility of consumption should equal the marginal value of extra resources carries over to it.

:::{margin}
In discrete time the identity holds for market resources {math}`\mNrm_{t}`; as the period shrinks, the output produced within it vanishes and {math}`\mNrm_{t}` becomes {math}`\kap_{t}`, so in continuous time capital is the right measure.
:::

The costate equation is

```{math}
:label: eq:lamgrow

\begin{gathered}\begin{aligned}
        \dot{\vk} & =  \timeRate\vk - \vk(\fFunc^{\prime}(\kap)-(\popGro+\depr))
\\      \dot{\vk}/\vk & =  \timeRate-(\rfree-\popGro) .
\end{aligned}\end{gathered}
```

The accumulation equation for capital must also hold,

```{math}
:label: eq:accum

\dot{\kap} = \fFunc(\kap)-\cons-(\popGro+\depr)\kap,
```

the continuous-time counterpart of the [discrete-time accumulation equation](#eq:HVD-bellman), which we have previously called the Dynamic Budget Constraint.

## The Costate Equation as a Limit

Up to now in this course we haven't thought very much about what the
time period is. Generally, we have expressed things in terms of
yearly rates, so that for example we might choose {math}`\Rfree=1.04` and
{math}`\Discount=1/1.04` to represent an interest rate of
4 percent and a discount rate of 4 percent.

One of the attractive features of the time-consistent model we have
been using is that it generates self-similar behavior as the time interval is
changed. A quarterly version of the model takes the fourth roots, {math}`\Rfree=1.04^{1/4} \approx 1.0099` and {math}`\Discount=1.04^{-1/4}`, and implies
consumption of almost exactly 1/4 of the amount implied by the annual
model, so that four quarters of such behavior would aggregate to the
prediction of the annual model. In general, dividing the year into {math}`J` periods makes the per-period factors the {math}`J`th roots of the annual ones.

In this model the per-period factors are {math}`\Discount = e^{-\timeRate/J}` and {math}`\Rfree_{t+1} \approx e^{(\rfree-\popGro)/J}`. Taking logs of the [discrete-time Euler equation](#eq:HVD-discEuler),

```{math}
\log \VFunc^{\prime}(\mNrm_{t+1}) - \log \VFunc^{\prime}(\mNrm_{t}) = -\log \Discount - \log \Rfree_{t+1} \approx (\timeRate-(\rfree-\popGro))/J,
```

and multiplying by {math}`J`,

```{math}
:label: eq:vpk

J(\log \VFunc^{\prime}(\mNrm_{t+1}) - \log \VFunc^{\prime}(\mNrm_{t})) \approx \timeRate-(\rfree-\popGro) .
```

The left side is the change in {math}`\log \VFunc^{\prime}` over one period, expressed at an annual rate. As {math}`J \rightarrow \infty`, {math}`\mNrm_{t}` becomes {math}`\kap`, {math}`\VFunc^{\prime}` becomes {math}`\VFuncCts'`, and the left side becomes {math}`(d/dt)\log \VFuncCts'(\kap) = \dot{\vk}/\vk`. The approximations become exact in the limit, which leaves [the costate equation](#eq:lamgrow). So the costate equation of the Hamiltonian method is the discrete-time condition {math}`\VFunc^{\prime}(\mNrm_{t})=\Discount\Rfree_{t+1}\VFunc^{\prime}(\mNrm_{t+1})`, taken to continuous time.

## The Transversality Condition

Finally, the transversality condition is

```{math}
\lim_{t \rightarrow \infty} e^{-\timeRate t} \vk \kap = 0
```

and its discrete-time counterpart is

```{math}
:label: eq:ibc

\lim_{t \rightarrow \infty} \Discount^{t} \uFunc^{\prime}(\cons_{t}) \kap_{t} = 0.
```

By the discrete-time conditions, for any utility function, {math}`\Discount^{t}\uFunc^{\prime}(\cons_{t}) = \uFunc^{\prime}(\cons_{0})/\prod_{s=1}^{t}\Rfree_{s}`, so the condition says {math}`\lim_{t \rightarrow \infty} \kap_{t}/\prod_{s=1}^{t}\Rfree_{s} = 0`: the present value of capital in the far future is zero. (With a constant {math}`\Rfree` it reads {math}`\lim_{t \rightarrow \infty} \Rfree^{-t}\kap_{t} = 0`.) In continuous time, the costate equation gives {math}`e^{-\timeRate t}\vk = \vk(0)e^{-\int_{0}^{t}(\rfree_{\tau}-\popGro)\,d\tau}`, so the condition is {math}`\lim_{t \rightarrow \infty} e^{-\int_{0}^{t}(\rfree_{\tau}-\popGro)\,d\tau}\kap = 0`.

The constraint {math}`\kap > 0`, like the no-Ponzi condition in the consumer's problem, rules out ending with negative wealth in present value; the transversality condition, an optimality condition, rules out ending with positive wealth in present value, which would be capital never consumed. Together they make the intertemporal budget constraint hold with equality.

Among the infinite number of time paths of {math}`\cons` and {math}`\kap` that
satisfy the first-order conditions above, only one also satisfies the
constraint {math}`\kap > 0` and this transversality condition. A path that starts
with consumption too high runs capital to zero in finite time; one that starts
too low accumulates capital past the golden rule, where its return
{math}`\rfree-\popGro` is negative, so the transversality condition fails.

## Consumption Growth

Now differentiate [the condition for optimal consumption](#eq:uceqvk) with respect to time,

```{math}
\dot{\cons} \uFunc^{\prime\prime}(\cons) =  \dot{\vk} ,
```

divide by {math}`\vk = \uFunc^{\prime}(\cons)`, and use [the costate equation](#eq:lamgrow):

```{math}
:label: eq:trans1

\begin{gathered}\begin{aligned}
        \frac{\dot{\cons} \uFunc^{\prime\prime}(\cons)}{\uFunc^{\prime}(\cons)} & =  \timeRate-(\rfree-\popGro)  \\
        \dot{\cons} & =  -\frac{\uFunc^{\prime}(\cons)}{\uFunc^{\prime\prime}(\cons)} (\rfree-\popGro-\timeRate) .
\end{aligned}\end{gathered}
```

For a CRRA utility function {math}`\uFunc(\cons)=\cons^{1-\CRRA}/(1-\CRRA)`, {math}`-\uFunc^{\prime\prime}(\cons) \cons/\uFunc^{\prime}(\cons) = \CRRA`, so this becomes

```{math}
:label: eq:trans2

\dot{\cons}/\cons = \CRRA^{-1}(\rfree-\popGro-\timeRate) ,
```

the counterpart of the discrete-time {math}`\cons_{t+1}/\cons_{t} = (\Discount\Rfree_{t+1})^{1/\CRRA}`.

## The Hamilton-Jacobi-Bellman Equation

Modern treatments write a continuous-time problem like this one as a single equation for its value function, the Hamilton-Jacobi-Bellman (HJB) equation:

```{math}
:label: eq:HVD-hjb

\timeRate \VFuncCts(\kap) = \max_{\cons} \{\uFunc(\cons) + \VFuncCts'(\kap)(\fFunc(\kap)-\cons-(\popGro+\depr)\kap)\} = \max_{\cons} \Ham(\kap,\cons,\VFuncCts'(\kap)) .
```

It is the [Bellman equation](#eq:HVD-bellman) taken to continuous time. Read as an asset-pricing equation, it says that the return required on the value of the problem, {math}`\timeRate \VFuncCts(\kap)`, equals the dividend, the flow of utility {math}`\uFunc(\cons)`, plus the capital gain, {math}`\VFuncCts'(\kap)\dot{\kap}`. Its maximand is the current-value Hamiltonian with the costate set to {math}`\vk = \VFuncCts'(\kap)`, hence the "Hamilton" in its name. Its first-order condition is [the condition for optimal consumption](#eq:uceqvk); and differentiating it with respect to {math}`\kap`, by the envelope theorem, gives {math}`\timeRate \VFuncCts'(\kap) = \VFuncCts''(\kap)\dot{\kap} + \VFuncCts'(\kap)(\rfree-\popGro)`, which, since {math}`\dot{\vk} = \VFuncCts''(\kap)\dot{\kap}`, is [the costate equation](#eq:lamgrow). The Hamiltonian's conditions describe the optimal path from one starting point; the HJB equation describes the whole value function at once, which is what many numerical methods solve for.

Benjamin Moll's [lecture notes on HJB equations](https://benjaminmoll.com/wp-content/uploads/2019/07/Lecture3_2149.pdf) derive the equation from the discrete-time Bellman equation of the neoclassical growth model and show its connection to the Hamiltonian; Wikipedia's [article on the HJB equation](https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi%E2%80%93Bellman_equation) states it in general. {cite:t}`achdouHACT` write the problem of each household facing uninsurable income risk as an HJB equation and the distribution of wealth as a Kolmogorov forward equation, which makes a heterogeneous-agent model a system of two partial differential equations; theirs is the form much of the modern continuous-time literature in macroeconomics uses.

## Summary

Each condition of the continuous-time solution, beside its discrete-time counterpart (consumption growth for CRRA utility):

```{math}
\begin{array}{lll}
  & \text{continuous time} & \text{discrete time}
\\ \text{value} & \timeRate\VFuncCts(\kap) & \VFunc(\mNrm_{t})=\max_{\cons_{t}}\{\uFunc(\cons_{t})
\\ & \quad {}=\max_{\cons}\Ham(\kap,\cons,\VFuncCts'(\kap)) & \quad {}+\Discount\VFunc(\mNrm_{t+1})\}
\\ \text{consumption} & \uFunc^{\prime}(\cons)=\vk=\VFuncCts'(\kap) & \uFunc^{\prime}(\cons_{t})=\VFunc^{\prime}(\mNrm_{t})
\\ \text{marginal value} & \dot{\vk}/\vk=\timeRate-(\rfree-\popGro) & \VFunc^{\prime}(\mNrm_{t})=\Discount\Rfree_{t+1}\VFunc^{\prime}(\mNrm_{t+1})
\\ \text{resources} & \dot{\kap}=\fFunc(\kap)-\cons-(\popGro+\depr)\kap & \kap_{t+1}=(\mNrm_{t}-\cons_{t})/(1+\popGro)
\\ \text{transversality} & \lim_{t\rightarrow\infty}e^{-\timeRate t}\vk\kap=0 & \lim_{t\rightarrow\infty}\Discount^{t}\uFunc^{\prime}(\cons_{t})\kap_{t}=0
\\ \text{consumption growth} & \dot{\cons}/\cons=\CRRA^{-1}(\rfree-\popGro-\timeRate) & \cons_{t+1}/\cons_{t}=(\Discount\Rfree_{t+1})^{1/\CRRA}
\end{array}
```
