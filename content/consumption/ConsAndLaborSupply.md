(sec:ConsAndLaborSupply)=

# Consumption and Labor Supply

Consider a consumer who has a utility function

```{math}
\uFunc(c_{t},\leisure_{t})
```

where {math}`\leisure_{t}` is leisure (mnemonic: {math}`z` for laZiness) and {math}`c_{t}` is consumption. Normalize the maximum possible labor supply to {math}`1`; actual labor supply is {math}`\labor_{t}`, so that

```{math}
\labor_{t} + \leisure_{t} = 1.
```

The wage earned for working one unit of time is {math}`\Wage_{t}`, and labor income is the wage rate multiplied by the amount of labor supplied,

```{math}
\begin{aligned}
y_{t} & = \Wage_{t}\labor_{t} \\
& = (1-\leisure_{t})\Wage_{t}.
\end{aligned}
```

Suppose the consumer has a fixed amount {math}`x_{t}` to spend in period {math}`t` on consumption and leisure,

```{math}
:label: eq:xdef

x_{t} = c_{t}+\leisure_{t} \Wage_{t},
```

where {math}`x_{t}` can differ from income {math}`y_{t}` because this might be a single period in a multi-period problem.

The price of leisure is {math}`\Wage_{t}` (your income is lower by this amount for every extra unit of time you spend not working) and the price of consumption is 1, so the first order condition from the optimal choice of leisure says that the ratio of the marginal utility of leisure to the marginal utility of consumption should be

:::{exercise}
:label: ex:foc-derive
Derive and explain the first order condition
:::

:::{solution} ex:foc-derive
:class: dropdown
The price of leisure is {math}`\Wage_{t}` (your income is lower by this amount for every extra unit of time you spend not working) and the price of consumption is 1, so the first order condition from the optimal choice of leisure says that the ratio of the marginal utility of leisure to the marginal utility of consumption should be

```{math}
:label: eq:CLS-focwucul

\Wage_{t} = \left(\frac{\uFunc^{\leisure}}{\uFunc^{c}}\right).
```

To see this formally, note that the consumer's goal is to

```{math}
:label: eq:CLS-intramax

\max_{\{c_{t},\leisure_{t}\}} \uFunc(c_{t},\leisure_{t})
```

subject to a budget constraint

```{math}
:label: eq:lifebudget

c_{t} = x_{t}-\Wage_{t}\leisure_{t}
```

so {eq}`eq:CLS-intramax` becomes

```{math}
:label: eq:CLS-intramax2

\max_{\{ \leisure_{t} \}} \uFunc(x_{t}-\Wage_{t}\leisure_{t},\leisure_{t})
```

for which the FOC is

```{math}
\begin{aligned}
- \uFunc^{c}\Wage_{t} + \uFunc^{\leisure} & = 0 \\
\Wage_{t} & = (\uFunc^{\leisure}/\uFunc^{c}).
\end{aligned}
```

This is just the classic condition that says that the ratio of prices of two goods should equal the ratio of their marginal utilities, which applies in any standard microeconomic problem. For a quantitative comparison of how this condition manifests itself in the U.S. and Europe, see {cite:t}`zwiebelLeisure`.
:::

Now, assume there is an "outer" utility function {math}`{f}(\bullet)` which depends on a Cobb-Douglas aggregate of consumption and leisure

```{math}
\uFunc(c_{t},\leisure_{t}) = {f}\left(c_{t}^{1-\leiShare}\leisure_{t}^{\leiShare}\right)
```

:::{exercise}
:label: ex:cobb-douglas
Show that
:::

:::{solution} ex:cobb-douglas
:class: dropdown
The inner function has the property that {math}`\leisure_{t} \Wage_{t} = c_{t} \eta` for {math}`\eta=\leiShare/(1-\leiShare)`, which implies utility can be written

```{math}
{f}((\Wage_{t}/\eta)^{-\leiShare}c_{t}).
```

To see this, note that the maximization problem is

