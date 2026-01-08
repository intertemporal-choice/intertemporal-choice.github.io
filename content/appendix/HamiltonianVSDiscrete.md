(sec:HamiltonianVSDiscrete)=
# Ramsey Growth in Discrete and Continuous Time
This section solves a continuous-time version of the Ramsey/Cass-Koopmans (RCK) model using the Hamiltonian method, and shows the relationship between that method and the discrete-time approach.

The problem is to choose a path of consumption per capita {math}`\cons` from the present moment (arbitrarily called time 0) into the infinite future, {math}`\{c\}_{0}^{\infty}`, that solves the problem

```{math}
:label: eq:HVD-maxprob

\max_{\{c\}_{0}^{\infty}} \int_{0}^{\infty} \uFunc(\cons) e^{-\timeRate t}
```

subject to

```{math}
\begin{gathered}\begin{aligned}
        \dot{\kap} & =  \fFunc(\kap) - \cons - (\popGro+\depr)\kap 
\\      \kap & >  0 ~\forall~t
\end{aligned}\end{gathered}
```

where {math}`\timeRate` is the time preference rate, {math}`\popGro` is the population growth rate, and {math}`\depr` is the depreciation rate. (In continuous time, we think of all variables as implicitly being a function of time, but it is cumbersome to write, e.g., {math}`\cons(t)` everywhere, so the time argument is omitted; we are also thinking of the initial value of capital at date 0 as being a ‘given’ in the problem, so that {math}`\kap(0)=\bullet` for some specific

:::{margin}
Dealing with continuous-time problems, there is an implicit (t) argument that is never written out.
:::

value of {math}`\bullet`).

To emphasize the similarity between the continuous-time and the discrete-time solutions where we have typically

used the roman {math}`V` to denote value, for the continuous-time problem we define ‘curly’ value as a function of the initial level of capital as {math}`\mathcal{V}(\kap)`.

The current-value (discounted) Hamiltonian is

```{math}
:label: eq:hamilt

\mathcal{H}(\kap,\cons,\lambda) = \uFunc(\cons) + (\fFunc(\kap)-c-(\popGro+\depr)\kap)\lambda
```

where {math}`\kap` is the state variable, {math}`\cons` is the control variable, and

{math}`\lambda` is the costate variable.

{math}`\lambda` is the continuous-time equivalent of a Lagrange

multiplier, so its value should be equivalent to the value of relaxing

the corresponding constraint by an infinitesimal amount. But the

constraint in question is the capital-accumulation constraint. Thus

{math}`\lambda` should be equal to the value of having a tiny bit more

capital, {math}`\frac{\mathcal{V}(\kap+\Delta k)-\mathcal{V}(\kap)}{\Delta k}`. In other words,

you can think of {math}`\lambda=\mathcal{V}'(\kap)`.

The first necessary Hamiltonian condition for optimality is

:::{margin}
This corresponds to {math}`\uFunc^{\prime}(\cons_{t})=\VFunc^{\prime}(x_{t})` in discrete-time model.
:::

```{math}
:label: eq:uceqvk

\begin{gathered}\begin{aligned}
        \frac{\partial \mathcal{H}}{\partial c} & =  0  \\
        \uFunc^{\prime}(\cons) & =  \lambda %
\\  \uFunc^{\prime}(\cons) & =  \mathcal{V}'(\kap) .
\end{aligned}\end{gathered}
```

Note the similarity between {eq}`eq:uceqvk` and the result we

usually obtain by using the Envelope theorem in the discrete-time

:::{margin}
Basically only difference is {math}`x_{t}` versus {math}`\kap_{t}`.  {math}`\kap_{t}` is the right measure in a continuous-time model.
:::

problem,

```{math}
\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(\cons_{t}) & =  \VFunc^{\prime}(\kap_{t})
.
\end{aligned}\end{gathered}
```

Thus, you can use the intuition you (should have) developed by now

about why the marginal utility of consumption should be equal to the

marginal value of extra resources to understand this Hamiltonian optimality

condition.

The second necessary condition is

:::{margin}
This corresponds to {math}`\VFunc^{\prime}(x_{t})=\Discount \Rfree \VFunc^{\prime}(x_{t+1})`.
:::

```{math}
:label: eq:lamgrow

\begin{gathered}\begin{aligned}
        \dot{\lambda} & =  \timeRate\lambda - \lambda(\fFunc^{\prime}(\kap)-(\popGro+\depr)) %
\\      \left(\frac{\dot{\lambda}}{\lambda}\right) & =  \timeRate-(\fFunc^{\prime}(\kap)-(\popGro+\depr))
\end{aligned}\end{gathered}
```

