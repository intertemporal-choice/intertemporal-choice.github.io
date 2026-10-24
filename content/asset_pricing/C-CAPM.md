(sec:C-CAPM)=
# The Consumption Capital Asset Pricing Model (C-CAPM)

Consider a representative agent solving the joint consumption and portfolio allocation problem:

```{math}
\begin{gathered}\begin{aligned}
        \vFunc(\mRat_{t}) & =  \max \uFunc(c_{t}) + \Ex_{t}\left[\sum_{n=1}^{\infty} \Discount^{n} \uFunc(c_{t+n}) \right]
\\  & \text{s.t.}
\\      \mRat_{t+1} & =  (\mRat_{t}-c_{t})\Rport_{t+1} + y_{t+1}
\\      \Rport_{t+1} & =  \sum_{i=1}^{m}\omega_{t,i}\Risky_{t+1,i}+\left(1-\sum_{i=1}^{m} \omega_{t,i}\right)\Rfree
\end{aligned}\end{gathered}
```

where {math}`\Rfree` denotes the return factor on a perfectly riskless asset and {math}`\Risky_{t+1,i}` denotes the return factor on asset {math}`i` between periods {math}`t` and {math}`t+1`, {math}`\omega_{t,i}` is the share of end-of-period savings invested in asset {math}`i`, and {math}`\Rport_{t+1}` is the portfolio-weighted return factor, and {math}`y_{t+1}` is noncapital income in period {math}`t+1`.

As usual, the objective can be rewritten in recursive form:

```{math}
\begin{gathered}\begin{aligned}
        \vFunc(\mRat_{t}) & =  \max_{\{c_{t},\omega_{t,1},\omega_{t,2},\ldots\}} \uFunc(c_{t}) +\Discount \Ex_{t}\left[\vFunc(\Rport_{t+1}(\mRat_{t}-c_{t})+{y}_{t+1})\right]
\end{aligned}\end{gathered}
```

The first order condition with respect to {math}`c_{t}` is

```{math}
:label: eq:CCAPM-cfoc

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t}) & =  \Discount \Ex_{t}[\Rport_{t+1}\vFunc^{\prime}(\mRat_{t+1})].
\end{aligned}\end{gathered}
```

and the FOC with respect to {math}`\omega_{t,i}` is

```{math}
:label: eq:CCAPM-gamfoc

\begin{gathered}\begin{aligned}
        \Ex_{t}[(\Risky_{t+1,i}-\Rfree)\vFunc^{\prime}(\mRat_{t+1})] & =  0
\end{aligned}\end{gathered}
```

But the usual logic of the [Envelope theorem](#sec:Envelope) tells us that

```{math}
:label: eq:CCAPM-envelope

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t+1}) & =  \vFunc^{\prime}(\mRat_{t+1}),
\end{aligned}\end{gathered}
```

so, substituting {eq}`eq:CCAPM-envelope` into {eq}`eq:CCAPM-cfoc` and {eq}`eq:CCAPM-gamfoc` we have

```{math}
:label: eq:CCAPM-ceuler

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t}) & =  \Ex_{t}\left[\Discount \Rport_{t+1} \uFunc^{\prime}({c}_{t+1})\right]
\end{aligned}\end{gathered}
```

```{math}
:label: eq:CCAPM-gameuler

\begin{gathered}\begin{aligned}
        \Ex_{t}[(\Risky_{t+1,i}-\Rfree)\uFunc^{\prime}({c}_{t+1})] & =  0
.
\end{aligned}\end{gathered}
```

Now assume CRRA utility, {math}`\uFunc(c) \equiv c^{1-\CRRA}/(1-\CRRA)` and divide both sides of {eq}`eq:CCAPM-gameuler` by {math}`c_{t}^{-\CRRA}` to get

```{math}
:label: eq:CCAPM-gameulernew

\begin{gathered}\begin{aligned}
        \Ex_{t}[(c_{t+1}/c_{t})^{-\CRRA}(\Risky_{t+1,i}-\Rfree)] & =  0
\end{aligned}\end{gathered}
```

If consumption growth is small, {math}`c_{t+1}/c_{t} \approx 1+ \Delta \log c_{t+1}` ([ExpEps](#fact:expeps)), and if {math}`z` is small, {math}`(1+z)^{\lambda} \approx 1 + \lambda z` ([TaylorOne](#fact:taylorone)). With these, {eq}`eq:CCAPM-gameulernew` can be approximated by

```{math}
\Ex_{t}[(1-\CRRA \Delta \log {c}_{t+1})(\Risky_{t+1,i}-\Rfree)] \approx 0
```

and by the definition of covariance, {math}`\Ex [xy] = \Ex [x]\Ex [y] + \cov(x,y)`,

```{math}
(1-\CRRA \Ex_{t}[\Delta \log {c}_{t+1}])(\Ex_{t}[\Risky_{t+1,i}]-\Rfree)-\CRRA \cov_{t}(\Delta \log {c}_{t+1},\Risky_{t+1,i}) \approx 0,
```

so that *for every asset {math}`i`*

```{math}
:label: eq:CCAPM-eqprem

\begin{gathered}\begin{aligned}
        \Ex_{t}[\Risky_{t+1,i}]-\Rfree & \approx  \frac{\CRRA \cov_{t}(\Delta \log {c}_{t+1},\Risky_{t+1,i})}{1-\CRRA \Ex_{t}[ \Delta \log {c}_{t+1}]}
\\                             & \approx  \CRRA \cov_{t}(\Delta \log {c}_{t+1},\Risky_{t+1,i})
\end{aligned}\end{gathered}
```

where the last approximation holds when {math}`\CRRA\Ex_{t}[\Delta \log {c}_{t+1}]` is small.

What does this imply about asset pricing?

Consider an asset for which the return covaries positively with consumption, {math}`\cov(\Risky_{t+1,i},\Delta \log c_{t+1}) > 0`. For such an asset, the *marginal utility* will negatively covary with the return. Thus the expected return must be higher for an asset that "does well" when consumption is high. But for a given average stream of dividends or payouts, if the average return is high, the average price must be low. Thus this indicates that prices should be low for assets whose payoffs are procyclical, and high for assets whose payoffs are countercyclical.

Risk aversion moves prices in two ways, and {eq}`eq:CCAPM-eqprem` shows only one. Through the covariance it governs *relative* prices: a higher {math}`\CRRA` raises every asset's premium in proportion to its covariance with consumption, so assets that covary more lose value relative to those that covary less. The *level* of all prices also depends on the riskless rate, which {eq}`eq:CCAPM-eqprem` takes as given. A higher {math}`\CRRA` moves that rate in two directions: precaution lowers it, which raises prices, as in the economies without growth of [The Lucas Asset Pricing Model](#sec:LucasAssetPrice); and when consumption is expected to grow, a lower willingness to substitute over time raises it, which lowers prices. For consumption-like growth and risk the second effect dominates (see [When Dividends Follow a Random Walk](#When-Dividends-Follow-a-Random-Walk)).