```{math}
\max_{\leisure_{t}} {f}\left((x_{t}-\leisure_{t}\Wage_{t})^{1-\leiShare}\leisure_{t}^{\leiShare}\right)
```

FOC:

```{math}
:label: eq:23

\begin{aligned}
(1-\leiShare) \Wage_{t}(x_{t}-\leisure_{t}\Wage_{t})^{-\leiShare}\leisure_{t}^{\leiShare}{f}^{\prime} & = \leiShare (x_{t}-\leisure_{t}\Wage_{t})^{1-\leiShare}\leisure_{t}^{\leiShare-1}{f}^{\prime} \\
\Wage_{t} \leisure_{t} & = c_{t} \underbrace{\leiShare/(1-\leiShare)}_{\equiv \eta}
\end{aligned}
```

so

```{math}
:label: eq:CLS-5

\begin{aligned}
{f}(c_{t}^{1-\leiShare}\leisure_{t}^{\leiShare}) & = {f}(c_{t}^{1-\leiShare}(\eta c_{t}/\Wage_{t})^{\leiShare}) \\
& = {f}((\Wage_{t}/\eta)^{-\leiShare}c_{t})
\end{aligned}
```
:::

Over long periods of time as wages have risen in the U.S., the proportion of time spent working has not changed very much (an old stylized fact recently reconfirmed by {cite:t}`rameyFrancisLeisure`). Similarly, across countries with vastly different levels of per capita income, or across people with vastly different levels of wages, the amount of variation in {math}`\leisure_{t}` is small compared to the size of the difference in wages.

These facts motivate the choice of utility function; {cite:t}`kpr:prodn` show that other choices of utility functions produce trends, but no such trends are evident in the data.

:::{exercise}
:label: ex:trends-leisure
Explain how these facts motivate the choice of utility function; {cite:t}`kpr:prodn` show that other choices of utility functions produce trends, but no such trends are evident in the data. Hint: To see why the trends are produced, think about a model in which the lifetime lasts only a single period, with a lifetime budget constraint {math}`\Wage_{t} = c_{t}+\leisure_{t}\Wage_{t}`.
:::

:::{solution} ex:trends-leisure
:class: dropdown
Using the hint along with the result, we can solve for the level of consumption over the lifetime as

```{math}
\begin{aligned}
\Wage_{t} & = (1+\eta)c_{t} \\
c_{t} & = \Wage_{t}/(1+\eta)
\end{aligned}
```

implying that leisure is

```{math}
\begin{aligned}
\leisure_{t} & = \eta c_{t}/\Wage_{t} \\
& = \eta/(1+\eta)
\end{aligned}
```

which is a constant (i.e. the amount of leisure does not trend up or down with the level of wages). Obviously this is what motivates the choice of an "inner" utility function that is Cobb-Douglas: For such a function, people will choose to spend constant proportions of their resources on consumption and leisure as wages rise.
:::

Now consider a two period lifetime version of the model in which each period of life is characterized by a utility function of the same form and the lifetime optimization problem is

```{math}
:label: eq:26

\max \uFunc(c_{1},\leisure_{1}) + \DiscFac \uFunc(c_{2},\leisure_{2})
```

subject to a lifetime budget constraint

```{math}
:label: eq:DBC

c_{2} = (\Wage_{1}(1-\leisure_{1})-c_{1})\Rfree + (1-\leisure_{2}) \Wage_{2}
```

If the "outer" utility function is of the CRRA form {math}`{f}(\chi) = \chi^{1-\CRRA}/(1-\CRRA)` then the FOC with respect to {math}`c_{1}` implies that

```{math}
\begin{aligned}
(\Wage_{1}/\eta)^{-\leiShare} {f}^{\prime}_{1} & = \Rfree \DiscFac (\Wage_{2}/\eta)^{-\leiShare} {f}^{\prime}_{2} \\
\Wage_{1}^{-\leiShare} (c_{1}(\Wage_{1}/\eta)^{-\leiShare})^{-\CRRA} & = \Rfree\DiscFac \Wage_{2}^{-\leiShare} (c_{2}(\Wage_{2}/\eta)^{-\leiShare})^{-\CRRA} \\
\Wage_{1}^{-\leiShare(1-\CRRA)} c_{1}^{-\CRRA} & = \Rfree\DiscFac \Wage_{2}^{-\leiShare(1-\CRRA)} c_{2}^{-\CRRA} \\
c_{2}/c_{1} & = (\Rfree\DiscFac)^{1/\CRRA} (\Wage_{2}/\Wage_{1})^{-\leiShare(1-\CRRA)/\CRRA}
\end{aligned}
```

