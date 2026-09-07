(sec:BlanchardFiniteHorizon)=
# The Blanchard (1985) Model of Perpetual Youth

This section analyzes a way to relax the standard assumption of infinite
lifetimes in the Ramsey/Cass-Koopmans
growth model. The trick, introduced by
{cite:t}`blanchardFinite`, is to assume that the economy
is populated by agents who face a constant probability of death.

Thus, an agent who has lived a thousand years is no more likely to die
in the next year than an agent who was born yesterday.

Time is measured continuously. If there is an instantaneous
probability {math}`\pDies` of dying, the probability (as viewed by a person
alive in period {math}`t`) of still being alive (not dead) in period
{math}`\tThen` is

```{math}
:label: eq:living

\begin{gathered}\begin{aligned}
        \Alive_{t}^{\tThen} & =  e^{-\pDies(\tThen-t)} . 
\end{aligned}\end{gathered}
```

Assuming the instantaneous utility function is {math}`\uFunc(c) =  \log c`, and that the pure rate of time preference is {math}`\timeRate`,
explain why the objective function at time {math}`t` of an individual
household in this model will be to maximize

```{math}
:label: eq:objfunc

\int_{t}^{\infty} (\log c_{\tThen}) e^{-(\timeRate+\pDies)(\tThen-t)} d\tThen.
```

where {math}`c_{\tThen}` is the consumer's consumption at time {math}`\tThen`. For convenience,
you may wish to define

```{math}
:label: eq:thetahat

\begin{gathered}\begin{aligned}
        \hat{\timeRate} & =  \timeRate+\pDies. 
\end{aligned}\end{gathered}
```

> *Answer:*
>
>
> A consumer with a pure time preference rate of zero will downweight
>
> the utility he receives conditional on being alive by the probability
>
> that he is still alive, yielding a discounted utility of
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \int_{t}^{\infty} (\log c_{\tThen}) \Alive_{t}^{\tThen} e^{-\timeRate (\tThen-t)}d\tThen & =  \int_{t}^{\infty} (\log c_{\tThen}) e^{-\timeRate (\tThen-t)} e^{-\pDies (\tThen-t)} d\tThen \\
>          & =    \int_{t}^{\infty} (\log c_{\tThen}) e^{-(\timeRate+\pDies) (\tThen-t)} d\tThen
> \\       & =    \int_{t}^{\infty} (\log c_{\tThen}) e^{-\hat{\timeRate} (\tThen-t)} d\tThen
> \end{aligned}\end{gathered}
> ```
>
> where {math}`\hat{\timeRate} = \timeRate+\pDies`.
>
> A similar point holds in the discrete time model. A sensible thing to
>
> assume is that if you have died before {math}`t+1`, you get zero utility in
>
> {math}`t+1` and after. Thus, in the two-period context, if the probability
>
> of death between {math}`T-1` and {math}`T` was zero we would have
>
> ```{math}
> V_{T-1} = \max \uFunc(C_{T-1}) + \left(\frac{1}{1+\timeRate}\right) \uFunc(C_{T})
> ```
>
> while if there is a probability {math}`\pDies` of dying between {math}`T` and {math}`T+1`
>
> value would be:
>
> ```{math}
> :label: eq:approx
>
> \begin{gathered}\begin{aligned}
>    V_{T-1} & =  \max \uFunc(C_{T-1}) + (1-\pDies)\left(\frac{1}{1+\timeRate}\right) \uFunc(C_{T}) + \pDies \Discount \cdot 0 
> \\   & =  \max \uFunc(C_{T-1}) + \left(\frac{1-\pDies}{1+\timeRate}\right) \uFunc(C_{T})
> \\   & \approx  \max \uFunc(C_{T-1}) + \left(\frac{1}{1+\timeRate+\pDies}\right) \uFunc(C_{T})  
> \end{aligned}\end{gathered}
> ```
>
> But behavior in this case is virtually indistinguishable from the
>
> behavior that would be induced if the consumer had a time preference
>
> rate of {math}`\timeRate+\pDies`. In continuous time, the approximation in
>
> {eq}`eq:approx` becomes exact.

If the probability of death is constant, the expected remaining life
for an agent of any age is given by

```{math}
\int_{0}^{\infty} \pDies \tau e^{-\pDies \tau}d\tau = \pDies^{-1}.
```

which we will call the agent's 'horizon.' For example, if the chances
of dying per year are {math}`\pDies=1/50`, then the agent's horizon is 50 years.

We will assume that at every instant of time, a large cohort, whose size
is normalized to be {math}`\pDies`, is born.

For an economy that has existed forever, explain why the
formula for the aggregate population at time {math}`t`, {math}`P_{t}`, will be

```{math}
:label: eq:totpop

