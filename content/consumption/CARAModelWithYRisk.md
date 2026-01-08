(sec:CARAModelWithYRisk)=

# Consumption with Constant Absolute Risk Aversion (CARA) Utility

Consider the optimization problem of a consumer with a constant absolute risk aversion instantaneous utility function {math}`\uFunc(\CRat)= -(1/\CARA) e^{-\CARA \CRat}` implying {math}`\uFunc^{\prime}(\CRat) = e^{-\CARA \CRat}` facing an interest rate that is constant at {math}`\rfree=\Rfree-1`.[^caballero-ref] The consumer's optimization problem is

[^caballero-ref]: A problem like this was considered in a well-known paper by {cite:t}`caballero:jme`.

```{math}
:label: eq:CARA-maxprob

\max_{\{\CFunc\}_{t}^{T}}~~ \Ex_{t}\left\{\sum_{s=t}^{T} \Discount^{s-t} \uFunc(\CRat_{s})\right\}
```

subject to the constraints

:::{margin}
Introducing {math}`K` and {math}`X` because useful to have a term for non-income resources at beginning of period.
:::

```{math}
\begin{aligned}
B_{t+1} & = ({M}_{t}-\CRat_{t})\Rfree \\
{M}_{t+1} & = B_{t+1}+Y_{t+1}
\end{aligned}
```

where {math}`Y_{t+1}` is the consumer's idiosyncratic income, which exhibits a random-walk deviation from an exogenously-growing trend:

```{math}
\begin{aligned}
\bar{\PLev}_{t+1} & = \PGro \bar{\PLev}_{t} \\
Y_{t+1} & = \bar{\PLev}_{t+1}+\PLev_{t+1} \\
\PLev_{t+1} & = \PLev_{t}+\PShk_{t+1}.
\end{aligned}
```

Bellman's equation for this problem is

:::{margin}
Bellman's eqn relates {math}`\VFunc_{t}` and {math}`\VFunc_{t+1}` through the controls and states. Doesn't necessarily require writing bud constr.
:::

```{math}
:label: eq:CARA-vmax

\VFunc_{t}({M}_{t},\bar{\PLev}_{t},\PLev_{t}) = \max_{\{\CFunc\}_{t}^{T}} ~~ \uFunc(\CRat_{t}) + \Ex_{t}[\Discount \VFunc_{t+1}({M}_{t+1},\bar{\PLev}_{t+1},{\PLev}_{t+1})].
```

The first order condition (FOC) for the CARA utility problem is

```{math}
\uFunc^{\prime}(\CRat_{t}) = \Rfree \Discount \Ex_{t}[\VFunc_{t+1}^{M}]
```