:::{exercise}
:label: ex:log-utility
Show that this implies that {math}`c_{2}/c_{1} = \Rfree\DiscFac`. To see why, start by noting that the budget constraint can be rewritten
:::

:::{solution} ex:log-utility
:class: dropdown
```{math}
\begin{aligned}
c_{2} & = (\Wage_{1}-\overbrace{\leisure_{1}\Wage_{1}}^{=\eta c_{1}}-c_{1})\Rfree + \Wage_{2} - \overbrace{\Wage_{2}\leisure_{2}}^{\eta c_{2}} \\
0 & = (\Wage_{1}-(1+\eta) c_{1})R+\Wage_{2}-(1+\eta) c_{2} \\
c_{2} & = (\Rfree \Wage_{1}+\Wage_{2})/(1+\eta)- \Rfree c_{1}
\end{aligned}
```

so the lifetime optimization problem becomes

```{math}
\max_{c_{1}} \left\{\log c_{1}-\leiShare \log \Wage_{1} + \DiscFac \left(\log c_{2} - \leiShare \log \Wage_{2} \right)\right\}
```

with FOC

```{math}
\begin{aligned}
1/c_{1} & = \Rfree \DiscFac / c_{2} \\
c_{2}/c_{1} & = \Rfree\DiscFac.
\end{aligned}
```
:::

:::{exercise}
:label: ex:solve-consumption
Use IBC to solve for the level of consumption {math}`c_{1}`
:::

:::{solution} ex:solve-consumption
:class: dropdown
```{math}
\begin{aligned}
PD\VFunc_{1}(c) & = c_{1}(1+R^{-1}(\Rfree \DiscFac)) \\
& = c_{1}(1+\DiscFac)
\end{aligned}
```

```{math}
\begin{aligned}
PD\VFunc_{1}(y) & = \Wage_{1}(1-\leisure_{1}) + R^{-1}(\Wage_{2}(1-\leisure_{2})) \\
& = \Wage_{1}+R^{-1}\Wage_{2}-\eta (c_{1}+R^{-1} c_{2})
\end{aligned}
```

```{math}
\begin{aligned}
PD\VFunc_{1}(c) & = PD\VFunc_{1}(y) \\
c_{1}(1+\DiscFac)(1+\eta) & = \Wage_{1}+R^{-1}\Wage_{2} \equiv h_{1} \\
c_{1} & = h_{1}/((1+\DiscFac)(1+\eta))
\end{aligned}
```
:::

:::{exercise}
:label: ex:fisherian-separation
Show that in this model, the profile of labor supply satisfies
```{math}
(1-\labor_{2})/(1-\labor_{1}) = \Rfree\DiscFac \Wage_{1}/\Wage_{2}
```
and explain why this makes sense in economic terms.
:::

:::{solution} ex:fisherian-separation
:class: dropdown
```{math}
:label: eq:LabSup

\begin{aligned}
\Wage_{2} \leisure_{2}/\Wage_{1}\leisure_{1} & = \eta c_{2}/\eta c_{1} = \Rfree\DiscFac \\
\leisure_{2}/\leisure_{1} & = \Rfree\DiscFac \Wage_{1}/\Wage_{2} \\
(1-\labor_{2})/(1-\labor_{1}) & = \Rfree\DiscFac \Wage_{1}/\Wage_{2}
\end{aligned}
```
so leisure moves in the opposite direction from wages, which means labor supply {math}`\labor = 1-z` moves in the same direction as wages. This makes intuitive sense: You want to work harder when work pays better.
:::

