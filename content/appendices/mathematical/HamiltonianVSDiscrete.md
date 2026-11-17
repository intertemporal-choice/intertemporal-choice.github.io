(sec:HamiltonianVSDiscrete)=
# Ramsey Growth in Discrete and Continuous Time

This section solves a continuous-time version of the Ramsey/Cass-Koopmans (RCK) model, without productivity growth, using the Hamiltonian method, and shows the relationship between that method and the discrete-time approach.

The problem is to choose a path of consumption per capita {math}`\cons` from the present moment (arbitrarily called date 0) into the infinite future, {math}`\{\cons\}_{0}^{\infty}`, that solves the problem

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

where {math}`\timeRate` is the time preference rate, {math}`\popGro` is the population growth rate, and {math}`\depr` is the depreciation rate. (In continuous time, we think of all variables as implicitly being a function of time, but it is cumbersome to write, e.g., {math}`\cons(t)` everywhere, so the time argument is omitted; we are also thinking of the initial value of capital at date 0 as being a 'given' in the problem, so that {math}`\kap(0)=\bullet` for some specific value of {math}`\bullet`).

:::{margin}
In continuous-time problems there is an implicit {math}`(t)` argument that is never written out.
:::

To emphasize the similarity between the continuous-time and the discrete-time solutions where we have typically
used the roman {math}`V` to denote value, for the continuous-time problem we define 'curly' value as a function of the initial level of capital as {math}`\mathcal{V}(\kap)`.

The current-value Hamiltonian is

```{math}
:label: eq:hamilt

\mathcal{H}(\kap,\cons,\lambda) = \uFunc(\cons) + (\fFunc(\kap)-\cons-(\popGro+\depr)\kap)\lambda
```

where {math}`\kap` is the state variable, {math}`\cons` is the control variable, and
{math}`\lambda` is the costate variable.

{math}`\lambda` is the continuous-time equivalent of a Lagrange
multiplier, so its value should be equivalent to the value of relaxing
the corresponding constraint by an infinitesimal amount. But the
constraint in question is the capital-accumulation constraint. Thus
{math}`\lambda` should be equal to the value of having a tiny bit more
capital, {math}`\frac{\mathcal{V}(\kap+\Delta \kap)-\mathcal{V}(\kap)}{\Delta \kap}`. In other words,
you can think of {math}`\lambda=\mathcal{V}'(\kap)`.

The condition for optimal consumption is

:::{margin}
This corresponds to {math}`\uFunc^{\prime}(\cons_{t})=\VFunc^{\prime}(\mNrm_{t})` in the discrete-time model.
:::

```{math}
:label: eq:uceqvk

\begin{gathered}\begin{aligned}
        \frac{\partial \mathcal{H}}{\partial \cons} & =  0  \\
        \uFunc^{\prime}(\cons) & =  \lambda
\\  \uFunc^{\prime}(\cons) & =  \mathcal{V}'(\kap) .
\end{aligned}\end{gathered}
```

Note the similarity between {eq}`eq:uceqvk` and the result we
usually obtain by using the Envelope theorem in the discrete-time problem,

:::{margin}
In discrete time the identity holds for market resources {math}`\mNrm_{t}`; as the period shrinks, the output produced within it vanishes and {math}`\mNrm_{t}` becomes {math}`\kap_{t}`, so in continuous time capital is the right measure.
:::

```{math}
\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(\cons_{t}) & =  \VFunc^{\prime}(\mNrm_{t})
.
\end{aligned}\end{gathered}
```

Thus, you can use the intuition you (should have) developed by now
about why the marginal utility of consumption should be equal to the
marginal value of extra resources to understand this Hamiltonian optimality
condition.

The costate equation is

:::{margin}
This corresponds to {math}`\VFunc^{\prime}(\mNrm_{t})=\Discount \Rfree \VFunc^{\prime}(\mNrm_{t+1})`.
:::

