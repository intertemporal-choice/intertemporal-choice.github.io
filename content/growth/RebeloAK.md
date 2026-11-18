(sec:RebeloAK)=
# The Rebelo AK Growth Model

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

This problem can be solved with the same Hamiltonian apparatus we used
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
capital in this model is always {math}`\PtyAgg = \rfree`, because {math}`\fFunc^{\prime}(\KLvl) = \PtyAgg`. Note
further that according to this equation, the growth rate of consumption
is always the same; unlike the Cass-Koopmans model with a normal
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
:label: eq:Rebelo-1

\begin{gathered}\begin{aligned}
  \CLvl/\KLvl & =  \PtyAgg - \balGroEndog.
\end{aligned}\end{gathered}
```

This is a model with a constant saving rate, because

```{math}
:label: eq:Rebelo-2

\begin{gathered}\begin{aligned}
  \SLvl/\PtyAgg\KLvl & =  (\PtyAgg\KLvl - \CLvl)/\PtyAgg\KLvl
\\ & =  1 - \PtyAgg^{-1} (\CLvl/\KLvl)
\\ & =  \balGroEndog/\PtyAgg
\\ \balGroEndog & =  \PtyAgg (\SLvl/\PtyAgg\KLvl).
\end{aligned}\end{gathered}
```

Thus, the steady-state growth rate in a Rebelo economy is
directly proportional to the saving rate.

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
'impatience' condition that we imposed in the infinite
horizon perfect foresight consumption model. In fact,
the Rebelo {math}`\PtyAgg\KLvl` model is essentially just a way of
reinterpreting the perfect foresight infinite horizon
consumption problem as a model for economic growth.

The principal distinction is that we usually use the
perfect foresight infinite horizon model to analyze
circumstances where the agent has both labor and
capital income, whereas the Rebelo model rules out
labor income by assumption.
