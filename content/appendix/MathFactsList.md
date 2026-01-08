(fact:mathfactslist)=
# Math Facts Useful for Graduate Macroeconomics
The following collection of facts is useful in many macroeconomic models. No proof is offered in most cases because the derivations are standard elements of prerequisite mathematics or microeconomics classes; this section is offered as an aide memoire and for reference purposes.

Throughout this document, typographical distinctions should be interpreted as meaningful; for example, the variables {math}`\risky` and {math}`\rport` are different from each other, like {math}`x` and {math}`y`.

Furthermore, a version of a variable without a subscript should be interpreted as the population mean of that variable. Thus, if {math}`\Risky_{t+1}` is a stochastic variable, then {math}`\Risky` denotes its mean value.

## Utility Functions

(fact:crralim)=
:::{note} Fact: CRRALim

$$
\lim_{\CRRA \rightarrow 1} \left(\frac{\cLev^{1-\CRRA}-1}{1-\CRRA}\right) = \log \cLev
$$
:::

This follows from L'Hopital's rule[^jqenGvrOCB] because for any {math}`\CRRA \neq 1` the derivative exists,

[^jqenGvrOCB]: Given recent decrees of the relevant authorities, the circumflex may need to be eliminated from future versions of these notes. Which is OK, because the gentleman in question paid someone smarter for the result anyway.

```{math}
\begin{gathered}\begin{aligned}
  \uFunc^{\prime}(\cLev) & =  \cLev^{-\CRRA},
\end{aligned}\end{gathered}
```

and {math}`\lim_{\CRRA \rightarrow 1} \cLev^{-\CRRA} = 1/\cLev` but {math}`\int (1/\cLev) = \log c`.

Thus, we can conclude that as {math}`\CRRA \rightarrow 1`, the behavior of the consumer with {math}`\uFunc(\cLev)=\cLev^{1-\CRRA}/(1-\CRRA)` becomes identical to the behavior of a consumer with {math}`\uFunc(\cLev)=\log c`.[^BCWfEsTpT1]

[^BCWfEsTpT1]: Recall that *behavior* is not affected by adding a constant to the utility function ...

(fact:finsum)=
:::{tip} Fact: FinSum

$$
\sum_{i=0}^{T} \gamma^{i} = \left(\frac{1-\gamma^{T+1}}{1-\gamma}\right)
$$
:::

(fact:infsum)=
:::{note} Fact: InfSum

If $0 < \gamma < 1$, then

$$
\sum_{i=0}^{\infty} \gamma^{i} = \left(\frac{1}{1-\gamma}\right)
$$
:::

(fact:finsummult)=
:::{tip} Fact: FinSumMult

$$
\sum_{i=0}^{T} i \gamma^{i} = \left(\frac{\gamma + \gamma^{T+1}(T(\gamma-1)-1)}{(1-\gamma)^{2}}\right)
$$
:::

(fact:infsummult)=
:::{note} Fact: InfSumMult

If $0 < \gamma < 1$, then

$$
\sum_{i=0}^{\infty} i \gamma^{i} = \left(\frac{\gamma}{(1-\gamma)^{2}}\right)
$$
:::

## 'Small' Number Approximations

Sometimes economic models are written in continuous time and sometimes in discrete time. Generically, there is a close correspondence between the two approaches, which is captured (for example) by the future value of a series that is growing at rate {math}`\divGro`.

```{math}
\begin{gathered}\begin{aligned}
  e^{\divGro t} & \text{corresponds to}  (1+\divGro)^{t} \equiv \DivGro^{t}.
\end{aligned}\end{gathered}
```

The words 'corresponds to' are not meant to imply that these objects are mathematically identical, but rather that these are the corresponding ways in which constant growth is treated in continuous and in discrete time; while for small values of {math}`\divGro` they will be numerically very close, continuous-time compounding does yield slightly different values after any given time interval than does discrete growth (for example, continuous growth at a 10 percent rate after 1 year yields {math}`e^{0.1} \approx 1.10517` while in discrete time we would write it as {math}`\DivGro=1.1`.)

