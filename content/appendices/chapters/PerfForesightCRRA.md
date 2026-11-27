(sec:PerfForesightCRRA-Appendix)=
# Appendix: Consumption Under Perfect Foresight and CRRA Utility

This is the appendix to the chapter [Consumption Under Perfect Foresight and CRRA Utility](#sec:PerfForesightCRRA), which [states its results](#sec:PerfForesightCRRA-AppendixResults) without proof.

(sec:PFwhenFHWfails)=
## The Limiting Solution to the Perfect Foresight Model if the FHWC Fails

### When the RIC Holds

Consider first a circumstance in which the RIC holds ({math}`\RPFac<1`). In this case, the perfect foresight unconstrained model does not have a sensible solution because human wealth is infinite while the model implies that the optimal policy is to consume a positive proportion of human wealth. {math}`\cFunc(\mNrm)=\infty~\forall~\mNrm` is not a useful (or plausible!) solution.

### When the RIC Fails

The alternative case is when the RIC fails ({math}`\RPFac>1`). Here, the only way to make sense of the model is to think about the limit of the finite horizon model as the horizon extends to infinity. This is because behavior reflects a competition between two pathologies that characterize the infinite horizon solution: It exhibits a limiting MPC of zero out of total wealth, which includes human wealth, which approaches infinity. A limiting solution of {math}`\cFunc(\mNrm) = 0 \times \infty` is even less useful than {math}`\cFunc(\mNrm) = \infty`!

It turns out that the limiting solution is not ambiguous, however. When the end of life is {math}`n` periods in the future, the MPC is {math}`\MPC_{n} = (1-\RPFac)/(1-\RPFac^{n+1})` and human wealth is {math}`\hNrm_{n} = (1-(\Rfree^{-1}\PermGroFac)^{n+1})/(1-\Rfree^{-1}\PermGroFac)`, so consumption out of human wealth is

```{math}
\MPC_{n} \hNrm_{n} = \left(\frac{\RPFac-1}{\Rfree^{-1}\PermGroFac-1}\right)\left(\frac{(\Rfree^{-1}\PermGroFac)^{n+1}-1}{\RPFac^{n+1}-1}\right).
```

When the FHWC also fails ({math}`\PermGroFac > \Rfree`), both the numerator and the denominator of the second fraction diverge, so its limit is governed by the ratio of their dominant terms. Since {math}`\Rfree^{-1}\PermGroFac/\RPFac = \PermGroFac/\APFac = 1/\GPFac`,

```{math}
\lim_{n \uparrow \infty} \MPC_{n} \hNrm_{n} = \left(\frac{\RPFac-1}{\Rfree^{-1}\PermGroFac-1}\right) \lim_{n \uparrow \infty} \GPFac^{-(n+1)},
```

so the limit depends on the growth impatience condition:

- If the GIC holds ({math}`\GPFac<1`), consumption out of human wealth grows without bound.
- If {math}`\GPFac=1`, then {math}`\RPFac = \Rfree^{-1}\PermGroFac`, the two fractions cancel, and {math}`\MPC_{n} \hNrm_{n} = 1` at every horizon: consumption converges to permanent income.
- If the GIC fails ({math}`\GPFac>1`), consumption out of human wealth goes to zero. The MPC {math}`\MPC_{n}` goes to zero too when the RIC fails, so consumption itself does: {math}`\cFunc(\mNrm) = 0`.

The same limits hold when {math}`\PermGroFac = \Rfree`, where the closed form for human wealth divides by zero and the sum gives {math}`\hNrm_{n} = n+1`: then {math}`\GPFac = \RPFac > 1`, and consumption goes to zero. (In the case treated above, where the RIC holds rather than fails, {math}`\GPFac<1` follows automatically, because {math}`\APFac < \Rfree` and {math}`\Rfree \leq \PermGroFac` together imply the GIC {math}`\APFac < \PermGroFac`.) The boundary of the RIC, {math}`\RPFac = 1`, behaves like the case where it holds: the closed form for the MPC divides by zero and the sum gives {math}`\MPC_{n} = 1/(n+1)`, while {math}`\hNrm_{n}` grows geometrically when {math}`\PermGroFac > \Rfree`, so consumption out of human wealth grows without bound; the GIC holds, since {math}`\APFac = \Rfree < \PermGroFac`.

Finally, for completeness: when the RIC fails but the FHWC holds, human wealth is finite while the MPC goes to zero, so consumption goes to zero too: {math}`\cFunc(\mNrm)=0`.

(sec:PerfForesightCRRA-MPCRecursion)=
## The MPC Recursion

Consumption is proportional to overall wealth {math}`\oLvl_{t}`, the sum of human and nonhuman wealth: {math}`\cLvl_{t} = \MPC_{t}\oLvl_{t}`, where overall wealth evolves as {math}`\oLvl_{t+1} = (\oLvl_{t}-\cLvl_{t})\Rfree`. Substituting both into the chapter's [Euler equation for consumption](#eq:PFCRRA-cgrow) gives a convenient recursive formula for the inverse of the MPC:

```{math}
:label: eq:MPCrecursive

\begin{aligned}
  \uFunc^{\prime}(\MPC_{t} \oLvl_{t}) & = \Rfree \DiscFac \uFunc^{\prime}(\MPC_{t+1}\overbrace{\oLvl_{t}(1-\MPC_{t})\Rfree}^{\oLvl_{t+1}})
\\ \MPC_{t} \oLvl_{t} & = (\Rfree \DiscFac)^{-1/\CRRA} \MPC_{t+1}\oLvl_{t}(1-\MPC_{t}) \Rfree
\\ \underbrace{\Rfree^{-1} (\Rfree \DiscFac)^{1/\CRRA}}_{\RPFac} \MPC_{t}  & =  \MPC_{t+1}(1-\MPC_{t})
\\ \MPC_{t}^{-1}-1 = (1-\MPC_{t}) \MPC_{t}^{-1}  & = \RPFac  \MPC_{t+1}^{-1}
\\ \MPC_{t}^{-1}  & = 1+\RPFac  \MPC_{t+1}^{-1}
\end{aligned}
```

which implies that if the MPC in the last period {math}`T` is {math}`\MPC_{T}=1` then from any date {math}`t \leq T` we can write

```{math}
:label: eq:MPCrecursiveSum

\MPC_{t}^{-1} = 1 + \RPFac + \RPFac^{2} + ... + \RPFac^{T-t}.
```

(sec:PerfForesightCRRA-ValueClosedForm)=
## Value in Closed Form

Given the result from the chapter's [Euler equation for consumption](#eq:PFCRRA-cgrow) that

```{math}
\cLvl_{t+n} = \APFac^{n} \cLvl_{t}
```

we can rewrite the value function as

```{math}
\begin{aligned}
  \vLvl_{t} & =  \uFunc(\cLvl_{t}) + \DiscFac \uFunc(\cLvl_{t}\APFac) + \DiscFac^{2} \uFunc(\cLvl_{t} \APFac^{2}) + \dots + \DiscFac^{T-t} \uFunc(\cLvl_{t} \APFac^{T-t})
  \\ & =  (1-\CRRA)^{-1}\cLvl_{t}^{1-\CRRA}\left(1+\DiscFac \APFac^{1-\CRRA} + (\DiscFac \APFac^{1-\CRRA})^{2} + \dots + (\DiscFac \APFac^{1-\CRRA})^{T-t} \right)
\\ & =  \uFunc(\cLvl_{t})\left(1+\DiscFac \APFac^{1-\CRRA} + (\DiscFac \APFac^{1-\CRRA})^{2} + \dots + (\DiscFac \APFac^{1-\CRRA})^{T-t} \right)
\end{aligned}
```

but since {math}`\DiscFac \APFac^{1-\CRRA} = \RPFac`, this reduces to

:::{margin}
```{math}
\begin{aligned}
  \DiscFac \APFac^{1-\CRRA} & =  \DiscFac (\Rfree \DiscFac)^{\frac{1-\CRRA}{\CRRA}}
  \\ & =                               \DiscFac (\Rfree \DiscFac)^{1/\CRRA-1}
  \\ & =             (\Rfree \DiscFac)^{1/\CRRA} / \Rfree
           \\ & =  \RPFac
\end{aligned}
```
:::


```{math}
:label: eq:vFuncAnalytical

\vLvl_{t} = \uFunc(\cLvl_{t})\overbrace{(1+\RPFac+\RPFac^{2}+...+\RPFac^{T-t})}^{= \PDV_{t}^{T}(\cLvl)/\cLvl_{t}}
```

where {math}`\PDV_{t}^{T}(\cLvl)/\cLvl_{t}`, the chapter's [present discounted value of consumption](#eq:cfin) divided by today's consumption, is the discounted value of future consumption growth (that is, the discounted value of the ratio of future consumption to today's consumption).

This sum is the sum in [the MPC recursion](#eq:MPCrecursiveSum), so {math}`\PDV_{t}^{T}(\cLvl)/\cLvl_{t} = \MPC_{t}^{-1}`, and we can write value as

```{math}
\begin{aligned}
  \vLvl_{t} & =  \uFunc(\cLvl_{t})\MPC^{-1}_{t}
  \\ & =  \left(\frac{(\oLvl_{t}\MPC_{t})^{1-\CRRA}}{1-\CRRA}\right)\MPC_{t}^{-1}
\\ & =  \uFunc(\oLvl_{t})\MPC_{t}^{-\CRRA}
\end{aligned}
```

Now define the utility-inverse of the value function, {math}`\vInv \equiv \left((1-\CRRA) \vFunc\right)^{1/(1-\CRRA)}` (for {math}`\CRRA \neq 1`). In ratios to permanent income, overall wealth is market resources in excess of their minimum possible value {math}`\underline{\mNrm}`, the point at which consumption is {math}`\cFunc(\underline{\mNrm})=0`; so consumption is {math}`c_{t}=\MPC_{t}(\mNrm_{t}-\underline{\mNrm}_{t})`, and

```{math}
\begin{aligned}
  \vInv_{t}(m) &= \MPC_{t}(\mNrm_{t}-\underline{m}_{t}) \MPC_{t}^{-1/(1-\CRRA)}
  \\ & = (m - \underline{m})\MPC^{((1-\CRRA)/(1-\CRRA)-1/(1-\CRRA))}
  \\ & = (m - \underline{m})\MPC^{-\CRRA/(1-\CRRA)}
\end{aligned}
```

which is linear, and makes it very easy to compute

```{math}
\vFunc_{t}(\mNrm) = \uFunc\left((m-\underline{m})\MPC_{t}^{-\CRRA/(1-\CRRA)}\right)
```