which expresses the growth rate of {math}`\lambda` at an annual rate (because

the interest rate {math}`\rfree` and time preference rate {math}`\timeRate` are measured at an annual rate).

To interpret this in terms of our discrete-time model, begin with

the condition

```{math}
\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\kap_{t}) & =  \Rfree\Discount \VFunc^{\prime}(\kap_{t+1}).
\end{aligned}\end{gathered}
```

The final necessary condition is just that the accumulation equation for

capital is satisfied,

```{math}
:label: eq:accum

\dot{\kap} = \fFunc(\kap)-c-(\popGro+\depr)\kap.
```

This is the continuous-time equivalent of what we have previously called

the Dynamic Budget Constraint.

:::{margin}
Emphasize that {math}`\dot{\lambda}/\lambda` is at an annual rate.
:::

Up to now in this course we haven’t thought very much about what the

time period is. Generally, we have expressed things in terms of

yearly rates, so that for example we might choose {math}`\Rfree=1.04` and

{math}`\Discount=1/(1+\timeRate)=1/(1.04)` to represent an interest rate of

4 percent and a discount rate of 4 percent.

One of the attractive features of the time-consistent model we have

been using is that it generates self-similar behavior as the time interval is

changed. Thus if we wanted to solve a quarterly version of the model

we would choose {math}`\Rfree=1.01` and {math}`\Discount=1/1.01` and it would imply

consumption of almost exactly 1/4 of the amount implied by the annual

model, so that four quarters of such behavior would aggregate to the

prediction of the annual model.

To put this in the most general form, suppose {math}`\Rfree` and {math}`\Discount`

correspond to ‘annual rate’ values and we want to divide the year into

{math}`m` periods. Then the appropriate interest rate and discount factor

on a per-period basis would be {math}`\Rfree^{1/m}` and {math}`\Discount^{1/m}`. Thus the

discrete-time equation could be rewritten

```{math}
\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\kap_{t}) & =  \Rfree^{1/m}\Discount^{1/m} \VFunc^{\prime}(\kap_{t+1})
\end{aligned}\end{gathered}
```

where the time interval is now {math}`1/m`th of a year (e.g. if {math}`m`=52,

we’re talking weekly, so that period {math}`t+1` is one week after period

{math}`t`). Now we can use our old friend, the fact that {math}`e^{z} \approx 1+z`,

to note that this is approximately

```{math}
:label: eq:vpk

\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\kap_{t}) & \approx  [e^{\rfree}]^{1/m}[e^{-\timeRate}]^{1/m} \VFunc^{\prime}(\kap_{t+1})  
\\   & =  e^{(1/m)\rfree}e^{-(1/m)\timeRate} \VFunc^{\prime}(\kap_{t+1})       
\\       & =  e^{(1/m)(\rfree-\timeRate)} \VFunc^{\prime}(\kap_{t+1})  
\\       & =  e^{(1/m)(\rfree-\timeRate)} (\VFunc^{\prime}(\kap_{t})+\Delta \VFunc^{\prime}(\kap_{t+1}))
\\      1 & =  e^{(1/m)(\rfree-\timeRate)} \left(\frac{\VFunc^{\prime}(\kap_{t})+\Delta \VFunc^{\prime}(\kap_{t+1})}{\VFunc^{\prime}(\kap_{t})}\right)
\\      e^{(1/m)(\timeRate-\rfree)} & =  \left(\frac{\VFunc^{\prime}(\kap_{t})+\Delta \VFunc^{\prime}(\kap_{t+1})}{\VFunc^{\prime}(\kap_{t})}\right)
\\ \VFunc^{\prime}(\kap_{t})(\underbrace{e^{(1/m)(\timeRate - \rfree)}-1}_{\approx 1+(1/m)(\timeRate-\rfree)-1}) & =  \Delta \VFunc^{\prime}(\kap_{t+1})
\\  \frac{\Delta \VFunc^{\prime}(\kap_{t+1})}{\VFunc^{\prime}(\kap_{t})}                  & \approx  (1/m)(\timeRate - \rfree) 
\\  \frac{m\Delta \VFunc^{\prime}(\kap_{t+1})}{\VFunc^{\prime}(\kap_{t})}             & \approx  (\timeRate - \rfree) 
%\\ \VFunc^{\prime}(\kap_{t+n})-\VFunc^{\prime}(\kap_{t}) & \approx  \VFunc^{\prime}(\kap_{t})(\timeRate-\rfree)
.
\end{aligned}\end{gathered}
```

We defined the interest rate and time preference

rate on an annual basis, but the time interval between {math}`t` and {math}`t+1`