```{math}
:label: eq:lamgrow

\begin{gathered}\begin{aligned}
        \dot{\lambda} & =  \timeRate\lambda - \lambda(\fFunc^{\prime}(\kap)-(\popGro+\depr))
\\      \left(\frac{\dot{\lambda}}{\lambda}\right) & =  \timeRate-(\fFunc^{\prime}(\kap)-(\popGro+\depr))
\end{aligned}\end{gathered}
```

which expresses the growth rate of {math}`\lambda` at an annual rate (because
the interest rate {math}`\rfree` and time preference rate {math}`\timeRate` are measured at an annual rate).

To interpret this in terms of our discrete-time model, begin with
the condition

```{math}
\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\mNrm_{t}) & =  \Rfree\Discount \VFunc^{\prime}(\mNrm_{t+1}).
\end{aligned}\end{gathered}
```

:::{margin}
Note that {math}`\dot{\lambda}/\lambda` is expressed at an annual rate.
:::

Up to now in this course we haven't thought very much about what the
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
correspond to 'annual rate' values and we want to divide the year into
{math}`J` periods. Then the appropriate interest rate and discount factor
on a per-period basis would be {math}`\Rfree^{1/J}` and {math}`\Discount^{1/J}`. Thus the
discrete-time equation could be rewritten

```{math}
\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\mNrm_{t}) & =  \Rfree^{1/J}\Discount^{1/J} \VFunc^{\prime}(\mNrm_{t+1})
\end{aligned}\end{gathered}
```

where the time interval is now {math}`1/J`th of a year (e.g. if {math}`J=52`,
we're talking weekly, so that period {math}`t+1` is one week after period
{math}`t`). Now we can use our old friend, the fact that {math}`e^{z} \approx 1+z`,
to note that this is approximately

```{math}
:label: eq:vpk

\begin{gathered}\begin{aligned}
        \VFunc^{\prime}(\mNrm_{t}) & \approx  [e^{\rfree}]^{1/J}[e^{-\timeRate}]^{1/J} \VFunc^{\prime}(\mNrm_{t+1})  
\\   & =  e^{(1/J)\rfree}e^{-(1/J)\timeRate} \VFunc^{\prime}(\mNrm_{t+1})       
\\       & =  e^{(1/J)(\rfree-\timeRate)} \VFunc^{\prime}(\mNrm_{t+1})  
\\       & =  e^{(1/J)(\rfree-\timeRate)} (\VFunc^{\prime}(\mNrm_{t})+\Delta \VFunc^{\prime}(\mNrm_{t+1}))
\\      1 & =  e^{(1/J)(\rfree-\timeRate)} \left(\frac{\VFunc^{\prime}(\mNrm_{t})+\Delta \VFunc^{\prime}(\mNrm_{t+1})}{\VFunc^{\prime}(\mNrm_{t})}\right)
\\      e^{(1/J)(\timeRate-\rfree)} & =  \left(\frac{\VFunc^{\prime}(\mNrm_{t})+\Delta \VFunc^{\prime}(\mNrm_{t+1})}{\VFunc^{\prime}(\mNrm_{t})}\right)
\\ \VFunc^{\prime}(\mNrm_{t})(\underbrace{e^{(1/J)(\timeRate - \rfree)}-1}_{\approx 1+(1/J)(\timeRate-\rfree)-1}) & =  \Delta \VFunc^{\prime}(\mNrm_{t+1})
\\  \frac{\Delta \VFunc^{\prime}(\mNrm_{t+1})}{\VFunc^{\prime}(\mNrm_{t})}                  & \approx  (1/J)(\timeRate - \rfree) 
\\  \frac{J\Delta \VFunc^{\prime}(\mNrm_{t+1})}{\VFunc^{\prime}(\mNrm_{t})}             & \approx  (\timeRate - \rfree) 
.
\end{aligned}\end{gathered}
```

