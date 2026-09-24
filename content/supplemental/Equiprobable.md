(sec:Equiprobable)=
# An Equiprobable Approximation to the Bivariate Lognormal

Economic agents face risks of many kinds, which may mutually
covary. A stock broker, for example, is likely to earn a salary
bonus that is positively related to the performance of the stock
market; if that broker also has personal stock investments, his
financial wealth and labor income will be positively correlated.

The first part of this section presents a convenient (and empirically
realistic) formulation in which a consumer faces two shocks (which can
be interpreted as a shock to noncapital income and a shock to the rate
of return) that are distributed according to a multivariate lognormal
that allows for correlation between them. The second part describes a
computationally simple and convenient method for approximating that joint
distribution.

## Theory

Consider a consumer who faces both a risk to transitory noncapital income[^gOxRS4n81Q]

[^gOxRS4n81Q]: The assumed distribution has the property {math}`\Ex[\ShkMeanOne_{1,t+1}]=1`, cf. [Math Facts](#fact:mathfactslist).

```{math}
\begin{gathered}\begin{aligned}
   \ShkMeanOneLog_{1,t+1} \equiv \log \ShkMeanOne_{1,t+1}  & \sim  \mathcal{N}(-0.5\sigma^{2}_{1},\sigma^{2}_{1})
\end{aligned}\end{gathered}
```

and a risky log rate-of-return that is affected by following factors: the riskless rate {math}`\rfree`;

a risk premium {math}`\EpremLog`; an additional constant {math}`\zeta` (whose purpose will become clear below); a component
that is linearly related to {math}`\ShkMeanOneLog_{1,t+1}`; and an independent shock {math}`\ShkMeanOneLog_{2} \sim
 \mathcal{N}(-0.5 \sigma^{2}_{2},\sigma^{2}_{2})`:

```{math}
:label: corrToCov

\begin{gathered}\begin{aligned}
  {\risky}_{t+1} \equiv \log {\Risky}_{t+1} & =  \rfree+\EpremLog+\zeta + \omega \ShkMeanOneLog_{1,t+1} (\sigma_{2}/\sigma_{1})   + \ShkMeanOneLog_{2,t+1} 
\end{aligned}\end{gathered}
```

for some constant {math}`\omega`. Since {math}`(\sigma_{2}/\sigma_{1}) \omega \ShkMeanOneLog_{1,t+1}` is the only component of {math}`\risky_{t+1}` that covaries with {math}`\ShkMeanOneLog_{1,t+1}`,

```{math}
\begin{gathered}\begin{aligned}
  \cov(\ShkMeanOneLog_{1,t+1} ,\risky_{t+1}) & =  \cov(\ShkMeanOneLog_{1,t+1} , (\sigma_{2}/\sigma_{1}) \omega \ShkMeanOneLog_{1,t+1} )
\\ & =  \omega (\sigma_{2}/\sigma_{1}) \underbrace{\cov(\ShkMeanOneLog_{1,t+1} ,\ShkMeanOneLog_{1,t+1} )}_{=\sigma^{2}_{1}}
\\ & =  \omega \sigma_{2}\sigma_{1}
.
\end{aligned}\end{gathered}
```

Equation {eq}`corrToCov` yields a description of the return process
in which the parameter {math}`\omega` controls the correlation between the
risky log return shock and the risky log labor income shock. If
{math}`\omega = 0` the processes are independent.

Now we want to find the value of {math}`\zeta` such that the mean risky
return is unaffected by {math}`\sigma^{2}_{1}` (so that we will be able to
understand clearly the distinct effects of labor income risk, the
independent component of rate-of-return risk {math}`\sigma^{2}_{2}`, and the
correlation between labor income risk and rate-of-return risk,
{math}`\omega`). Thus, we want to find the {math}`\zeta` such that

```{math}
\begin{gathered}\begin{aligned}
  \Ex_{t}[\Risky_{t+1}] & =  e^{\rfree+\EpremLog}
\end{aligned}\end{gathered}
```

regardless of the values of {math}`\sigma^{2}_{1}` and {math}`\sigma^{2}_{2}`. We therefore need:

```{math}
\begin{gathered}\begin{aligned}
         \Ex[e^{\zeta+ (\sigma_{2}/\sigma_{1}) \omega \ShkMeanOneLog_{1,t+1}  + \ShkMeanOneLog_{2,t+1}}] & =  1.
\\ \log  \Ex[e^{\zeta+ (\sigma_{2}/\sigma_{1}) \omega \ShkMeanOneLog_{1,t+1}  + \ShkMeanOneLog_{2,t+1}}] & =  0.
\end{aligned}\end{gathered}
```

Using standard facts about lognormals (cf. [Math Facts](#fact:mathfactslist)), and for convenience
defining {math}`\hat{\omega}= (\sigma_{2}/\sigma_{1}) \omega`, we have

```{math}
\begin{gathered}\begin{aligned}
  0. & =  \zeta - 0.5 \hat{\omega} \sigma^{2}_{1} - 0.5 \sigma^{2}_{2} + 0.5\hat{\omega}^{2}\sigma^{2}_{1}+0.5  \sigma^{2}_{2}
\\ & =  \zeta -0.5 \sigma^{2}_{1} \hat{\omega}(1-\hat{\omega})
\\ \zeta & =  0.5 (\hat{\omega}-\hat{\omega}^{2}) \sigma^{2}_{1} = 0.5 (\omega \sigma_{2} \sigma_{1}-\omega^{2} \sigma^{2}_{2}).
\end{aligned}\end{gathered}
```

Because the two shocks are independent by construction, the joint distribution takes a
convenient form. Stacking {math}`\ShkMeanOneLog_{1,t+1}` and {math}`\ShkMeanOneLog_{2,t+1}`
into a vector {math}`\vec{\ShkMeanOneLog}`, we can write

```{math}
\vec{\ShkMeanOneLog} \sim \mathcal{N}(\vec{\mu},\Sigma)
```

where {math}`\vec{\mu}= \{-0.5 \sigma^{2}_{1},-0.5 \sigma^{2}_{2}\}^{\prime}` and the
covariance matrix {math}`\Sigma` is diagonal, carrying {math}`\sigma^{2}_{1}` and
{math}`\sigma^{2}_{2}`.[^independent-representation]

[^independent-representation]: An alternative would be to work with {math}`\ShkMeanOneLog_{1,t+1}` and {math}`\risky_{t+1}` directly, which would require a multivariate normal with nonzero off-diagonal elements. The two approaches are mathematically indistinguishable, and we take the independent one because it is the more convenient to integrate against below.

## Computation

A key step in the computational solution of any model with uncertainty is the calculation
of expectations. Writing {math}`\tilde{\ShkMeanOne}_{1} \equiv \tilde{\ShkMeanOne}_{1,t+1}` and {math}`\tilde{\Risky} \equiv \Risky_{t+1}` and {math}`\Ex[\bullet] = \Ex_{t}[\bullet_{t+1}]`, the expectation of some function {math}`\hFunc` that depends on the realization of
the risky return {math}`\tilde{\Risky}` and the labor income shock is:

```{math}
\begin{gathered}\begin{aligned}
  \Ex[\hFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})] & =  \int_{\underline{\ShkMeanOne}_{1}}^{\bar{\ShkMeanOne}_{1}}\int_{\underline{\Risky}}^{\bar{\Risky}} \hFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky}) d\FFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})
\end{aligned}\end{gathered}
```

where {math}`\FFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})` is the joint cumulative distribution
function. Standard numerical computation software can compute this
double integral, but at such a slow speed as to be almost unusable.

Computation of the expectation can be massively speeded up by
advance construction of a numerical approximation to
{math}`\FFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})`.

Such approximations generally take the approach of replacing the distribution function
with a discretized approximation to it; appropriate weights {math}`w_{i,j}` are attached to
each of a finite set of points indexed by {math}`i` and {math}`j`, and
the approximation to the integral is given by:

```{math}
:label: eq:Equi-wtdAvg

\begin{gathered}\begin{aligned}
  \Ex[\hFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})] & \approx  \sum_{i=1}^{n}\sum_{j=1}^{m} \hFunc(\hat{\ShkMeanOne}_{1}[i,j],\hat{\Risky}[i,j])w[i,j]
\end{aligned}\end{gathered}
```

where the {math}`\hat{\ShkMeanOne}_{1}` and {math}`\hat{\Risky}` matrices contain the conditional means of the two variables in each of the {math}`\{i,j\}` regions. Various methods are used for constructing the weights {math}`w[i,j]` and the nodes (the {math}`i` and {math}`j` points for
{math}`\ShkMeanOne_{1}` and {math}`\Risky`).

Perhaps the most popular such method is Gauss-Hermite interpolation (see
{cite:t}`judd:book` for an exposition, or {cite:t}`kopecky2010finite` for
some alternatives). Here, we will pursue a particularly intuitive
alternative: Equiprobable discretization. In this method, {math}`m=n` and
boundaries on the joint CDF are determined in such a way as to divide
up the total probability mass into submasses of equal size (each of
which therefore has a mass of {math}`n^{-2}`). This is conceptually easier
if we represent the underlying shocks as statistically
independent, as with {math}`\ShkMeanOneLog_{1,t+1}` and {math}`\ShkMeanOneLog_{2,t+1}` above; in that case, each submass is a square region
in the {math}`\ShkMeanOne_{1}` and {math}`\ShkMeanOne_{2}` grid. We then compute the average
value of {math}`\ShkMeanOne_{1}` and {math}`\Risky`  conditional on their being
located in each of the subdivisions of the range of the CDF. Since,
in this specification, {math}`\Risky` is a function of {math}`\ShkMeanOne_{1}`, the
{math}`\Risky` values are indexed by both {math}`i` and {math}`j`, but since we have
written {math}`\ShkMeanOne_{1}` as IID, the representation of the approximating
summation is even simpler than {eq}`eq:Equi-wtdAvg`:

```{math}
:label: eq:Equi-wtdAvgMod

\begin{gathered}\begin{aligned}
  \Ex[\hFunc(\tilde{\ShkMeanOne}_{1},\tilde{\Risky})] & \approx  n^{-2} \sum_{i=1}^{n}\sum_{j=1}^{n} \hFunc(\hat{\ShkMeanOne}_{1}[i],\Risky(\hat{\ShkMeanOne}_{1}[i],\hat{\ShkMeanOne}_{2}[j])) 
\end{aligned}\end{gathered}
```

where the function {math}`\Risky(\ShkMeanOne_{1},\ShkMeanOne_{2})` is implicitly defined by {eq}`corrToCov`.

Details can be found in the  Mathematica notebook associated with this
section. A particular example, in which {math}`\sigma^{2}_{2} = \sigma^{2}_{1}` and {math}`\omega = 0.5`,
is illustrated in {numref}`fig:corr0p5`; the red dots reflect the height of the approximation
to the CDF above the conditional mean values for {math}`\ShkMeanOne_{1}` and {math}`\Risky` within each of the equiprobable
regions.

:::{figure} /content/figures/Equiprobable/CDFPlot.png
:name: fig:corr0p5

'True' CDF With Approximation Points in Red for {math}`\omega=0.5`
:::