Many of the following facts can be interpreted as manifestations of the limiting relationships between continuous and discrete time approaches to economic problems. (The continuous time formulations often yield simpler expressions, while the discrete formulations are useful for computational solutions; one of the purposes of the approximations is to show how the discrete-time solution becomes close to the corresponding continuous-time problem as the time interval shrinks).

(fact:taylorone)=
:::{hint} Fact: TaylorOne

For $\epsilon$ near zero ('small'), a first order Taylor expansion of $(1+\epsilon)^{\zeta}$ around 1 yields

$$
(1+\epsilon)^{\zeta} \approx 1+ \epsilon\zeta
$$
:::

(fact:taylortwo)=
:::{tip} Fact: TaylorTwo

For $\epsilon$ near zero ('small'), a second order Taylor expansion of $(1+\epsilon)^{\zeta}$ around 1 yields

$$
\begin{gathered}\begin{aligned}
 (1+\epsilon)^{\zeta} & \approx  1+ \zeta \epsilon  + \epsilon^{2} \zeta (\zeta-1)/2
\\ & =  1 + \left(1 + \left(\frac{\zeta - 1}{2}\right)\epsilon\right)\zeta \epsilon
\end{aligned}\end{gathered}
$$
:::

(fact:logeps)=
:::{hint} Fact: LogEps

For $\epsilon$ near zero ('small')

$$
\log (1+\epsilon) \approx \epsilon
$$
:::

(fact:expeps)=
:::{tip} Fact: ExpEps

For $\epsilon$ near zero ('small')

$$
(1+\epsilon) \approx e^{\epsilon}
$$
:::

(fact:overplus)=
:::{hint} Fact: OverPlus

For $\epsilon$ near zero ('small')

$$
1/(1+\epsilon) \approx 1-\epsilon
$$
:::

(fact:multplus)=
:::{tip} Fact: MultPlus

For $\epsilon$ and $\zeta$ near zero ('small')

$$
(1+\epsilon)(1+\zeta) \approx 1+\epsilon+\zeta
$$
:::

(fact:expplus)=
:::{hint} Fact: ExpPlus

For real numbers $\epsilon$ and $\zeta$

$$
\exp(\zeta)\exp(\epsilon) = \exp(\zeta+\epsilon)
$$
:::

(fact:smallsmallzero)=
:::{tip} Fact: SmallSmallZero

If $\epsilon$ is small and $\zeta$ is small then $\epsilon\zeta$ can be approximated by zero.
:::

## Statistics/Probability Facts

(fact:sumnormsisnorm)=
:::{important} Fact: SumNormsIsNorm

