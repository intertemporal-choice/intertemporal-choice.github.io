(sec:RebeloAK)=
# The Rebelo (1991) AK Model

{cite:t}`rebelo:long` examines a model in which a social planner maximizes the discounted sum of utility
in an economy with an {math}`\PtyAgg\KLvl` production function:

```{math}
:label: eq:Rebelo-maxutil

\max_{\{\CLvl\}_{0}^{\infty}} \int_0^{\infty} \uFunc(\CLvl) e^{-\discRte t} dt
```

subject to

```{math}
:label: eq:Rebelo-kdot

\dot{\KLvl} = \PtyAgg\KLvl - \CLvl,
```

where we have assumed zero population growth and zero depreciation
to make the analysis less cluttered.

This problem can be solved with the same [Hamiltonian apparatus](#sec:HamiltonianVSDiscrete) we used
to solve the Ramsey/Cass-Koopmans model. In particular, with CRRA
utility with risk aversion {math}`\CRRA` one can show that optimal behavior
requires

```{math}
:label: eq:Rebelo-cgrow

\begin{gathered}\begin{aligned}
  \dot{\CLvl}/\CLvl & =  \CRRA^{-1}(\PtyAgg - \discRte).
\end{aligned}\end{gathered}
```

Note that this equation comes about because the marginal product of
capital in this model is always {math}`\PtyAgg = \rfree`: the equation is the RCK model's [Keynes-Ramsey rule](#eq:cdotOc) with no population or productivity growth, consumption growth of {math}`\CRRA^{-1}(\rfree - \discRte)`. Note
further that according to this equation, the growth rate of consumption
is always the same; unlike the [Ramsey/Cass-Koopmans model](#sec:RamseyCassKoopmans) with a normal
production function, this model has no transitional dynamics.

We can also use {eq}`eq:Rebelo-kdot` to obtain an expression for the
steady-state growth rate:

```{math}
:label: eq:Rebelo-ssg

\begin{gathered}\begin{aligned}
  \dot{\KLvl}/\KLvl & =  \PtyAgg - \CLvl/\KLvl.
\end{aligned}\end{gathered}
```

If the model has a steady-state growth rate of {math}`\balGroEndog = \dot{\KLvl}/\KLvl`,
this equation implies that

```{math}
:label: eq:Rebelo-CKRatio

\begin{gathered}\begin{aligned}
  \CLvl/\KLvl & =  \PtyAgg - \balGroEndog.
\end{aligned}\end{gathered}
```

This is a model with a constant saving rate, because

```{math}
:label: eq:Rebelo-savRte

\begin{gathered}\begin{aligned}
  \SLvl/\PtyAgg\KLvl & =  (\PtyAgg\KLvl - \CLvl)/\PtyAgg\KLvl
\\ & =  1 - \PtyAgg^{-1} (\CLvl/\KLvl)
\\ & =  \balGroEndog/\PtyAgg
\\ \balGroEndog & =  \PtyAgg (\SLvl/\PtyAgg\KLvl).
\end{aligned}\end{gathered}
```

Thus, the steady-state growth rate in a Rebelo economy is
directly proportional to the saving rate. A Rebelo economy is the constant-returns {math}`\PtyAgg\KLvl` case of the [generic analysis of endogenous growth](#sec:Endogenous), which assumed a constant saving rate; here the planner chooses the saving rate, and it is constant.

A further requirement for the Rebelo model to have a well-defined
solution is that

```{math}
:label: eq:rebelo-impatience

\begin{gathered}\begin{aligned}
  \CRRA^{-1}(\PtyAgg-\discRte) & <  \PtyAgg.
\end{aligned}\end{gathered}
```

Recalling that {math}`\PtyAgg` is effectively the real interest rate
in this model, this equation can be interpreted as the
[return impatience condition](#eq:PatR) that we imposed in the infinite
horizon perfect foresight consumption model. Since consumption and capital grow at the same rate in the steady state, {math}`\balGroEndog = \CRRA^{-1}(\PtyAgg-\discRte)`, it is also the requirement that the economy grow more slowly than the interest rate, {math}`\balGroEndog < \rfree`, which keeps consumption positive and is what the [transversality condition](#eq:tvc) requires. In fact,
the Rebelo {math}`\PtyAgg\KLvl` model is essentially just a way of
reinterpreting the [perfect foresight infinite horizon
consumption problem](#sec:PerfForesightCRRA) as a model for economic growth.

The principal distinction is that we usually use the
perfect foresight infinite horizon model to analyze
circumstances where the agent has both labor and
capital income, whereas the Rebelo model rules out
labor income by assumption.
