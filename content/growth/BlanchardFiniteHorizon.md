(sec:BlanchardFiniteHorizon)=
# The Blanchard (1985) Model of Perpetual Youth

This chapter analyzes a way to relax the standard assumption of infinite
lifetimes in the Ramsey/Cass-Koopmans
growth model. The trick, introduced by
{cite:t}`blanchardFinite`, is to assume that the economy
is populated by agents who face a constant probability of death.

Thus, an agent who has lived a thousand years is no more likely to die
in the next year than an agent who was born yesterday.

Time is measured continuously. If there is an instantaneous
probability {math}`\diePrb` of dying, the probability (as viewed by a person
alive in period {math}`t`) of still being alive (not dead) in period
{math}`\tau` is

```{math}
:label: eq:living

\begin{gathered}\begin{aligned}
        \Alive_{t}^{\tau} & =  e^{-\diePrb(\tau-t)} . 
\end{aligned}\end{gathered}
```

Assuming the instantaneous utility function is {math}`\uFunc(\cNrm) =  \lcNrm`, and that the pure rate of time preference is {math}`\discRte`,
explain why the objective function at time {math}`t` of an individual
household in this model will be to maximize

```{math}
:label: eq:objfunc

\int_{t}^{\infty} (\lcNrm_{\tau}) e^{-(\discRte+\diePrb)(\tau-t)} d\tau.
```

where {math}`\cNrm_{\tau}` is the consumer's consumption at time {math}`\tau`. For convenience,
you may wish to define

```{math}
:label: eq:thetahat

\begin{gathered}\begin{aligned}
        \discRteEff & =  \discRte+\diePrb. 
\end{aligned}\end{gathered}
```

> *Answer:*
>
>
> A consumer with a pure time preference rate of {math}`\discRte` will downweight
>
> the utility he receives conditional on being alive by the probability
>
> that he is still alive, yielding a discounted utility of
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \int_{t}^{\infty} (\lcNrm_{\tau}) \Alive_{t}^{\tau} e^{-\discRte (\tau-t)}d\tau & =  \int_{t}^{\infty} (\lcNrm_{\tau}) e^{-\discRte (\tau-t)} e^{-\diePrb (\tau-t)} d\tau \\
>          & =    \int_{t}^{\infty} (\lcNrm_{\tau}) e^{-(\discRte+\diePrb) (\tau-t)} d\tau
> \\       & =    \int_{t}^{\infty} (\lcNrm_{\tau}) e^{-\discRteEff (\tau-t)} d\tau
> \end{aligned}\end{gathered}
> ```
>
> where {math}`\discRteEff = \discRte+\diePrb`.
>
> A similar point holds in the discrete time model. A sensible thing to
>
> assume is that if you have died before {math}`t+1`, you get zero utility in
>
> {math}`t+1` and after. Thus, in the two-period context, if the probability
>
> of death between {math}`t` and {math}`t+1` was zero we would have
>
> ```{math}
> \VFunc_{t} = \max \uFunc(\cNrm_{t}) + \left(\frac{1}{1+\discRte}\right) \uFunc(\cNrm_{t+1})
> ```
>
> while if there is a probability {math}`\diePrb` of dying between {math}`t` and {math}`t+1`
>
> value would be:
>
> ```{math}
> :label: eq:approx
>
> \begin{gathered}\begin{aligned}
>    \VFunc_{t} & =  \max \uFunc(\cNrm_{t}) + (1-\diePrb)\left(\frac{1}{1+\discRte}\right) \uFunc(\cNrm_{t+1}) + \diePrb \left(\frac{1}{1+\discRte}\right) \cdot 0 
> \\   & =  \max \uFunc(\cNrm_{t}) + \left(\frac{1-\diePrb}{1+\discRte}\right) \uFunc(\cNrm_{t+1})
> \\   & \approx  \max \uFunc(\cNrm_{t}) + \left(\frac{1}{1+\discRte+\diePrb}\right) \uFunc(\cNrm_{t+1})  
> \end{aligned}\end{gathered}
> ```
>
> But behavior in this case is virtually indistinguishable from the
>
> behavior that would be induced if the consumer had a time preference
>
> rate of {math}`\discRte+\diePrb`. In continuous time, the approximation in
>
> {eq}`eq:approx` becomes exact.

If the probability of death is constant, the expected remaining life
for an agent of any age is given by

```{math}
\int_{0}^{\infty} \diePrb \tau e^{-\diePrb \tau}d\tau = \diePrb^{-1}.
```

which we will call the agent's 'horizon.' For example, if the chances
of dying per year are {math}`\diePrb=1/50`, then the agent's horizon is 50 years.

We will assume that at every instant of time, a large cohort, whose size
is normalized to be {math}`\diePrb`, is born.

For an economy that has existed forever, explain why the
formula for the aggregate population at time {math}`t`, {math}`\PopnLvl_{t}`, will be

```{math}
:label: eq:totpop

