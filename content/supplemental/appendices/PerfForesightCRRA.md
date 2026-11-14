(sec:PerfForesightCRRA-Appendix)=
# Appendix: Consumption Under Perfect Foresight and CRRA Utility

This is the appendix to the chapter [Consumption Under Perfect Foresight and CRRA Utility](#sec:PerfForesightCRRA), which [states its results](#sec:PerfForesightCRRA-AppendixResults) without proof.

(sec:PFwhenFHWfails)=
## The Limiting Solution to the Perfect Foresight Model if the FHWC Fails

### When the RIC Holds

Consider first a circumstance in which the RIC holds ({math}`\PatR<1`). In this case, the perfect foresight unconstrained model does not have a sensible solution because human wealth is infinite while the model implies that the optimal policy is to consume a positive proportion of human wealth. {math}`\cFunc(\mRat)=\infty~\forall~\mRat` is not a useful (or plausible!) solution.

### When the RIC Fails

The alternative case is when the RIC fails ({math}`\PatR>1`). Here, the only way to make sense of the model is to think about the limit of the finite horizon model as the horizon extends to infinity. This is because behavior reflects a competition between two pathologies that characterize the infinite horizon solution: It exhibits a limiting MPC of zero out of total wealth, which includes human wealth, which approaches infinity. A limiting solution of {math}`\cFunc(\mRat) = 0 \times \infty` is even less useful than {math}`\cFunc(\mRat) = \infty`!

It turns out that the limiting solution is not ambiguous, however. When the end of life is {math}`n` periods in the future, the MPC is {math}`\MPC_{n} = (1-\PatR)/(1-\PatR^{n+1})` and human wealth is {math}`\hRat_{n} = (1-(\Rfree^{-1}\WGro)^{n+1})/(1-\Rfree^{-1}\WGro)`, so consumption out of human wealth is

```{math}
\MPC_{n} \hRat_{n} = \left(\frac{\PatR-1}{\Rfree^{-1}\WGro-1}\right)\left(\frac{(\Rfree^{-1}\WGro)^{n+1}-1}{\PatR^{n+1}-1}\right).
```

When the FHWC also fails ({math}`\WGro > \Rfree`), both the numerator and the denominator of the second fraction diverge, so its limit is governed by the ratio of their dominant terms. Since {math}`\Rfree^{-1}\WGro/\PatR = \WGro/\Pat = 1/\PatWGro`,

```{math}
\lim_{n \uparrow \infty} \MPC_{n} \hRat_{n} = \left(\frac{\PatR-1}{\Rfree^{-1}\WGro-1}\right) \lim_{n \uparrow \infty} \PatWGro^{-(n+1)},
```

so the limit depends on the growth impatience condition:

- If the GIC holds ({math}`\PatWGro<1`), consumption out of human wealth grows without bound.
- If {math}`\PatWGro=1`, then {math}`\PatR = \Rfree^{-1}\WGro`, the two fractions cancel, and {math}`\MPC_{n} \hRat_{n} = 1` at every horizon: consumption converges to permanent income.
- If the GIC fails ({math}`\PatWGro>1`), consumption out of human wealth goes to zero. The MPC {math}`\MPC_{n}` goes to zero too when the RIC fails, so consumption itself does: {math}`\cFunc(\mRat) = 0`.

The same limits hold when {math}`\WGro = \Rfree`, where the closed form for human wealth divides by zero and the sum gives {math}`\hRat_{n} = n+1`: then {math}`\PatWGro = \PatR > 1`, and consumption goes to zero. (In the case treated above, where the RIC holds rather than fails, {math}`\PatWGro<1` follows automatically, because {math}`\Pat < \Rfree` and {math}`\Rfree \leq \WGro` together imply the GIC {math}`\Pat < \WGro`.) The boundary of the RIC, {math}`\PatR = 1`, behaves like the case where it holds: the closed form for the MPC divides by zero and the sum gives {math}`\MPC_{n} = 1/(n+1)`, while {math}`\hRat_{n}` grows geometrically when {math}`\WGro > \Rfree`, so consumption out of human wealth grows without bound; the GIC holds, since {math}`\Pat = \Rfree < \WGro`.

(sec:PerfForesightCRRA-MPCRecursion)=
## The MPC Recursion

Consumption is proportional to overall wealth {math}`\oLev_{t}`, the sum of human and nonhuman wealth: {math}`\cLevBF_{t} = \MPC_{t}\oLev_{t}`, where overall wealth evolves as {math}`\oLev_{t+1} = (\oLev_{t}-\cLevBF_{t})\Rfree`. Substituting both into the chapter's [Euler equation for consumption](#eq:PFCRRA-cgrow) gives a convenient recursive formula for the inverse of the MPC:

```{math}
:label: eq:MPCrecursive

\begin{aligned}
  \uFunc^{\prime}(\MPC_{t} \oLev_{t}) & = \Rfree \DiscFac \uFunc^{\prime}(\MPC_{t+1}\overbrace{\oLev_{t}(1-\MPC_{t})\Rfree}^{\oLev_{t+1}})
\\ \MPC_{t} \oLev_{t} & = (\Rfree \DiscFac)^{-1/\CRRA} \MPC_{t+1}\oLev_{t}(1-\MPC_{t}) \Rfree
\\ \underbrace{\Rfree^{-1} (\Rfree \DiscFac)^{1/\CRRA}}_{\PatR} \MPC_{t}  & =  \MPC_{t+1}(1-\MPC_{t})
\\ (\PatR \MPC_{t})^{-1}  & =  \MPC_{t+1}^{-1}(1-\MPC_{t})^{-1}
\\ (1-\MPC_{t}) \MPC_{t}^{-1}  & = \PatR  \MPC_{t+1}^{-1}
\\ \MPC_{t}^{-1}-1  & = \PatR  \MPC_{t+1}^{-1}
\\ \MPC_{t}^{-1}  & = 1+\PatR  \MPC_{t+1}^{-1}
\end{aligned}
```

which implies that if the MPC in the last period {math}`T` is {math}`\MPC_{T}=1` then from any date {math}`t \leq T` we can write

```{math}
:label: eq:MPCrecursiveSum

\MPC_{t}^{-1} = 1 + \PatR + \PatR^{2} + ... + \PatR^{T-t}.
```

(sec:PerfForesightCRRA-ValueClosedForm)=
## Value in Closed Form

Given the result from the chapter's [Euler equation for consumption](#eq:PFCRRA-cgrow) that

```{math}
\cLevBF_{t+n} = \Pat^{n} \cLevBF_{t}
```

we can rewrite the value function as

```{math}
\begin{aligned}
  \vFunc_{t} & =  \uFunc(\cLevBF_{t}) + \DiscFac \uFunc(\cLevBF_{t}\Pat) + \DiscFac^{2} \uFunc(\cLevBF_{t} \Pat^{2}) + \dots + \DiscFac^{T-t} \uFunc(\cLevBF_{t} \Pat^{T-t})
  \\ & =  (1-\CRRA)^{-1}\cLevBF_{t}^{1-\CRRA}\left(1+\DiscFac \Pat^{1-\CRRA} + (\DiscFac \Pat^{1-\CRRA})^{2} + \dots + (\DiscFac \Pat^{1-\CRRA})^{T-t} \right)
\\ & =  \uFunc(\cLevBF_{t})\left(1+\DiscFac \Pat^{1-\CRRA} + (\DiscFac \Pat^{1-\CRRA})^{2} + \dots + (\DiscFac \Pat^{1-\CRRA})^{T-t} \right)
\end{aligned}
```

but since {math}`\DiscFac \Pat^{1-\CRRA} = \PatR`,[^patr-derivation] this reduces to

[^patr-derivation]:

    ```{math}
    \begin{aligned}
      \DiscFac \Pat^{1-\CRRA} & =  \DiscFac (\Rfree \DiscFac)^{\frac{1-\CRRA}{\CRRA}}
      \\ & =                               \DiscFac (\Rfree \DiscFac)^{1/\CRRA-1}
      \\ & =             (\Rfree \DiscFac)^{1/\CRRA} / \Rfree
               \\ & =  \PatR
    \end{aligned}
    ```


```{math}
:label: eq:vFuncAnalytical

\vFunc_{t} = \uFunc(\cLevBF_{t})\overbrace{(1+\PatR+\PatR^{2}+...+\PatR^{T-t})}^{\equiv \cPDVFunc_{t}}
```

where {math}`\cPDVFunc_{t}` is the discounted value of future consumption growth (that is, the discounted value of the ratio of future consumption to today's consumption).

The sum that defines {math}`\cPDVFunc_{t}` is the sum in [the MPC recursion](#eq:MPCrecursiveSum), so {math}`\cPDVFunc_{t} = \MPC_{t}^{-1}`, and we can write value as

```{math}
\begin{aligned}
  \vFunc_{t} & =  \uFunc(\cLevBF_{t})\MPC^{-1}_{t}
  \\ & =  \left(\frac{(\oLev_{t}\MPC_{t})^{1-\CRRA}}{1-\CRRA}\right)\MPC_{t}^{-1}
\\ & =  \uFunc(\oLev_{t})\MPC_{t}^{-\CRRA}
\end{aligned}
```

Now define the utility-inverse of the value function, {math}`\vInv \equiv \left((1-\CRRA) \vFunc\right)^{1/(1-\CRRA)}` (for {math}`\CRRA \neq 1`). In ratios to permanent income, overall wealth is market resources in excess of their minimum possible value {math}`\underline{\mRat}`, the point at which consumption is {math}`\cFunc(\underline{\mRat})=0`; so consumption is {math}`c_{t}=\MPC_{t}(\mRat_{t}-\underline{\mRat}_{t})`, and

```{math}
\begin{aligned}
  \vInv_{t}(m) &= \MPC_{t}(\mRat_{t}-\underline{m}_{t}) \MPC_{t}^{-1/(1-\CRRA)}
  \\ & = (m - \underline{m})\MPC^{((1-\CRRA)/(1-\CRRA)-1/(1-\CRRA))}
  \\ & = (m - \underline{m})\MPC^{-\CRRA/(1-\CRRA)}
\end{aligned}
```

which is linear, and makes it very easy to compute

```{math}
\vFunc_{t}(\mRat) = \uFunc\left((m-\underline{m})\MPC_{t}^{-\CRRA/(1-\CRRA)}\right)
```
