(sec:CARAModelWithYRisk)=
# Consumption with Constant Absolute Risk Aversion (CARA) Utility

Consider the optimization problem of a consumer with a constant absolute risk aversion instantaneous utility function {math}`\uFunc(\CRat)= -(1/\CARA) e^{-\CARA \CRat}` implying {math}`\uFunc^{\prime}(\CRat) = e^{-\CARA \CRat}` facing an interest rate that is constant at {math}`\rfree=\Rfree-1`.[^caballero-ref] The consumer's optimization problem is

[^caballero-ref]: A problem like this was considered in a well-known paper by {cite:t}`caballero:jme`.

```{math}
:label: eq:CARA-maxprob

\max_{\{\CFunc\}_{t}^{T}}~~ \Ex_{t}\left\{\sum_{s=t}^{T} \Discount^{s-t} \uFunc(\CRat_{s})\right\}
```

subject to the constraints

```{math}
\begin{aligned}
B_{t+1} & = ({M}_{t}-\CRat_{t})\Rfree \\
{M}_{t+1} & = B_{t+1}+Y_{t+1}
\end{aligned}
```

Here {math}`M_t` denotes "market resources," the consumer's total resources available for consumption at the beginning of period {math}`t`, combining beginning-of-period bank balances {math}`B_t` with current income. The consumer's idiosyncratic income {math}`Y_{t+1}` exhibits a random-walk deviation from an exogenously-growing trend:

```{math}
\begin{aligned}
\bar{\PLev}_{t+1} & = \PGro \bar{\PLev}_{t} \\
Y_{t+1} & = \bar{\PLev}_{t+1}+\PLev_{t+1} \\
\PLev_{t+1} & = \PLev_{t}+\PShk_{t+1}.
\end{aligned}
```

Bellman's equation relates the value function at time {math}`t` to the value function at {math}`t+1` through the choice variables and state variables:

```{math}
:label: eq:CARA-vmax

\VFunc_{t}({M}_{t},\bar{\PLev}_{t},\PLev_{t}) = \max_{\{\CFunc\}_{t}^{T}} ~~ \uFunc(\CRat_{t}) + \Ex_{t}[\Discount \VFunc_{t+1}({M}_{t+1},\bar{\PLev}_{t+1},{\PLev}_{t+1})].
```

The first order condition (FOC) for the CARA utility problem is

```{math}
\uFunc^{\prime}(\CRat_{t}) = \Rfree \Discount \Ex_{t}[\VFunc_{t+1}^{M}]
```

and the [Envelope theorem](#sec:Envelope) tells us that

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

Now we need [InfSumMult](#fact:infsummult): if {math}`\Rfree > 1`, then {math}`\displaystyle \sum_{i=0}^{\infty} i/\Rfree^{i} = \left(\frac{\Rfree}{(\Rfree-1)^{2}}\right)`.

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

The finite-horizon version of the problem, together with the "impatience" and "finite human wealth" conditions under which the horizon can be extended to infinity, is worked out for CRRA utility in the [perfect foresight CRRA](#sec:PerfForesightCRRA) section. The CARA counterpart of that apparatus replaces the multiplicative consumption growth factor {math}`(\Rfree\Discount)^{1/\CRRA}` with the additive drift {math}`\log (\Rfree\Discount)^{1/\CARA}` derived in {eq}`eq:CARA-cgrow`.