\begin{gathered}\begin{aligned}
        \PopnLvl_{t} & =  \diePrb \int_{-\infty}^{t} \Alive_{s}^{t} ds 
\end{aligned}\end{gathered}
```

and show that this formula implies that the population is {math}`\PopnLvl_{t}=1`.

> *Answer:*
>
>
> The aggregate population will be the sum of the still-alive persons
>
> from all past generations.
>
> The proportion of a population born at time {math}`s` that is still living
>
> at time {math}`\tau` is {math}`\Alive_{s}^{\tau}` by equation {eq}`eq:living`.
>
> Thus, the absolute size at time {math}`\tau` of a cohort of size {math}`\diePrb` born at
>
> time {math}`s` is {math}`\diePrb \Alive_{s}^{\tau} = \diePrb e^{-\diePrb (\tau-s)}`. The economy's
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
>         \PopnLvl_{t} & =  \diePrb \int_{-\infty}^{t} e^{-\diePrb(t-s)} ds 
> \\        & =  \diePrb \int_{t}^{\infty} e^{-\diePrb(s-t)} ds 
> \\        & =  \diePrb \int_{0}^{\infty} e^{-\diePrb \tau}d\tau
> \\        & =  \diePrb \diePrb^{-1}  
> \\        & =  1 
> \end{aligned}\end{gathered}
> ```
>
> where the third line comes from a change of variables {math}`\tau = s-t`.

Now some notation. We will define variable {math}`x(s,t)` as the value at
date {math}`t` of the variable {math}`x` for a consumer who was born at date {math}`s`.

Thus, {math}`\cNrm(s,t)` is consumption at {math}`t` of a consumer born at {math}`s`.

Suppose that the consumers in this economy do not have a bequest
motive. If they have positive assets at the instant when they die,
they are no happier than if they had zero assets. This means that if
someone were willing to pay them something while they are still alive
for the right to inherit their assets whenever they die, these consumers would
happily take that deal.

For a consumer with wealth {math}`\netWorth(s,t)` who has probability of dying {math}`\diePrb`,
the flow value of the right to inherit that wealth is {math}`\diePrb \netWorth(s,t)`. We
will therefore assume that insurance companies exist that pay a
consumer with wealth {math}`\netWorth(s,t)` an amount {math}`\diePrb \netWorth(s,t)` in exchange for the
right to receive that consumer's wealth when he dies. (The insurance
company will make zero profits).

But notice that from the standpoint of the consumer, this is
equivalent to saying that the interest rate received on wealth is
higher by amount {math}`\diePrb`.

Now suppose the marginal product of capital in this
perfectly-competitive economy is constant at {math}`\rfree` and suppose an agent
born in {math}`s` receives exogenous labor income in period {math}`t` of {math}`\wage(s,t)`.

This plus the insurance scheme implies that the agent's dynamic budget
constraint is given by

```{math}
:label: eq:budconstr

\begin{gathered}\begin{aligned}
        \dot{\netWorth}(s,t) & =  (\rfree+\diePrb) \netWorth(s,t) + \wage(s,t)-\cNrm(s,t) .
\end{aligned}\end{gathered}
```

Define the 'effective' interest rate as viewed by a consumer as {math}`\rfreeEff  = \rfree+\diePrb`.

Write the current-value Hamiltonian for the
individual's maximization problem and use it to show that the growth
rate of consumption in period {math}`t` for a consumer born at time {math}`s` is
given by

```{math}
\begin{gathered}\begin{aligned}
        \left(\frac{\dot{\cNrm}(s,t)}{\cNrm(s,t)}\right) & =  \rfreeEff - \discRteEff
\\  & =  \rfree-\discRte.     
\end{aligned}\end{gathered}
```