\begin{gathered}\begin{aligned}
        P_{t} & =  \pDies \int_{-\infty}^{t} \Alive_{s}^{\tNow} ds 
\end{aligned}\end{gathered}
```

and show that this formula implies that the population is {math}`P_{t}=1`.

> *Answer:*
>
>
> The aggregate population will be the sum of the still-alive persons
>
> from all past generations.
>
> The proportion of a population born at time {math}`s` that is still living
>
> at time {math}`\tThen` is {math}`\Alive_{s}^{\tThen}` by equation {eq}`eq:living`.
>
> Thus, the absolute size at time {math}`\tThen` of a cohort of size {math}`\pDies` born at
>
> time {math}`s` is {math}`\pDies \Alive_{s}^{\tThen} = \pDies e^{-\pDies (\tThen-s)}`. The economy's
>
> total population will be the sum of the populations of all the cohorts
>
> that are currently living. Since the economy has existed forever,
>
> there will be remaining members of every cohort back to {math}`s=-\infty`.
>
> Thus, indexing each cohort by a time index {math}`s`, {eq}`eq:totpop` is
>
> simply the sum of the populations of all currently living members of
>
> every generation.
>
> Substituting the formula for {math}`\Alive`, the integral becomes
>
> ```{math}
> :label: eq:fmhint
>
> \begin{gathered}\begin{aligned}
>         P_{t} & =  \pDies \int_{-\infty}^{t} e^{-\pDies(t-s)} ds 
> \\        & =  \pDies \int_{t}^{\infty} e^{-\pDies(s-t)} ds 
> \\        & =  \pDies \int_{0}^{\infty} e^{-\pDies \tThen}d\tThen
> \\        & =  \pDies \pDies^{-1}  
> \\        & =  1 
> \end{aligned}\end{gathered}
> ```
>
> where the second line comes from a change of variables {math}`\tThen = s-t`
>
> and {eq}`eq:fmhint` follows from the hint.

Now some notation. We will define variable {math}`x(s,t)` as the value at
date {math}`t` of the variable {math}`x` for a consumer who was born at date {math}`s`.

Thus, {math}`c(s,t)` is consumption at {math}`t` of a consumer born at {math}`s`.

Suppose that the consumers in this economy do not have a bequest
motive. If they have positive assets at the instant when they die,
they are no happier than if they had zero assets. This means that if
someone were willing to pay them something while they are still alive
for the right to inherit their assets whenever they die, these consumers would
happily take that deal.

For a consumer with wealth {math}`w(s,t)` who has probability of dying {math}`\pDies`,
the flow value of the right to inherit that wealth is {math}`\pDies w(s,t)`. We
will therefore assume that insurance companies exist that pay a
consumer with wealth {math}`w(s,t)` an amount {math}`\pDies w(s,t)` in exchange for the
right to receive that consumer's wealth when he dies. (The insurance
company will make zero profits).

But notice that from the standpoint of the consumer, this is
equivalent to saying that the interest rate received on wealth is
higher by amount {math}`\pDies`.

Now suppose the marginal product of capital in this
perfectly-competitive economy is constant at {math}`\rfree` and suppose an agent
born in {math}`s` receives exogenous labor income in period {math}`t` of {math}`y(s,t)`.

This plus the insurance scheme implies that the agent's dynamic budget
constraint is given by

```{math}
:label: eq:budconstr

\begin{gathered}\begin{aligned}
        \dot{w}(s,t) & =  (\rfree+\pDies) w(s,t) + y(s,t)-c(s,t) .
\end{aligned}\end{gathered}
```

Define the 'effective' interest rate as viewed by a consumer as {math}`\hat{\rfree}  = \rfree+\pDies`.

Write the current-value Hamiltonian for the
individual's maximization problem and use it to show that the growth
rate of consumption in period {math}`t` for a consumer born at time {math}`s` is
given by

```{math}
\begin{gathered}\begin{aligned}
        \left(\frac{\dot{c}(s,t)}{c(s,t)}\right) & =  \hat{\rfree} - \hat{\timeRate}
