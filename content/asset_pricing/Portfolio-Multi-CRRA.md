(sec:Portfolio-Multi-CRRA)=
# CRRA Portfolio Choice with Two Risky Assets
{cite:t}`merton:restat` and {cite:t}`samuelson:portfolio` study optimal portfolio allocation for a consumer with Constant Relative Risk Aversion utility {math}`\uFunc(c) = (1-\CRRA)^{-1}c^{1-\CRRA}` who can choose among many risky investment options.

Using their framework, here we study a consumer who has wealth {math}`\aRat_{t}` at the end of period {math}`t`, and is deciding how much to invest in two risky assets with lognormally distributed return factors {math}`\Risky_{t+1}=(\Risky_{1,t+1}, \Risky_{2,t+1})'`, {math}`\log \Risky_{t+1} = \risky_{t+1}=(\risky_{1,t+1}, \risky_{2,t+1})' \sim \left ( \mathcal{N}(\risky_1,\sigma^{2}_{1}), \mathcal{N}(\risky_2,\sigma^{2}_{2}) \right)'`, with covariance matrix

```{math}
\left(\begin{array}{cc}\sigma_1^2 & \sigma_{12} \\ \sigma_{12}& \sigma_2^2\end{array}\right).
```

If the period-{math}`t` consumer invests proportion {math}`\riskyshare_i` of {math}`\aRat_{t}` in risky asset {math}`i`, {math}`i=1,2` (so that {math}`\riskyshare_{1}=(1-\riskyshare_{2})` and vice-versa), spending all available resources in the last period of life[^samuelson] {math}`t+1` will yield:

[^samuelson]: The portfolio allocation solution obtained below induces back to earlier periods of life, as {cite:t}`samuelsonFallacy` and {cite:t}`samuelsonJudgment` famously emphasized.

```{math}
:label: eq:PortMulti-RportDef

c_{t+1}  =  \underbrace{(\riskyshare \cdot \Risky_{t+1} )}_{\equiv \Rport_{t+1}} \aRat_{t}
```

where {math}`\Rport_{t+1}` is the portfolio-weighted return factor.

{cite:t}`cvAppendix` point out that a good approximation to the portfolio rate of return is obtained by

```{math}
\rport_{t+1} = \risky_{1,t+1}+\riskyshare_{2} (\risky_{2,t+1}-\risky_{1,t+1})+ \riskyshare_2 (1-\riskyshare_2) \eta/2
```

where

```{math}
\eta=(\sigma_1^2+\sigma_2^2-2\sigma_{12}).
```

Using this approximation, the expectation as of date {math}`t` of utility at date {math}`t+1` is:

```{math}
:label: eq:PortMulti-exputil

\begin{aligned}
  \Ex_{t}[\uFunc(c_{t+1})] & \approx  (1-\CRRA)^{-1}\Ex_{t}\left[\left(\aRat_{t}e^{\risky_{1,t+1}}e^{\riskyshare_2 (\risky_{2,t+1}-\risky_{1,t+1})+\riskyshare_2(1-\riskyshare_2)\eta /2}\right)^{1-\CRRA}\right]
\\                      & \approx  \underbrace{ (1-\CRRA)^{-1}\aRat_{t}^{1-\CRRA}}_{\text{constant $< 0$}}\underbrace{e^{ (1-\CRRA)\riskyshare_2(1-\riskyshare_2)\eta/2}\Ex_{t}\left[e^{(\risky_{1,t+1}+\riskyshare_2 (\risky_{2,t+1}-\risky_{1,t+1}))  (1-\CRRA)}\right]}_{\text{excess return utility factor}}
  \end{aligned}
```

where the first term is a negative constant under the usual assumption that relative risk aversion {math}`\CRRA>1.`

Our foregoing assumptions imply that

```{math}
(1-\CRRA) (\riskyshare_1 \risky_{1,t+1}+\riskyshare_2 \risky_{2,t+1})
   \sim \mathcal{N}( (1-\CRRA)(\riskyshare_1\risky_1+\riskyshare_2 \risky_2),      (1-\CRRA)^2 (   \riskyshare_1^2\sigma_1^2+\riskyshare_2^2\sigma_2^2+2\riskyshare_1\riskyshare_2\sigma_{12}))
```

(using [LogELogNormTimes](#fact:logelognormtimes)). With a couple of extra lines of derivation we can show that the log of the expectation in {eq}`eq:PortMulti-exputil` is

```{math}
:label: eq:PortMulti-Ex

  \log \Ex_{t}\left[e^{(\risky_{1,t+1}+\riskyshare_2 (\risky_{2,t+1}-\risky_{1,t+1}))  (1-\CRRA)}\right]  =  {(1-\CRRA)(\riskyshare_1 \risky_1+\riskyshare_2 \risky_2) + (1-\CRRA)^2 (\riskyshare_1^2\sigma_1^2+\riskyshare_2^2\sigma_2^2+2\riskyshare_1\riskyshare_2\sigma_{12})/2}
```

Substituting from {eq}`eq:PortMulti-Ex` for the log of the expectation in {eq}`eq:PortMulti-exputil`, the log of the "excess return utility factor" in {eq}`eq:PortMulti-exputil` is

```{math}
  (1-\CRRA)\riskyshare_2(1-\riskyshare_2)\eta/2+(1-\CRRA) (\risky_1+\riskyshare_2(\risky_2-\risky_1))+(\CRRA-1)^2 (\sigma_1^2+\riskyshare_2^2 \eta+2\riskyshare_2(\sigma_{12}-\sigma_2^2))/2
.
```

The {math}`\riskyshare` that minimizes this log will also minimize the level; the FOC for minimizing this expression is

```{math}
:label: eq:PortMulti-riskyshareMS

\begin{aligned}
         (1-2\riskyshare_2)\eta/2+ \risky_2-\risky_1+(1-\CRRA) (\riskyshare_2 \eta+(\sigma_{12}-\sigma_1^2)) & =  0 \\
         \quad(\risky_2-\risky_1+\frac{\eta}{2})+(1-\CRRA) (\sigma_{12}-\sigma_1^2) & = \CRRA \eta \riskyshare_2.
\end{aligned}
```

So

```{math}
\riskyshare_2  =  \left(\frac{\risky_2-\risky_1+\eta/2+(1-\CRRA)(\sigma_{12}-\sigma_1^2)}{\CRRA\eta}\right)
```

and note that if the first asset is riskfree so that {math}`\sigma_{1}=\sigma_{12}=0` then this reduces to

```{math}
:label: eq:riskyshare2

\riskyshare_2  =  \left(\frac{\risky_2-\risky_1+\sigma^{2}_{2}/2}{\CRRA\sigma^{2}_{2}}\right)
```

but the log of the expected return premium (in levels) on the risky over the safe asset in this case is {math}`\EpremLog \equiv \log \Risky_{2}/\Risky_{1} = \risky_{2}-\risky_{1}+\sigma^{2}_{2}/2` (recalling that we have assumed {math}`\sigma_{12}=\sigma^{2}_{1}=0`), so {eq}`eq:riskyshare2` becomes

```{math}
\riskyshare_2  =  \left(\frac{\EpremLog}{\CRRA\sigma^{2}_{2}}\right)
```

which corresponds to the solution obtained for the case of a single risky asset in the [](#sec:Portfolio-CRRA).
