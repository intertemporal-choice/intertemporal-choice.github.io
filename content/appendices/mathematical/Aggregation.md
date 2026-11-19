(sec:Aggregation)=
# Aggregation For Dummies (Macroeconomists)

Consider an economy populated by a set of agents distributed uniformly along
the unit interval with a total population mass of 1. That is, for {math}`i \in [0,1]` the
probability distribution function is {math}`f(i) = 1` and {math}`f(i)=0` elsewere; the CDF on the {math}`[0,1]` interval is therefore
{math}`F(i)=i`, implying an aggregate population mass of {math}`F(1)=1`.

Agent {math}`i`'s value of variable {math}`\bullet` at date {math}`t` is {math}`\bullet_{t,i}`.

Thus aggregate consumption is

```{math}
\begin{gathered}\begin{aligned}
  C_{t} & =  \int_{0}^{1} c_{t,i} f(i) di,
\\ & =  \int_{0}^{1} c_{t,i} di,
\end{aligned}\end{gathered}
```

and a similar notation applies to other variables.

Since the aggregate population is normalized to 1, capital
letters refer not only to aggregate variables but also to
per capita variables, since per-capita consumption is
aggregate consumption divided by aggregate population:

```{math}
\begin{gathered}\begin{aligned}
  \left(\frac{\int_{0}^{1} c_{t,i} f(i) di}{\int_{0}^{1} f(i) di}\right) & =  \left(\frac{C_{t}}{1}\right) = C_{t}.
\end{aligned}\end{gathered}
```

Each individual agent is infinitesimally small, and can therefore
neglect the effects of its own actions on aggregates.

## Blanchard Lives

For many purposes the assumption that economic agents live forever is useful;

but for other purposes it is necessary to be able to analyze agents with finite horizons. {cite:t}`blanchardFinite` introduced a
tractable framework that permits analysis of many of the key issues
posed by finite lifetimes.

The key assumption is that the probability
of death is independent of the agent's age. (This is similar to the {cite:t}`calvoPrices`
assumption that the probability that a firm will change its prices is independent of the time
elapsed since the last price change).

The most convenient formulation of the model is one in which the number of dying
individuals is always equal to the number of newborn individuals, so that the population
remains constant.

### Discrete Time

As above, suppose that the population alive at time {math}`t` is arranged on the unit interval.

The probability of death is {math}`\diePrb` (and the probability of not dying is {math}`\LivPrb = 1-\diePrb`).

Then for a person living at any location {math}`i \in [0,1]`, expected remaining lifetime including the
current period will be

```{math}
\begin{gathered}\begin{aligned}
  1 + \overbrace{(1-\DiePrb)}^{\LivPrb} + (1-\DiePrb)^{2} + \ldots & =  \left(\frac{1}{1-(1-\DiePrb)}\right)
\\ & =  1/\DiePrb
.
\end{aligned}\end{gathered}
```

If a new cohort of size {math}`\DiePrb` has been born each period since the beginning of time, the total population will be given by the size of a new cohort {math}`\DiePrb` multiplied by the expected lifetime {math}`\DiePrb^{-1}`:

```{math}
\begin{gathered}\begin{aligned}
  \DiePrb \DiePrb^{-1} & =  1,
\end{aligned}\end{gathered}
```

so that the mass of the aggregate population is constant at 1, as above.

### Continuous Time

Blanchard's original treatment was in continuous time, with a constant
rate of death {math}`\diePrb`, so that the probability of remaining alive (not dead)
after {math}`t` periods for a consumer born in period 0 is

:::{margin}
The number of people who will die during the first period in the continuous-time model is measured by the difference between an initial population of size 1 and the size of the population remaining alive after one period, {math}`1-\Alive_{1}=1-e^{-\diePrb}`. [ExpEps](#fact:expeps) in the [Math Facts](#fact:mathfactslist) list implies that {math}`e^{-\diePrb} \approx 1-\diePrb`; therefore the proportion who have died will be approximately {math}`1-(1- \diePrb)=\diePrb`. Hence for small death rates, in order for the same population to survive for one period in a continuous-time model with death rate {math}`\diePrb` and the discrete-time model with death rate {math}`\DiePrb`, one would need {math}`\diePrb \approx \DiePrb`.
:::

```{math}
\begin{gathered}\begin{aligned}
  \Alive_{t} & =  e^{-\diePrb \tNow}
\end{aligned}\end{gathered}
```

so that the expected life span is

```{math}
\begin{gathered}\begin{aligned}
  \int_{0}^{\infty} e^{-\diePrb \tau} d\tau & =  1/\diePrb
\end{aligned}\end{gathered}
```

and if the flow arrival rate of new population is {math}`\diePrb` (that is, at each instant a flow of new population arrives at rate {math}`\diePrb`) then again the population
mass is constant at

```{math}
\begin{gathered}\begin{aligned}
  \diePrb/\diePrb & =  1.
\end{aligned}\end{gathered}
```

### Population Growth

Now suppose that the population in the discrete-time model is growing by a factor {math}`\PopGroFac \approx 1+\popGroRte` from period to period; if the number of newborns in period 0 was 1, then the number of newborns in period {math}`t` is given by

:::{margin}
The population growth rate is written {math}`\PopnGroRte`: {math}`\PopnGroFac` is the population's growth factor and {math}`\lnat` is the natural log, so {math}`\PopnGroRte = \log \PopnGroFac`. In discrete time, where the population grows by the factor {math}`\PopnGroFac` a period, {math}`\PopnGroRte` stands for the net rate {math}`\PopnGroFac-1`, which it approximates when growth is slow.
:::

```{math}
\begin{gathered}\begin{aligned}
  \PopGroFac^{t}.
\end{aligned}\end{gathered}
```

In this framework we want to keep track of the  relative population of each cohort compared
to the size of the newborn cohort. At age {math}`\age`, the cohort that was born in period 0
will be of relative size

```{math}
\begin{gathered}\begin{aligned}
  (\LivPrb/\PopGroFac)^{\age}
\end{aligned}\end{gathered}
```

The total relative populations will be

```{math}
:label: eq:4

\begin{gathered}\begin{aligned}
  1 + (\LivPrb/\PopGroFac) + (\LivPrb/\PopGroFac)^{2} + ... & =  \left(\frac{1}{1-\LivPrb/\PopGroFac}\right)
\end{aligned}\end{gathered}
```

so that if in period 0 the population was of size {math}`(1-\LivPrb/\PopGroFac)` then the sizes
of the relative populations will add up to one even as the absolute population grows by
the factor {math}`\PopGroFac`.