If $\rport_{t+1} \sim \mathcal{N}(\rport,\sigma^{2}_{\rport})$ and $\risky_{t+1} \sim \mathcal{N}(\risky,\sigma^{2}_{\risky})$ and $\rport_{t+1}$ and $\risky_{t+1}$ are [independent](http://en.wikipedia.org/wiki/Independence_(probability_theory)) (written $\rport_{t+1} \perp \risky_{t+1}$), then

$$
\rport_{t+1}+\risky_{t+1} = \mathcal{N}(\rport+\risky,\sigma^{2}_{\rport}+\sigma^{2}_{\risky})
$$
:::

(fact:elognorm)=
:::{seealso} Fact: ELogNorm

If from the viewpoint of period $t$ the stochastic variable $\Risky_{t+1}$ is lognormally distributed with mean ${\risky}$ and variance $\sigma_{\risky}^{2}$, $\risky_{t+1} \sim \mathcal{N}({\risky},\sigma_{\risky}^{2})$, then

$$
\Ex_{t}[e^{\risky_{t+1}}] = e^{{\risky}+\sigma_{\risky}^{2}/2}
$$
:::

(fact:elognormmeanone)=
:::{important} Fact: ELogNormMeanOne

If from the viewpoint of period $t$ the stochastic variable $\Risky_{t+1}$ is lognormally distributed with mean $-\sigma^{2}/2$ and variance $\sigma_{\risky}^{2}$, $\log \Risky_{t+1} \sim \mathcal{N}(-\sigma^{2}/2,\sigma^{2})$, then

$$
\Ex_{t}[e^{\risky_{t+1}}] = e^{-\sigma_{\risky}^{2}/2+\sigma_{\risky}^{2}/2}=e^{0}=1
$$
:::

(fact:logelognorm)=
:::{seealso} Fact: LogELogNorm

If $\Risky_{t+1}$ is lognormally distributed as in [ELogNorm](#fact:elognorm), then

$$
\begin{gathered}\begin{aligned}
\log \Ex_{t}[\Risky_{t+1}] & =  \Ex_{t}[\log \Risky_{t+1}]+\sigma_{\risky}^{2}/2
\\ & =  \risky +\sigma_{\risky}^{2}/2
\end{aligned}\end{gathered}
$$

This follows from taking the log of both sides of the equation in [ELogNorm](#fact:elognorm).
:::

(fact:normtimes)=
:::{important} Fact: NormTimes

If $\risky_{t+1} \sim \mathcal{N}({\risky},\sigma_{\risky}^{2})$, then

$$
\gamma \risky_{t+1} \sim \mathcal{N}(\gamma \risky,\gamma^{2} \sigma_{\risky}^{2})
$$
:::

(fact:meanone)=
:::{seealso} Fact: MeanOne

If $\log \Risky_{t+1} \sim \mathcal{N}(-\sigma_{\risky}^{2}/2,\sigma_{\risky}^{2})$, then

$$
\begin{gathered}\begin{aligned}
\Ex_{t}[\Risky_{t+1}] & =  1
\end{aligned}\end{gathered}
$$

for any value of $\sigma_{\risky}^{2} \geq 0.$
:::

This follows from substituting $-\sigma_{\risky}^{2}/2$ for $\risky$ in [ELogNorm](#fact:elognorm).

(fact:logmeanmps)=
:::{important} Fact: LogMeanMPS

If $\log \Risky_{t+1} \sim \mathcal{N}({\risky}-\sigma_{\risky}^{2}/2,\sigma_{\risky}^{2})$, then

$$
\begin{gathered}\begin{aligned}
      \log  \Ex_{t}[\Risky_{t+1}] & =  \risky
\end{aligned}\end{gathered}
$$

for any value of $\sigma_{\risky}^{2} \geq 0.$
:::

This follows from substituting $\risky - \sigma_{\risky}^{2}/2$ for $\risky$ in [ELogNorm](#fact:elognorm) and taking the log.

(fact:elognormtimes)=
:::{seealso} Fact: ELogNormTimes

If $\log \hat{\Risky}_{t+1} = \gamma \log \Risky_{t+1}$ where $\log \Risky_{t+1} \sim \mathcal{N}(\risky,\sigma_{\risky}^{2})$, then

$$
\Ex_{t}[\hat{\Risky}_{t+1}] = e^{\gamma \risky+\gamma^{2}\sigma_{\risky}^{2}/2}
$$
:::

(fact:logelognormtimes)=
:::{important} Fact: LogELogNormTimes

If $\log \hat{\Risky}_{t+1} = \gamma \log \Risky_{t+1}$ where $\log \Risky_{t+1} \sim \mathcal{N}(\risky,\sigma_{\risky}^{2})$, then

$$
\log \Ex_{t}[\hat{\Risky}_{t+1}] = \gamma \risky+\gamma^{2}\sigma_{\risky}^{2}/2
$$

This follows from taking the log of [ELogNormTimes](#fact:elognormtimes).
:::

## Other Facts

(fact:eulerstheorem)=
:::{tip} Fact: EulersTheorem

If $Y=\FFunc(K,L)$ is a constant returns to scale production function, then

$$
\begin{gathered}\begin{aligned}
        Y & =  \FFunc_{K} K + \FFunc_{L} L,
\end{aligned}\end{gathered}
$$

and if this production function characterizes output in a perfectly competitive economy then $\FFunc_{K}$ is the interest factor and $\FFunc_{L}$ is the wage rate.
:::