\\  & =  \rfree-\timeRate.     
\end{aligned}\end{gathered}
```

> *Answer:*
>
>
> The current-value Hamiltonian is written
>
> ```{math}
> \Ham(c,w,\lambda) = \log c(s,t) + \lambda(\hat{\rfree} w(s,t) + y(s,t) - c(s,t))
> ```
>
> so the first optimality condition {math}`\partial \Ham/\partial c(s,t) = 0` implies
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         1/c(s,t) & =  \lambda
> \\  - \dot{c}(s,t)/c(s,t)^{2} & =  \dot{\lambda}       
> \end{aligned}\end{gathered}
> ```
>
> and the second optimization condtion implies
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \dot{\lambda} & =  \hat{\timeRate} \lambda - \partial \Ham/\partial w(s,t)  
> \\       & =  \hat{\timeRate} \lambda - \hat{\rfree} \lambda  
> \\      \left(\frac{\dot{\lambda}}{\lambda}\right) & =  \hat{\timeRate}-\hat{\rfree}
> \\  \left(\frac{-\dot{c}(s,t) c(s,t)}{c(s,t)^{2}}\right) & =  \hat{\timeRate}-\hat{\rfree}
> \\  \left(\frac{\dot{c}(s,t)}{c(s,t)}\right) & =  \hat{\rfree}-\hat{\timeRate} 
> \\   & =  \rfree-\timeRate     .
> \end{aligned}\end{gathered}
> ```


Use the first order condition for consumption and the
intertemporal budget constraint implied by {eq}`eq:budconstr` to
show that the level of consumption in time {math}`t` for an individual born
at time {math}`s` is

```{math}
c(s,t) = \hat{\timeRate}(w(s,t)+h(s,t))
```

where recall that {math}`\hat{\timeRate}=\timeRate+\pDies` and human wealth is

```{math}
h(s,t) = \int_{t}^{\infty} \left(y(s,\tThen)/\hat{\mathcal{R}}_{t}^{\tThen}\right) d\tThen
```

where

```{math}
\begin{gathered}\begin{aligned}
  \hat{\mathcal{R}}_{t}^{\tThen} & =  e^{\int_{t}^{\tThen} (\rfree_{\mu}+\pDies) d\mu}
\end{aligned}\end{gathered}
```

(this is simply the compound discount factor necessary to take
account of time-varying interest rates; if interest rates are
constant at {math}`\rfree` it reduces to the usual term {math}`e^{-\rfree(\tThen-t)}`).

> *Answer:*
>
>
> The IBC says that the PDV of consumption must equal wealth plus the PDV
>
> of future labor income:
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \int_{t}^{\infty} (c(s,\tThen)/\hat{\mathcal{R}}_{t}^{\tThen})  d\tThen & =  w(s,t) + \int_{t}^{\infty} y(\tThen,t)/\hat{\mathcal{R}}_{t}^{\tThen} d\tThen
> \\      \int_{t}^{\infty} (c(s,\tThen)/\hat{\mathcal{R}}_{t}^{\tThen}) d\tThen & =  w(s,t) + h(s,t).
> \end{aligned}\end{gathered}
> ```
>
> But if {math}`\dot{c}(s,t)/c(s,t) = \hat{\rfree}_{t}-\hat{\timeRate}` then
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         c(s,\tThen) & =  c(s,t)e^{\int_{s}^{\tThen}\hat{\rfree}_\mu d\mu}e^{-\hat{\timeRate}(\tThen-t)}
> \end{aligned}\end{gathered}
> ```
>
> implying
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \int_{t}^{\infty} (c(s,\tThen)/\hat{\mathcal{R}}_{t}^{\tThen}) d\tThen & =  
> \int_{t}^{\infty} c(s,t) e^{\int_{s}^{\tThen}\hat{\rfree}_\mu  d\mu}e^{-\hat{\timeRate}(\tThen-t)}e^{-\int_{s}^{\tThen}\hat{\rfree}_\mu d\mu} d\tThen
> \\         & =  c(s,t) \int_{t}^{\infty} e^{-\hat{\timeRate}(\tThen-t)} d\tThen
> \\   & =  c(s,t)/\hat{\timeRate}
> \end{aligned}\end{gathered}
> ```
>
> so that the IBC becomes:
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         c(s,t)/\hat{\timeRate} & =  w(s,t)+h(s,t)  \\
>         c(s,t) & =  \hat{\timeRate} (w(s,t)+h(s,t)) .
> \end{aligned}\end{gathered}
> ```

Suppose we define upper-case variables as the aggregate value across all
generations currently living of the corresponding lower-case value, e.g.

aggregate consumption is

```{math}
\begin{gathered}\begin{aligned}
        C(t) & =  \int_{-\infty}^{t} \pDies c(\tThen,t) \Alive_{\tThen}^{t} d\tThen.
