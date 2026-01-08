(sec:SocSecAndKAccum)=

# Social Security and Capital Accumulation

Consider a household with a 2-period lifetime, whose optimization problem is written in the most general way possible, with the last line reflecting the assumption that no labor income is earned in period 2:

```{math}
\begin{aligned}
\vFunc(\bRat_{1,t}) & = \max_{\{\cRat_{1,t}\}} ~~ \uFunc(\cRat_{1,t}) + \Discount \uFunc(\cRat_{2,t+1}) \\
& \text{s.t.} \\
\yRat_{1,t} & = (\Wage_{1,t}-\taxNetTrans_{1,t}) \\
\aRat_{1,t} & = \yRat_{1,t} - \cRat_{1,t} \\
\yRat_{2,t+1} & = (\Wage_{2,t+1}-\taxNetTrans_{2,t+1}) = -\taxNetTrans_{2,t+1} \\
\cRat_{2,t+1} & = \Rfree_{t+1} \aRat_{1,t}+\yRat_{2,t+1}.
\end{aligned}
```

Under logarithmic utility, section [](#sec:2PeriodLCModel) shows that the solution to this problem is

```{math}
:label: eq:c1

\cRat_{1,t} = \left(\frac{\yRat_{1,t}+\yRat_{2,t+1}/\Rfree_{t+1}}{1+\Discount}\right).
```

The only role of government in this economy is to run a Social Security program. Suppose that initially this economy had no Social Security system and we are interested in the effects of introducing a Pay-As-You-Go Social Security system that is expected to remain a constant size from generation to generation from now on: {math}`\taxNetTrans_{2,t+1} = -\taxNetTrans_{1,t+1}` while {math}`\taxNetTrans_{1,t+1} = \taxNetTrans_{1,t}`, so that taxes are greater than transfers when young and transfers are greater than taxes when old.

The effects of Social Security on first period consumption can be seen by writing out explicitly the value for {math}`\cRat_{1,t}` from equation {eq}`eq:c1`, substituting the definitions of {math}`\yRat_{1,t}` and {math}`\yRat_{2,t+1}`:

```{math}
\begin{aligned}
\cRat_{1,t} & = \left(\Wage_{1,t}-\taxNetTrans_{1,t}-\taxNetTrans_{2,t+1}/\Rfree_{t+1}\right)/(1+\Discount) \\
& = \left(\Wage_{1,t}-\underbrace{\rfree_{t+1}\taxNetTrans_{1,t}/\Rfree_{t+1}}_{\text{consume less b/c poorer}}\right)/(1+\Discount)
\end{aligned}
```

where the expression with the underbrace comes from the effect of introducing a constant-sized PAYG Social Security system in section [](#sec:GenAcctsAndGov). If taxes paid when young {math}`\taxNetTrans_{1,t}` are positive (as they are after the introduction of the Social Security system) and the interest rate is positive, the expression with the underbrace is a positive number, and since it is being subtracted from {math}`\Wage_{1,t}` it is clear that consumption in the first period of life will *decline* with the introduction of the Social Security system. The reason is that the household is poorer in a lifetime sense: the rate of return on Social Security contributions is lower than the market interest rate.

Does the decline in consumption mean the saving rate rises? No - because saving is *after-tax* income minus consumption, and net taxes on the young have risen. For saving we have

```{math}
\begin{aligned}
\aRat_{1,t} & = \overbrace{(\Wage_{1,t}-\taxNetTrans_{1,t})}^{\text{Less after-tax income}} - \overbrace{\cRat_{1,t}}^{\text{Lower consumption b/c poorer}} \\
& = (\Wage_{1,t}(1-1/(1+\Discount)) - \taxNetTrans_{1,t}+ [r_{t+1}\taxNetTrans_{1,t}/\Rfree_{t+1}]/(1+\Discount) \\
& = \Wage_{1,t}\left(\frac{\Discount}{1+\Discount}\right)-\taxNetTrans_{1,t}\left(1-\frac{r_{t+1}}{\Rfree_{t+1}(1+\Discount)}\right) \\
& = \Wage_{1,t}\left(\frac{\Discount}{1+\Discount}\right)-\taxNetTrans_{1,t}\left(\frac{\Rfree_{t+1}(1+\Discount)-r_{t+1}}{\Rfree_{t+1}(1+\Discount)}\right) \\
& = \Wage_{1,t}\left(\frac{\Discount}{1+\Discount}\right)-\taxNetTrans_{1,t}\left(\frac{1+\Rfree_{t+1}\Discount}{\Rfree_{t+1}(1+\Discount)}\right).
\end{aligned}
```

So if {math}`\taxNetTrans_{1,t}>0` then saving is less than before the introduction of Social Security.

Now consider the implications in a {cite:t}`diamond:olg` OLG model where saving is the source of capital accumulation. Suppose there is no population growth so that

```{math}
\begin{aligned}
K_{t+1} & = \aRat_{1,t} \\
& = \Wage_{1,t}\left(\frac{\Discount}{1+\Discount}\right)-\taxNetTrans_{1,t}\left(\frac{1+\Rfree_{t+1}\Discount}{\Rfree_{t+1}(1+\Discount)}\right) \\
& = (1-\varepsilon)K^{\varepsilon}_{t} \left(\frac{\Discount}{1+\Discount}\right)-\taxNetTrans_{1,t}\left(\frac{1+\Rfree_{t+1}\Discount}{\Rfree_{t+1}(1+\Discount)}\right) \\
& = \mathcal{Q} K^{\varepsilon}_{t} -\taxNetTrans_{1,t}\left(\frac{1+\Rfree_{t+1}\Discount}{\Rfree_{t+1}(1+\Discount)}\right)
\end{aligned}
```

where {math}`\mathcal{Q}=(1-\varepsilon)\Discount/(1+\Discount)` as before in the [](#sec:OLGModel) section.

Thus the capital accumulation curve is shifted down (the figure simplifies by assuming a constant downward shift, though strictly speaking {math}`\Rfree_{t+1}` depends on {math}`k_{t+1}`). The dynamics of the introduction of Social Security are captured in the figure, under the assumption that the economy was at its steady-state equilibrium level {math}`\bar{k}` before the Social Security system was introduced. The effect of introduction is an immediate increase in consumption, as the old generation spends everything it gets and the young generation doesn't need to do as much retirement saving as before. Over time the economy will converge to its new, lower level of capital {math}`\bar{\bar{k}}`.

:::{figure} /sources/consumption/SocSecAndKAccum/LaTeX/Figures/SocSecAndKAccum.png
:name: fig:SocSecAndKAccum

Convergence of OLG Economy After Intro of Social Security
:::
