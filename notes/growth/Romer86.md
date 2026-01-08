(sec:Romer86)=

# The Romer (1986) Model of Growth

{cite:t}`romer:growth` relaunched the growth literature with a paper that

presented a model of increasing returns in which there was a stable

positive equilibrium growth rate that resulted from endogenous accumulation

of knowledge. This was an important break with the existing literature,

in which technological progress had largely been treated as completely

exogenous.[^nAMCrIHY0T]

[^nAMCrIHY0T]: See also the prescient paper by {cite:t}`arrowGrowth`; Afred Marshall articulated similar ideas in the late 19th century.

In Romer’s model, firm {math}`j`’s production function is of the form

```{math}
\begin{gathered}\begin{aligned}
  y_{t,j} & =  \PtyLev_{t} \FFunc(\kap_{t,j},\ell_{t,j})
\end{aligned}\end{gathered}
```

where aggregate output-augmenting technological progress is captured by

{math}`\PtyLev_{t}`. Its capital accumulates without depreciation,

```{math}
:label: eq:Kdot

\begin{gathered}\begin{aligned}
  
  \dot{\kap}_{t,j} & =  i_{t,j}.
\end{aligned}\end{gathered}
```

Firms and individuals are distributed along the unit interval with a total mass of 1,

as in [](#sec:Aggregation) (and,

importantly, there is no population growth). Thus, aggregate investment is, e.g.,

```{math}
:label: eq:Romer-1

\begin{gathered}\begin{aligned}

  I_{t} & =  \int_{0}^{1} i_{t,j} dj
.
\end{aligned}\end{gathered}
```

Romer assumes that the aggregate stock of knowledge in the economy is

proportional to the cumulative sum of past aggregate investment

```{math}
\begin{gathered}\begin{aligned}
  \Xi_{t} & =   \int_{-\infty}^{t} I_v dv 
\end{aligned}\end{gathered}
```

which, not coincidentally, is identical to the size of the aggregate capital stock,

```{math}
\begin{gathered}\begin{aligned}
  K_{t} & =   \int_{-\infty}^{t} I_v dv .
\end{aligned}\end{gathered}
```

Romer makes the crucial assumption that the effect of the stock of knowledge determines

productivity via

```{math}
\begin{gathered}\begin{aligned}
  \PtyLev_{t} & =  \Xi_{t}^{\eta}
\end{aligned}\end{gathered}
```

where {math}`\eta < 1`. Thus, suppressing the {math}`t` subscript, the firm-level

Cobb-Douglas production function can be written

```{math}
\begin{gathered}\begin{aligned}
  y_{j} & =  \kap_{j}^{\kapShare}\ell_{j}^{1-\kapShare}\Xi^{\eta}
\end{aligned}\end{gathered}
```

which is CRS at the firm level in {math}`(k,\ell)` holding aggregate knowledge {math}`\Xi` fixed.

Aggregate output is

```{math}
\begin{gathered}\begin{aligned}
  \YLev & =  {\Kap}^\kapShare \Labor^{1-\kapShare} \Xi^{\eta}
\end{aligned}\end{gathered}
```

Dividing by the size of the labor force {math}`L` (or, equivalently, normalizing to {math}`L=1`), we have

```{math}
\begin{gathered}\begin{aligned}
  \yRat & =  k^{\kapShare}\Xi^{\eta}.
\end{aligned}\end{gathered}
```

Now assume that households maximize a typical CRRA utility function,

but each household ignores the trivial effect its own investment

decision has on aggregate knowledge. Thus from the individual

firm/consumer’s perspective, the marginal product of capital is

{math}`\kapShare \kap_{t,i}^{\kapShare-1}
 \ell_{t,i}^{1-\kapShare}\Xi_{t}^{\eta}`. If we normalize the model by

assuming that the aggregate quantity of labor adds upt to {math}`L_{t}=1`,

we can set up and solve the Hamiltonian to obtain

```{math}
\begin{gathered}\begin{aligned}
  \dot{c}_{t,i}/c_{t,i} & =  \CRRA^{-1}(\kapShare \kap_{t,i}^{\kapShare-1} \Xi_{t}^{\eta} - \timeRate).
\end{aligned}\end{gathered}
```

But if all households are identical and {math}`\Xi_{t}=K_{t}`, this means that aggregate consumption

per capita evolves according to

```{math}
\begin{gathered}\begin{aligned}
  \dot{c}_{t}/c_{t} & =  \CRRA^{-1}(\kapShare \kap_{t}^{\kapShare-1}\Xi_{t}^{\eta}  - \timeRate)
\\  & =  \CRRA^{-1}(\kapShare \kap_{t}^{\kapShare+\eta-1}  - \timeRate).
\end{aligned}\end{gathered}
```

A balanced growth path can occur in this economy if {math}`\kapShare+\eta=1`, in which case

```{math}
\begin{gathered}\begin{aligned}
  \dot{c}_{t}/c_{t} & =  \CRRA^{-1}(\kapShare  - \timeRate)
\end{aligned}\end{gathered}
```

so there is constant growth forever at a rate that depends on the degree

of impatience and capital’s share in output.

Note finally that the steady-state growth rate that would be chosen by the

social planner is

```{math}
\begin{gathered}\begin{aligned}
  \dot{c}_{t}/c_{t} & =  \CRRA^{-1}(\kapShare +\eta - \timeRate),
\end{aligned}\end{gathered}
```

because the social planner would take into account the fact that

the externalities imply that there are higher returns to capital

accumulation at the social level than at the individual level.

Thus, this model implies that capital accumulation should be subsidized

if the social planner wants to induce the private economy to move toward

the social optimum.


:::{admonition} Scraps/draft material
:class: dropdown

Households maximize a typical CRRA utility function subject to the usual capital accumulation equation

:::{margin}

Again, no pop growth
:::

```{math}
\begin{gathered}\begin{aligned}
  \dot{\kap}_{t} & =  \kap_{t}^{\kapShare}\Xi_{t}^{\eta} - c_t
\end{aligned}\end{gathered}
```

Households now solve this problem but each individual household ignores the
fact that their own saving decision has an effect on aggregate capital
and therefore interest rates and wages.

Setting up and solving the Hamiltonian optimization problem gives the first order
condition yields

```{math}
\begin{gathered}\begin{aligned}
  \dot{c}/c & =   \CRRA^{-1}[\kapShare \kap_{t}^{(\kapShare-1)+\eta }\Labor^{\eta} - \timeRate]c
\end{aligned}\end{gathered}
```

Assume that the number of opin
:::