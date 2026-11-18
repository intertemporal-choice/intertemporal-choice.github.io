(sec:Romer86)=
# The Romer (1986) Model of Growth

{cite:t}`romer:growth` relaunched the growth literature with a paper that
presented a model of increasing returns in which there was a stable
positive equilibrium growth rate that resulted from endogenous accumulation
of knowledge. This was an important break with the existing literature,
in which technological progress had largely been treated as completely
exogenous.

:::{margin}
See also the prescient paper by {cite:t}`arrowGrowth`; Afred Marshall articulated similar ideas in the late 19th century.
:::

In Romer's model, firm {math}`j`'s production function is of the form

```{math}
\begin{gathered}\begin{aligned}
  \yNrm_{j,t} & =  \PtyAgg_{t} \FFunc(\kNrm_{j,t},\labor_{j,t})
\end{aligned}\end{gathered}
```

where aggregate output-augmenting technological progress is captured by
{math}`\PtyAgg_{t}`. Its capital accumulates without depreciation,

```{math}
:label: eq:Kdot

\begin{gathered}\begin{aligned}
  \dot{\kNrm}_{j,t} & =  \iNrm_{j,t}.
\end{aligned}\end{gathered}
```

Firms and individuals are distributed along the unit interval with a total mass of 1,
as in the [Aggregation](#sec:Aggregation) appendix (and,
importantly, there is no population growth). Thus, aggregate investment is, e.g.,

```{math}
:label: eq:Romer-1

\begin{gathered}\begin{aligned}
  \ILvl_{t} & =  \int_{0}^{1} \iNrm_{j,t} dj
.
\end{aligned}\end{gathered}
```

Romer assumes that the aggregate stock of knowledge in the economy is
proportional to the cumulative sum of past aggregate investment

```{math}
\begin{gathered}\begin{aligned}
  \Knwl_{t} & =   \int_{-\infty}^{t} \ILvl_{\tau} d\tau 
\end{aligned}\end{gathered}
```

which, not coincidentally, is identical to the size of the aggregate capital stock,

```{math}
\begin{gathered}\begin{aligned}
  \KLvl_{t} & =   \int_{-\infty}^{t} \ILvl_{\tau} d\tau .
\end{aligned}\end{gathered}
```

Romer makes the crucial assumption that the effect of the stock of knowledge determines
productivity via

```{math}
\begin{gathered}\begin{aligned}
  \PtyAgg_{t} & =  \Knwl_{t}^{\extElas}
\end{aligned}\end{gathered}
```

where {math}`\extElas < 1`. Thus, suppressing the {math}`t` subscript, the firm-level
Cobb-Douglas production function can be written

```{math}
\begin{gathered}\begin{aligned}
  \yNrm_{j} & =  \kNrm_{j}^{\kapShare}\labor_{j}^{1-\kapShare}\Knwl^{\extElas}
\end{aligned}\end{gathered}
```

which is CRS at the firm level in {math}`(\kNrm,\labor)` holding aggregate knowledge {math}`\Knwl` fixed.

Aggregate output is

```{math}
\begin{gathered}\begin{aligned}
  \YLvl & =  {\KLvl}^\kapShare \LLvl^{1-\kapShare} \Knwl^{\extElas}
\end{aligned}\end{gathered}
```

Dividing by the size of the labor force {math}`\LLvl` (or, equivalently, normalizing to {math}`\LLvl=1`), we have

```{math}
\begin{gathered}\begin{aligned}
  \yNrm & =  \kNrm^{\kapShare}\Knwl^{\extElas}.
\end{aligned}\end{gathered}
```

Now assume that households maximize a typical CRRA utility function,
but each household ignores the trivial effect its own investment
decision has on aggregate knowledge. Thus from the individual
firm/consumer's perspective, the marginal product of capital is
{math}`\kapShare \kNrm_{j,t}^{\kapShare-1}
 \labor_{j,t}^{1-\kapShare}\Knwl_{t}^{\extElas}`. If we normalize the model by
assuming that the aggregate quantity of labor adds upt to {math}`\LLvl_{t}=1`,
we can set up and solve the Hamiltonian to obtain

```{math}
\begin{gathered}\begin{aligned}
  \dot{\cNrm}_{j,t}/\cNrm_{j,t} & =  \CRRA^{-1}(\kapShare \kNrm_{j,t}^{\kapShare-1} \Knwl_{t}^{\extElas} - \discRte).
\end{aligned}\end{gathered}
```

But if all households are identical and {math}`\Knwl_{t}=\KLvl_{t}`, this means that aggregate consumption
per capita evolves according to

```{math}
\begin{gathered}\begin{aligned}
  \dot{\cNrm}_{t}/\cNrm_{t} & =  \CRRA^{-1}(\kapShare \kNrm_{t}^{\kapShare-1}\Knwl_{t}^{\extElas}  - \discRte)
\\  & =  \CRRA^{-1}(\kapShare \kNrm_{t}^{\kapShare+\extElas-1}  - \discRte).
\end{aligned}\end{gathered}
```

A balanced growth path can occur in this economy if {math}`\kapShare+\extElas=1`, in which case

```{math}
\begin{gathered}\begin{aligned}
  \dot{\cNrm}_{t}/\cNrm_{t} & =  \CRRA^{-1}(\kapShare  - \discRte)
\end{aligned}\end{gathered}
```

so there is constant growth forever at a rate that depends on the degree
of impatience and capital's share in output.

Note finally that the steady-state growth rate that would be chosen by the
social planner is

```{math}
\begin{gathered}\begin{aligned}
  \dot{\cNrm}_{t}/\cNrm_{t} & =  \CRRA^{-1}(\kapShare +\extElas - \discRte),
\end{aligned}\end{gathered}
```

because the social planner would take into account the fact that
the externalities imply that there are higher returns to capital
accumulation at the social level than at the individual level.

Thus, this model implies that capital accumulation should be subsidized
if the social planner wants to induce the private economy to move toward
the social optimum.
