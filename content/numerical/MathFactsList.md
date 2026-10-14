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

(fact:friedmanpihregression)=
:::{important} Fact: FriedmanPIHRegression

Suppose that each household's measured income is the sum of permanent and transitory income, $y=y^{P}+y^{T}$, where transitory income has mean zero and is uncorrelated with permanent income, and that consumption is proportional to permanent income, $c=k\,y^{P}$ (and Friedman assumed $k=1$). Then a regression of consumption on measured income across households, ${c=\alpha_{0}+\alpha_{1}y}$, has the coefficients

$$
\begin{gathered}\begin{aligned}
\alpha_{1} & = k\,\frac{\operatorname{var}(y^{P})}{\operatorname{var}(y^{P})+\operatorname{var}(y^{T})},
\\ \alpha_{0} & = (k-\alpha_{1})\,\Ex[y^{P}].
\end{aligned}\end{gathered}
$$

The measured marginal propensity to consume, $\alpha_{1}$, is the propensity to consume out of permanent income, $k$, times the share of the variance of income that is permanent. It is below $k$, and the intercept is positive.
:::

You should remember from your econometrics courses that the [least-squares slope](https://en.wikipedia.org/wiki/Simple_linear_regression#Formulation_and_computation) is the covariance of $c$ and $y$ divided by the variance of $y$. Substituting $c=k\,y^{P}$ and $y=y^{P}+y^{T}$, and using $\operatorname{cov}(y^{P},y^{T})=0$,

$$
\begin{gathered}\begin{aligned}
\operatorname{cov}(c,y) & = \operatorname{cov}(k\,y^{P},\,y^{P}+y^{T}) = k\operatorname{var}(y^{P}),
\\ \operatorname{var}(y) & = \operatorname{var}(y^{P})+\operatorname{var}(y^{T}).
\end{aligned}\end{gathered}
$$

Their ratio is $\alpha_{1}$. The fitted line passes through the means, $\Ex[c]=\alpha_{0}+\alpha_{1}\Ex[y]$, and since $\Ex[y^{T}]=0$, both $\Ex[c]=k\,\Ex[y^{P}]$ and $\Ex[y]=\Ex[y^{P}]$; so $\alpha_{0}=(k-\alpha_{1})\Ex[y^{P}]$.

The intuition: households with high measured income are, on average, partly households with high permanent income and partly households that drew a positive transitory shock. Only the permanent part raises consumption, so consumption rises with measured income by $k$ times the fraction of the differences in income that are permanent. If consumption also has a transitory part uncorrelated with income, the slope is unchanged ([AttenuationByNoise](#fact:attenuationbynoise)).

(fact:attenuationbynoise)=
:::{seealso} Fact: AttenuationByNoise

If a variable is measured with noise, $y=p+\xi$, and another variable depends on it as $z=k\,p+u$, where $p$, $\xi$ and $u$ are uncorrelated, then the coefficient of a regression of $z$ on $y$ is

$$
\frac{\operatorname{cov}(z,y)}{\operatorname{var}(y)}=k\,\frac{\operatorname{var}(p)}{\operatorname{var}(p)+\operatorname{var}(\xi)}:
$$

$k$ times the share of the variance of $y$ that comes from $p$. The noise biases the coefficient toward zero.
:::

Since $p$, $\xi$ and $u$ are uncorrelated, $\operatorname{cov}(z,y)=\operatorname{cov}(k\,p+u,\,p+\xi)=k\operatorname{var}(p)$ and $\operatorname{var}(y)=\operatorname{var}(p)+\operatorname{var}(\xi)$. It generalizes [FriedmanPIHRegression](#fact:friedmanpihregression): $z$ need only depend on $p$, and may carry noise $u$ of its own.

(fact:varianceofincomedifferences)=
:::{important} Fact: VarianceOfIncomeDifferences

If log income is the sum of a permanent component that follows a random walk and a transitory shock, $y_{t}=p_{t}+\xi_{t}$ with $p_{t}=p_{t-1}+\psi_{t}$, where the shocks are independent with variances $\sigma_{\psi}^{2}$ and $\sigma_{\xi}^{2}$, then the variance of the change in income over $d\geq1$ periods is

$$
\operatorname{var}(y_{t+d}-y_{t})=d\,\sigma_{\psi}^{2}+2\,\sigma_{\xi}^{2}.
$$

It rises linearly with the length of the difference: the slope is the variance of the permanent shock and the intercept twice the variance of the transitory shock. {cite:t}`carroll:brookings` used this to estimate both variances from household income in the PSID, by regressing the squared $d$-year differences of income on $d$.

If instead $p_{t}=\tau\,p_{t-1}+\psi_{t}$ with $0<\tau<1$, starting from its long-run distribution, the variance rises toward a ceiling:

$$
\operatorname{var}(y_{t+d}-y_{t})=2\operatorname{var}(p)\,(1-\tau^{d})+2\,\sigma_{\xi}^{2},\qquad\operatorname{var}(p)=\frac{\sigma_{\psi}^{2}}{1-\tau^{2}}.
$$

And if consumption is permanent income plus a transitory part of its own, $c_{t}=p_{t}+u_{t}$, with $p$ a random walk, a regression of the $d$-period change in consumption on the $d$-period change in income has the coefficient

$$
\frac{d\,\sigma_{\psi}^{2}}{d\,\sigma_{\psi}^{2}+2\,\sigma_{\xi}^{2}},
$$

which rises toward one as the difference lengthens.
:::

Over $d$ periods the permanent component accumulates $d$ permanent shocks, while the transitory shocks of the first and last periods both appear:

$$
y_{t+d}-y_{t}=\sum_{j=1}^{d}\psi_{t+j}+\xi_{t+d}-\xi_{t}.
$$

These $d+2$ shocks are independent, so the variance of their sum is the sum of their variances, $d\,\sigma_{\psi}^{2}+2\,\sigma_{\xi}^{2}$.

With $0<\tau<1$, $p$ has the same variance in every period, and since $\psi_{t}$ is independent of $p_{t-1}$, $\operatorname{var}(p)=\tau^{2}\operatorname{var}(p)+\sigma_{\psi}^{2}$, which gives $\operatorname{var}(p)=\sigma_{\psi}^{2}/(1-\tau^{2})$. Since $p_{t+d}=\tau^{d}p_{t}$ plus shocks after $t$, $\operatorname{cov}(p_{t+d},p_{t})=\tau^{d}\operatorname{var}(p)$, so $\operatorname{var}(p_{t+d}-p_{t})=2\operatorname{var}(p)(1-\tau^{d})$, and the transitory shocks add $2\sigma_{\xi}^{2}$ as before. As $\tau\to1$, $(1-\tau^{d})/(1-\tau^{2})\to d/2$, which gives back $d\,\sigma_{\psi}^{2}$.

In the regression, $c_{t+d}-c_{t}=(p_{t+d}-p_{t})+(u_{t+d}-u_{t})$ and $y_{t+d}-y_{t}=(p_{t+d}-p_{t})+(\xi_{t+d}-\xi_{t})$. So [AttenuationByNoise](#fact:attenuationbynoise) applies with $k=1$, a common part of variance $d\,\sigma_{\psi}^{2}$ and noise of variance $2\,\sigma_{\xi}^{2}$. The longer the difference, the larger the permanent part's share of the change in income: that is why Friedman's model predicts a larger coefficient in long differences than in short ones.

Measured transitory income is not white noise: {cite:t}`abowdCard` find that annual changes in earnings are correlated with the changes one and two years away, and not beyond. If $\xi_{t}$ is correlated with its own values up to $q$ periods apart, then for $d>q$, $\operatorname{var}(\xi_{t+d}-\xi_{t})=2\operatorname{var}(\xi)$, and the formulas hold with $\operatorname{var}(\xi)$ in place of $\sigma_{\xi}^{2}$: only the intercept changes. {cite:t}`carroll:brookings` used only differences of three years or more for this reason.

(fact:randomwalkspread)=
:::{seealso} Fact: RandomWalkSpread

If $x_{s}$ follows a random walk over $n$ consecutive periods, with independent shocks of variance $\sigma^{2}$, then the expected sum of its squared deviations from its own mean $\bar{x}$ over those periods is

$$
\Ex\Bigl[\sum_{s=1}^{n}(x_{s}-\bar{x})^{2}\Bigr]=\sigma^{2}\,\frac{n^{2}-1}{6}.
$$

Its average squared deviation from its own mean, about $\sigma^{2}n/6$, grows in proportion to the length of the history, while that of $n$ independent draws with variance $\sigma^{2}$ stays about $\sigma^{2}$.
:::

The sum of squared deviations from the mean equals the sum of all the squared pairwise differences, divided by $2n$:

$$
\sum_{s=1}^{n}(x_{s}-\bar{x})^{2}=\frac{1}{2n}\sum_{s=1}^{n}\sum_{u=1}^{n}(x_{s}-x_{u})^{2}.
$$

(Expanding the right side gives $\frac{1}{2n}\bigl[2n\sum_{s}x_{s}^{2}-2(\sum_{s}x_{s})^{2}\bigr]$, which is the left side.) By [VarianceOfIncomeDifferences](#fact:varianceofincomedifferences) with no transitory shock, $\Ex[(x_{s}-x_{u})^{2}]=|s-u|\,\sigma^{2}$. Of the $n^{2}$ pairs, $2(n-d)$ are $d$ periods apart, for $d=1,\ldots,n-1$, so

$$
\begin{gathered}\begin{aligned}
\Ex\Bigl[\sum_{s=1}^{n}(x_{s}-\bar{x})^{2}\Bigr]
& = \frac{\sigma^{2}}{2n}\sum_{d=1}^{n-1}2(n-d)\,d
\\ & = \frac{\sigma^{2}}{n}\Bigl[n\,\frac{n(n-1)}{2}-\frac{(n-1)n(2n-1)}{6}\Bigr]
\\ & = \frac{\sigma^{2}}{n}\cdot\frac{(n-1)n(n+1)}{6}
\\ & = \sigma^{2}\,\frac{n^{2}-1}{6}.
\end{aligned}\end{gathered}
$$

(fact:ar1randomwalkplusnoise)=
:::{important} Fact: AR1RandomWalkPlusNoise

Let $y_{t}=p_{t}+\xi_{t}$ for $t=0,1,\ldots,T$, where $p_{t}=p_{t-1}+\psi_{t}$ is a random walk and $\xi_{t}$ is white noise, with independent shocks of variances $\sigma_{\psi}^{2}$ and $\sigma_{\xi}^{2}$. In a regression of $y_{t}$ on a constant and $y_{t-1}$ over this one history, the coefficient on $y_{t-1}$ is about

$$
\frac{T\,\sigma_{\psi}^{2}}{T\,\sigma_{\psi}^{2}+6\,\sigma_{\xi}^{2}},
$$

below one for any finite history and approaching one as the history lengthens. The formula sets aside a second bias, from estimating the history's own mean, which pulls the coefficient down further and is not small in histories of the length real panels have {cite:p}`nickellBiases`.
:::

This year's income is $y_{t}=p_{t-1}+(\psi_{t}+\xi_{t})$: last year's permanent income with the coefficient one, plus shocks uncorrelated with last year's income $y_{t-1}=p_{t-1}+\xi_{t-1}$. So [AttenuationByNoise](#fact:attenuationbynoise) applies with $k=1$, with the variation within the history in place of the variances: about $\sigma_{\psi}^{2}T/6$ for the random walk ([RandomWalkSpread](#fact:randomwalkspread)) and $\sigma_{\xi}^{2}$ for the white noise. The coefficient is

$$
\frac{\sigma_{\psi}^{2}T/6}{\sigma_{\psi}^{2}T/6+\sigma_{\xi}^{2}}=\frac{T\,\sigma_{\psi}^{2}}{T\,\sigma_{\psi}^{2}+6\,\sigma_{\xi}^{2}}.
$$

The random walk's variation within the history grows with the history's length and the white noise's does not, so the transitory part's weight, $6\sigma_{\xi}^{2}/(T\sigma_{\psi}^{2}+6\sigma_{\xi}^{2})$, falls as the history lengthens.

(fact:ar1persistentplusnoise)=
:::{seealso} Fact: AR1PersistentPlusNoise

If instead $p_{t}=\tau\,p_{t-1}+\psi_{t}$ with $0<\tau<1$, starting from its long-run distribution, the coefficient on $y_{t-1}$ in a long history approaches

$$
\tau\,\frac{\operatorname{var}(p)}{\operatorname{var}(p)+\sigma_{\xi}^{2}}=\frac{\tau\,\sigma_{\psi}^{2}}{\sigma_{\psi}^{2}+(1-\tau^{2})\,\sigma_{\xi}^{2}},
$$

where $\operatorname{var}(p)=\sigma_{\psi}^{2}/(1-\tau^{2})$ is the long-run variance of $p$.

Unlike the random walk's, this bias does not fade as the history lengthens. As $\tau\to1$ the coefficient approaches one, because $\operatorname{var}(p)$ grows without bound.
:::

Now $y_{t}=\tau\,p_{t-1}+(\psi_{t}+\xi_{t})$ and $y_{t-1}=p_{t-1}+\xi_{t-1}$, so [AttenuationByNoise](#fact:attenuationbynoise) applies with $k=\tau$. Since $\psi_{t}$ is independent of $p_{t-1}$, $\operatorname{var}(p)=\tau^{2}\operatorname{var}(p)+\sigma_{\psi}^{2}$, which gives ${\operatorname{var}(p)=\sigma_{\psi}^{2}/(1-\tau^{2})}$. In a long history the sample variances and covariances approach these population values. Substituting it and multiplying numerator and denominator by $1-\tau^{2}$ gives the result.

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