\end{aligned}\end{gathered}
```

(Easy) Show that the aggregate level of consumption in
this economy is

```{math}
:label: eq:cagg

\begin{gathered}\begin{aligned}
        C(t) & =  \hat{\timeRate} (W(t) + H(t)) . 
\end{aligned}\end{gathered}
```

> *Answer:*
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         C(t) & =   \int_{-\infty}^{t} \pDies c(\tThen,t) \Alive_{\tThen}^{t} d\tThen \\
>          & =  \int_{-\infty}^{t} \pDies \hat{\timeRate}(w(\tThen,t)+h(\tThen,t)) \Alive_{\tThen}^{t} d\tThen \\
>          & =  \hat{\timeRate} (W(t)+H(t))
> \end{aligned}\end{gathered}
> ```
>
> from the definition of {math}`W(t)` and {math}`H(t)`.

Suppose all living agents in this economy receive the same noncapital
income, {math}`y(s,t) = Y(t)`. Since every member of the population has the
same income, and the size of the population is one, aggregate income
will also be {math}`Y(t)`. Aggregate human wealth at {math}`t` is therefore

```{math}
\begin{gathered}\begin{aligned}
        H(t) & =  \int_{t}^{\infty} (Y(\tThen)/\hat{\mathcal{R}}_{t}^{\tThen}) d\tThen
\end{aligned}\end{gathered}
```

where

```{math}
\begin{gathered}\begin{aligned}
        \dot{H}(t) & =  \hat{\rfree}_{t} H(t) - Y(t) .
\end{aligned}\end{gathered}
```

The differential equation for aggregate wealth can be
shown to be

```{math}
:label: eq:Wdot

\begin{gathered}\begin{aligned}
        \dot{W}(t) & =  w(t,t) - \pDies W(t) + \int_{-\infty}^{t} \dot{w}(\tThen,t) \pDies e^{-\pDies(t-\tThen)} d\tThen,
\end{aligned}\end{gathered}
```

where {math}`w(t,t)=0` is the wealth of newly born generations, {math}`\pDies W(t)` is
the wealth of those who are dying at the moment, and the last term is
the change in wealth for those who neither die nor are born in this
period. But {eq}`eq:budconstr` implies that

```{math}
\begin{gathered}\begin{aligned}
  \int_{-\infty}^{t} \dot{w}(\tThen,t) \pDies e^{-\pDies(t-\tThen)} d\tThen & =  (\rfree+\pDies) W(t) + Y(t)-C(t)
\end{aligned}\end{gathered}
```

so {eq}`eq:Wdot` becomes

```{math}
\begin{gathered}\begin{aligned}
        \dot{W}(t) & =  \rfree W(t) + Y(t)-C(t).
\end{aligned}\end{gathered}
```

Collecting, writing out {math}`\hat{\rfree}=\rfree+\pDies` and {math}`\hat{\timeRate}=\timeRate+\pDies`, and
dropping the {math}`(t)` arguments gives us the following equations for
aggregate variables:

```{math}
:label: eq:clevel

\begin{gathered}\begin{aligned}
        C & =  (\pDies+\timeRate) (H+W)  \\
        \dot{H} & =  (\rfree+\pDies) H - Y  \\
        \dot{W} & =  \rfree W + Y - C
\end{aligned}\end{gathered}
```

Use these equations to show that in this economy

```{math}
:label: eq:aggCdot

\begin{gathered}\begin{aligned}
        \dot{C} & =  (\rfree-\timeRate) C - \pDies(\pDies+\timeRate) W
\end{aligned}\end{gathered}
```

