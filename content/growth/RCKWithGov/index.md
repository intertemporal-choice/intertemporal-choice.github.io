(sec:RCKWithGov)=
# The Ramsey/Cass-Koopmans (RCK) Model with Government

This chapter adds a government to the [decentralized RCK economy](#sec:decentralizingrck). Government spending paid for by lump-sum taxes leaves the competitive equilibrium efficient, given the spending; a permanent increase in spending crowds out consumption one for one, while a temporary one crowds out less, runs down capital and raises the interest rate; the timing of lump-sum taxes does not matter, which is Ricardian equivalence; and a tax on capital income lowers the steady-state capital stock below the planner's, even when all its revenue is rebated.

:::{margin}
{cite:t}`blanchard&fischer:text`, chapter 2, the course reading, add government to this model after the planner and the decentralized economy, and QuantEcon's [Cass-Koopmans model with distorting taxes](https://python.quantecon.org/cass_fiscal.html) computes fiscal experiments like these in discrete time.
:::

There is no population or productivity growth, so per capita quantities are the RCK model's quantities per efficiency unit. Households are identical and form a unit mass ([Aggregation](#sec:Aggregation)), so per capita and aggregate quantities are the same and the household index is dropped. Capital depreciates at the rate {math}`\deprRte`, so the interest rate is {math}`\rfree = \fFunc^{\prime}(\kap) - \deprRte` and the wage is {math}`\Wage = \fFunc(\kap) - \kap\fFunc^{\prime}(\kap)`.

(sec:RCKGov-LumpSum)=
## Spending Paid for by Lump-Sum Taxes

The government spends {math}`\GovSpend` per unit of time, which yields no utility, and pays for it with a lump-sum tax {math}`\TaxLev` on each household; it balances its budget, {math}`\TaxLev = \GovSpend` at every date, so it never borrows. Taking the paths of the interest rate, the wage and the tax as given, a household with net worth {math}`\aNrm` solves the problem of the [decentralized economy](#sec:decentralizingrck) with the tax subtracted from its income:

```{math}
:label: eq:hhbc

\dot{\aNrm} = \rfree\aNrm + \Wage - \cNrm - \TaxLev .
```

The tax depends on nothing the household chooses, so it drops out of the household's costate equation, [the planner's](#eq:lamgrow) with the household's return {math}`\rfree` in its place, and consumption grows as in the [economy without government](#eq:cdotindiv):

```{math}
:label: eq:RCKGov-cdot

\dot{\cNrm}/\cNrm = \CRRA^{-1}(\rfree - \discRte) .
```

The tax does change the household's lifetime budget. As without government, the no-Ponzi condition and the transversality condition together make the intertemporal budget constraint hold with equality. With {math}`\PDV_{0}(\bullet) \equiv \int_{0}^{\infty} \bullet_{t}\, e^{-\int_{0}^{t}\rfree_{s}\,ds}\,dt` the present discounted value at date 0 of a flow {math}`\bullet`, and [human wealth](#eq:humwealth) {math}`\hNrm_{0} = \PDV_{0}(\Wage)`,

```{math}
:label: eq:RCKGov-hhibc

\PDV_{0}(\cNrm) = \aNrm_{0} + \hNrm_{0} - \PDV_{0}(\TaxLev) :
```

the present discounted value of consumption equals net worth plus human wealth minus the present discounted value of taxes.

A planner who must provide the same spending, and who has the households' utility function, maximizes the same objective subject to the economy's resource constraint:

```{math}
:label: eq:RCKGov-kdot

\dot{\kap} = \fFunc(\kap) - \deprRte\kap - \cNrm - \GovSpend .
```

Net output is consumed, spent by the government, or invested. Spending does not depend on {math}`\kap`, so it drops out of the planner's costate equation too, and the planner's consumption follows the [Keynes-Ramsey rule](#eq:cdotOc) with {math}`\PopnGroRte=\PtyGroRte=0`, {math}`\dot{\cNrm}/\cNrm = \CRRA^{-1}(\fFunc^{\prime}(\kap) - \deprRte - \discRte)`, which is the household's Euler equation, since {math}`\rfree = \fFunc^{\prime}(\kap) - \deprRte`. In equilibrium a household's net worth is the capital stock, {math}`\aNrm = \kap`, because identical households owe each other nothing, as in the [decentralized economy](#sec:decentralizingrck), and this government does not borrow; and by [Euler's theorem](#fact:eulerstheorem) the factor payments exhaust output, so that, net of depreciation, {math}`\rfree\kap + \Wage = \fFunc(\kap) - \deprRte\kap`. So with {math}`\TaxLev = \GovSpend` the household's budget constraint is the planner's resource constraint, and with {math}`\aNrm = \kap` its transversality condition is the planner's. The two economies follow the same equations from the same {math}`\kap_{0}`, with the same condition at infinity: spending paid for by lump-sum taxes takes resources, but leaves the market's allocation of what remains efficient.

(sec:RCKGov-Spending)=
## Permanent and Temporary Increases in Spending

In the [phase diagram](#fig:RamseySSPlot) of the RCK model with {math}`\PopnGroRte=\PtyGroRte=0`, the {math}`\dot{\cNrm}=0` locus, {math}`\fFunc^{\prime}(\kap) = \deprRte + \discRte`, does not involve spending, so neither the steady-state capital stock {math}`\Steady{\kap}` nor the steady-state interest rate, {math}`\discRte`, depends on it. The [locus where capital is constant](#eq:RCK-kdotEq0), {math}`\dot{\kap}=0`, is here {math}`\cNrm = \fFunc(\kap) - \deprRte\kap - \GovSpend`: it shifts down one for one with spending, and a steady state with positive consumption requires {math}`\GovSpend < \fFunc(\Steady{\kap}) - \deprRte\Steady{\kap}`. It is spending that shifts the locus, not taxes: by [Ricardian equivalence](#sec:RCKGov-Debt), when the taxes that pay for the spending are levied does not matter.

**A permanent increase.** From the steady state, spending rises unexpectedly, and for good, from {math}`\GovSpend` to {math}`\GovSpend+\Delta\GovSpend`. Capital cannot jump, but consumption can. The only point on the new saddle path with capital {math}`\Steady{\kap}` is the new steady state, so consumption falls at once by exactly {math}`\Delta\GovSpend`, and nothing else changes, then or later: capital, the interest rate and the wage stay where they were. Each unit of spending crowds out a unit of private consumption.

**A temporary increase.** From the steady state, spending rises unexpectedly at date 0, and everyone knows that it will return to {math}`\GovSpend` at date {math}`t_{1}`. From {math}`t_{1}` on, the economy follows its original equations of motion, so at {math}`t_{1}` it must be on the original saddle path. Consumption cannot jump at {math}`t_{1}`, a date everyone foresaw: as with [a foreseen change in the q model](#Future-Shock-To-Productivity), a jump in marginal utility at a known date would leave a gain from moving consumption across it. So consumption falls at date 0 to the level from which, following the equations of motion with high spending, it reaches the original saddle path exactly at {math}`t_{1}`. It falls by less than {math}`\Delta\GovSpend`, because the spending lasts only until {math}`t_{1}`. Consumption is then above the new {math}`\dot{\kap}=0` locus, so capital falls; with capital below {math}`\Steady{\kap}`, the interest rate {math}`\fFunc^{\prime}(\kap)-\deprRte` is above {math}`\discRte`, so consumption rises. At {math}`t_{1}` spending falls back, investment jumps up by {math}`\Delta\GovSpend`, and the economy returns along the original saddle path to its old steady state: capital is rebuilt, the interest rate falls back to {math}`\discRte`, and consumption keeps rising. {numref}`fig:RCKGovPhase` and {numref}`fig:RCKGovPaths` show both experiments.

:::{figure} figures/RCKGovPhase.png
:name: fig:RCKGovPhase

Permanent and Temporary Increases in Spending

Note: From the steady state E, spending rises unexpectedly from 20 to 25 percent of output. If the increase is permanent, consumption drops at once from E to E′. If it lasts ten years, consumption drops at once to A; capital then runs down until the spending ends, at B on the original saddle path; and the economy returns along that path to E. With {math}`\CRRA=2`, {math}`\kapShare=0.3`, {math}`\discRte=0.02` and {math}`\deprRte=0.08`, the parameters of the RCK chapter's figures without growth. Drawn by the [notebook](RCKWithGov.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RCKWithGov.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RCKWithGov/RCKWithGov.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RCKWithGov/RCKWithGov.ipynb).
:::

:::{figure} figures/RCKGovPaths.png
:name: fig:RCKGovPaths

Consumption, Capital and the Interest Rate after an Increase in Spending

Note: The same economy. The temporary increase is solid, the permanent one dashed, and the shading marks the ten years of high spending. Consumption falls at once by about three fifths of the increase in spending, capital falls by 8 percent while the spending lasts, and the interest rate rises from 2.0 to 2.6 percent. Drawn by the [notebook](RCKWithGov.ipynb); run it in your browser with nothing to install, in [JupyterLite](https://intertemporal-choice.github.io/lite/notebooks/index.html?path=RCKWithGov.ipynb), or open it in [Colab](https://colab.research.google.com/github/intertemporal-choice/intertemporal-choice.github.io/blob/main/content/growth/RCKWithGov/RCKWithGov.ipynb) or [Binder](https://mybinder.org/v2/gh/intertemporal-choice/intertemporal-choice.github.io/main?labpath=content/growth/RCKWithGov/RCKWithGov.ipynb).
:::

So a temporary increase in spending is paid for partly by lower consumption and partly by running down capital, and it raises the interest rate, most when the spending ends; a permanent one is paid for by consumption alone and leaves the interest rate where it was. {cite:t}`romer:text`, section 2.7, works through the same experiments, and {cite:t}`barroWarSpendingUK` finds the pattern in British data from 1701 to 1918: temporary, wartime increases in military spending raised long-term interest rates.

(sec:RCKGov-Debt)=
## Debt and Ricardian Equivalence

Now let the government borrow. Spending keeps its path, but taxes {math}`\TaxLev_{t}` may differ from it at any date. With {math}`\Debt` its debt, the government's dynamic budget constraint, the continuous-time counterpart of [the one in Generational Accounts and the Government](#eq:recurse), is

```{math}
\dot{\Debt}_{t} = \GovSpend_{t} + \rfree_{t}\Debt_{t} - \TaxLev_{t} :
```

debt rises by the amount by which spending, including the interest on the debt, exceeds taxes. The government cannot pay the interest on its debt by borrowing more forever, {math}`\lim_{t\rightarrow\infty} e^{-\int_{0}^{t}\rfree_{s}\,ds}\Debt_{t} \leq 0`, and it does not end with assets it never uses, so the limit is zero; integrating its budget constraint then gives its intertemporal budget constraint, the counterpart of [the discrete-time one](#eq:govibc2): its taxes are worth its initial debt plus its spending,

```{math}
:label: eq:RCKGov-govibc

\PDV_{0}(\TaxLev) = \Debt_{0} + \PDV_{0}(\GovSpend) .
```

Households can now hold government bonds as well as capital, {math}`\aNrm = \kap + \Debt`. Both are riskless, so they must pay the same return, {math}`\rfree = \fFunc^{\prime}(\kap)-\deprRte`, or no one would hold the one that pays less. Unlike the households' loans to one another in the [decentralized economy](#sec:decentralizingrck), government bonds do not net out: the households hold them, and no household owes them. The household's problem is unchanged, so its Euler equation is too, and so is its [intertemporal budget constraint](#eq:RCKGov-hhibc), now with {math}`\aNrm_{0} = \kap_{0} + \Debt_{0}`. Substituting the government's intertemporal budget constraint into it eliminates both the taxes and the debt:

```{math}
:label: eq:famibc

\PDV_{0}(\cNrm) = \kap_{0} + \Debt_{0} + \hNrm_{0} - \PDV_{0}(\TaxLev) = \kap_{0} + \hNrm_{0} - \PDV_{0}(\GovSpend) .
```

The bonds a household holds are matched by the present value of the taxes that will service them: government bonds are not net wealth {cite:p}`barro:bondsnetworth`. Taxes and debt drop out date by date too: subtracting the government's budget constraint from the household's gives {math}`\dot{\kap} = \dot{\aNrm} - \dot{\Debt} = \rfree\kap + \Wage - \cNrm - \GovSpend`, the economy's [resource constraint](#eq:RCKGov-kdot), with neither taxes nor debt in it; and the household's transversality condition, with the government's condition on its debt at infinity, is the planner's. Since taxes enter neither the resource constraint nor the Euler equation, every path of lump-sum taxes that satisfies the government's intertemporal budget constraint supports the same path of consumption, capital and interest rates. This is [Ricardian equivalence](https://en.wikipedia.org/wiki/Ricardian_equivalence), in a perfect foresight economy; {cite:t}`elmendorfMankiw` survey the theory and the evidence.

:::{margin}
Ricardian equivalence needs lump-sum taxes ([a tax on capital income](#sec:RCKGov-CapitalTax) is not one), households that borrow and lend at the government's interest rate, and households that in effect live as long as the government, as generations linked by operative bequests or gifts do {cite:p}`barro:bondsnetworth`. When lives are finite and unlinked, debt is net wealth to the generations alive and crowds out capital, as in [Diamond's model](#sec:OLGModel) {cite:p}`diamond:olg` and [Blanchard's](#sec:BlanchardFiniteHorizon) {cite:p}`blanchardFinite`. Equivalence also fails when households cannot borrow against future income, as in [Aiyagari's economy](#sec:Aiyagari) {cite:p}`aiyagari:ge`, and when the taxes that later service the debt fall on risky income, insuring it and so reducing precautionary saving {cite:p}`barskymankiwzeldes:aer`.
:::

(sec:RCKGov-CapitalTax)=
## A Tax on Capital Income

Finally, let the government tax capital income, net of depreciation, at the rate {math}`\TaxRte`, and return the revenue to households as a lump sum, {math}`\TaxRte\rfree\kap` to each, so that it neither spends nor borrows. The household's budget constraint becomes

```{math}
\dot{\aNrm} = (1-\TaxRte)\rfree\aNrm + \Wage - \cNrm + \TaxRte\rfree\kap .
```

The rebate depends on aggregate capital {math}`\kap`, not on the household's own net worth {math}`\aNrm`, and the household takes it as given: one household's saving changes aggregate capital by nothing ([Aggregation](#sec:Aggregation)). So in its current-value Hamiltonian {math}`\partial\Ham/\partial\aNrm = (1-\TaxRte)\rfree\vk` rather than {math}`\rfree\vk`: the tax lowers the return on saving in the household's costate equation, and the Euler equation becomes

```{math}
\dot{\cNrm}/\cNrm = \CRRA^{-1}((1-\TaxRte)\rfree - \discRte) .
```

In the steady state with the tax, the after-tax return equals the time preference rate:

```{math}
:label: eq:RCKGov-kTaxSteady

(1-\TaxRte)(\fFunc^{\prime}(\Steady{\kap})-\deprRte) = \discRte, \qquad \fFunc^{\prime}(\Steady{\kap}) = \deprRte + \discRte/(1-\TaxRte) ,
```

so the marginal product of capital is higher, and the capital stock lower, than at the planner's [modified golden rule](#eq:RCK-modGoldenRule), where the marginal product of capital is only {math}`\deprRte + \discRte`: before tax, capital must earn {math}`\discRte/(1-\TaxRte)` to pay savers {math}`\discRte` after it, as in the [cost of capital with taxes](#HallJorgensonTaxes) of {cite:t}`hall&jorgenson:i` when depreciation deductions match economic depreciation, as they do for a tax on income net of depreciation.

Yet the resource constraint does not change, because the revenue comes back to households: with {math}`\aNrm = \kap`,

```{math}
\dot{\kap} = (1-\TaxRte)\rfree\kap + \Wage - \cNrm + \TaxRte\rfree\kap = \fFunc(\kap) - \deprRte\kap - \cNrm .
```

So the planner's problem, and with it the planner's steady state, the modified golden rule, is what it was. What has changed is the households' Euler equation, so the competitive equilibrium no longer reproduces the planner's allocation: it converges to less capital, and less consumption, than the planner would choose.

Why does a tax whose revenue all comes back change anything? A household that saves one more unit earns the after-tax return {math}`(1-\TaxRte)\rfree` on it. The tax on that unit's income, {math}`\TaxRte\rfree`, is spread over the whole population as rebates, so the saver gets none of it back: the others get it. When every household saves one more unit, the rebates return the tax to them, and the economy as a whole earns the full {math}`\rfree`. The tax drives a wedge between the private return to saving, {math}`(1-\TaxRte)\rfree`, and its social return, {math}`\rfree`: the return the household earns on its own saving is no longer the net marginal product of capital, which is what [the decentralization](#sec:decentralizingrck) said it would take for the two solutions to differ. A knowledge externality drives the same kind of wedge in [Paul Romer's model](#sec:Romer86) {cite:p}`romer:growth`.

:::{margin}
A constant tax on capital income taxes consumption at a date the more heavily the later the date: it raises the price of consumption at {math}`t`, in units of consumption at date 0, by the factor {math}`e^{\TaxRte\int_{0}^{t}\rfree_{s}\,ds}`, which grows without bound. This is the usual intuition for the result of {cite:t}`juddRedistributive` and {cite:t}`chamleyCapitalTax` that the optimal tax on capital income is zero in the long run. {cite:t}`straubWerningChamleyJudd` overturn the result and undercut its intuition: in Judd's model the optimal long-run tax on capital is positive whenever {math}`\CRRA > 1`, as in this chapter's calibration. {cite:t}`aiyagari:opttax` finds it positive with uninsurable income risk and borrowing constraints, which push the interest rate [below the time preference rate](#res:aiyagari-r-below-time-preference).
:::