> *Answer:*
>
>
> The current-value Hamiltonian is written
>
> ```{math}
> \Ham(\netWorth,\cNrm,\vk) = \lcNrm(s,t) + (\rfreeEff \netWorth(s,t) + \wage(s,t) - \cNrm(s,t))\vk
> ```
>
> so the optimality condition for consumption, {math}`\partial \Ham/\partial \cNrm(s,t) = 0`, implies
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         1/\cNrm(s,t) & =  \vk
> \\  - \dot{\cNrm}(s,t)/\cNrm(s,t)^{2} & =  \dot{\vk}       
> \end{aligned}\end{gathered}
> ```
>
> and the costate equation implies
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \dot{\vk} & =  \discRteEff \vk - \partial \Ham/\partial \netWorth(s,t)  
> \\       & =  \discRteEff \vk - \rfreeEff \vk  
> \\      \left(\frac{\dot{\vk}}{\vk}\right) & =  \discRteEff-\rfreeEff
> \\  \left(\frac{-\dot{\cNrm}(s,t) \cNrm(s,t)}{\cNrm(s,t)^{2}}\right) & =  \discRteEff-\rfreeEff
> \\  \left(\frac{\dot{\cNrm}(s,t)}{\cNrm(s,t)}\right) & =  \rfreeEff-\discRteEff 
> \\   & =  \rfree-\discRte     .
> \end{aligned}\end{gathered}
> ```


Use the first order condition for consumption and the
intertemporal budget constraint implied by {eq}`eq:budconstr` to
show that the level of consumption in time {math}`t` for an individual born
at time {math}`s` is

```{math}
\cNrm(s,t) = \discRteEff(\netWorth(s,t)+\hNrm(s,t))
```

where recall that {math}`\discRteEff=\discRte+\diePrb` and human wealth is

```{math}
\hNrm(s,t) = \PDVEff_{t}(\wage(s,\cdot))
```

where

```{math}
\begin{gathered}\begin{aligned}
  \PDVEff_{t}(\bullet) & \equiv  \int_{t}^{\infty} \bullet_{\tau}\, e^{-\int_{t}^{\tau} \rfreeEff_{\mu} d\mu}\, d\tau
\\ e^{\int_{t}^{\tau} \rfreeEff_{\mu} d\mu} & =  e^{\int_{t}^{\tau} (\rfree_{\mu}+\diePrb) d\mu}
\end{aligned}\end{gathered}
```

(the second line is simply the compound interest factor necessary to take
account of time-varying interest rates; if interest rates are
constant at {math}`\rfree` it reduces to {math}`e^{(\rfree+\diePrb)(\tau-t)}`, and dividing by it discounts at {math}`\rfree+\diePrb`).

> *Answer:*
>
>
> The IBC says that the PDV of consumption must equal wealth plus the PDV
>
> of future labor income:
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \PDVEff_{t}(\cNrm(s,\cdot)) & =  \netWorth(s,t) + \PDVEff_{t}(\wage(s,\cdot))
> \\      \PDVEff_{t}(\cNrm(s,\cdot)) & =  \netWorth(s,t) + \hNrm(s,t).
> \end{aligned}\end{gathered}
> ```
>
> But if {math}`\dot{\cNrm}(s,t)/\cNrm(s,t) = \rfreeEff_{t}-\discRteEff` then
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \cNrm(s,\tau) & =  \cNrm(s,t)e^{\int_{t}^{\tau}\rfreeEff_\mu d\mu}e^{-\discRteEff(\tau-t)}
> \end{aligned}\end{gathered}
> ```
>
> implying
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \PDVEff_{t}(\cNrm(s,\cdot)) & =  
> \int_{t}^{\infty} \cNrm(s,t) e^{\int_{t}^{\tau}\rfreeEff_\mu  d\mu}e^{-\discRteEff(\tau-t)}e^{-\int_{t}^{\tau}\rfreeEff_\mu d\mu} d\tau
> \\         & =  \cNrm(s,t) \int_{t}^{\infty} e^{-\discRteEff(\tau-t)} d\tau
> \\   & =  \cNrm(s,t)/\discRteEff
> \end{aligned}\end{gathered}
> ```
>
> so that the IBC becomes:
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \cNrm(s,t)/\discRteEff & =  \netWorth(s,t)+\hNrm(s,t)  \\
>         \cNrm(s,t) & =  \discRteEff (\netWorth(s,t)+\hNrm(s,t)) .
> \end{aligned}\end{gathered}
> ```

