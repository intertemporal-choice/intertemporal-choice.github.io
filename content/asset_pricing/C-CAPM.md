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

where {math}`\Rfree` denotes the return on a perfectly riskless asset and {math}`\Risky_{t+1,i}` denotes the return on asset {math}`i` between periods {math}`t` and {math}`t+1`, {math}`\omega_{t,i}` is the share of end-of-period savings invested in asset {math}`i`, and {math}`\Rport_{t+1}` is the portfolio-weighted rate of return, and {math}`y_{t+1}` is noncapital income in period {math}`t+1`.

As usual, the objective can be rewritten in recursive form:

```{math}
\begin{gathered}\begin{aligned}
        \vFunc(\mRat_{t}) & =  \max_{\{c_{t},\omega_{1,t},\omega_{2,t},\ldots\}} \uFunc(c_{t}) +\beta \Ex_{t}\left[\vFunc(\Rport_{t+1}(\mRat_{t}-c_{t})+{y}_{t+1})\right]
\end{aligned}\end{gathered}
```

The first order condition with respect to {math}`c_{t}` is

```{math}
:label: eq:CCAPM-cfoc

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t}) & =  \beta \Ex_{t}[\Rport_{t+1}\vFunc^{\prime}({m}_{t+1})].
\end{aligned}\end{gathered}
```

and the FOC with respect to {math}`\omega_{t,i}` is

```{math}
:label: eq:CCAPM-gamfoc

\begin{gathered}\begin{aligned}
        \Ex_{t}[(\Risky_{t+1,i}-\Rfree)\vFunc^{\prime}({m}_{t+1})] & =  0
\end{aligned}\end{gathered}
```

But the usual logic of the Envelope theorem tells us that

```{math}
:label: eq:CCAPM-envelope

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t+1}) & =  \vFunc^{\prime}(\mRat_{t+1}),
\end{aligned}\end{gathered}
```

so, substituting {eq}`eq:CCAPM-envelope` into {eq}`eq:CCAPM-cfoc` and {eq}`eq:CCAPM-gamfoc` we have

```{math}
:label: eq:gameuler

\begin{gathered}\begin{aligned}
        \uFunc^{\prime}(c_{t}) & =  \Ex_{t}\left[\beta \Rport_{t+1} \uFunc^{\prime}({c}_{t+1})\right]
\\      \Ex_{t}[(\Risky_{t+1,i}-\Rfree)\uFunc^{\prime}({c}_{t+1})] & =  0
.
\end{aligned}\end{gathered}
```

Now assume CRRA utility, {math}`\uFunc(c) \equiv c^{1-\rho}/(1-\rho)` and divide both sides of {eq}`eq:gameuler` by {math}`c_{t}^{-\rho}` to get

```{math}
:label: eq:CCAPM-gameulernew

\begin{gathered}\begin{aligned}
        \Ex_{t}[(c_{t+1}/c_{t})^{-\rho}(\Risky_{t+1,i}-\Rfree)] & =  0
\end{aligned}\end{gathered}
```

We can now follow the same steps as in the "Equity Premium Puzzle" section to obtain the relation that *for every asset {math}`i`*

```{math}
:label: eq:CCAPM-eqprem

\begin{gathered}\begin{aligned}
        \Ex_{t}[\Risky_{t+1,i}]-\Rfree & \approx  \frac{\rho \text{cov}_{t}(\Delta \log {c}_{t+1},\Risky_{t+1,i})}{1-\rho \Ex_{t}[ \Delta \log {c}_{t+1}]}
\\                             & \approx  \rho \text{cov}_{t}(\Delta \log {c}_{t+1},\Risky_{t+1,i})
\end{aligned}\end{gathered}
```

What does this imply about asset pricing?

Consider an asset for which the return covaries positively with consumption, {math}`\mbox{cov}(\Risky_{t+1,i},\Delta \log c_{t+1}) > 0`. For such an asset, the *marginal utility* will negatively covary with the return. Thus the expected return must be higher for an asset that "does well" when consumption is high. But for a given average stream of dividends or payouts, if the average return is high, the average price must be low. Thus this indicates that prices should be low for assets whose payoffs are procyclical, and high for assets whose payoffs are countercyclical.
