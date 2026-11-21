(sec:CARAModelWithYRisk)=
# Consumption with Constant Absolute Risk Aversion (CARA) Utility

Consider the optimization problem of a consumer with a constant absolute risk aversion instantaneous utility function {math}`\uFunc(\CNrm)= -(1/\CARA) e^{-\CARA \CNrm}` implying {math}`\uFunc^{\prime}(\CNrm) = e^{-\CARA \CNrm}` facing an interest rate that is constant at {math}`\rfree=\Rfree-1`. The consumer's optimization problem is

:::{margin}
A problem like this was considered in a well-known paper by {cite:t}`caballero:jme`.
:::

```{math}
:label: eq:CARA-maxprob

\max_{\{\CFunc\}_{t}^{T}}~~ \Ex_{t}\left\{\sum_{s=t}^{T} \DiscFac^{s-t} \uFunc(\CNrm_{s})\right\}
```

subject to the constraints

```{math}
\begin{aligned}
B_{t+1} & = ({M}_{t}-\CNrm_{t})\Rfree \\
{M}_{t+1} & = B_{t+1}+Y_{t+1}
\end{aligned}
```

Here {math}`M_t` denotes "market resources," the consumer's total resources available for consumption at the beginning of period {math}`t`, combining beginning-of-period bank balances {math}`B_t` with current income. The consumer's idiosyncratic income {math}`Y_{t+1}` exhibits a random-walk deviation from an exogenously-growing trend:

```{math}
\begin{aligned}
\bar{\PLev}_{t+1} & = \PermGroFac \bar{\PLev}_{t} \\
Y_{t+1} & = \bar{\PLev}_{t+1}+\PLev_{t+1} \\
\PLev_{t+1} & = \PLev_{t}+\PermShkAgg_{t+1}.
\end{aligned}
```

Bellman's equation relates the value function at time {math}`t` to the value function at {math}`t+1` through the choice variables and state variables:

```{math}
:label: eq:CARA-vmax

\VFunc_{t}({M}_{t},\bar{\PLev}_{t},\PLev_{t}) = \max_{\{\CFunc\}_{t}^{T}} ~~ \uFunc(\CNrm_{t}) + \Ex_{t}[\DiscFac \VFunc_{t+1}({M}_{t+1},\bar{\PLev}_{t+1},{\PLev}_{t+1})].
```

The first order condition (FOC) for the CARA utility problem is

```{math}
\uFunc^{\prime}(\CNrm_{t}) = \Rfree \DiscFac \Ex_{t}[\VFunc_{t+1}^{M}]
```

