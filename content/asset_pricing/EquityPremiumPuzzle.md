(sec:EquityPremiumPuzzle)=
# The Equity Premium Puzzle and the Riskfree Rate

This section derives the equity premium puzzle ({cite:t}`mehraPrescottPuzzle`). Consider a representative agent solving the joint consumption and portfolio allocation problem:

```{math}
\begin{aligned}
\vFunc(m_{t}) & = \max_{\{c_{t},\riskyshare_{t}\}} ~\uFunc(c_{t}) + \Ex_{t}\left[\sum_{n=1}^{\infty} \Discount^{n} \uFunc(c_{t+n}) \right] \\
& \text{s.t.} \\
m_{t+1} & = (m_{t}-c_{t})\Rport_{t+1} + y_{t+1} \\
\Rport_{t+1} & = \riskyshare_{t}\Risky_{t+1}+(1-\riskyshare_{t})\Rfree
\end{aligned}
```

where {math}`\Rfree` denotes the return on a perfectly riskless asset and {math}`\Risky_{t+1}` denotes the return on equities (the risky asset) held between periods {math}`t` and {math}`t+1`, {math}`\riskyshare_{t}` is the share of end-of-period savings invested in the risky asset, {math}`\Rport_{t+1}` is the portfolio-weighted rate of return, and {math}`y_{t+1}` is noncapital income in period {math}`t+1`.

As usual, the objective can be rewritten in recursive form:

```{math}
\vFunc(m_{t}) = \max_{\{c_{t},\riskyshare_{t}\}} ~\uFunc(c_{t}) +\Discount \Ex_{t}\left[\vFunc\left(\underbrace{[\riskyshare_{t}\Risky_{t+1}+(1-\riskyshare_{t})\Rfree]}_{{\Rport}_{t+1}}(m_{t}-c_{t})+{y}_{t+1}\right)\right]
```

The first order condition with respect to {math}`c_{t}` is

```{math}
:label: eq:EPP-cfoc

\uFunc^{\prime}(c_{t}) = \Discount \Ex_{t}[ \Rport_{t+1}\vFunc^{\prime}({m}_{t+1})]
```

and the FOC with respect to {math}`\riskyshare_{t}` is

```{math}
:label: eq:EPP-gamfoc

\begin{aligned}
\Ex_{t}[(\Risky_{t+1}-\Rfree)\vFunc^{\prime}({m}_{t+1})({m}_{t}-{c}_{t})] & = 0 \\
\Ex_{t}[(\Risky_{t+1}-\Rfree)\vFunc^{\prime}({m}_{t+1})] & = 0
\end{aligned}
```