We defined the interest rate and time preference
rate on an annual basis, but the time interval between {math}`t` and {math}`t+1`
is only {math}`(1/J)`th of a year. Thus {math}`J \Delta \VFunc^{\prime}(\mNrm_{t+1})` expresses
the speed of change in {math}`\VFunc^{\prime}(\mNrm_{t})` at an annual rate.

:::{margin}
Recall that {math}`\dot{\lambda}/\lambda` was expressed at an annual rate.
:::

Now, note that since the effective interest rate in this model is
{math}`\fFunc^{\prime}(\kap)-(\popGro+\depr)`, equation {eq}`eq:vpk` is basically the same as
{eq}`eq:lamgrow` since {math}`\lambda = \mathcal{V}'(\kap)` and {math}`J \Delta \VFunc^{\prime}(\mNrm_{t+1}) \rightarrow (d/dt)\mathcal{V}'(\kap) = \dot{\lambda}` as {math}`J \rightarrow \infty`. Hence, the
costate equation of the Hamiltonian optimization method is
basically equivalent to the condition {math}`\VFunc^{\prime}(\mNrm_{t})=\Rfree\Discount \VFunc^{\prime}(\mNrm_{t+1})`
from the discrete-time optimization method!

The accumulation equation for capital must also hold,

```{math}
:label: eq:accum

\dot{\kap} = \fFunc(\kap)-\cons-(\popGro+\depr)\kap.
```

This is the continuous-time equivalent of what we have previously called
the Dynamic Budget Constraint.

Finally, the transversality condition is

:::{margin}
This corresponds to the intertemporal budget constraint.
:::

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
 \cons_{t}`. Thus considered from date zero {eq}`eq:ibc` becomes

```{math}
\begin{gathered}\begin{aligned}
        \lim_{t \rightarrow \infty} \Discount^{t} (\cons_{0} ((\Rfree\Discount)^{1/\CRRA})^{t})^{-\CRRA} \kap_{t} & =  \cons_{0}^{-\CRRA} \lim_{t \rightarrow \infty} \Discount^{t}[(\Rfree\Discount)^{t/\CRRA}]^{-\CRRA} \kap_{t}
\\  & =  \cons_{0}^{-\CRRA} \lim_{t \rightarrow \infty} \Discount^{t} \Discount^{-t} \Rfree^{-t} \kap_{t}
\\  & =  \cons_{0}^{-\CRRA} \lim_{t \rightarrow \infty} \Rfree^{-t} \kap_{t} ,
\end{aligned}\end{gathered}
```

so the condition is {math}`\lim_{t \rightarrow \infty} \Rfree^{-t} \kap_{t} = 0`.

What this says is that you cannot behave in such a way that you expect
{math}`\kap_{t}` to grow at least as fast as the interest rate
forever.

:::{margin}
Note that this also rules out negative {math}`\kap_{t}` values that grow at least as fast as the interest rate.
:::

This is the infinite-horizon version of the intertemporal budget constraint.

Among the infinite number of time paths of {math}`\cons` and {math}`\kap` that
satisfy the first-order conditions above, only one also satisfies the
constraint {math}`\kap > 0` and this transversality condition. A path that starts
with consumption too high runs capital to zero in finite time; one that starts
too low accumulates capital past the golden rule, where its return
{math}`\fFunc^{\prime}(\kap)-(\popGro+\depr)` is negative, so the transversality condition fails.

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
{math}`\uFunc(\cons)=\cons^{1-\CRRA}/(1-\CRRA), -\uFunc^{\prime\prime}(\cons) \cons/\uFunc^{\prime}(\cons) = \CRRA`, this becomes

```{math}
:label: eq:trans2

\begin{gathered}\begin{aligned}
        \dot{\cons} & =  (\cons/\CRRA) (\fFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate) 
\\  \dot{\cons}/\cons & =  \CRRA^{-1}(\fFunc^{\prime}(\kap)-(\popGro+\depr)-\timeRate)
\end{aligned}\end{gathered}
```