and the [Envelope theorem](#sec:Envelope) tells us that

```{math}
\VFunc^{M}_{t} = \Rfree \DiscFac \Ex_{t}[\VFunc_{t+1}^{M}].
```

In the perfect foresight version of the model in which {math}`\PermShkAgg_{t} = 0 ~\forall~t`, the Euler equation will be

```{math}
:label: eq:CARA-cgrow

\begin{aligned}
\uFunc^{\prime}(\CNrm_{t}) & = \Rfree\DiscFac \uFunc^{\prime}(\CNrm_{t+1}) \\
\exp[-\CARA \CNrm_{t}] & = \Rfree \DiscFac \exp[-\CARA \CNrm_{t+1}] \\
1 & = \Rfree\DiscFac \exp[-\CARA (\CNrm_{t+1}-\CNrm_{t})] \\
\exp[\CARA (\CNrm_{t+1}-\CNrm_{t})] & = \Rfree\DiscFac \\
\CARA (\CNrm_{t+1}-\CNrm_{t}) & = \log \Rfree\DiscFac \\
\CNrm_{t+1} & = \CNrm_{t}+\log (\Rfree\DiscFac)^{1/\CARA}.
\end{aligned}
```

The {math}`\log (\Rfree\DiscFac)^{1/\CARA}` term reflects the intertemporal substitution factor in consumption. Notice that intertemporal substitution takes the form of *additive* changes in the *level* of consumption in the CARA utility model, rather than multiplicative changes that affect the growth rate of consumption, as in the CRRA model.

Now suppose we are interested in the case where permanent income shocks are distributed normally, {math}`\PermShkAgg_{t} \sim \mathcal{N}(0,\sigma_{\PermShkAgg}^{2})`. Then it turns out that the process

```{math}
:label: eq:soln

\CNrm_{t+1} = \CNrm_{t} + \log (\Rfree\DiscFac)^{1/\CARA} + \CARA \sigma^{2}_{\PermShkAgg}/2+\PermShkAgg_{t+1}
```

satisfies the FOC under uncertainty:

```{math}
\begin{aligned}
1 & = \Rfree \DiscFac \Ex_{t}[\exp[-\CARA ({c}_{t+1}-c_{t})]] \\
1 & = \Rfree \DiscFac \Ex_{t}[\exp[-\CARA (\CARA \sigma_{\PermShkAgg}^{2}/2+{\PermShkAgg}_{t+1}+(1/\CARA)\log (\Rfree\DiscFac) +c_{t}-c_{t})]] \\
1 & = \Rfree \DiscFac \exp[-\CARA^{2} \sigma_{\PermShkAgg}^{2}/2] \Ex_{t} \{\exp[-\CARA {\PermShkAgg}_{t+1}]\}\exp[-\CARA (1/\CARA) \log \Rfree\DiscFac] \\
1 & = \Rfree \DiscFac \exp[-\CARA^{2}(\sigma_{\PermShkAgg}^{2}/2)]\exp[\CARA^{2}(\sigma_{\PermShkAgg}^{2}/2)]\exp[\log (\Rfree\DiscFac)^{-1}] \\
1 & = \Rfree \DiscFac (\Rfree\DiscFac)^{-1} \\
1 & = 1.
\end{aligned}
```

Define {math}`\kappa = \log (\Rfree\DiscFac)^{1/\CARA} + \CARA \sigma^{2}_{\PermShkAgg}/2`, so that {eq}`eq:soln` becomes:

```{math}
\CNrm_{t+1} = \CNrm_{t} + \PermShkAgg_{t+1} + \kappa.
```

The expected present discounted value of consumption is

:::{margin}
The {math}`\PermShkAgg_{t+n}` terms disappear when expectations are taken.
:::

```{math}
\begin{aligned}
\PDV_{t}(\CNrm) & = \CNrm_{t}+(\CNrm_{t}+\PermShkAgg_{t+1}+\kappa)/\Rfree + (\CNrm_{t}+\PermShkAgg_{t+1}+\kappa + \PermShkAgg_{t+2} + \kappa)/\Rfree^{2} + \ldots \\
\Ex_{t}[\PDV_{t}(\CNrm)] & = \CNrm_{t}+\CNrm_{t}/\Rfree+\CNrm_{t}/\Rfree^{2}+ \ldots + \kappa/\Rfree + 2\kappa/\Rfree^{2} + 3\kappa/\Rfree^{3} + \ldots \\
& = \CNrm_{t}(1+\Rfree^{-1}+\Rfree^{-2}+\ldots) + \kappa \sum_{i=1}^{\infty} i/\Rfree^{i}.
\end{aligned}
```

Now we need [InfSumMult](#fact:infsummult): if {math}`\Rfree > 1`, then {math}`\displaystyle \sum_{i=0}^{\infty} i/\Rfree^{i} = \left(\frac{\Rfree}{(\Rfree-1)^{2}}\right)`.

Thus, the expectation of the infinite horizon PDV of consumption is:

```{math}
\Ex_{t}[\PDV_{t}(\CNrm)] = \CNrm_{t}\left(\frac{1}{1-1/\Rfree}\right)+\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right).
```

Given the process for income described above, we have

```{math}
\begin{aligned}
\PDV_{t}(Y) & = Y_{t}+Y_{t+1}/\Rfree+Y_{t+2}/\Rfree^{2}+\ldots \\
& = \bar{\PLev}_{t}+\PLev_{t}+(\PermGroFac\bar{\PLev}_{t}+\PLev_{t+1})/\Rfree + (\PermGroFac^{2}\bar{\PLev}_{t}+\PLev_{t+2})/\Rfree^{2}+ \ldots \\
& = \bar{\PLev}_{t}\left(1+\PermGroFac/\Rfree + (\PermGroFac/\Rfree)^{2} + \ldots \right)+ \\
& \PLev_{t}+(\PLev_{t}+\PermShkAgg_{t+1})/\Rfree+(\PLev_{t}+\PermShkAgg_{t+1}+\PermShkAgg_{t+2})/\Rfree^{2}+\ldots \\
\Ex_{t}[\PDV_{t}(Y)] & = \left(\frac{\bar{\PLev}_{t}}{1-\PermGroFac/\Rfree}\right)+\PLev_{t}\sum_{s=0}^{\infty} \Rfree^{-s} \\
& = \left(\frac{\bar{\PLev}_{t}}{1-\PermGroFac/\Rfree}\right)+\left(\frac{ \PLev_{t}}{1-1/\Rfree}\right)
\end{aligned}
```

The IBC says

```{math}
:label: eq:CARA-ibc

\PDV_{t}(\CNrm) = B_{t}+\PDV_{t}(Y),
```

Because the intertemporal budget constraint must hold in every state of the world, the expectation of the PDV of consumption must equal current wealth plus the expectation of the PDV of income. Thus,

```{math}
\begin{aligned}
\Ex_{t}[\PDV_{t}(\CNrm)] & = B_{t}+\Ex_{t}[\PDV_{t}(Y)] \\
\CNrm_{t}\left(\frac{1}{1-1/\Rfree}\right) & = B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PermGroFac/\Rfree}\right)+\left(\frac{ \PLev_{t}}{1-1/\Rfree}\right)-\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right) \\
\CNrm_{t} & = \PLev_{t} + \left(\frac{\rfree}{\Rfree}\right)\left[ B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PermGroFac/\Rfree}\right)-\left(\frac{\kappa \Rfree}{(1-\Rfree)^{2}}\right) \right] \\
& = \PLev_{t} + \left(\frac{\rfree}{\Rfree}\right)\left[ B_{t}+ \left(\frac{\bar{\PLev}_{t}}{1-\PermGroFac/\Rfree}\right)\right] -\rfree\left(\frac{\log (\Rfree\DiscFac)^{1/\CARA} + \CARA \sigma^{2}_{\PermShkAgg}/2 }{(1-\Rfree)^{2}}\right)
\end{aligned}
```

The {math}`\PLev_{t}` term reflects the consumer's idiosyncratic level of permanent income, which has no systematic growth (or decline). The next term reflects the MPC out of total "certain" wealth, human and nonhuman. The final term reflects the combination of the intertemporal substitution motive (in the {math}`\log (\Rfree\DiscFac)^{1/\CARA}` term) and the precautionary motive in the {math}`\CARA \sigma^{2}_{\PermShkAgg}` term, as is evident from the fact that it equals zero if either there is no precautionary motive ({math}`\CARA=0`) or there is no uncertainty {math}`\sigma^{2}_{\PermShkAgg}=0`.

Note some peculiar aspects of this solution. First, observe that, marginally, the consumer spends exactly the interest income on capital, {math}`d \CNrm_{t}/d B_{t} = \rfree/\Rfree`. The reason this is peculiar is that the MPC out of capital *does not depend on how impatient the consumer is*. Impatience is reflected in the change in consumption over time, but not in the level of consumption except as that is affected by the budget constraint.

Second, notice that the effect of income uncertainty on saving is the same in absolute dollars regardless of the level of resources or permanent income.

The finite-horizon version of the problem, together with the "impatience" and "finite human wealth" conditions under which the horizon can be extended to infinity, is worked out for CRRA utility in the [perfect foresight CRRA](#sec:PerfForesightCRRA) section. The CARA counterpart of that apparatus replaces the multiplicative consumption growth factor {math}`(\Rfree\DiscFac)^{1/\CRRA}` with the additive drift {math}`\log (\Rfree\DiscFac)^{1/\CARA}` derived in {eq}`eq:CARA-cgrow`.