Suppose we define upper-case variables as the aggregate value across all
generations currently living of the corresponding lower-case value, e.g.

aggregate consumption is

```{math}
\begin{gathered}\begin{aligned}
        \CNrm(t) & =  \int_{-\infty}^{t} \diePrb \cNrm(s,t) \Alive_{s}^{t} ds.
\end{aligned}\end{gathered}
```

(Easy) Show that the aggregate level of consumption in
this economy is

```{math}
:label: eq:cagg

\begin{gathered}\begin{aligned}
        \CNrm(t) & =  \discRteEff (\NetWorth(t) + \HNrm(t)) . 
\end{aligned}\end{gathered}
```

> *Answer:*
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \CNrm(t) & =   \int_{-\infty}^{t} \diePrb \cNrm(s,t) \Alive_{s}^{t} ds \\
>          & =  \int_{-\infty}^{t} \diePrb \discRteEff(\netWorth(s,t)+\hNrm(s,t)) \Alive_{s}^{t} ds \\
>          & =  \discRteEff (\NetWorth(t)+\HNrm(t))
> \end{aligned}\end{gathered}
> ```
>
> from the definition of {math}`\NetWorth(t)` and {math}`\HNrm(t)`.

Suppose all living agents in this economy receive the same noncapital
income, {math}`\wage(s,t) = \Wage(t)`. Since every member of the population has the
same income, and the size of the population is one, aggregate income
will also be {math}`\Wage(t)`. Aggregate human wealth at {math}`t` is therefore

```{math}
\begin{gathered}\begin{aligned}
        \HNrm(t) & =  \PDVEff_{t}(\Wage)
\end{aligned}\end{gathered}
```

where

```{math}
\begin{gathered}\begin{aligned}
        \dot{\HNrm}(t) & =  \rfreeEff_{t} \HNrm(t) - \Wage(t) .
\end{aligned}\end{gathered}
```

The differential equation for aggregate wealth can be
shown to be

```{math}
:label: eq:Wdot

\begin{gathered}\begin{aligned}
        \dot{\NetWorth}(t) & =  \diePrb \netWorth(t,t) - \diePrb \NetWorth(t) + \int_{-\infty}^{t} \dot{\netWorth}(s,t) \diePrb e^{-\diePrb(t-s)} ds,
\end{aligned}\end{gathered}
```

where {math}`\diePrb \netWorth(t,t)=0` is the wealth of newly born generations, {math}`\diePrb \NetWorth(t)` is
the wealth of those who are dying at the moment, and the last term is
the change in wealth for those who neither die nor are born in this
period. But {eq}`eq:budconstr` implies that

```{math}
\begin{gathered}\begin{aligned}
  \int_{-\infty}^{t} \dot{\netWorth}(s,t) \diePrb e^{-\diePrb(t-s)} ds & =  (\rfree+\diePrb) \NetWorth(t) + \Wage(t)-\CNrm(t)
\end{aligned}\end{gathered}
```

so {eq}`eq:Wdot` becomes

```{math}
\begin{gathered}\begin{aligned}
        \dot{\NetWorth}(t) & =  \rfree \NetWorth(t) + \Wage(t)-\CNrm(t).
\end{aligned}\end{gathered}
```

Collecting, writing out {math}`\rfreeEff=\rfree+\diePrb` and {math}`\discRteEff=\discRte+\diePrb`, and
dropping the {math}`(t)` arguments gives us the following equations for
aggregate variables:

```{math}
:label: eq:clevel

\begin{gathered}\begin{aligned}
        \CNrm & =  (\diePrb+\discRte) (\HNrm+\NetWorth)  \\
        \dot{\HNrm} & =  (\rfree+\diePrb) \HNrm - \Wage  \\
        \dot{\NetWorth} & =  \rfree \NetWorth + \Wage - \CNrm
\end{aligned}\end{gathered}
```

Use these equations to show that in this economy

```{math}
:label: eq:aggCdot

\begin{gathered}\begin{aligned}
        \dot{\CNrm} & =  (\rfree-\discRte) \CNrm - \diePrb(\diePrb+\discRte) \NetWorth
