(sec:decentralizingrck)=
# Decentralizing the Ramsey/Cass-Koopmans Model

{cite:t}`ramseySave`, {cite:t}`cass:growth` and {cite:t}`koopmans:growth` posed optimal growth as a planner's problem. This chapter shows that, under special conditions, an economy of households and firms trading in competitive markets, each taking prices as given, reaches the allocation chosen by the planner of the [Ramsey/Cass-Koopmans model](#sec:RamseyCassKoopmans). The conditions are infinitely lived households with identical preferences, perfect foresight, perfect capital markets, competitive firms with constant returns to scale, and no externalities or distorting taxes. The chapter follows {cite:t}`blanchard&fischer:text`, section 2.2, which takes up the decentralized economy after the planner and before [government](#sec:RCKWithGov); {cite:t}`romer:text`, chapter 2, and {cite:t}`barro&salaimartin:book`, chapter 2, start from households and firms instead.

:::{margin}
QuantEcon's [Cass-Koopmans Competitive Equilibrium](https://python.quantecon.org/cass_koopmans_2.html) works through the same decentralization in discrete time, with a long but finite horizon, and computes it, and Daron Acemoglu's [lectures on neoclassical growth](https://ocw.mit.edu/courses/14-452-economic-growth-fall-2016/resources/mit14_452f16_lec5and6/) derive it in continuous time, in different notation.
:::

The economy is the RCK model without population or productivity growth, {math}`\PopnGroRte=\PtyGroRte=0` and {math}`\PtyLab=1`, so quantities per capita and per efficiency unit are the same. Households have mass one, spread over the unit interval ([Aggregation](#sec:Aggregation)), and each supplies one unit of labor, so every per capita quantity is also an aggregate. Capital depreciates at the rate {math}`\deprRte`.

:::{margin}
With population growth, each household is a dynasty whose members grow in number at the rate {math}`\PopnGroRte`, so its net worth per member earns {math}`\rfree-\PopnGroRte`. If it counts each member's utility once at each date, as [the planner](#eq:RCK-maxprob) does, its Euler equation is {math}`\dot{\cNrm}/\cNrm = \CRRA^{-1}(\rfree-\PopnGroRte-\discRte)`, the planner's [per capita Euler equation](#eq:trans2). The argument then goes through unchanged, as it does with productivity growth, per efficiency unit of labor.
:::

## The Household's Problem

Household {math}`i` supplies its labor inelastically at the wage {math}`\Wage_{t}` and holds net worth {math}`\aNrm_{t,i}`: capital, plus loans to other households, minus debts to them. Under perfect foresight a loan and a unit of capital must pay the same net return, the interest rate {math}`\rfree_{t}`, so only net worth matters. Taking the paths of {math}`\Wage_{t}` and {math}`\rfree_{t}` as given, the household chooses consumption to solve

```{math}
:label: eq:DecRCK-maxprob

\max_{\{\cNrm_{t,i}\}_{0}^{\infty}} \int_{0}^{\infty} \uFunc(\cNrm_{t,i}) e^{-\discRte t}\,dt
```

with the [planner's](#eq:RCK-maxprob) CRRA utility, {math}`\uFunc(\cNrm) = \cNrm^{1-\CRRA}/(1-\CRRA)`, and time preference rate {math}`\discRte > 0`, subject to the dynamic budget constraint

```{math}
:label: eq:DecRCK-dbc

\dot{\aNrm}_{t,i} = \rfree_{t}\aNrm_{t,i} + \Wage_{t} - \cNrm_{t,i}
```

and the no-Ponzi condition {math}`\lim_{t \rightarrow \infty} e^{-\int_{0}^{t}\rfree_{s}\,ds}\aNrm_{t,i} \geq 0`, which forbids paying the interest on debt by borrowing more, forever.

The household's current-value Hamiltonian is

:::{margin}
The [planner's](#eq:RCK-H1A) conditions have the same form. [Ramsey Growth in Discrete and Continuous Time](#sec:HamiltonianVSDiscrete) derives them and relates each to its discrete-time Bellman counterpart.
:::

```{math}
\Ham(\aNrm,\cNrm,\vk) = \uFunc(\cNrm) + (\rfree_{t}\aNrm + \Wage_{t} - \cNrm)\vk .
```

The [condition for optimal consumption](#eq:uceqvk) is {math}`\uP(\cNrm_{t,i}) = \vk_{t,i}`, and the [costate equation](#eq:lamgrow), with the household's return {math}`\rfree_{t}` in place of the planner's, is {math}`\dot{\vk}_{t,i} = \discRte\vk_{t,i} - \partial\Ham/\partial\aNrm = (\discRte-\rfree_{t})\vk_{t,i}`. Since {math}`\uP(\cNrm) = \cNrm^{-\CRRA}`, differentiating the condition for optimal consumption with respect to time gives {math}`\dot{\vk}/\vk = -\CRRA\dot{\cNrm}/\cNrm`, so

```{math}
:label: eq:cdotindiv

\dot{\cNrm}_{t,i}/\cNrm_{t,i} = \CRRA^{-1}(\rfree_{t}-\discRte),
```

the [Euler equation](#eq:PFCRRA-cgrow) of the perfect foresight model, in continuous time. Nothing on its right side is specific to household {math}`i`: every household's consumption grows at the same rate, whatever its wealth.

Since the costate equation gives {math}`e^{-\discRte t}\vk_{t,i} = \vk_{0,i}e^{-\int_{0}^{t}\rfree_{s}\,ds}`, the transversality condition {math}`\lim_{t \rightarrow \infty} e^{-\discRte t}\vk_{t,i}\aNrm_{t,i} = 0` is {math}`\lim_{t \rightarrow \infty} e^{-\int_{0}^{t}\rfree_{s}\,ds}\aNrm_{t,i} = 0`. The no-Ponzi condition rules out ending with negative net worth in present value; the transversality condition, an optimality condition, rules out ending with positive net worth in present value, resources never consumed. Together they make the dynamic budget constraint, integrated forward, the [intertemporal budget constraint](#eq:PFCRRA-ibc), with equality. Writing {math}`\PDV_{0}(\bullet) \equiv \int_{0}^{\infty} \bullet_{t}\, e^{-\int_{0}^{t}\rfree_{s}\,ds}\,dt` for the present discounted value at date 0 of a flow {math}`\bullet`, it says

```{math}
:label: eq:DecRCK-ibc

\PDV_{0}(\cNrm_{i}) = \aNrm_{0,i} + \hNrm_{0},
```

where [human wealth](#eq:PFCRRA-yfin), the present discounted value of labor income,

:::{margin}
Human wealth depends on the whole path of interest rates. Its response to them is the [human wealth effect](#eq:dlogcdr) of the perfect foresight model, separate from the income and substitution effects, which work through the share of total wealth the household spends.
:::

```{math}
:label: eq:humwealth

\hNrm_{0} = \PDV_{0}(\Wage),
```

is the same for every household, because all earn the same wage.

## The Firm's Problem

Firms hire labor at the wage {math}`\Wage_{t}` and rent capital at the rental rate {math}`\kapRent_{t}`, taking both as given, and produce with the RCK model's Cobb-Douglas technology. Since their number does not matter, one price-taking firm can stand for them all, hiring all the labor and renting all the capital. Because it rents its capital, its problem is static: at each date it chooses

:::{margin}
With constant returns to scale, a firm's size is indeterminate and the number of firms irrelevant; like households, firms are atomistic price takers. They rent capital and own none, as in the [Hall-Jorgenson model](#sec:HallJorgenson) {cite:p}`hall&jorgenson:i`, so the firm's problem has no intertemporal dimension; with costs of adjusting capital it would become the problem of the [q model](#sec:qModel).
:::

```{math}
\max_{\KLvl_{t},\,\LLvl_{t}}\ \FFunc(\KLvl_{t},\LLvl_{t}) - \Wage_{t}\LLvl_{t} - \kapRent_{t}\KLvl_{t},
```

the Hall-Jorgenson firm's problem with labor added. With {math}`\kap = \KLvl/\LLvl` and {math}`\fFunc(\kap) = \FFunc(\KLvl,\LLvl)/\LLvl = \kap^{\kapShare}`, its first-order conditions, [the Hall-Jorgenson firm's](#eq:khj) with a wage added, set each price to a marginal product,

```{math}
:label: eq:DecRCK-prices

\kapRent_{t} = \fFunc^{\prime}(\kap_{t}), \qquad \Wage_{t} = \fFunc(\kap_{t}) - \kap_{t}\fFunc^{\prime}(\kap_{t}),
```

as in the [Diamond OLG model](#eq:rEqfp), where capital does not depreciate. By [Euler's theorem](#fact:eulerstheorem) for [homogeneous functions](https://en.wikipedia.org/wiki/Homogeneous_function#Euler's_theorem), these payments exhaust output, {math}`\fFunc(\kap_{t}) = \Wage_{t} + \kapRent_{t}\kap_{t}`, so profits are zero whatever the firm's size.

## Equilibrium

Households own the capital and rent it to firms. A unit of capital earns {math}`\kapRent_{t}` and depreciates at the rate {math}`\deprRte`, so its net return, the interest rate, is

```{math}
:label: eq:DecRCK-r

\rfree_{t} = \kapRent_{t} - \deprRte = \fFunc^{\prime}(\kap_{t}) - \deprRte,
```

the [Hall-Jorgenson](#eq:ctarb) no-arbitrage condition with the price of capital fixed at one, since output turns into capital one for one; with the wage, it gives the [Aiyagari model's prices](#eq:Aiyagari-Prices).

:::{margin}
Differences in wealth across households would change no aggregate. With CRRA utility, perfect foresight and perfect capital markets, every household spends the same fraction of its total wealth, net worth plus human wealth, a fraction that depends only on the path of interest rates, so aggregate consumption depends only on aggregate wealth {cite:p}`gorman1953community`. Uninsurable income risk and liquidity constraints break this, because they make consumption a concave function of wealth, as in the [Aiyagari model](#sec:Aiyagari). How much the distribution of wealth then matters for aggregates is a quantitative question: {cite:t}`ksHetero` find that its mean almost suffices, and {cite:t}`carrollRequiem` that it does not when the model matches microeconomic facts; see also {cite:t}`carroll:brookings`.
:::

Firms employ the one unit of labor that households supply. In a closed economy with no government, every household's debt is another household's asset, so loans net out and aggregate net worth is the capital stock,

```{math}
:label: eq:DecRCK-clear

\aNrm_{t} \equiv \int_{0}^{1} \aNrm_{t,i}\,di = \kap_{t},
```

where, with a unit mass of workers, capital per worker {math}`\kap_{t}` is also the aggregate capital stock. If households are identical, each holds {math}`\kap_{t}` and no loans.

A perfect foresight equilibrium is a path of capital {math}`\{\kap_{t}\}_{0}^{\infty}` from the given {math}`\kap_{0}`, with the interest rates and wages it implies through {eq}`eq:DecRCK-r` and {eq}`eq:DecRCK-prices`, such that households who expect those prices and optimize hold, in total, exactly that capital. Their expectations of the path of capital are then self-fulfilling.

## The Equilibrium Is the Planner's Solution

Write {math}`\cNrm_{t} \equiv \int_{0}^{1}\cNrm_{t,i}\,di` for aggregate consumption, which grows at the rate every household's does. Integrating the households' budget constraints over {math}`i` and substituting market clearing and the prices into them and into the Euler equation gives

:::{margin}
Only one set of expectations is self-fulfilling here: from a given {math}`\kap_{0}`, only the [saddle path](#fig:RamseySaddlePlot) satisfies the equilibrium conditions and the [transversality condition](#eq:tvc). In other models several paths can each be self-fulfilling; Wikipedia's article on [sunspots](https://en.wikipedia.org/wiki/Sunspots_\(economics\)#Sunspots_and_the_Indeterminacy_School_in_Macroeconomics) discusses such multiple equilibria.
:::

```{math}
:label: eq:DecRCK-aggkdot

\begin{gathered}\begin{aligned}
  \dot{\kap}_{t} & =  \rfree_{t}\kap_{t} + \Wage_{t} - \cNrm_{t}
\\ & = (\fFunc^{\prime}(\kap_{t})-\deprRte)\kap_{t} + \fFunc(\kap_{t}) - \kap_{t}\fFunc^{\prime}(\kap_{t}) - \cNrm_{t}
\\ & = \fFunc(\kap_{t}) - \deprRte\kap_{t} - \cNrm_{t}
\\ \dot{\cNrm}_{t}/\cNrm_{t} & = \CRRA^{-1}(\fFunc^{\prime}(\kap_{t})-\deprRte-\discRte),
\end{aligned}\end{gathered}
```

the planner's [accumulation equation](#eq:RCK-kdot) and [Keynes-Ramsey rule](#eq:cdotOc) with {math}`\PopnGroRte=\PtyGroRte=0`. With {math}`\aNrm_{t}=\kap_{t}`, the household's transversality condition is the planner's [transversality condition](#eq:tvc). The same two differential equations, from the same {math}`\kap_{0}` and with the same condition at infinity, select the same path: the economy follows the planner's [saddle path](#fig:RamseySaddlePlot) to the [modified golden rule](#eq:RCK-modGoldenRule), where the interest rate equals the time preference rate, {math}`\rfree = \discRte`.

:::{margin}
So human wealth is finite, and the economy cannot save too much: its interest rate exceeds its growth rate, zero. With population and productivity growth, the steady-state interest rate exceeds the growth rate {math}`\PopnGroRte+\PtyGroRte` by {math}`\discRte-(1-\CRRA)\PtyGroRte`, which is positive under the condition that keeps [the planner's objective](#eq:maxprobmod) finite. The competitive economy is therefore dynamically efficient, which the [Diamond OLG economy](#sec:OLGModel) need not be.
:::

The two coincide because the household maximizes the planner's objective and, in equilibrium, its budget constraint is the planner's resource constraint: factors are paid their marginal products, so the interest rate the household earns is the net marginal product of capital that the planner trades off against consumption. This is an instance of the [first fundamental theorem of welfare economics](https://en.wikipedia.org/wiki/Fundamental_theorems_of_welfare_economics#First_Fundamental_Theorem): with competitive and complete markets and no externalities, a competitive equilibrium is Pareto efficient, and when households are identical, the efficient allocation that treats them alike is the planner's; {cite:t}`romer:text`, section 2.4, makes this argument for this model. The result is convenient: a planner's problem, usually the easier one to solve, can be read as describing a market economy, as long as we are careful about the assumptions.

## When the Market and the Planner Differ

The equivalence fails when a household's budget constraint or objective differs from the planner's in a way that matters. Wikipedia lists [common failures](https://en.wikipedia.org/wiki/Fundamental_theorems_of_welfare_economics#Common_failures_of_the_assumptions) of the welfare theorem's assumptions; four arise in this book:

- **Externalities.** When one agent's accumulation raises others' productivity, as in [Paul Romer's model](#sec:Romer86) {cite:p}`romer:growth` and the [Lucas model](#sec:LucasGrowth) {cite:p}`lucasGrowth`, the market accumulates too little.
- **Distorting taxes.** A tax on capital income, even with its revenue rebated lump sum, lowers the capital stock in the [RCK model with government](#sec:RCKWithGov), while the planner's choice is unchanged.
- **Uninsurable idiosyncratic risk.** With complete insurance markets, households would insure their idiosyncratic risks at actuarially fair rates and behave as under perfect foresight. Without them, households save for precaution, so the interest rate settles [below the time preference rate](#res:aiyagari-r-below-time-preference) and capital above the modified golden rule level, as in the [Aiyagari model](#sec:Aiyagari) {cite:p}`aiyagari:ge`.
- **Finite lives.** In the [Diamond OLG model](#sec:OLGModel) {cite:p}`diamond:olg` the competitive equilibrium can accumulate capital beyond the golden rule, which an infinitely lived planner, stopping at the modified golden rule, never does. In [Blanchard's perpetual youth model](#sec:BlanchardFiniteHorizon) {cite:p}`blanchardFinite` a debt-financed tax cut raises consumption, so Ricardian equivalence, which holds in the [RCK model with government](#sec:RCKWithGov), fails.
