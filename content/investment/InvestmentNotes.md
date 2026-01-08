(sec:InvestmentNotes)=

# Investment Notes
## Broad Comments

### Why Study Investment?

1. Although investment is much smaller as a fraction of GDP than consumption, investment is much more *variable* than consumption. So *fluctuations* in investment spending account for a large proportion of business-cycle frequency fluctuations in GDP. (See the figure below for one way of measuring this).

2. In the long run, the average magnitude of investment spending determines the size of the capital stock. If we think accounting for capital is an important component of explaining macroeconomic outcomes, then we need an understanding of investment.

### History of Thought

- Keynes: {math}`I` determined by "animal spirits" which fluctuated strongly
- {cite:t}`samuelsonI`/Hansen/Harrod: Keynesian "Multiplier/Accelerator" model of investment
- {cite:t}`hall&jorgenson:i` neoclassical model with no costs of adjustment
- {cite:t}`tobinsQ`'s {math}`q` model
- {cite:t}`abel:q`-{cite:t}`hayashi:q` "marginal {math}`\q`" model with smooth convex costs of adjustment
- Models with nonconvex costs of adjustment
- Models with capital market imperfections

## The Samuelson Multiplier-Accelerator Model

From today's perspective, the distinctive feature of Samuelson's model of investment is its emphasis on the proposition that levels of investment were determined by impulses from outside the market for investment. While the model is highly sophisticated in many ways, the essence of it for our purposes can be captured by a very simple equation:

```{math}
:label: eq:samuelsonI

I_{t} = \alpha Y_{t} + \gamma \rfree_{t}
```

When paired with equations determining consumption and income, and with some lags added, the model generated the classic Keynesian multiplier-accelerator framework. But the key feature of the investment component of the model was that it assumed that the desired level of investment depended in a simple linear way on the autonomous evolution of other variables: Output {math}`Y` and interest rates {math}`\rfree`. These variables were in turn affected by {math}`I`, and the model was capable of producing rich dynamics as a result. But for the purpose of explaining investment itself, the model's key implication could be boiled down to {eq}`eq:samuelsonI`.

In purely statistical terms, an equation like {eq}`eq:samuelsonI` performs remarkably well in "explaining" investment spending. But this is not very satisfactory because income, investment, and interest rates are presumably all determined by deeper underlying features of the environment, and so it is highly problematic to interpret this equation as instructive about the fundamental determinants of investment.

## Hall and Jorgensen

{cite:t}`hall&jorgenson:i` made an important step forward by constructing a model in which an optimizing firm chooses the level of its capital stock with reference to fundamental features of the economic environment like its production function, depreciation rates, tax considerations, and a comparison of interest rates to the productivity of the firm's available uses of capital.

The [](#sec:HallJorgenson) presents a stripped-down version of this model.

An important objection to this framework, however, was that it assumes that firms have the ability to instantly and costlessly move their capital stocks to the level that would be justified by the prevailing economic environment. If something happens to make the firm wish to be larger, it can, say, quadruple its capital stock overnight, paying no cost of adjustment for such a radical change.

## {math}`\q` Models

A seminal paper by {cite:t}`tobinsQ` provided the intuition for how to move forward. Tobin defined a variable

```{math}
Q = \left(\frac{\text{Stock Mkt Val of Firm}}{\text{Replacement Cost of K}}\right)
```

and proposed that investment should obey the rule

```{math}
:label: eq:InvNotes-1

\begin{cases}
 i_{t} > 0 & \text{if $Q_{t} > 1$}
\\ i_{t} < 0 & \text{if $Q_{t} < 1$}
\end{cases}
```

That is, firms which have a value greater than what it would cost to reproduce their capital should be growing, while firms which are not worth what it would cost to reproduce them should be shrinking.

Tobin's {math}`Q` is now one of the basic tools of financial market analysis; it is used regularly as one of several tools designed to try to assess firms' prospects.

Tobin's paper inspired a large amount of empirical and theoretical work, culminating in two classic papers, by {cite:t}`abel:q` and {cite:t}`hayashi:q`, which put the theory on a rigorous mathematical basis. The canonical model that emerged from this literature is summarized in the [](#sec:qModel).

:::{admonition} The Entrepreneurial Firm Under Perfect Foresight
:class: dropdown

One unsatisfactory feature of the {math}`\q` model is that the motivations of the firm's owners are not very clearly delineated. Shareholders are assumed to be risk-neutral return maximizers, and the firm chooses its investment policies accordingly, but the model has no real implications for the firm's dividend policy or holdings of cash. (This is an example of the famous {cite:t}`mmTheorem` theorem derived under perfect capital markets). Yet there are clearly systematic patterns to the choices firms make about dividend payouts. In fact, much of what is studied in corporate finance is how to manage such payouts.

One way to produce a well defined dividend payout policy is to consider the firm as being wholly owned by a utility-maximizing entrepreneur whose consumption is determined by the dividend payout from the firm. That approach is explored in the [](#sec:EntrepreneurPF). The surprising upshot is that, in the perfect foresight case, the behavior of the firm owned by an entrepreneur is indistinguishable from the behavior of a "publicly traded" firm, while the consumption behavior of the entrepreneur is indistinguishable from the behavior of a consumer who does not own any business enterprises. (This conclusion relies importantly on the assumption of perfect foresight.)
:::

## Imperfect Capital Markets

One of the foundations of the {math}`\q` model as developed by Abel and Hayashi is its reliance on an assumption that capital markets are perfect, in the sense that in these models investment is pursued right up to the point where the marginal value of an additional unit of investment has been driven down to the exact value of the riskless interest rate (after accounting appropriately for tax features, depreciation, etc), which reflects the optimal quantity of investment.

The key reason that the assumption of perfect capital markets is so useful is that it implies that it is not necessary to keep track of the firm's cash management or financial activities.

Useful though it may be, the assumption of perfect capital markets is clearly very far from reality. A vast literature has explored what happens when a wide variety of imperfections are introduced. The section [DynanImperfCapMkts.pdf](http://www.econ2.jhu.edu/people/ccarroll/Choice/LectureNotes/investment/DynanImperfCapMkts.pdf) summarizes one particular model of capital market imperfections that produces implications that are similar to those that emerge from many other models.

The implication of capital market imperfections that has been most vigorously explored is that the amount of investment may be affected by a firm's financial position. The crux of that literature is summarized in the [](#sec:iAndCashFlow).

<!-- Figure from Torsten Slok at DB, in presentation for 2011/10, email from torsten.slok@db.com, Slok_Presentation_Oct.pdf -->

:::{figure} ../sources/investment/InvestmentNotes/LaTeX/Figures/InvestmentDrivesCycle.png
:name: fig:InvestmentDrivesCycle

Investment Drives the Cycle
:::
