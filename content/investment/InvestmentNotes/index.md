(sec:InvestmentNotes)=
# Investment Notes

The chapter's [notebook](InvestmentNotes.ipynb) draws its figures from the national accounts and solves Samuelson's multiplier-accelerator model, with sliders; open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/investment/InvestmentNotes/InvestmentNotes.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/investment/InvestmentNotes/InvestmentNotes.ipynb).

## Broad Comments

### Why Study Investment?

1. Although investment is much smaller as a fraction of GDP than consumption, investment is much more *variable* than consumption. So *fluctuations* in investment spending account for a large proportion of business-cycle frequency fluctuations in GDP: over the business cycle, investment is several times as volatile as output {cite:p}`stockWatsonHandbook`. {numref}`fig:InvestmentVolatility` shows one way of measuring this: since 1948, real investment's growth over four quarters has varied four times as much as real GDP's, and, measured by the covariance of its growth with GDP's, investment accounts for about half of the variance of GDP's growth.

2. In the long run, the average magnitude of investment spending determines the size of the capital stock. If we think accounting for capital is an important component of explaining macroeconomic outcomes, then we need an understanding of investment.

### History of Thought

- {cite:t}`keynesGeneralTheory`, in the chapter on "The State of Long-Term Expectation": {math}`I` determined by "animal spirits" which fluctuated strongly. The same chapter anticipates {math}`\q`: "there is no sense in building up a new enterprise at a cost greater than that at which a similar existing enterprise can be purchased."
- The acceleration principle of {cite:t}`clarkAccelerator`, and the Keynesian "Multiplier/Accelerator" model of investment of {cite:t}`samuelsonI`, Hansen and Harrod
- The neoclassical model with no costs of adjustment: {cite:t}`jorgensonCapitalTheory` and {cite:t}`hall&jorgenson:i`
- The {math}`q` of {cite:t}`brainardTobinPitfalls` and {cite:t}`tobinsQ`
- Convex costs of adjustment {cite:p}`eisnerStrotz,lucasAdjustmentCosts,gouldAdjustmentCosts,treadwayInvestment`, and the {cite:t}`abel:q`-{cite:t}`hayashi:q` "marginal {math}`\q`" model
- Irreversibility and nonconvex costs of adjustment {cite:p}`abel&eberly:unified,dixitPindyck,caballeroEngelSs,cooperHaltiwangerAdjCosts`
- Capital market imperfections {cite:p}`fhp,bernankeGertlerAgency,kiyotakiMooreCredit`

## The Samuelson Multiplier-Accelerator Model

The acceleration principle of {cite:t}`clarkAccelerator` says that investment depends on the *change* in demand: a firm that needs {math}`v` units of capital to produce a unit of output must invest {math}`v` units when its sales rise by one. {cite:t}`samuelsonI` combined it with the Keynesian consumption function. Output is the sum of government spending, consumption and investment; consumption depends on last period's income; and investment is induced by the change in consumption:

```{math}
\begin{aligned}
Y_{t} &= G_{t} + C_{t} + I_{t} \\
C_{t} &= c Y_{t-1} \\
I_{t} &= v (C_{t}-C_{t-1})
\end{aligned}
```

where {math}`c` is the marginal propensity to consume and {math}`v` is the accelerator. With government spending constant at {math}`G`, substituting gives a second-order difference equation for output,

```{math}
:label: eq:samuelsonI

Y_{t} = G + c(1+v)Y_{t-1} - c v Y_{t-2},
```

whose steady state is the Keynesian multiplier's {math}`G/(1-c)`. The model was famous for its dynamics, which depend only on {math}`c` and {math}`v`. Output cycles when the roots of {math}`x^{2}-c(1+v)x+cv=0` are complex, which happens when {math}`c(1+v)^{2} < 4v`, and it converges when {math}`cv < 1`. So output can converge smoothly, converge in damped cycles, cycle with growing amplitude, or explode ({numref}`fig:MultiplierAccelerator`). In the cyclical case, the amplitude of the cycles changes each period by the factor {math}`\sqrt{cv}`, the modulus of the roots.

:::{figure} figures/MultiplierAccelerator.png
:name: fig:MultiplierAccelerator

The multiplier-accelerator's four regimes. Left, the map: below the solid curve output cycles, and below the dashed one it converges. Right, output after government spending rises by 10 percent for good at {math}`t = 0`, relative to the change's long-run effect (0 is the old steady state, 1 the new), at the four numbered points. Drawn by the chapter's notebook, which you can open in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/investment/InvestmentNotes/InvestmentNotes.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/investment/InvestmentNotes/InvestmentNotes.ipynb).
:::

From today's perspective, the distinctive feature of Samuelson's model of investment is its emphasis on the proposition that levels of investment were determined by impulses from outside the market for investment. Empirical work in this tradition boiled the investment component down to a reduced form like

```{math}
:label: eq:InvNotes-reducedForm

I_{t} = \alpha Y_{t} + \gamma \rfree_{t}, \qquad \gamma < 0,
```

in which the desired level of investment depends in a simple linear way on the autonomous evolution of other variables: Output {math}`Y` and interest rates {math}`\rfree`. These variables were in turn affected by {math}`I`, and the model was capable of producing rich dynamics as a result.

