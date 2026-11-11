(sec:PerfForesightCRRA-Appendix)=
# Appendix: Consumption Under Perfect Foresight and CRRA Utility

This is the appendix to the chapter [Consumption Under Perfect Foresight and CRRA Utility](#sec:PerfForesightCRRA), which [states its results](#sec:PerfForesightCRRA-AppendixResults) without proof.

(sec:PFwhenFHWfails)=
## The Limiting Solution to the Perfect Foresight Model if the FHWC Fails

### When the RIC Holds

Consider first a circumstance in which the RIC holds ({math}`\PatR<1`). In this case, the perfect foresight unconstrained model does not have a sensible solution because human wealth is infinite while the model implies that the optimal policy is to consume a positive proportion of human wealth. {math}`\cFunc(\mRat)=\infty~\forall~\mRat` is not a useful (or plausible!) solution.

### When the RIC Fails

The alternative case is when the RIC fails ({math}`\PatR>1`). Here, the only way to make sense of the model is to think about the limit of the finite horizon model as the horizon extends to infinity. This is because behavior reflects a competition between two pathologies that characterize the infinite horizon solution: It exhibits a limiting MPC of zero out of total wealth, which includes human wealth, which approaches infinity. A limiting solution of {math}`\cFunc(\mRat) = 0 \times \infty` is even less useful than {math}`\cFunc(\mRat) = \infty`!

It turns out that the limiting solution is not ambiguous, however. The finite horizon solution implies that consumption out of human wealth when the end of life is {math}`n` periods in the future is

```{math}
\MPC_{n} \hRat_{n} = \left(\frac{(\Rfree^{-1}{\WGro})^{{n}+1}-1}{[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{{n}+1}-1}\right)
```

whose limit is given by

```{math}
\begin{aligned}
\lim_{{n} \uparrow \infty} \MPC_{n} \hRat_{n} & =  \lim_{n \uparrow \infty} \left(\frac{(\Rfree^{-1}{\WGro})^{{n}+1}}{[\Rfree^{-1}(\Rfree\Discount)^{1/\CRRA}]^{{n}+1}}\right)
\\ & =  \lim_{n \uparrow \infty} \left(\frac{1}{\PatWGro^{(n+1)}}\right)
\\ & =  \infty
\end{aligned}
```

since when the RIC fails and the FHWC also fails ({math}`\WGro > \Rfree`), both the numerator and the denominator diverge, so the limit is governed by the ratio of the dominant terms. That ratio is infinite as long as the growth patience factor satisfies {math}`\PatWGro < 1`, in which case {math}`\PatWGro^{n+1}` approaches zero as {math}`n \uparrow \infty`. (In the case treated above, where the RIC holds rather than fails, {math}`\PatWGro<1` follows automatically, because {math}`\Pat < \Rfree` and {math}`\Rfree < \WGro` together imply the GIC {math}`\Pat < \WGro`.)

(Useful-Analytical-Results)=
## Useful Analytical Results

Given the result from the chapter's [Euler equation for consumption](#eq:PFCRRA-cgrow) that

```{math}
c_{t+n} = \Pat^{n} c_{t}
```

we can rewrite the value function as

```{math}
\begin{aligned}
  \vFunc_{\tNow} & =  \uFunc(c_{t}) + \DiscFac \uFunc(c_{t}\Pat) + \DiscFac^{2} \uFunc(c_{t} \Pat^{2}) + ...
  \\ & =  (1-\CRRA)^{-1}\left(c_{t}^{1-\CRRA} + \DiscFac (c_{t}\Pat)^{1-\CRRA} + \DiscFac^{2} (c_{t} \Pat^{2})^{1-\CRRA} + ...\right)
  \\ & =  (1-\CRRA)^{-1}\left(c_{t}^{1-\CRRA}\left(1+\DiscFac \Pat^{1-\CRRA} + (\DiscFac \Pat^{1-\CRRA})^{2} + ... \right) \right)
\\ & =  \uFunc(c_{t})\left(1+\DiscFac \Pat^{1-\CRRA} + (\DiscFac \Pat^{1-\CRRA})^{2} + ... \right)
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

\vFunc_{t} = \uFunc(c_{t})\overbrace{(1+\PatR+\PatR^{2}+...+\PatR^{T-t})}^{\equiv \cPDVFunc_{t}}
```

where {math}`\cPDVFunc_{t}` is the discounted value of future consumption growth (that is, the discounted value of the ratio of future consumption to today's consumption).

{cite:t}`BufferStockTheory` shows ([in an appendix](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory.pdf#nameddest=MPCnvrs)) that {math}`\cPDVFunc_{t} = \MPC_{t}^{-1}`, which means that we can write value as

```{math}
\begin{aligned}
  \vFunc_{t} & =  \uFunc(c_{t})\MPC^{-1}_{t}
  \\ & =  \left(\frac{(\oRat_{t}\MPC_{t})^{1-\CRRA}}{1-\CRRA}\right)\MPC_{t}^{-1}
\\ & =  \uFunc(\oRat_{t})\MPC_{t}^{-\CRRA}
\end{aligned}
```

## Additional Derivations

If consumption is simply a function of overall wealth bank balances {math}`\oRat_{t}`, we can derive a convenient recursive formula for the inverse of the MPC:

```{math}
:label: eq:MPCrecursive

\begin{aligned}
  \uFunc^{\prime}(\MPC_{t} \oRat_{t}) & = \Rfree \DiscFac \uFunc^{\prime}(\MPC_{t+1}\overbrace{\oRat_{t}(1-\MPC_{t})\Rfree}^{\oRat_{t+1}})
\\ \MPC_{t} \oRat_{t} & = (\Rfree \DiscFac)^{-1/\CRRA} \MPC_{t+1}\oRat_{t}(1-\MPC_{t}) \Rfree
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

But the series on the RHS in {eq}`eq:vFuncAnalytical` and {eq}`eq:MPCrecursiveSum` are identical! So {math}`\MPC^{-1}_{t} = \cPDVFunc_{t}`, and we can equivalently write

```{math}
\vFunc_{t} = \uFunc(c_{t})\MPC^{-1}_{t}.
```

Now note that if we define a utility-inverse of the value function as {math}`\vInv \equiv \left((1-\CRRA) \vFunc\right)^{1/(1-\CRRA)}`, then consumption exceeds its minimum possible value at {math}`\underline{\mRat}` (where consumption exceeds {math}`\cFunc(\underline{\mRat})=0`) by {math}`c_{t}=\MPC_{t}(\mRat-\underline{m})`:

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