is only {math}`(1/m)`th of a year. Thus {math}`m \Delta \VFunc^{\prime}(\kap_{t+1})` expresses

the speed of change in {math}`\VFunc^{\prime}(\kap_{t})` at an annual rate.

:::{margin}
Recall that {math}`\dot{\lambda}/\lambda` was expressed at an annual rate.
:::

Now, note that since the effective interest rate in this model is

{math}`\fFunc^{\prime}(\kap)-(\popGro+\depr)`, equation {eq}`eq:vpk` is basically the same as

{eq}`eq:lamgrow` since {math}`\lambda = \mathcal{V}'(\kap)` and {math}`m \Delta 
 \VFunc^{\prime}(\kap_{t+1}) = (d/dt)\mathcal{V}'(\kap) = \dot{\lambda}`. Hence, the

second optimality condition in the Hamiltonian optimization method is

basically equivalent to the condition {math}`\VFunc^{\prime}(\kap_{t})=\Rfree\Discount \VFunc^{\prime}(\kap_{t+1})`

from the discrete-time optimization method!

The final required condition (the transversality constraint)

:::{margin}
This corresponds to the intertemporal budget constraint.
:::

is

```{math}
\begin{gathered}\begin{aligned}
        \lim_{t \rightarrow \infty} \lambda \kap e^{-\timeRate t}& =  0 
\end{aligned}\end{gathered}
```

The translation of this into the discrete-time model is

```{math}
:label: eq:ibc

\lim_{t \rightarrow \infty} \Discount^{t} \uFunc^{\prime}(\cons_{t}) \kap_{t} = 0.
```

Consider the simple model with a constant gross interest rate {math}`\Rfree` and CRRA

utility. In that model, recall that {math}`\cons_{t+1}= (\Rfree\Discount)^{1/\CRRA} 
 \cons_{t}`. Thus considered from time zero {eq}`eq:ibc` becomes

```{math}
\begin{gathered}\begin{aligned}
        \lim_{t \rightarrow \infty} \Discount^{t} (\cons_{0} ((\Rfree\Discount)^{1/\CRRA})^{t})^{-\CRRA} \kap_{t} & =  0
\\  & =  \cons_{0}^{-\CRRA} \Discount^{t}[(\Rfree\Discount)^{t/\CRRA}]^{-\CRRA} \kap_{t}
\\  & =  \cons_{0}^{-\CRRA} \Discount^{t} \Discount^{-t} \Rfree^{-t} \kap_{t}
\\  & =  \cons_{0}^{-\CRRA} \Rfree^{-t} \kap_{t}
\\ \rightarrow \lim_{t \rightarrow \infty} \Rfree^{-t} \kap_{t} & =  0
.
\end{aligned}\end{gathered}
```

What this says is that you cannot behave in such a way that you expect

{math}`\kap_{t}` to grow faster than the interest rate

forever.[^h2DGSZMi5A]

[^h2DGSZMi5A]: Note that this also rules out negative {math}`\kap_{t}` values that grow faster than the interest rate. This is the

infinite-horizon version of the intertemporal budget constraint.

Among the infinite number of time paths of {math}`\cons` and {math}`\kap` that

will satisfy the first order conditions above, only one will also

satisfy this transversality constraint - because all the others imply

a violation of the intertemporal budget constraint.

% \section{The Consumption Euler Equation}

Now differentiate {eq}`eq:uceqvk` with respect to time

```{math}
\begin{gathered}\begin{aligned}
        \dot{\cons} \uFunc^{\prime\prime}(\cons) & =  \dot{\lambda}
\end{aligned}\end{gathered}
```

and substitute this into equation {eq}`eq:lamgrow` to get

```{math}
:label: eq:trans1

\begin{gathered}\begin{aligned}
        \frac{\dot{\cons} \uFunc^{\prime\prime}(\cons)}{\uFunc^{\prime}(\cons)} & =  (\timeRate-(\fFunc^{\prime}(\kap)-(\popGro+\depr)))  \\
        \dot{\cons} & =  -\frac{\uFunc^{\prime}(\cons)}{\uFunc^{\prime\prime}(\cons)} (\fFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate) 
      \end{aligned}\end{gathered}
```

using the fact

derived earlier that for a CRRA utility function

{math}`\uFunc(\cons)=c^{1-\CRRA}/(1-\CRRA), -\uFunc^{\prime\prime}(\cons) c/\uFunc^{\prime}(\cons) = \CRRA`,, this becomes

```{math}
:label: eq:trans2

\begin{gathered}\begin{aligned}
         & =  (\cons/\CRRA) (\fFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate) 
\\  \dot{\cons}/\cons & =  \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate)
\end{aligned}\end{gathered}
```