Hint: Differentiate {eq}`eq:clevel` and substitute out for {math}`H` by solving
{eq}`eq:clevel` for {math}`H`.
> *Answer:*
>
> Time differentiate {eq}`eq:clevel` and substitute for {math}`\dot{H}`,
>
> {math}`\dot{W}`, and {math}`H` to get
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \dot{C} & =  (\pDies+\timeRate)\left[(\rfree+\pDies) H - Y + \rfree W + Y - C\right]
> \\       & =  (\pDies+\timeRate)\left[(\rfree+\pDies) H + \rfree W \right] - C (\pDies+\timeRate)
> \\       & =  (\pDies+\timeRate)\left[(\rfree+\pDies) \left(\frac{C}{\pDies+\timeRate}-W\right)+r W\right] - C (\pDies+\timeRate)
> \\   & =  (\rfree+\pDies) C + (\pDies+\timeRate)\left[    rW - (\rfree+\pDies) W \right] - C(\pDies+\timeRate)
> \\   & =  (\rfree-\timeRate) C - (\pDies+\timeRate)\pDies W.
> \end{aligned}\end{gathered}
> ```

Now assume there is a standard production function
{math}`\FFunc(K)=K^{\alpha}-\delta K` and assume perfect competition so that the
net interest rate {math}`r` is equal to the net marginal product of capital,

```{math}
\rfree = \FFunc^{\prime}(K) = \alpha K^{\alpha-1}-\delta
```

and the aggregate capital stock at time {math}`t` is the same as aggregate
nonhuman wealth, {math}`K(t)=W(t)`. The aggregate accumulation equation is
just the usual

```{math}
:label: eq:BFH-aggkdot

\begin{gathered}\begin{aligned}
  \dot{K} & =  K^{\alpha}-\delta K -C.
\end{aligned}\end{gathered}
```

Show that the following equation

```{math}
:label: eq:CvsK1

\begin{gathered}\begin{aligned}
  \pDies(\pDies+\timeRate) K      & =  C(\alpha K^{\alpha-1}-\delta-\timeRate)
\end{aligned}\end{gathered}
```

describes the {math}`\dot{C}=0` locus. Use this equation to show that

```{math}
:label: eq:BFH-1

\begin{gathered}\begin{aligned}
  \lim_{C \rightarrow 0} K & =  0
\\ \lim_{C \rightarrow \infty} K & =  ((\timeRate+\delta)/\alpha)^{1/{\alpha-1}}.
\end{aligned}\end{gathered}
```

> *Answer:*
>
> Rewriting the {math}`\dot{C}` equation as a function of {math}`K` yields
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \dot{C} & =  (\alpha K^{\alpha-1} - \timeRate - \delta)C - (\pDies+\timeRate)\pDies K.
> \end{aligned}\end{gathered}
> ```
>
> The {math}`\dot{C}=0` locus is therefore given by
>
> ```{math}
> :label: eq:aggCdotmod
>
> \begin{gathered}\begin{aligned}
>       0 & =  (\alpha K^{\alpha-1}-\timeRate-\delta) - \pDies(\pDies+\timeRate) K/C
> \\  \pDies(\pDies+\timeRate) K/C       & =  (\alpha K^{\alpha-1}-\delta-\timeRate)
> \\  \pDies(\pDies+\timeRate) K      & =  C(\alpha K^{\alpha-1}-\delta-\timeRate)
> \end{aligned}\end{gathered}
> ```
>
> In the limit as {math}`C \rightarrow 0` this expression approaches
>
> ```{math}
> :label: eq:2
>
> \pDies(\pDies+\timeRate) K = 0
> ```
>
> which can be true only if {math}`\lim_{\{C \rightarrow 0\}} K = 0`.
>
> On the other hand, as {math}`C \rightarrow \infty` we know that {math}`K`
>
> must remain finite (because the DBC does not allow infinite
>
> accumulation of {math}`K`; infinite {math}`K` would imply infinite depreciation which
>
> could never be paid for by a production function with diminishing marginal returns), which means that
>
> ```{math}
> \begin{gathered}\begin{aligned}
> \lim_{\{C \rightarrow \infty\}} \alpha K^{\alpha-1} & =  (\timeRate+\delta)
> \\ K^{*} & =  ((\timeRate+\delta)/\alpha)^{1/{\alpha-1}}.
> \end{aligned}\end{gathered}
> ```