\end{aligned}\end{gathered}
```

Hint: Differentiate {eq}`eq:clevel` and substitute out for {math}`\HNrm` by solving
{eq}`eq:clevel` for {math}`\HNrm`.
> *Answer:*
>
> Time differentiate {eq}`eq:clevel` and substitute for {math}`\dot{\HNrm}`,
>
> {math}`\dot{\NetWorth}`, and {math}`\HNrm` to get
>
> ```{math}
> \begin{gathered}\begin{aligned}
>         \dot{\CNrm} & =  (\diePrb+\discRte)\left[(\rfree+\diePrb) \HNrm - \Wage + \rfree \NetWorth + \Wage - \CNrm\right]
> \\       & =  (\diePrb+\discRte)\left[(\rfree+\diePrb) \HNrm + \rfree \NetWorth \right] - \CNrm (\diePrb+\discRte)
> \\       & =  (\diePrb+\discRte)\left[(\rfree+\diePrb) \left(\frac{\CNrm}{\diePrb+\discRte}-\NetWorth\right)+\rfree \NetWorth\right] - \CNrm (\diePrb+\discRte)
> \\   & =  (\rfree+\diePrb) \CNrm + (\diePrb+\discRte)\left[    \rfree\NetWorth - (\rfree+\diePrb) \NetWorth \right] - \CNrm(\diePrb+\discRte)
> \\   & =  (\rfree-\discRte) \CNrm - (\diePrb+\discRte)\diePrb \NetWorth.
> \end{aligned}\end{gathered}
> ```

Now assume there is a standard production function, with output {math}`\KNrm^{\kapShare}`
and output net of depreciation {math}`\FFunc(\KNrm)=\KNrm^{\kapShare}-\deprRte \KNrm`, and assume perfect competition so that the
net interest rate {math}`\rfree` is equal to the net marginal product of capital,

```{math}
\rfree = \FFunc^{\prime}(\KNrm) = \kapShare \KNrm^{\kapShare-1}-\deprRte
```

and, without government debt, the aggregate capital stock at time {math}`t` is the same as aggregate
nonhuman wealth, {math}`\KNrm(t)=\NetWorth(t)`. The aggregate accumulation equation is
just the usual

```{math}
:label: eq:BFH-aggkdot

\begin{gathered}\begin{aligned}
  \dot{\KNrm} & =  \KNrm^{\kapShare}-\deprRte \KNrm -\CNrm.
\end{aligned}\end{gathered}
```

Show that the following equation

```{math}
:label: eq:CvsK1

\begin{gathered}\begin{aligned}
  \diePrb(\diePrb+\discRte) \KNrm      & =  \CNrm(\kapShare \KNrm^{\kapShare-1}-\deprRte-\discRte)
\end{aligned}\end{gathered}
```

describes the {math}`\dot{\CNrm}=0` locus. Use this equation to show that

```{math}
:label: eq:BFH-1

\begin{gathered}\begin{aligned}
  \lim_{\CNrm \rightarrow 0} \KNrm & =  0
\\ \lim_{\CNrm \rightarrow \infty} \KNrm & =  ((\discRte+\deprRte)/\kapShare)^{1/(\kapShare-1)}.
\end{aligned}\end{gathered}
```

> *Answer:*
>
> Rewriting the {math}`\dot{\CNrm}` equation as a function of {math}`\KNrm` yields
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \dot{\CNrm} & =  (\kapShare \KNrm^{\kapShare-1} - \discRte - \deprRte)\CNrm - (\diePrb+\discRte)\diePrb \KNrm.
> \end{aligned}\end{gathered}
> ```
>
> The {math}`\dot{\CNrm}=0` locus is therefore given by
>
> ```{math}
> :label: eq:aggCdotmod
>
> \begin{gathered}\begin{aligned}
>       0 & =  (\kapShare \KNrm^{\kapShare-1}-\discRte-\deprRte) - \diePrb(\diePrb+\discRte) \KNrm/\CNrm
> \\  \diePrb(\diePrb+\discRte) \KNrm/\CNrm       & =  (\kapShare \KNrm^{\kapShare-1}-\deprRte-\discRte)
> \\  \diePrb(\diePrb+\discRte) \KNrm      & =  \CNrm(\kapShare \KNrm^{\kapShare-1}-\deprRte-\discRte)
> \end{aligned}\end{gathered}
> ```
>
> In the limit as {math}`\CNrm \rightarrow 0` this expression approaches
>
> ```{math}
> :label: eq:2
>
> \diePrb(\diePrb+\discRte) \KNrm = 0
> ```
>
> which can be true only if {math}`\lim_{\CNrm \rightarrow 0} \KNrm = 0`.
>
> On the other hand, as {math}`\CNrm \rightarrow \infty` we know that {math}`\KNrm`
>
> must remain finite (because the DBC does not allow infinite
>
> accumulation of {math}`\KNrm`; infinite {math}`\KNrm` would imply infinite depreciation which
>
> could never be paid for by a production function with diminishing marginal returns), which means that
>
> ```{math}
> \begin{gathered}\begin{aligned}
> \lim_{\CNrm \rightarrow \infty} \kapShare \KNrm^{\kapShare-1} & =  (\discRte+\deprRte)
> \\ \KNrm^{*} & =  ((\discRte+\deprRte)/\kapShare)^{1/(\kapShare-1)}.
> \end{aligned}\end{gathered}
> ```

