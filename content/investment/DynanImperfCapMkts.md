(sec:DynanImperfCapMkts)=
# Investment and Capital Market Imperfections

Every model of investment we have seen so far assumes that capital markets are
perfect. A project is valued at its expected payoff and its risk, it is undertaken
whenever that value exceeds the cost of acquiring and installing the capital, and the
cost is governed by an economy-wide interest rate. The amount of investment that
results is efficient.

Capital markets in the real world are not like this, and the largest reason is
asymmetric information. A firm knows more about its own projects than the people it
borrows from. Two distinct problems follow. Under adverse selection, lenders cannot tell
good credit risks from bad ones, so the market rate reflects the average risk; the good
risks are unwilling to borrow at that rate, and the market fills with bad ones. Under
moral hazard, the money having already been lent, the borrower has an incentive to do
things that are not in the lender's interest.

## Sources of External Finance

One place these problems show up is in the structure of the financial system itself.
Funds flow from savers to borrowers by two routes. They travel directly when a household
buys a firm's stocks or bonds, and indirectly when a household deposits at a bank that
then lends to the firm. Asymmetric information is worse along the direct route, because
a household knows far less about a firm's projects than the firm does, and because no
single household has a stake large enough to make paying for monitoring worthwhile.

Financial intermediaries exist largely because of this. A bank becomes a specialist in
acquiring information about firms, which is more efficient done at scale, and so gets
around some of the problem. It does not get around all of it, and there remains
asymmetric information along the indirect route as well (and between depositors and the
bank).

The composition of firms' external finance reflects this. Of the external funds raised
by U.S. nonfinancial businesses between 1970 and 1985, loans supplied 61.9 percent,
bonds 29.8 percent, and stocks 2.1 percent. Most financing is done indirectly, through
intermediaries, which is what the information problems predict. The skew is in fact
sharper than those numbers suggest, since financial intermediaries rather than
households hold much of the stock and most of the bonds. Note also how small a role
equity plays. The model we turn to now explains why a debt contract is generally the
optimal arrangement between a lender and a borrower.

## Costly State Verification

The formal treatment follows {cite:t}`romer:text`. It is deliberately specific, since it
takes up one particular information problem, but it generalizes to others and the
qualitative conclusions survive.

An entrepreneur can undertake a project requiring one unit of resources. Project output
is distributed uniformly on {math}`[0,2\mu]`, so expected output is {math}`\mu`, and
{math}`\mu` varies across entrepreneurs. The entrepreneur has wealth {math}`W` and must
borrow {math}`1-W` from outsiders. Because all of her money is tied up in the project,
her payment back to lenders cannot exceed the project's output, so the lenders bear some
of the risk. Everyone is risk neutral, the risk-free interest rate is {math}`\rfree`,
and outside investors are competitive, so in equilibrium their expected rate of return
must equal {math}`\rfree`. The entrepreneur undertakes the project when

```{math}
:label: eq:DICM-undertake

\mu - \Ex[\text{payment to outsiders}] > (1+\rfree)W.
```

Suppose first that outside investors can observe output without cost, so that they know
what the firm knows. Every project with {math}`\mu > 1+\rfree` is financed, and the loan
contract is written so that the expected payment to the investor is
{math}`(1-W)(1+\rfree)`. The investor is content, earning exactly what lending at the
risk-free rate would have paid. So is the entrepreneur, whose expected income is

```{math}
\mu - (1-W)(1+\rfree) = W(1+\rfree) + \mu - (1+\rfree),
```

which exceeds {math}`W(1+\rfree)` precisely because {math}`\mu > 1+\rfree`.

Now let the investor pay a cost {math}`c>0` to observe the entrepreneur's output. We take
up this case, "costly state verification," because it is the most straightforward of the
information problems to analyze, and we should be honest that in practice other frictions
matter more. We also assume the outsider's wealth exceeds {math}`1-W`, so that a single
investor can fund a project. (Drop that assumption and lenders begin waiting for someone
else to pay the verification cost, which is a complication of its own.)

The expected payment to the investor must cover the required return and the verification
costs it expects to bear,

```{math}
:label: eq:DICM-breakeven

\Ex[\text{payment to investor}] = (1+\rfree)(1-W) + \Ex[\text{verification costs}],
```