and the [](#sec:Envelope) theorem tells us that

```{math}
\VFunc^{M}_{t} = \Rfree \Discount \Ex_{t}[\VFunc_{t+1}^{M}].
```

In the perfect foresight version of the model in which {math}`\PShk_{t} = 0 ~\forall~t`, the Euler equation will be

```{math}
:label: eq:CARA-cgrow

\begin{aligned}
\uFunc^{\prime}(\CRat_{t}) & = \Rfree\Discount \uFunc^{\prime}(\CRat_{t+1}) \\
\exp[-\CARA \CRat_{t}] & = \Rfree \Discount \exp[-\CARA \CRat_{t+1}] \\
1 & = \Rfree\Discount \exp[-\CARA (\CRat_{t+1}-\CRat_{t})] \\
\exp[\CARA (\CRat_{t+1}-\CRat_{t})] & = \Rfree\Discount \\
\CARA (\CRat_{t+1}-\CRat_{t}) & = \log \Rfree\Discount \\
\CRat_{t+1} & = \CRat_{t}+\log (\Rfree\Discount)^{1/\CARA}.
\end{aligned}
```

The {math}`\log (\Rfree\Discount)^{1/\CARA}` term reflects the intertemporal substitution factor in consumption. Notice that intertemporal substitution takes the form of *additive* changes in the *level* of consumption in the CARA utility model, rather than multiplicative changes that affect the growth rate of consumption, as in the CRRA model.

Now suppose we are interested in the case where permanent income shocks are distributed normally, {math}`\PShk_{t} \sim \mathcal{N}(0,\sigma_{\PShk}^{2})`. Then it turns out that the process

```{math}
:label: eq:soln

\CRat_{t+1} = \CRat_{t} + \log (\Rfree\Discount)^{1/\CARA} + \CARA \sigma^{2}_{\PShk}/2+\PShk_{t+1}
```

satisfies the FOC under uncertainty:

```{math}
\begin{aligned}
1 & = \Rfree \Discount \Ex_{t}[\exp[-\CARA ({c}_{t+1}-c_{t})]] \\
1 & = \Rfree \Discount \Ex_{t}[\exp[-\CARA (\CARA \sigma_{\PShk}^{2}/2+{\PShk}_{t+1}+(1/\CARA)\log (\Rfree\Discount) +c_{t}-c_{t})]] \\
1 & = \Rfree \Discount \exp[-\CARA^{2} \sigma_{\PShk}^{2}/2] \Ex_{t} \{\exp[-\CARA {\PShk}_{t+1}]\}\exp[-\CARA (1/\CARA) \log \Rfree\Discount] \\
1 & = \Rfree \Discount \exp[-\CARA^{2}(\sigma_{\PShk}^{2}/2)]\exp[\CARA^{2}(\sigma_{\PShk}^{2}/2)]\exp[\log (\Rfree\Discount)^{-1}] \\
1 & = \Rfree \Discount (\Rfree\Discount)^{-1} \\
1 & = 1.
\end{aligned}
```

Define {math}`\kappa = \log (\Rfree\Discount)^{1/\CARA} + \CARA \sigma^{2}_{\PShk}/2`, so that {eq}`eq:soln` becomes:

```{math}
\CRat_{t+1} = \CRat_{t} + \PShk_{t+1} + \kappa.
```

The expected present discounted value of consumption is[^pshk-disappears]

[^pshk-disappears]: The {math}`\PShk_{t+n}` terms disappear when expectations are taken.

```{math}
\begin{aligned}
\PDV_{t}(\CRat) & = \CRat_{t}+(\CRat_{t}+\PShk_{t+1}+\kappa)/\Rfree + (\CRat_{t}+\PShk_{t+1}+\kappa + \PShk_{t+2} + \kappa)/\Rfree^{2} + \ldots \\
\Ex_{t}[\PDV_{t}(\CRat)] & = \CRat_{t}+\CRat_{t}/\Rfree+\CRat_{t}/\Rfree^{2}+ \ldots + \kappa/\Rfree + 2\kappa/\Rfree^{2} + 3\kappa/\Rfree^{3} + \ldots \\
& = \CRat_{t}(1+\Rfree^{-1}+\Rfree^{-2}+\ldots) + \kappa \sum_{i=1}^{\infty} i/\Rfree^{i}.
\end{aligned}
```

Now we need [InfSumMult](#fact:infsummult): if {math}`\Rfree > 1`, then {math}`\displaystyle \sum_{i=0}^{\infty} i/\Rfree^{i} = \left(\frac{\Rfree}{(\Rfree-1)^{2}}\right)`

:::{margin}
The {math}`\PShk_{t+n}` terms disappear when expectations are taken.
:::

Thus, the expectation of the infinite horizon PDV of consumption is:

```{math}
\Ex_{t}[\PDV_{t}(\CRat)] = \CRat_{t}\left(\frac{1}{1-1/\Rfree}\right)+\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right).
```

Given the process for income described above, we have

```{math}
\begin{aligned}
\PDV_{t}(Y) & = Y_{t}+Y_{t+1}/\Rfree+Y_{t+2}/\Rfree^{2}+\ldots \\
& = \bar{\PLev}_{t}+\PLev_{t}+(\PGro\bar{\PLev}_{t}+\PLev_{t+1})/\Rfree + (\PGro^{2}\bar{\PLev}_{t}+\PLev_{t+2})/\Rfree^{2}+ \ldots \\
& = \bar{\PLev}_{t}\left(1+\PGro/\Rfree + (\PGro/\Rfree)^{2} + \ldots \right)+ \\
& \PLev_{t}+(\PLev_{t}+\PShk_{t+1})/\Rfree+(\PLev_{t}+\PShk_{t+1}+\PShk_{t+2})/\Rfree^{2}+\ldots \\
\Ex_{t}[\PDV_{t}(Y)] & = \left(\frac{\bar{\PLev}_{t}}{1-\PGro/\Rfree}\right)+\PLev_{t}\sum_{s=0}^{\infty} \Rfree^{-s} \\
& = \left(\frac{\bar{\PLev}_{t}}{1-\PGro/\Rfree}\right)+\left(\frac{ \PLev_{t}}{1-1/\Rfree}\right)
\end{aligned}
```

The IBC says

```{math}
:label: eq:CARA-ibc

\PDV_{t}(\CRat) = B_{t}+\PDV_{t}(Y),
```

Because the intertemporal budget constraint must hold in every state of the world, the expectation of the PDV of consumption must equal current wealth plus the expectation of the PDV of income. Thus,

```{math}
\begin{aligned}
\Ex_{t}[\PDV_{t}(\CRat)] & = B_{t}+\Ex_{t}[\PDV_{t}(Y)] \\
\CRat_{t}\left(\frac{1}{1-1/\Rfree}\right) & = B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PGro/\Rfree}\right)+\left(\frac{ \PLev_{t}}{1-1/\Rfree}\right)-\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right) \\
\CRat_{t} & = \PLev_{t} + \left(\frac{\rfree}{\Rfree}\right)\left[ B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PGro/\Rfree}\right)-\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right) \right] \\
& = \PLev_{t} + \left(\frac{\rfree}{\Rfree}\right)\left[ B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PGro/\Rfree}\right)\right] -\rfree\left(\frac{\log (\Rfree\Discount)^{1/\CARA} + \CARA \sigma^{2}_{\PShk}/2 }{(1-\Rfree)^{2}}\right)
\end{aligned}
```

The {math}`\PLev_{t}` term reflects the consumer's idiosyncratic level of permanent income, which has no systematic growth (or decline). The next term reflects the MPC out of total "certain" wealth, human and nonhuman. The final term reflects the combination of the intertemporal substitution motive (in the {math}`\log (\Rfree\Discount)^{1/\CARA}` term) and the precautionary motive in the {math}`\CARA \sigma^{2}_{\PShk}` term, as is evident from the fact that it equals zero if either there is no precautionary motive ({math}`\CARA=0`) or there is no uncertainty {math}`\sigma^{2}_{\PShk}=0`.

Note some peculiar aspects of this solution. First, observe that, marginally, the consumer spends exactly the interest income on capital, {math}`d \CRat_{t}/d B_{t} = \rfree/\Rfree`. The reason this is peculiar is that the MPC out of capital *does not depend on how impatient the consumer is*. Impatience is reflected in the change in consumption over time, but not in the level of consumption except as that is affected by the budget constraint.

Second, notice that the effect of income uncertainty on saving is the same in absolute dollars regardless of the level of resources or permanent income.

---

**Content after document end (draft/scratch work):**

If {math}`t+1 = T` so that {math}`c_{t+1} = (m_{t}-c_{t})\Rfree+\PShk_{t+1}` then the Euler equation becomes

```{math}
\begin{aligned}
\uFunc^{\prime}(c_{t}) & = \Rfree\Discount \Ex_{t}[\uFunc^{\prime}(c_{t+1})] \\
\exp[-\CARA c_{t}] & = \Rfree \Discount \Ex_{t}[\exp[-\CARA {c}_{t+1}]] \\
1 & = \Rfree \Discount \Ex_{t}[\exp[-\CARA ((m_{t}-c_{t})\Rfree+{\PShk}_{t+1}-c_{t})]] \\
0 & = \log (\Rfree\Discount) + \log \Ex_{t}[\exp[-\CARA (-c_{t}(1+\Rfree) + Rm_{t})]\exp[-\CARA {\PShk}_{t+1}]] \\
0 & = \log (\Rfree\Discount) + (\CARA c_{t}(1+\Rfree) - \CARA \Rfree m_{t})+ \log \Ex_{t}[\exp[-\CARA {\PShk}_{t+1}]] \\
c_{t} \CARA (1+\Rfree) & = - \log (\Rfree\Discount) + \CARA \Rfree m_{t} - (\CARA^{2} \sigma^{2}_{\PShk}/2) \\
c_{t} & = \left(\frac{1}{1+\Rfree}\right)\left[\log (\Rfree\Discount)^{-1/\CARA} + \Rfree m_{t} - \CARA \sigma^{2}_{\PShk}/2 \right]
\end{aligned}
```

**Additional derivations (continued draft work):**

```{math}
\begin{aligned}
\uFunc^{\prime}(c_{t}) & = \Rfree\Discount \Ex_{t}[\uFunc^{\prime}(c_{t+1})] \\
\exp[-\CARA c_{t}] & = \Rfree \Discount \Ex_{t}[\exp[-\CARA {c}_{t+1}]] \\
1 & = \Rfree \Discount \Ex_{t}[\exp[-\CARA (\left(\frac{1}{1+\Rfree}\right)\left[\log (\Rfree\Discount)^{-1/\CARA} + \Rfree ((m_{t}-c_{t})\Rfree+\PShk_{t+1}) - \CARA \sigma^{2}_{\PShk}/2 \right]-c_{t})]] \\
1 & = \Rfree\Discount \Ex_{t}\left\{\exp[-\CARA (\left(\frac{1}{1+\Rfree}\right)\left[\log (\Rfree\Discount)^{-1/\CARA} + \Rfree ((m_{t}-c_{t})\Rfree) - \CARA \sigma^{2}_{\PShk}/2 \right]-c_{t})]\exp[\left(\frac{-\CARA \Rfree {\PShk}_{t+1}}{1+\Rfree}\right)] \right\}
\end{aligned}
```

**Postulated consumption rule:**

Based on this, let's postulate a consumption rule of the form {math}`c_{t} = \mu + \omega m_{t}` and see whether we can determine coefficients {math}`\mu, \omega,` such that the equation holds in the infinite horizon case.

```{math}
\begin{aligned}
0 & = \log (\Rfree \Discount)+ \log \Ex_{t}\left\{ \exp[-\CARA ({c}_{t+1}-c_{t})]\right\} \\
c_{t+1}-c_{t} & = \mu + \omega((m_{t}-c_{t})\Rfree+y_{t+1})-c_{t} \\
& = \mu + \omega(\Rfree m_{t}+y_{t+1}) - c_{t}(\omega \Rfree + 1)
\end{aligned}
```

**Finite horizon facts:** See [FinSum](#fact:finsum), [InfSum](#fact:infsum), and [InfSumMult](#fact:infsummult) in the Math Facts appendix.

The Intertemporal Budget Constraint tells us that the present discounted value of consumption must be equal to the PDV of total resources:

```{math}
\PDV_{t}(\CRat) = B_{t}+\PDV_{t}(P)
```

Using [FinSum](#fact:finsum), the PDV of labor income (also called "human wealth" {math}`H_{t}`) is

```{math}
:label: eq:CARA-yfin

\begin{aligned}
H_{t} = \PDV_{t}(P) & = \sum_{s=t}^{T} \Rfree^{-(s-t)}\PLev_{s} \\
& = \PLev_{t}\sum_{s=t}^{T} \Rfree^{-(s-t)}\PGro^{(s-t)} \\
& = \PLev_{t}\sum_{s=t}^{T} (\PGro/\Rfree)^{(s-t)} \\
& = \PLev_{t}\left(\frac{1-(\PGro/\Rfree)^{T-t+1}}{1-(\PGro/\Rfree)}\right)
\end{aligned}
```

while the PDV of consumption is

```{math}
:label: eq:CARA-cfin

\begin{aligned}
\PDV_{t}(\CRat) & = \sum_{s=t}^{T} \Rfree^{-(s-t)}\CRat_{s} \\
& = \CRat_{t}+(\CRat_{t}+ \log (\Rfree\Discount)^{-1/\CARA})/\Rfree +(\CRat_{t}+ 2 \log (\Rfree\Discount)^{-1/\CARA})/\Rfree^{2} + \ldots \\
& = \CRat_{t}(1+1/\Rfree+1/\Rfree^{2}+\ldots) + \log (\Rfree\Discount)^{-1/\CARA}/\Rfree + 2 \log (\Rfree\Discount)^{-1/\CARA}/\Rfree^{2} + \ldots \\
& = \left(\frac{\CRat_{t}}{1-1/\Rfree}\right) + \log (\Rfree\Discount)^{-1/\CARA}\left(\frac{\Rfree}{(\Rfree-1)^{2}}\right)
\end{aligned}
```

Therefore we can solve the model by combining {eq}`eq:CARA-cfin` and {eq}`eq:CARA-yfin` using {eq}`eq:CARA-ibc`:

```{math}
:label: eq:CARA-cfinhoriz

\CRat_{t} = \left(\frac{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CARA}]}{1-[\Rfree^{-1}(\Rfree\Discount)^{1/\CARA}]^{T+1}}\right)\left[B_{t}+\PLev_{t}\left(\frac{1-(\PGro/\Rfree)^{T+1}}{1-(\PGro/\Rfree)}\right)\right]
```

Now recall that in the infinite-horizon case ({math}`T=\infty`), [InfSum](#fact:infsum) requires that for human wealth to be well-defined we need the condition

```{math}
:label: eq:pdvyinf

\begin{aligned}
\PGro/\Rfree & < 1 \\
\PGro & < R.
\end{aligned}
```

Why is this? Because if income will grow faster than the interest rate forever, then the PDV of future income is infinite and the problem has no well-defined solution.

Similarly, in order for the PDV of consumption to be finite we must impose:

```{math}
:label: eq:pdvcinf

\begin{aligned}
\Rfree^{-1}(\Rfree\Discount)^{1/\CARA}& < 1 \\
(\Rfree\Discount)^{1/\CARA} & < R.
\end{aligned}
```

What this says is that the growth rate of consumption must be less than the interest rate in order for the model to have a well-defined solution. Otherwise, the PDV of future consumption is infinite, and the model does not have a well-defined solution. Note that this amounts to a requirement that there be at least a certain degree of "impatience."

If these conditions do hold, then the model has a well-defined infinite horizon solution, as can be seen by realizing that if {math}`(\PGro/\Rfree)<1` then {math}`\lim_{T \rightarrow \infty} (\PGro/\Rfree)^{T-t+1} = 0` and if {math}`\Rfree^{-1}(\Rfree\Discount)^{1/\CARA} < 1` then {math}`\displaystyle \lim_{T \rightarrow \infty} (\Rfree^{-1}(\Rfree\Discount)^{1/\CARA})^{T-t+1} = 0`. Substituting these zeros into {eq}`eq:CARA-cfinhoriz` yields

```{math}
:label: eq:cinfhor

\CRat_{t} = \left(1-\Rfree^{-1}(\Rfree\Discount)^{1/\CARA}\right)\left[B_{t}+\left(\frac{\PLev_{t}}{1-(\PGro/\Rfree)}\right)\right]
```

```{math}
:label: eq:cmpk

= \left(1-\Rfree^{-1}(\Rfree\Discount)^{1/\CARA}\right)\left[B_{t}+H_{t}\right]
```

```{math}
:label: eq:CARA-cOfw

= \left(\frac{\Rfree-(\Rfree\Discount)^{1/\CARA}}{\Rfree}\right)W_{t}
```

where {math}`W_{t}` is the consumer's "total wealth," the sum of human and nonhuman wealth.

Now consider the question "What is the level of {math}`\CRat_{t}` that will leave total wealth intact, allowing the same value of consumption in period {math}`t+1` and forever after?"

The intuitive answer is that if one wants to leave one's wealth[^permanent-income-note] intact, that is possible only if spending is exactly equal to the dividend and interest earnings on one's total wealth.

[^permanent-income-note]: Note that this was interpreted as "permanent income" in the 1960s and 70s, but will not be called such in this class. Point out that wealth here is exactly like an asset that yields a dividend {math}`P`.

Because human wealth is exactly like any other kind of wealth in this framework, it is possible to work directly with the level of total wealth {math}`W`. Suppose we assume the consumer will spend fraction {math}`\kappa` of total wealth in each period, and we want to find the {math}`\kappa` that leaves wealth intact.

```{math}
:label: eq:CARA-kappa

\begin{aligned}
W_{t+1} & = (W_{t}-\CRat_{t})R \\
\bar{W} & = (\bar{W}-\kappa \bar{W})R \\
1 & = \Rfree(1-\kappa) \\
1/\Rfree & = (1-\kappa) \\
\kappa & = 1-1/\Rfree \\
& = \left(\frac{\Rfree-1}{\Rfree}\right) \\
& = \rfree/\Rfree
\end{aligned}
```

Thus, the consumer can spend only the interest earnings {math}`\rfree` on their wealth, divided by the gross return {math}`\Rfree`. (The division occurs because we assume that interest is earned between periods rather than within periods; the right intuition is that if you want to preserve your wealth, you can only spend the interest on it and none of the principal).

Note that the coefficient multiplying total wealth in {eq}`eq:CARA-cOfw` is also divided by {math}`\Rfree`. Thus, whether the consumer is spending more than his total income, exactly his total income, or less than his total income depends upon whether the numerator in {eq}`eq:CARA-cOfw` is greater than, equal to, or less than {math}`\rfree`. If we call a consumer who is spending more than his income "impatient," the consumer will be impatient if

```{math}
\begin{aligned}
R-(\Rfree\Discount)^{1/\CARA} & > r \\
1-(\Rfree\Discount)^{1/\CARA} & > 0 \\
1 & > (\Rfree\Discount)^{1/\CARA}
\end{aligned}
```

Now note that if {math}`\Rfree\Discount=1` (which is to say, the interest rate is exactly equal to the time preference rate so that they offset each other), then {math}`(\Rfree\Discount)^{1/\CARA}=1` regardless of the value of {math}`\CARA` so that the consumer is precisely poised on the balance between patience and impatience and exactly spends his income.[^income-note]

[^income-note]: Income here means inclusive of interest income on total wealth.

The consumer will be impatient, spending more than his income, if {math}`\Rfree\Discount>1`, and patient, spending less than his income, if {math}`\Rfree\Discount<1`.

Equation {eq}`eq:cinfhor` can be simplified into something a bit easier to handle by making some approximations. If {math}`\Discount = 1/(1+\tau)`, then we can use

[LogEps](#fact:logeps): {math}`\log (1+\PShk) \approx \PShk`

and its inverse [ExpEps](#fact:expeps): {math}`\exp(\PShk) \approx 1+\PShk`

to discover that

```{math}
\begin{aligned}
\log (\Rfree\Discount)^{1/\CARA}/\Rfree & = (1/\CARA) (\log \Rfree + \log [1/(1+\tau) ]) - \log \Rfree \\
& = (1/\CARA) (\log(1+r) + \log 1 - \log (1+\tau) ) - \log \Rfree \\
& \approx \CARA^{-1}(\rfree -\tau) ) - r \\
(\Rfree\Discount)^{1/\CARA}/\Rfree & \approx 1+(\CARA^{-1}(\rfree-\tau)-\rfree)
\end{aligned}
```

Substituting this into {eq}`eq:cmpk` gives

```{math}
:label: eq:CARA-capprox

\CRat_{t} \approx \left(\rfree-\CARA^{-1}(\rfree-\tau)\right)W_{t}
```

Now we can see again that whether the consumer is patient or impatient depends on the relationship between {math}`\rfree` and {math}`\tau`. Note also that if {math}`\CARA = \infty` then the consumer is infinitely averse to changing the level of consumption, and so once again the consumer spends exactly his income.

Now a brief note on what "income" means in this model. Suppose for simplicity that the consumer had no capital assets {math}`K`, and suppose that income was expected to stay constant at level {math}`\bar{Y}` forever. In this case human wealth would be:

```{math}
\begin{aligned}
H_{t} & = \bar{Y}+\bar{Y}/\Rfree+\bar{Y}/\Rfree^{2}+\ldots \\
& = \bar{Y}(1+1/\Rfree+1/\Rfree^{2}+\ldots) \\
& = \bar{Y}\left(\frac{1}{1-1/\Rfree}\right) \\
& = \bar{Y}\left(\frac{\Rfree}{\Rfree-1}\right) \\
& = \bar{Y}\left(\frac{\Rfree}{\rfree}\right)
\end{aligned}
```

Now recall that we found in equation {eq}`eq:CARA-kappa` that the level of consumption that leaves "wealth" {math}`W_{t}` intact was

```{math}
\begin{aligned}
\CRat_{t} & = \kappa W_{t} \\
& = \kappa [B_{t}+H_{t}] \\
& = \kappa \bar{Y}\left(\frac{\Rfree}{\rfree}\right) \\
& = \left(\frac{\rfree}{\Rfree}\right) \bar{Y} \left(\frac{\Rfree}{\rfree}\right) \\
& = \bar{Y}.
\end{aligned}
```

So in this case, spending the "interest income on human wealth" corresponds to spending exactly your labor income. This seems less mysterious if you think of income {math}`Y_{t}` as the "return" on your human capital asset {math}`H_{t}`. If you "capitalize" your stream of income at rate {math}`\Rfree` and then spend the interest income on the capitalized stream, it stands to reason that you are spending the flow of income from that source.

Note also that in this case we can rewrite {eq}`eq:CARA-capprox` as

```{math}
\CRat_{t} \approx \left(\rfree-\CARA^{-1}(\rfree-\tau)\right)\left[B_{t}+ \bar{Y}\left(\frac{\Rfree}{\rfree}\right)\right].
```

Note that {math}`\rfree` appears three times in this equation, which correspond (in order) to the income effect, the substitution effect, and the human wealth effect.[^human-wealth-intro] To see this, note that an increase in the first {math}`\rfree` basically corresponds to an increase in the payout rate on total wealth (to see this, set {math}`\bar{Y} = 0` and refer to our formula above for {math}`\kappa`, realizing that for small {math}`\rfree`, {math}`\rfree/\Rfree \approx \rfree`.) The second term corresponds to the substitution effect, as can be seen from its dependence on the intertemporal elasticity of substitution {math}`\CARA^{-1}`. Finally, the {math}`\bar{Y}/\rfree` term clearly corresponds to human wealth, and therefore the sensitivity of consumption to {math}`\rfree` coming through this term corresponds to the human wealth effect.

[^human-wealth-intro]: This is why I introduced the concept of the human wealth effect in my original treatment in the Fisher diagram.