To make further progress, assume {math}`\Rfree\DiscFac=1` and define wage growth as {math}`\WGro=\Wage_{2}/\Wage_{1}=(1+\wGro)`. Assume that young people tend to work about half of their waking hours {math}`\labor_{1}=(1/2)` (remember vacations, weekends, etc!).

:::{exercise}
:label: ex:rewrite-labsup
Show that under these assumptions we can rewrite {eq}`eq:LabSup` as
```{math}
\labor_{2} = (2 \wGro + 1)/2(1+\wGro)
```
:::

:::{solution} ex:rewrite-labsup
:class: dropdown
```{math}
\begin{aligned}
(1-\labor_{2})\WGro & = (1-\labor_{1}) \\
\wGro & = (1+\wGro) \labor_{2} - \labor_{1} \\
\labor_{2} & = (\wGro + \labor_{1})/(1+\wGro) \\
& = (2 \wGro + 1)/2(1+\wGro)
\end{aligned}
```
:::

Empirically, wages in the U.S. tend to grow between youth and middle age by a factor of {math}`\WGro \approx 2-4` (depending on occupation and education), so {math}`\wGro \approx 1-3`, but labor supply is about the same for 55 year olds as for 25 year olds, {math}`\labor_{2} \approx \labor_{1}`.

:::{exercise}
:label: ex:wgro-2
Suppose for analysis that {math}`\wGro=2`. Discuss the consistency of the theory with this evidence.
:::

:::{solution} ex:wgro-2
:class: dropdown
Suppose for analysis that {math}`\wGro=2`. Then {eq}`eq:LabSup` becomes
```{math}
\labor_{2} = (5/6)
```
so the theory says middle aged people work more than young people by {math}`(2/6)/(3/6)=2/3`. This is of course absurd - it implies that middle aged people would barely have time to breathe because they were working so hard.
:::

One objection to this analysis is that it assumed {math}`\Rfree\DiscFac=1`, which implies that consumption when young equals consumption when middle aged. In fact, on average consumption grows by about the same amount as wages between youth and middle age. So perhaps the right assumption is {math}`\Rfree\DiscFac/\WGro = 1`. Under this assumption, we obviously have {math}`\labor_{2}=\labor_{1}`, matching the empirical fact.

However, there is predictably different wage growth across occupations and education groups. Write {math}`\WGro_{i}=\WGro\Gamma_{i}`, where {math}`\Gamma_{i}` now will differ for people in different occupations indexed by {math}`i`, and plausible values range from {math}`\Gamma=0.5` (manual laborers) to {math}`\Gamma=1.5` (doctors), leaving the average value of {math}`\Gamma` across the two groups at {math}`\Gamma=1`. It is an empirical fact that the magnitude of variations in labor supply across these groups is rather small, both in youth and in middle age.

:::{exercise}
:label: ex:varying-categories
Assuming {math}`\Rfree\DiscFac/\WGro=1`, discuss whether the theory can now explain this fact.
:::

:::{solution} ex:varying-categories
:class: dropdown
rewrite {eq}`eq:LabSup` for each occupation as
```{math}
(1-\labor_{2})\Gamma_{i} = (1-\labor_{1})
```

For {math}`\Gamma_{i}=0.5`, if {math}`\labor_{1} = 1/2` we have
```{math}
(1-\labor_{2})0.5 = 1/2
```
implying {math}`\labor_{2} = 0` - manual laborers would work zero hours. However, if {math}`\Gamma=1.5` so that
```{math}
\begin{aligned}
(1-\labor_{2}) (3/2) & = 1/2 \\
(1-\labor_{2}) 3 & = 1 \\
\labor_{2} & = 2/3
\end{aligned}
```
so doctors would be working much harder when middle aged than when young. Thus, the theory says that if labor supplies are equal when young (which is approximately true), they should differ drastically by middle age (which is not remotely true). That is, lifetime labor supply does not seem to respond very much to predictable variation in lifetime wages. This is described in the literature as a "small intertemporal elasticity of labor supply."
:::