In purely statistical terms, an equation like {eq}`eq:InvNotes-reducedForm` performs remarkably well in "explaining" investment spending. But this is not very satisfactory because income, investment, and interest rates are presumably all determined by deeper underlying features of the environment, and so it is highly problematic to interpret this equation as instructive about the fundamental determinants of investment. In particular, there is no reason to expect its coefficients to stay the same when policy changes the environment that produced them {cite:p}`lucasCritique`.

## Hall and Jorgenson

{cite:t}`hall&jorgenson:i`, building on {cite:t}`jorgensonCapitalTheory`, made an important step forward by constructing a model in which an optimizing firm chooses the level of its capital stock with reference to fundamental features of the economic environment like its production function, depreciation rates, tax considerations, and a comparison of interest rates to the productivity of the firm's available uses of capital.

The [Hall-Jorgenson](#sec:HallJorgenson) section presents a stripped-down version of this model.

An important objection to this framework, however, was that it assumes that firms have the ability to instantly and costlessly move their capital stocks to the level that would be justified by the prevailing economic environment. If something happens to make the firm wish to be larger, it can, say, quadruple its capital stock overnight, paying no cost of adjustment for such a radical change.

## {math}`\q` Models

A seminal paper by {cite:t}`tobinsQ`, building on {cite:t}`brainardTobinPitfalls`, provided the intuition for how to move forward. Tobin defined a variable

```{math}
Q = \left(\frac{\text{Stock Mkt Val of Firm}}{\text{Replacement Cost of K}}\right)
```

and proposed that investment should obey the rule

```{math}
:label: eq:InvNotes-1

\begin{cases}
 i_{t}-\depr k_{t} > 0 & \text{if $Q_{t} > 1$}
\\ i_{t}-\depr k_{t} < 0 & \text{if $Q_{t} < 1$}
\end{cases}
```

where {math}`i_{t}-\depr k_{t}` is net investment: gross investment {math}`i_{t}` minus the depreciation {math}`\depr k_{t}` of the existing capital stock. That is, firms which have a value greater than what it would cost to reproduce their capital should be growing, while firms which are not worth what it would cost to reproduce them should be shrinking.

Tobin's {math}`Q` is now one of the basic tools of financial market analysis; it is used regularly as one of several tools designed to try to assess firms' prospects.

Tobin's paper inspired a large amount of empirical and theoretical work, culminating in two classic papers, by {cite:t}`abel:q` and {cite:t}`hayashi:q`, which put the theory on a rigorous mathematical basis. The canonical model that emerged from this literature is summarized in the [marginal q model](#sec:qModel) section.

One unsatisfactory feature of the {math}`\q` model is that the motivations of the firm's owners are not clearly delineated: shareholders are assumed to be risk-neutral return maximizers, so the model has no real implications for the firm's dividend policy or holdings of cash. The [entrepreneur's problem](#sec:EntrepreneurPF) section takes up the alternative of a firm wholly owned by a utility-maximizing entrepreneur whose consumption is the firm's dividend payout.

## Imperfect Capital Markets

One of the foundations of the {math}`\q` model as developed by Abel and Hayashi is its reliance on an assumption that capital markets are perfect, in the sense that in these models investment is pursued right up to the point where the marginal value of an additional unit of investment has been driven down to the exact value of the riskless interest rate (after accounting appropriately for tax features, depreciation, etc), which reflects the optimal quantity of investment. The return required is the riskless one because the firm's owners are assumed to be risk neutral; with risk-averse owners it would be a risk-adjusted return, but the logic would be the same.

The key reason that the assumption of perfect capital markets is so useful is that it implies that it is not necessary to keep track of the firm's cash management or financial activities. This is the theorem of {cite:t}`mmTheorem`: when capital markets are perfect, the value of a firm, and so its investment, does not depend on how the investment is financed (see [investment and cash flow](#sec:iAndCashFlow) for the argument in the {math}`\q` model).

Useful though it may be, the assumption of perfect capital markets is clearly very far from reality. A vast literature has explored what happens when a wide variety of imperfections are introduced. The chapter [Investment and Capital Market Imperfections](#sec:DynanImperfCapMkts) summarizes one particular model of capital market imperfections that produces implications that are similar to those that emerge from many other models.

The implication of capital market imperfections that has been most vigorously explored is that the amount of investment may be affected by a firm's financial position. The crux of that literature is summarized in the [investment and cash flow](#sec:iAndCashFlow) section.

:::{figure} figures/InvestmentVolatility.png
:name: fig:InvestmentVolatility

Investment drives the cycle: the growth over four quarters of real gross private domestic investment, real GDP and real personal consumption expenditures, in percent, 1948 to 2026, with the NBER's recessions shaded. The standard deviations of the three growth rates are 11.5, 2.6 and 2.3 percentage points. Data from the Bureau of Economic Analysis, via FRED (series GPDIC1, GDPC1, PCECC96 and USRECQ), downloaded on 2026-10-31. Drawn by the chapter's notebook, which you can open in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/investment/InvestmentNotes/InvestmentNotes.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/investment/InvestmentNotes/InvestmentNotes.ipynb).
:::