Using your results from the previous question and the aggregate
dynamic budget constraint, draw the phase diagram for this model and
discuss how and why it differs from the phase diagram for the
standard Ramsey-Cass/Koopmans model. (please use {math}`K^{*}` to
designate the RCK steady-state capital stock and {math}`\bar{K}` to
designate this model's steady-state {math}`K`.)

> *Answer:*
>
> Using {eq}`eq:BFH-aggkdot`, the {math}`\dot{K}=0` locus is
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   C & =  K^{\alpha}-\delta K
> \end{aligned}\end{gathered}
> ```
>
> which yields the usual hump-shaped {math}`\dot{K}=0` locus.
>
> Rewriting the {math}`\dot{C}` equation as a function of {math}`K` yields
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \dot{C} & =  (\alpha K^{\alpha-1} - \timeRate - \delta)C - (\pDies+\timeRate)\pDies K.
> \end{aligned}\end{gathered}
> ```
>
> The {math}`\dot{C}=0` locus is therefore given by
>
> ```{math}
> :label: eq:CvsK
>
> \begin{gathered}\begin{aligned}
>       0 & =  (\alpha K^{\alpha-1}-\timeRate-\delta) - \pDies(\pDies+\timeRate) K/C
> \\  \pDies(\pDies+\timeRate) K/C       & =  (\alpha K^{\alpha-1}-\delta-\timeRate)
> \\  \pDies(\pDies+\timeRate) K      & =  C(\alpha K^{\alpha-1}-\delta-\timeRate)
> \end{aligned}\end{gathered}
> ```
>
> In the limit as {math}`C \rightarrow 0` this expression approaches
>
> ```{math}
> \pDies(\pDies+\timeRate) K = 0
> ```
>
> which can be true only if {math}`\lim_{\{C \rightarrow 0\}} K = 0`.
>
> On the other hand, as {math}`C \rightarrow \infty` we know that {math}`K`
>
> must remain finite (because the DBC does not allow infinite
>
> accumulation of {math}`K`), which means that
>
> ```{math}
> \begin{gathered}\begin{aligned}
> \lim_{\{C \rightarrow \infty\}} \alpha K^{\alpha-1} & =  (\timeRate+\delta)
> \\ K^{*} & =  ((\timeRate+\delta)/\alpha)^{1/{(\alpha-1)}}.
> \end{aligned}\end{gathered}
> ```

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardFiniteHorizPhase1.png
:::

> In the infinite horizon economy we have {math}`\pDies = 0` and so the
>
> steady-state interest rate would be the {math}`K^{*}` where {math}`\alpha K^{\alpha-1}-\delta = \timeRate`. But since {math}`K/C` and {math}`\pDies(\pDies+\timeRate)` are
>
> strictly positive, in this finite-horizon economy we would have
>
> {math}`\dot{C}/C < 0` at {math}`K=K^{*}`. It is clear therefore that in order
>
> for {eq}`eq:aggCdotmod` to hold we will need {math}`\alpha K^{\alpha-1}`
>
> to be larger than it is at {math}`K^{*}`, which is to say we need a higher
>
> steady-state interest rate, and thus we need a lower steady-state
>
> capital stock, which is depicted in the figure as {math}`\bar{K}`.
>
> This makes sense because the finite-horizon consumers in this economy
>
> discount the future more than the representative agent does, because
>
> they die but a representative agent does not.
>
> These results are combined in the figure, which shows that the intersection
>
> of the {math}`\dot{C}=0` locus intersects the {math}`\dot{K}=0` locus at point {math}`A`
>
> which corresponds to a lower level of the capital stock than in the
>
> infinite horizon model.

Now consider the introduction of a government that finances spending
either by lump-sum taxes or by debt. Its dynamic budget constraint is

```{math}
\dot{D} =  \rfree D + G - \TaxLev
```

where {math}`D` is government debt, {math}`G` is government spending, and
{math}`\TaxLev` is a lump-sum per capita tax. Defining

```{math}
\begin{gathered}\begin{aligned}
  \mathcal{R}_t^{s} = e^{\int_t^{s}\rfree_v dv}
\end{aligned}\end{gathered}
```

as the compound interest factor between time {math}`t` and time {math}`s`, the
government is also required to satisfy the transversality condition

```{math}
:label: eq:10

\lim_{t \rightarrow \infty} D_t/\mathcal{R}_t^{s} = 0.
```

Consider the following fiscal policy experiment. Until time {math}`t` there
has been no government ({math}`G_s = D_s = \TaxLev_s=0~\forall~s<t`). At date
{math}`t` the government issues a quantity {math}`D` of debt and announces that
future lump sum taxes will be imposed in amounts exactly large enough
to pay the interest on this debt (so subsequently, {math}`\dot{D}=0`
forever). The government rebates the proceeds of its sale of debt to
the public as a per-capita lump sum of {math}`D` per person. The government
will never engage in any spending (aside from paying interest on the
debt). Define the new variables

```{math}
\begin{gathered}\begin{aligned}
  \mathcal{W} & =  K + D
\\ \mathcal{Y} & =  Y - \TaxLev
\\ \mathcal{H} & =  \int_{t}^{\infty} \mathcal{Y}/\hat{\mathcal{R}}_{t}^{s} ds
\end{aligned}\end{gathered}
```

Explain why the effect of this policy is to modify the aggregate
specification of the economy to

```{math}
:label: eq:Cnew

\begin{gathered}\begin{aligned}
   C & =  (\pDies+\timeRate) (\mathcal{H} + \mathcal{W})
\\ \dot{\mathcal{W}} & =  \rfree \mathcal{W} + \mathcal{Y}- C
\\ \dot{\mathcal{H}} & =  (\rfree+\pDies) \mathcal{H} - \mathcal{Y}
\end{aligned}\end{gathered}
```

> *Answer:*
>
> The effect of the government policy is twofold. On the one hand,
>
> the distribution of government bonds increases the consumers'
>
> wealth {math}`W` by an amount equal to the value of the bonds received,
>
> resulting in a new definition of wealth {math}`\mathcal{W}` which
>
> includes the bonds. On the other hand, the higher value of taxes
>
> off to infinity reduces the consumers' human wealth by an amount
>
> equal to the present discounted value of the taxes.
>
> The change in (redefined) wealth is now  net income {math}`Y-\timeRate`
>
> minus consumption.

Use these equations to show that the new dynamic equations for
the economy are

```{math}
\begin{gathered}\begin{aligned}
  \dot{C} & =  (\rfree - \timeRate)C - \pDies(\pDies+\timeRate)(K+D)
\\ \dot{K} & =  K^{\alpha}-\delta K - C
\end{aligned}\end{gathered}
```

Show how the policy change affects the economy over time, using a
phase diagram and a diagram showing the dynamics of aggregate
consumption after the policy is introduced. Explain the impact
of the policy on different generations in the economy.

> *Answer:*
>
> Time differentiating {eq}`eq:Cnew` yields
>
> ```{math}
> :label: eq:dotCnew
>
> \begin{gathered}\begin{aligned}
>   \dot{C} & =  (\pDies+\timeRate) (\dot{\mathcal{H}} + \dot{\mathcal{W}})
> \\ & =  (\pDies+\timeRate)(\rfree \mathcal{W}+(\rfree+\pDies)\mathcal{H}-C)
> \end{aligned}\end{gathered}
> ```
>
> Now solve {eq}`eq:Cnew` for {math}`\mathcal{H}`,
>
> ```{math}
> :label: eq:18
>
> \begin{gathered}\begin{aligned}
>   \mathcal{H} & =  \left(\frac{C}{\pDies+ \timeRate}\right)-\mathcal{W}
> \end{aligned}\end{gathered}
> ```
>
> and substitute into {eq}`eq:dotCnew` to obtain
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \dot{C} & =  (\pDies+\timeRate)(\rfree \mathcal{W}+(\rfree+\pDies)(C(\pDies+\timeRate)^{-1} - \mathcal{W})-C)
> \\        & =  (\rfree+\pDies)C - (\pDies+\timeRate)C- \pDies(\pDies+\timeRate)\mathcal{W}
> \\ & =  (\rfree-\timeRate)C - \pDies(\pDies+\timeRate)(K+D).
> \end{aligned}\end{gathered}
> ```
>
> Since we are assuming that {math}`D` is a constant (after the fiscal
>
> experiment), any combination of {math}`C` and {math}`W` that would have been on
>
> the {math}`\dot{C}=0` locus before the policy shift now has a value {math}`\dot{C} = -\pDies(\pDies+\timeRate)D`. This means that the {math}`C` that would restore
>
> {math}`\dot{C}=0` must be a larger {math}`C`, which says that the {math}`\dot{C}=0`
>
> locus shifts up (or, equivalently, to the left). Thus, the new
>
> equilibrium will be at a lower value of {math}`K` and a higher interest
>
> rate.
>
> The phase diagram shows that the new equilibrium point {math}`A'` is to the left
>
> of the original equilibrium. This is because at a given level of the aggregate
>
> capital stock, consumers spend more because {math}`\mathcal{W}>W`. Thus,
>
> Ricardian equivalence does not hold in this model, because a tax cut today
>
> financed by a future perpetual tax is a transfer of resources from future
>
> consumers to today's consumers, and there are no altruistic links that
>
> make current consumers offset this by saving more on behalf of future
>
> generations.

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardFiniteHorizPhase2.png
:::

> The next figure shows the path of consumption per capita in this
>
> economy. Prior to time 0, the economy was in its steady-state
>
> equilibrium at the level of consumption {math}`C_0` corresponding to the
>
> equilibrium labeled {math}`A` in the phase diagram. At time 0, the fiscal
>
> policy is carried out. The fiscal policy immediately increases
>
> consumption because it amounts to a transfer of resources from future
>
> to current generations. However, the higher level of consumption runs
>
> down the capital stock per capita, and so over time consumption asypmtotically
>
> approaches a new, lower equilibrium level of consumption {math}`C'`.

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardCDynamics.png
:::

Blanchard shows that if the model is changed so that each
consumer's income declines exponentially at rate {math}`\gamma` after
birth, the result is equivalent to assuming that future labor income
is discounted at an interest rate that is higher by {math}`\gamma`. He
further shows that the equations of motion of the model change to

```{math}
:label: eq:lccdot

\begin{gathered}\begin{aligned}
  \dot{C} & =  (\alpha K^{\alpha-1}-\delta +\gamma-\timeRate)C-(\pDies+\gamma)(\pDies+\timeRate)K
\\ \dot{K} & =  K^{\alpha}-\delta K - C.
\end{aligned}\end{gathered}
```

Note that it is possible to rewrite the {math}`\dot{C}=0` locus as

```{math}
:label: eq:lccdoteq0

\begin{gathered}\begin{aligned}
  (\alpha K^{\alpha-1}-\delta +\gamma-\timeRate)C & =  (\pDies+\gamma)(\pDies+\timeRate)K
\end{aligned}\end{gathered}
```

Use this equation to show that as {math}`C \rightarrow \infty`, the
{math}`\dot{C}=0` locus asymptotes to

```{math}
:label: eq:eqblcr

\begin{gathered}\begin{aligned}
 \rfree = \alpha K^{\alpha-1} - \delta & =  \timeRate - \gamma
\end{aligned}\end{gathered}
```

Thus, for a large enough value of {math}`\gamma` it is possible that the net
interest rate in this economy could be negative. Draw a phase diagram
corresponding to an equilibrium with a negative net interest rate, and
comment on why this is an interesting case to think about. In
particular, what new light does it shed on the fiscal policy
experiment examined above?

> *Answer:*
>
> As {math}`C` goes to infinity on the LHS of {eq}`eq:lccdoteq0`, the only way
>
> the equation can continue to hold is if
>
> ```{math}
> \begin{gathered}\begin{aligned}
>  \lim_{C \rightarrow \infty} (\alpha K^{\alpha-1}-\delta +\gamma-\timeRate) & =  0
> \end{aligned}\end{gathered}
> ```
>
> which implies {eq}`eq:eqblcr`.
>
> The new phase diagram shows the {math}`\dot{C}=0` locus intersecting the
>
> {math}`\dot{K}=0` locus to the right of the maximum of the {math}`\dot{K}=0` locus.
>
> This is implied by the fact that the net interest rate is negative, which
>
> means that the net interest rate could be increased by reducing
>
> the capital stock.
>
> The reason this is an interesting case is that in this case it is
>
> possible for the economy to be in a condition of dynamic inefficiency,
>
> just as in the 2-period OLG models discussed early in the class. The idea
>
> is to think of declining labor income as a way to generate a 'life cycle'
>
> saving motive. In such a case the fiscal experiment examined above
>
> is interesting because it could rescue an economy with too much capital
>
> from a state of dynamic inefficiency.

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardFiniteHorizPhase3.png
:::