Using your results from the previous question and the aggregate
dynamic budget constraint, draw the phase diagram for this model and
discuss how and why it differs from the phase diagram for the
standard Ramsey/Cass-Koopmans model. (please use {math}`\KNrm^{*}` to
designate the RCK steady-state capital stock and {math}`\Steady{\KNrm}` to
designate this model's steady-state {math}`\KNrm`.)

> *Answer:*
>
> Using {eq}`eq:BFH-aggkdot`, the {math}`\dot{\KNrm}=0` locus is
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \CNrm & =  \KNrm^{\kapShare}-\deprRte \KNrm
> \end{aligned}\end{gathered}
> ```
>
> which yields the usual hump-shaped {math}`\dot{\KNrm}=0` locus.

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardFiniteHorizPhase1.png
:::

> In the infinite horizon economy we have {math}`\diePrb = 0` and so the
>
> steady-state capital stock would be the {math}`\KNrm^{*}` where {math}`\kapShare \KNrm^{\kapShare-1}-\deprRte = \discRte`. But since {math}`\KNrm/\CNrm` and {math}`\diePrb(\diePrb+\discRte)` are
>
> strictly positive, in this finite-horizon economy we would have
>
> {math}`\dot{\CNrm}/\CNrm < 0` at {math}`\KNrm=\KNrm^{*}`. It is clear therefore that in order
>
> for {eq}`eq:aggCdotmod` to hold we will need {math}`\kapShare \KNrm^{\kapShare-1}`
>
> to be larger than it is at {math}`\KNrm^{*}`, which is to say we need a higher
>
> steady-state interest rate, and thus we need a lower steady-state
>
> capital stock, which is depicted in the figure as {math}`\Steady{\KNrm}`.
>
> This makes sense because the finite-horizon consumers in this economy
>
> discount the future more than the representative agent does, because
>
> they die but a representative agent does not.
>
> These results are combined in the figure, which shows that the
>
> {math}`\dot{\CNrm}=0` locus intersects the {math}`\dot{\KNrm}=0` locus at point {math}`A`
>
> which corresponds to a lower level of the capital stock than in the
>
> infinite horizon model.

Now consider the introduction of a government that finances spending
either by lump-sum taxes or by debt. Its dynamic budget constraint is

```{math}
\dot{\Debt} =  \rfree \Debt + \GovSpend - \TaxLev
```

where {math}`\Debt` is government debt, {math}`\GovSpend` is government spending, and
{math}`\TaxLev` is a lump-sum per capita tax. Defining

```{math}
\begin{gathered}\begin{aligned}
  e^{\int_t^{\tau}\rfree_\mu d\mu}
\end{aligned}\end{gathered}
```

as the compound interest factor between time {math}`t` and time {math}`\tau`, the
government is also required to satisfy its no-Ponzi condition with equality

```{math}
:label: eq:BFH-govDebtLimit

\lim_{\tau \rightarrow \infty} \Debt_\tau/e^{\int_t^{\tau}\rfree_\mu d\mu} = 0.
```

Consider the following fiscal policy experiment. Until time 0 there
has been no government ({math}`\GovSpend_\tau = \Debt_\tau = \TaxLev_\tau=0~\forall~\tau<0`). At date
0 the government issues a quantity {math}`\Debt` of debt and announces that
future lump sum taxes will be imposed in amounts exactly large enough
to pay the interest on this debt (so subsequently, {math}`\dot{\Debt}=0`
forever). The government rebates the proceeds of its sale of debt to
the public as a per-capita lump sum of {math}`\Debt` per person. The government
will never engage in any spending (aside from paying interest on the
debt). Aggregate net worth, and human wealth net of taxes, are now

```{math}
\begin{gathered}\begin{aligned}
  \NetWorth & =  \KNrm + \Debt
\\ \HNrm - \PDVEff_{t}(\TaxLev) & =  \PDVEff_{t}(\Wage - \TaxLev)
\end{aligned}\end{gathered}
```

Explain why the effect of this policy is to modify the aggregate
specification of the economy to

```{math}
:label: eq:Cnew

\begin{gathered}\begin{aligned}
   \CNrm & =  (\diePrb+\discRte) (\HNrm - \PDVEff_{t}(\TaxLev) + \NetWorth)
\\ \dot{\NetWorth} & =  \rfree \NetWorth + \Wage - \TaxLev- \CNrm
\\ \frac{d}{dt}(\HNrm - \PDVEff_{t}(\TaxLev)) & =  (\rfree+\diePrb) (\HNrm - \PDVEff_{t}(\TaxLev)) - (\Wage - \TaxLev)
\end{aligned}\end{gathered}
```

> *Answer:*
>
> The effect of the government policy is twofold. On the one hand,
>
> the distribution of government bonds increases the consumers'
>
> wealth {math}`\KNrm` by an amount equal to the value of the bonds received,
>
> resulting in a new definition of wealth {math}`\NetWorth` which
>
> includes the bonds. On the other hand, the higher value of taxes
>
> off to infinity reduces the consumers' human wealth by an amount
>
> equal to the present discounted value of the taxes.
>
> The change in (redefined) wealth is now  net income {math}`\rfree\NetWorth + \Wage - \TaxLev`
>
> minus consumption.

Use these equations to show that the new dynamic equations for
the economy are

```{math}
\begin{gathered}\begin{aligned}
  \dot{\CNrm} & =  (\rfree - \discRte)\CNrm - \diePrb(\diePrb+\discRte)(\KNrm+\Debt)
\\ \dot{\KNrm} & =  \KNrm^{\kapShare}-\deprRte \KNrm - \CNrm
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
>   \dot{\CNrm} & =  (\diePrb+\discRte) (\frac{d}{dt}(\HNrm - \PDVEff_{t}(\TaxLev)) + \dot{\NetWorth})
> \\ & =  (\diePrb+\discRte)(\rfree \NetWorth+(\rfree+\diePrb)(\HNrm - \PDVEff_{t}(\TaxLev))-\CNrm)
> \end{aligned}\end{gathered}
> ```
>
> Now solve {eq}`eq:Cnew` for {math}`\HNrm - \PDVEff_{t}(\TaxLev)`,
>
> ```{math}
> :label: eq:18
>
> \begin{gathered}\begin{aligned}
>   \HNrm - \PDVEff_{t}(\TaxLev) & =  \left(\frac{\CNrm}{\diePrb+ \discRte}\right)-\NetWorth
> \end{aligned}\end{gathered}
> ```
>
> and substitute into {eq}`eq:dotCnew` to obtain
>
> ```{math}
> \begin{gathered}\begin{aligned}
>   \dot{\CNrm} & =  (\diePrb+\discRte)(\rfree \NetWorth+(\rfree+\diePrb)(\CNrm(\diePrb+\discRte)^{-1} - \NetWorth)-\CNrm)
> \\        & =  (\rfree+\diePrb)\CNrm - (\diePrb+\discRte)\CNrm- \diePrb(\diePrb+\discRte)\NetWorth
> \\ & =  (\rfree-\discRte)\CNrm - \diePrb(\diePrb+\discRte)(\KNrm+\Debt).
> \end{aligned}\end{gathered}
> ```
>
> Since we are assuming that {math}`\Debt` is a constant (after the fiscal
>
> experiment), any combination of {math}`\CNrm` and {math}`\KNrm` that would have been on
>
> the {math}`\dot{\CNrm}=0` locus before the policy shift now has a value {math}`\dot{\CNrm} = -\diePrb(\diePrb+\discRte)\Debt`. This means that the {math}`\CNrm` that would restore
>
> {math}`\dot{\CNrm}=0` must be a larger {math}`\CNrm`, which says that the {math}`\dot{\CNrm}=0`
>
> locus shifts up (or, equivalently, to the left). Thus, the new
>
> equilibrium will be at a lower value of {math}`\KNrm` and a higher interest
>
> rate.
>
> The phase diagram shows that the new equilibrium point {math}`A'` is to the left
>
> of the original equilibrium. This is because at a given level of the aggregate
>
> capital stock, consumers spend more: they hold the bonds, {math}`\NetWorth>\KNrm`, but will pay only part of the taxes that service them; the rest falls on generations not yet born. Thus,
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
> equilibrium at the level of consumption {math}`\CNrm_{0}` corresponding to the
>
> equilibrium labeled {math}`A` in the phase diagram. At time 0, the fiscal
>
> policy is carried out. The fiscal policy immediately increases
>
> consumption because it amounts to a transfer of resources from future
>
> to current generations. However, the higher level of consumption runs
>
> down the capital stock per capita, and so over time consumption asymptotically
>
> approaches a new, lower equilibrium level of consumption {math}`\CNrm'`.

:::{figure} /content/figures/BlanchardFiniteHorizon/BlanchardCDynamics.png
:::

Blanchard shows that if the model is changed so that each
consumer's income declines exponentially at rate {math}`-\PermGroRte` after
birth, the result is equivalent to assuming that future labor income
is discounted at an interest rate that is higher by {math}`-\PermGroRte`. He
further shows that the equations of motion of the model change to

```{math}
:label: eq:lccdot

\begin{gathered}\begin{aligned}
  \dot{\CNrm} & =  (\kapShare \KNrm^{\kapShare-1}-\deprRte -\PermGroRte-\discRte)\CNrm-(\diePrb-\PermGroRte)(\diePrb+\discRte)\KNrm
\\ \dot{\KNrm} & =  \KNrm^{\kapShare}-\deprRte \KNrm - \CNrm.
\end{aligned}\end{gathered}
```

Note that it is possible to rewrite the {math}`\dot{\CNrm}=0` locus as

```{math}
:label: eq:lccdoteq0

\begin{gathered}\begin{aligned}
  (\kapShare \KNrm^{\kapShare-1}-\deprRte -\PermGroRte-\discRte)\CNrm & =  (\diePrb-\PermGroRte)(\diePrb+\discRte)\KNrm
\end{aligned}\end{gathered}
```

Use this equation to show that as {math}`\CNrm \rightarrow \infty`, the
{math}`\dot{\CNrm}=0` locus asymptotes to

```{math}
:label: eq:eqblcr

\begin{gathered}\begin{aligned}
 \rfree = \kapShare \KNrm^{\kapShare-1} - \deprRte & =  \discRte + \PermGroRte
\end{aligned}\end{gathered}
```

Thus, for a large enough value of {math}`-\PermGroRte` it is possible that the net
interest rate in this economy could be negative. Draw a phase diagram
corresponding to an equilibrium with a negative net interest rate, and
comment on why this is an interesting case to think about. In
particular, what new light does it shed on the fiscal policy
experiment examined above?

> *Answer:*
>
> As {math}`\CNrm` goes to infinity on the LHS of {eq}`eq:lccdoteq0`, the only way
>
> the equation can continue to hold is if
>
> ```{math}
> \begin{gathered}\begin{aligned}
>  \lim_{\CNrm \rightarrow \infty} (\kapShare \KNrm^{\kapShare-1}-\deprRte -\PermGroRte-\discRte) & =  0
> \end{aligned}\end{gathered}
> ```
>
> which implies {eq}`eq:eqblcr`.
>
> The new phase diagram shows the {math}`\dot{\CNrm}=0` locus intersecting the
>
> {math}`\dot{\KNrm}=0` locus to the right of the maximum of the {math}`\dot{\KNrm}=0` locus.
>
> This is implied by the fact that the net interest rate is negative, which
>
> means that output net of depreciation, and with it consumption at every date, could be increased by reducing
>
> the capital stock.
>
> The reason this is an interesting case is that in this case it is
>
> possible for the economy to be in a condition of dynamic inefficiency,
>
> just as in the Diamond OLG model. The idea
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

