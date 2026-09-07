(sec:Endogenous)=
# Generic Analysis of Endogenous Growth Models

The neoclassical theory of economic growth, as formulated
by Solow

:::{margin}
Why did Solow make the CRS assumption? CRS was required for perfect competition w/o externalities.
:::

 {cite:t}`solow:contribution`, and {cite:t}`cass:growth`-{cite:t}`koopmans:growth`, attributes virtually all long-run growth to technological

progress. The level of technology is taken to be an exogenously
growing factor outside the model. So the baseline model of growth
says that growth is caused mostly by a factor that is not in the model.

It is important to understand why Solow and others made this
assumption. The answer is that models of perfect competition
are the simplest existing models of firm behavior, with
well-understood implications.

:::{margin}
In a framework with constant returns to scale, perfect competition, and no externalities, it is impossible to incorporate an economic theory of {math}`g`, because all income is exhausted by payments to {math}`K` and {math}`L`.
:::

But models with perfect competition require
constant returns to scale, and say that all factors of production are
paid their marginal product; and [Euler's Theorem](#fact:eulerstheorem) says that the sum of the factor payments
exhausts all output:

```{math}
:label: eq:EulersTheorem

\begin{gathered}\begin{aligned}
  Y & =  F_K K + F_L L.
\end{aligned}\end{gathered}
```

Thus, the perfectly competitive firm has no money left over with which
to finance basic research, invent patentable technologies, or do anything
other than meet the payroll of production workers and pay the cost of
capital. Thus, no firm can afford to pay for technological research,
and there is therefore no alternative to the assumption that
technological progress occurs exogenously.

This unsatisfactory situation persisted for a long time, but a famous
paper by Paul {cite:t}`romer:growth` led the way to the formulation
of a new generation of models that allow a role for investment in
knowledge to affect growth.

The Romer paper spawned a great deal of further theoretical work by
a host of others, but a penetrating
paper by Sergio {cite:t}`rebelo:long` provided a succinct summary
of the key feature of all of these models. This section summarizes
the Rebelo point as interpreted by Barro and Sala-i-Martin
{cite:t}`barro&salaimartin:book`.

## The Key Point

Rebelo's key observation is as follows. Consider the class of models
with a Cobb-Douglas aggregate production function in capital and labor:

```{math}
:label: eq:prodfn

\begin{gathered}\begin{aligned}
  Y_t & =  A K_t^\kapShare L_t^\labShare
\end{aligned}\end{gathered}
```

where no restriction is made on the {math}`\labShare` and {math}`\kapShare` coefficients.

(Recall that Solow, Cass, and Koopmans all assumed {math}`\labShare+\kapShare=1`;

Rebelo is relaxing this restriction). Now suppose for simplicity that
in this economy saving is a constant proportion of gross income.

In continuous time, the growth of the capital stock is given by

```{math}
:label: eq:Endo-dbc

\begin{gathered}\begin{aligned}
  \dot{K}_t & =  s A K_t^\kapShare L_t^\labShare - \delta K_t.
\end{aligned}\end{gathered}
```

Suppose further that population growth is constant at

```{math}
:label: eq:n

\begin{gathered}\begin{aligned}
  \dot{L}_t/L_t & =  \popGro,
\end{aligned}\end{gathered}
```

and as usual define per-capita variables as the aggregate normalized
by population, e.g. {math}`k_t = K_t/L_t`. Then the aggregate per-capita accumulation
equation can be rewritten

```{math}
:label: eq:dbcpc

\begin{gathered}\begin{aligned}
  \dot{k}_t & =  s A k_t^\kapShare L^{\labShare+\kapShare-1}_t - (\delta+\popGro) k_t
\\ \dot{k}_{t}/k_{t} & =  s A k_{t}^{\kapShare-1} L^{\labShare+\kapShare-1}_{t}-(\delta+\popGro) .  
\end{aligned}\end{gathered}
```

## Characteristics of the Steady State

If this model has a steady-state growth rate, that rate must
satisfy

```{math}
:label: eq:ss

\begin{gathered}\begin{aligned}
  \dot{k}_t / k_t & =  \gamma
\end{aligned}\end{gathered}
```

for some constant {math}`\gamma`. (The value of {math}`A` does not affect the conclusions
from here on, and so we will assume without loss of generality that {math}`A=1`). From {eq}`eq:dbcpc`, this implies
that

```{math}
:label: eq:gdyn

\begin{gathered}\begin{aligned}
  \gamma & =  s k_t^{\kapShare-1} L^{\labShare+\kapShare-1}_t - (\delta+\popGro). 
\end{aligned}\end{gathered}
```

Take the time derivative of this equation to obtain

```{math}
:label: eq:AKeqn

\begin{gathered}\begin{aligned}
  0 & =  s\left((\kapShare-1)k_t^{\kapShare-2}\dot{k}_t L_t^{\labShare+\kapShare-1}+k_t^{\kapShare-1}(\labShare+\kapShare-1)\dot{L}_t L_t^{\labShare+\kapShare-2}\right)
\\  & =  k_{t}^{\kapShare-1}L_{t}^{\labShare+\kapShare-1}\left((\kapShare-1)\dot{k}_t/k_{t} +(\labShare+\kapShare-1)(\dot{L}_t/L_t)\right)
\\ 0 & =  (\kapShare-1) \dot{k}_t/k_t + (\dot{L}_t/L_t) (\labShare+\kapShare-1)
\\   & =  (\kapShare-1) \gamma + \popGro (\labShare+\kapShare-1). 
\end{aligned}\end{gathered}
```

Using this equation, we can construct a complete catalog of the
possible circumstances under which steady-state growth {math}`\gamma` can
be different from zero endogenously.

### Possibilities for Steady State Growth

1.  {math}`\labShare+\kapShare = 1` (Constant Returns Models)

    1.  {math}`\{\labShare, \kapShare\} < 1 \rightarrow \gamma = 0` (Solow case)

        :::{margin}
        In the Solow case {math}`\kapShare = 1-\labShare`, so the second term in {eq}`eq:AKeqn` vanishes.
        :::

    2.  {math}`\labShare = 0, \kapShare = 1`: {cite:t}`rebelo:long` {math}`AK` growth model

2.  {math}`\labShare+\kapShare > 1` (Increasing Returns Models)

    1.  {math}`\{\labShare, \kapShare\} < 1`

        1.  {math}`\popGro > 0 \rightarrow \gamma = \overbrace{\left(\frac{\labShare+\kapShare-1}{(1-\kapShare)}\right)}^{>0} \popGro`

            :::{margin}
            2.a.i.: Growth in per capita incomes faster the faster is pop growth. Exact opposite of facts.
            :::

        2.  {math}`\popGro = 0 \rightarrow \gamma = 0`

    2.  {math}`\labShare>0, \kapShare = 1`

        1.  {math}`\popGro>0 \rightarrow 0 = \popGro(\labShare+\kapShare-1)` which is not satisfied for any {math}`\gamma`

            :::{margin}
            Steady-state growth is impossible when {math}`\labShare+\kapShare \neq 1` and {math}`\popGro \neq 0`.
            :::

        2.  {math}`\popGro=0 \rightarrow 0 = 0` which can be satisfied for any {math}`\gamma`

So whatever the details of endogenous growth models may be, in the end
any model that generates perpetual growth without exogenous
technological progress must be mathematically reducible to a form like
that of either 1.b., 2.a.i., or 2.b.ii.

It is worth delving a bit further into why the Solow case cannot
generate perpetual growth. The answer can be understood using
the Solow growth accounting framework, which says that there are only three sources
of long-run growth: technology, labor, and capital. Thus, there are only
two potential sources of growth of output per unit of labor: Technology
and an increase in the capital/labor ratio. But if {math}`\kapShare < 1`,
the gross marginal product of capital approaches zero as the capital/labor
ratio approaches infinity; subtracting out depreciation, eventually the
net marginal product of capital becomes negative. Thus, capital accumulation
can sustain growth only so long.

The bottom line is that there are only two configurations of the model
that are capable of generating perpetual growth in a way that makes any
sense: 1.b. (the Rebelo {math}`AK` model) and 2.a.ii.

:::{margin}
Case 2.a.ii, the increasing-returns growth models, is taken up in the [Romer (1986) model](#sec:Romer86) section.
:::

What this means is that any model that aims to permit perpetual
long-run growth must ultimately boil down to a structure in which
there are constant returns to scale for some set of factors of
production that can jointly be accumulated forever.