But the usual logic of the [Envelope theorem](#sec:Envelope) tells us that

```{math}
:label: eq:EPP-envelope

\uFunc^{\prime}(c_{t+1}) = \vFunc^{\prime}(m_{t+1})
```

so, substituting {eq}`eq:EPP-envelope` into {eq}`eq:EPP-cfoc` and {eq}`eq:EPP-gamfoc` we have

```{math}
:label: eq:EPP-ceuler

\begin{aligned}
\uFunc^{\prime}(c_{t}) & = \Ex_{t}\left[\Discount \Rport_{t+1} \uFunc^{\prime}({c}_{t+1})\right] \\
\Ex_{t}[(\Risky_{t+1}-\Rfree)\uFunc^{\prime}({c}_{t+1})] & = 0
\end{aligned}
```

Now assume CRRA utility, {math}`\uFunc(c) = c^{1-\CRRA}/(1-\CRRA)` and divide both sides by {math}`c_{t}^{-\CRRA}` to get

```{math}
:label: eq:EPP-gameulernew

\Ex_{t}[(c_{t+1}/c_{t})^{-\CRRA}(\Risky_{t+1}-\Rfree)] = 0
```

Now recall the following two facts:

> **Fact 1:** If {math}`\Delta c_{t+1}/c_{t}` is small, {math}`c_{t+1}/c_{t} \approx 1+ \Delta \log c_{t+1}`.
>
> **Fact 2:** If {math}`z` is small, {math}`(1+z)^{\lambda} \approx 1 + \lambda z`.

Using these two facts, equation {eq}`eq:EPP-gameulernew` can be approximated by

```{math}
\Ex_{t}[(1-\CRRA \Delta \log {c}_{t+1})(\Risky_{t+1}-\Rfree)] \approx 0
```

Using one more fact,

> **Fact 3:** {math}`\Ex [xy] = \Ex [x]\Ex [y] + \text{cov}(x,y)`

we get

```{math}
(1-\CRRA \Ex_{t}[\Delta \log {c}_{t+1}])(\Rfree - \Ex_{t}[\Risky_{t+1}])+\text{cov}_{t}(-\CRRA \Delta \log {c}_{t+1},-\Risky_{t+1}) \approx 0
```

or

```{math}
:label: eq:EPP-eqprem

\begin{aligned}
\Ex_{t}[\Risky_{t+1}]-\Rfree & \approx \frac{\CRRA \text{cov}_{t}(\Delta \log {c}_{t+1},\Risky_{t+1})}{1-\CRRA \Ex_{t}[ \Delta \log {c}_{t+1}]} \\
& \approx \CRRA \text{cov}_{t}(\Delta \log {c}_{t+1},\Risky_{t+1})
\end{aligned}
```

where the last approximation holds because {math}`\Ex_{t}[\Delta \log {c}_{t+1}]` is small.

## The Equity Premium Puzzle

Because this expression must hold at all {math}`t`, we can check it empirically by calculating empirical estimates of the two components and assuming that the sample averages correspond to the representative agent's expectations. That is, if we have data for periods {math}`1 \ldots n`, we assume that the unconditional expectations correspond to the sample means, {math}`\Ex [\Risky] = (1/n) \sum_{s=1}^{n} \Risky_{s}`; {math}`\Ex [\Delta \log c] = (1/n) \sum_{s=1}^{n} \Delta \log c_{s}`; and {math}`\text{cov}(\Delta \log c,\Risky) = (1/n) \sum_{s=1}^{n} (\Delta \log c_{s} - \Ex [\Delta \log c])(\Risky_{s}-\Ex [\Risky])`.

The equity premium puzzle is essentially that {math}`\text{cov}(\Delta \log c,\Risky)` is very small (about 0.004) but {math}`\Ex [\Risky]-\Rfree` is about 0.08 (stocks have earned real returns of about 8 percent more than riskless assets over the historical period), which means that the only way equation {eq}`eq:EPP-eqprem` can hold is if {math}`\CRRA` is implausibly large (these values imply a value of {math}`\CRRA=20`).

How do we know what plausible values of {math}`\CRRA` are? Consider the following. You must choose between a gamble in which you consume \$50,000 for the rest of your life with probability 0.5 and \$100,000 with probability 0.5, or consuming some amount {math}`X` with certainty. The coefficient of relative risk aversion determines the {math}`X` which would make you indifferent between consuming X or being exposed to the gamble. For example, if {math}`\CRRA = 0`, then you have no risk aversion at all and you will be indifferent between \$75,000 with certainty and the 50/50 gamble with expected value of \$75,000. Here are the values of X associated with different values of {math}`\CRRA` (table taken from {cite:t}`mankiw&zeldes:stockholders`).

:::{list-table} Certainty equivalent {math}`X` for different coefficients of relative risk aversion
:header-rows: 1
:name: tbl:crra-certainty-equiv

* - {math}`\CRRA`
  - {math}`X`
* - 1
  - 70,711
* - 3
  - 63,246
* - 5
  - 58,565
* - 10
  - 53,991
* - 20
  - 51,858
* - 30
  - 51,209
* - {math}`\infty`
  - 50,000
:::

## The Riskfree Rate Puzzle

Rewrite the consumption Euler equation {eq}`eq:EPP-ceuler` as

```{math}
:label: eq:EPP-newgam

\uFunc^{\prime}(c_{t}) = \Ex_{t}\left[\Discount (\Rfree + \riskyshare_{t} [\Risky_{t+1} - \Rfree])\uFunc^{\prime}({c}_{t+1})\right]
```

and note that from {eq}`eq:EPP-gameulernew` we know that {math}`\Ex_{t}[\Discount \riskyshare_{t}(\Risky_{t+1}-\Rfree)\uFunc^{\prime}({c}_{t+1})] = 0` so that {eq}`eq:EPP-newgam` reduces to the ordinary Euler equation

```{math}
\begin{aligned}
\uFunc^{\prime}(c_{t}) & = \Ex_{t}[\Discount \Rfree \uFunc^{\prime}({c}_{t+1})] \\
1 & = \Discount \Rfree \Ex_{t}[ ({c}_{t+1}/c_{t})^{-\CRRA}]
\end{aligned}
```

Using the same "facts" and approximations as above, we get the standard approximation to the Euler equation,

```{math}
\Delta \log c_{t+1} \approx (1/\CRRA) (\rfree - \timeRate)
```

The "riskfree rate puzzle" is that average consumption growth per capita has been about 1.5 percent (in the US in the postwar period) while real riskfree interest rates have been at most 1 percent. Even if we assume a time preference rate of {math}`\timeRate=0` (no impatience at all, e.g. {math}`\Discount=1`), the only way this equation can hold is if {math}`\CRRA` is a very small number (maybe even less than one). Of course, this is precisely the opposite of the conclusion of the equity premium puzzle, which implies the {math}`\CRRA` must be very large.

The riskfree rate puzzle might in principle be explicable by overlapping generations, though in practice it is hard to make that work well. A precautionary saving motive also cuts against the puzzle, by adding a variance term to consumption growth.