and the entrepreneur keeps whatever output remains. Her income is therefore maximized by
the contract that minimizes expected verification costs, and that contract is debt. The
outsider receives a fixed payment {math}`D` whenever output is high enough to cover it,
verifying nothing; when output falls short, the outsider verifies and takes everything
there is. Verifying always would be wasteful, and a payment that varied with output
without verification would be worthless, since the entrepreneur would report that things
had turned out badly every time.

## The Equilibrium Debt Contract

The face value {math}`D` is endogenous, so we solve for it. Write the lender's expected
net receipts as {math}`\mathcal{R}(D)`. If {math}`D \geq 2\mu` the lender always takes the
whole output and always verifies, so {math}`\mathcal{R} = \mu - c`. If {math}`D < 2\mu`,
then with probability {math}`(2\mu-D)/2\mu` output exceeds {math}`D` and the lender
receives {math}`D` without verifying, while with probability {math}`D/2\mu` output falls
short and the lender verifies and collects {math}`D/2` on average (the mean of a uniform
draw conditional on landing below {math}`D`). Collecting terms,

```{math}
:label: eq:DICM-receipts

\mathcal{R}(D) = D - \frac{D^{2}}{4\mu} - \frac{Dc}{2\mu},
```

so that {math}`\mathcal{R}` is rising as long as {math}`2\mu - c > D`. Expected net receipts
therefore increase with {math}`D` up to {math}`D = 2\mu - c` and fall thereafter,
leveling out at {math}`D = 2\mu`.

Equilibrium sets {math}`\mathcal{R}(D)` equal to the return the lender requires,
{math}`(1+\rfree)(1-W)`. Three cases arise as that requirement rises. When it is low the
equation has a single relevant root on the rising branch. When it is higher there are
two roots, but the larger of them is not a competitive equilibrium, because another
investor would undercut anyone who offered it. When the requirement exceeds the maximum
of {math}`\mathcal{R}`, no lending takes place at all, since the entrepreneur cannot meet the
investor's required return in expected value.

Because the investor verifies whenever output falls below the equilibrium face value,
which happens with probability {math}`D^{*}/2\mu`, expected verification costs are
{math}`(D^{*}/2\mu)c`. Writing that wedge as an agency cost
{math}`\mathcal{A}(c,\rfree,W,\mu)`, the project is undertaken only when

```{math}
:label: eq:DICM-agency

\mu > 1 + \rfree + \mathcal{A}(c,\rfree,W,\mu),
```

and differentiation shows that the wedge grows with the verification cost and with the
interest rate, and shrinks with the entrepreneur's wealth and with the quality of her
project. Models built on moral hazard or adverse selection instead of costly state
verification deliver much the same comparative statics.

## Implications

Four things follow, and we think each of them marks a real departure from the
{math}`\q` theory of the [{math}`\q` model](#sec:qModel).

Agency costs raise the cost of external finance and reduce investment, since
{eq}`eq:DICM-agency` demands a strictly better project than the frictionless condition
{math}`\mu > 1+\rfree` would. Some worthwhile projects (those with
{math}`1+\rfree < \mu < 1+\rfree+\mathcal{A}`) simply go unfunded.

Output and interest rates acquire indirect effects on investment alongside the direct
ones the {math}`\q` model already delivers. Higher output raises current profitability
and with it the internal funds {math}`W` the entrepreneur can put into the project.
Interest rates move the face value {math}`D` and therefore the expected verification
costs.

Variables with no place in the {math}`\q` model begin to matter, cash flow most of all.
Firms with more of their own resources fund projects more cheaply, and the empirical
literature testing that link is large and mostly finds it. Unfortunately, the finding is
harder to interpret than it looks, because cash flow moves with profitability, which
ought to affect investment even when information is symmetric (a firm having a good year
is both richer and, plausibly, facing better projects). We take that identification
problem up in [investment and cash flow](#sec:iAndCashFlow).

Changes in the financial system itself alter investment, by making verification harder
or easier. The collapse of the banking system during the Great Depression destroyed
precisely the specialists who had been evaluating projects cheaply, which raised the
cost of investment and helped drive it down.
