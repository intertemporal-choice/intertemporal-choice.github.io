(sec:GenAcctsAndGov)=

# Generational Accounts and the Government
## The Government Budget Constraint

Consider a government that raises taxes {math}`\TaxLev_{t}`, makes expenditures {math}`\GovSpend_{t}`, and has an outstanding stock of debt {math}`\Debt_{t}` at the beginning of period {math}`t`, on which it must pay interest at rate {math}`\rfree_{t}`. The government can run a deficit only by raising funds via the issuing of new bonds.

:::{margin}
Other way would be to print money - see Larry Ball's class for this.
:::

The government's Dynamic Budget Constraint (DBC) is given by

```{math}
:label: eq:recurse

\begin{aligned}
\overbrace{\Debt_{t+1}-\Debt_{t}}^{\text{Deficit}} & = \overbrace{(\GovSpend_{t}+\rfree_{t}\Debt_{t})}^{\text{Outlays}}-\TaxLev_{t} \\
\Debt_{t+1} & = \GovSpend_{t}+\Rfree_{t}\Debt_{t}-\TaxLev_{t} \\
\Debt_{t} & = \left(\frac{\Debt_{t+1}+\TaxLev_{t}-\GovSpend_{t}}{\Rfree_{t}}\right).
\end{aligned}
```

But we can obtain a similar formula for {math}`\Debt_{t+1}` in terms of {math}`\Debt_{t+2}`, and substitute it into {eq}`eq:recurse`. Continued substitution gives

:::{aside}
This equation just says gov must plan to repay its debts. No constraint on what gov can do in any one or 2 periods. Diff from HHs in this way. Because gov has {math}`\infty` horizon, can obligate future generations to pay for spending of current generations. Quite a trick! (Japan 100 year mortgage).
:::

[^debt-repayment]: This equation just says gov must plan to repay its debts. No constraint on what gov can do in any one or 2 periods. Diff from HHs in this way. Because gov has {math}`\infty` horizon, can obligate future generations to pay for spending of current generations. Quite a trick! (Japan 100 year mortgage).

```{math}
:label: eq:govibc

\begin{aligned}
\Debt_{t} & = \overbrace{(\TaxLev_{t}-\GovSpend_{t})}^{\equiv \Surplus_{t}}/\Rfree_{t}+(\TaxLev_{t+1}-\GovSpend_{t+1})/\Rfree_{t}\Rfree_{t+1}+\ldots \\
& = \Surplus_{t}/\Rfree_{t}+\Surplus_{t+1}/\Rfree_{t}\Rfree_{t+1}+\ldots \\
\Rfree_{t}\Debt_{t} & = \mathbb{P}_{t}(\Surplus) \\
& = \mathbb{P}(\text{Govt Primary Surpluses})
\end{aligned}
```

where {math}`\mathbb{P}` denotes the present discounted value; this can be rewritten

```{math}
:label: eq:govibc2

\mathbb{P}_{t}(X) = \mathbb{P}_{t}(T)-\Rfree_{t}\Debt_{t}.
```

Equation {eq}`eq:govibc2` should look familiar: recall that in the consumption problem we had an Intertemporal Budget Constraint that said

:::{margin}
{math}`\mathbb{P}_{t}(Y) = H_{t}`.
:::

```{math}
\mathbb{P}_{t}(C) = \mathbb{P}_{t}(Y)+\Rfree_{t} \Kap_{t}
```

where {math}`\Kap_{t}` is the beginning-of-period level of capital wealth (before interest has been earned).

In each case, the PDV of expenditures must be equal to the PDV of income plus current wealth. Thus, equations {eq}`eq:govibc` and {eq}`eq:govibc2` are different ways to express the Government Intertemporal Budget Constraint (GIBC).[^gibc-footnote]

:::{margin}
It's {math}`RB` rather than {math}`B` because we set up budget constraint with timing of interest payments at beginning of period rather than end. Note that as time interval goes to zero, {math}`R \approx 1`.
:::

[^gibc-footnote]: The {math}`\Rfree_{t}` is present in the government's problem because for the consumer we were thinking about the situation after any interest income was received; if we were to think of the consumer's beginning-of-period capital as {math}`K_{t}` then we would have {math}`B_{t} = \Rfree_{t} K_{t}`; and note that the sign difference reflects the fact that {math}`D` is debt while {math}`B` is balances.

Now let's suppose that the only kind of expenditures the government engages in are transfers, so that {math}`\GovSpend_{t}` simply reflects money handed out to some members of the population in period {math}`t`. Then {math}`\Surplus_{t}` will be equal to total net transfers among the members of the population at period {math}`t`. Note that there is nothing that says that {math}`\Surplus_{t}` must be positive or negative in any particular period. The GIBC only places restrictions on the present discounted value of net transfers.

:::{margin}
This is net transfers in year {math}`t` (if we are only thinking of SS), 'primary surplus' if we think of govt activities more generally.
:::

The fact that government only has to satisfy the GIBC means that the government can potentially treat different generations very differently from each other. It is therefore useful to have a mechanism to keep track of how different generations are treated. The standard way of doing this is to construct a set of 'generational accounts,' as initially proposed by {cite:t}`akg:genaccts`.

If we assume that consumers live two-period lives, the generational account for the generation born at time {math}`t` is:

:::{margin}
Point out that either of these {math}`Z`'s can be negative, which would signify net transfers to households.
:::

```{math}
\begin{aligned}
\bar{Z}_{t} & = \Surplus_{1,t}+\Surplus_{2,t+1}/\Rfree_{t+1} \\
& = \text{PDV of lifetime taxes net of transfer payments}.
\end{aligned}
```

In the US and most other countries, working-age people pay more in taxes than they receive in transfers, so {math}`\Surplus_{1,t}` is positive, while old people receive more in transfers than they pay in taxes, so {math}`\Surplus_{2,t}` is negative.

:::{margin}
Largest transfers are Social Security and Medicare in US.
:::

Note now that the aggregate total of net transfers can be subdivided into the net transfers of the two age groups in the population,

```{math}
\Surplus_{t} = \Surplus_{1,t}+\Surplus_{2,t}.
```

% and note further that the GIBC can be rewritten as
% \begin{equation}\begin{gathered}\begin{aligned}
%         \Rfree_{t}\Debt_{t} & =  \mathbb{P}_{t}(T) - \mathbb{P}_{t}(X) = \mathbb{P}_{t}(T-X) = \mathbb{P}_{t}(Z)
% \end{aligned}\end{gathered}\end{equation}

Now write out the GIBC {eq}`eq:govibc` explicitly:

```{math}
\begin{aligned}
\mathbb{P}_{t}(Z) & = \phantom{+} \Surplus_{t}+\Surplus_{t+1}/\Rfree_{t+1}+ \ldots \\
& = \phantom{+} \Surplus_{1,t}+\Surplus_{1,t+1}/\Rfree_{t+1}+\Surplus_{1,t+2}/\Rfree_{t+1}\Rfree_{t+2}+\ldots \\
& \phantom{=} +\Surplus_{2,t}+\Surplus_{2,t+1}/\Rfree_{t+1}+\Surplus_{2,t+2}/\Rfree_{t+1}\Rfree_{t+2}+\ldots \\
& = \Surplus_{2,t}+[\Surplus_{1,t}+\Surplus_{2,t+1}/\Rfree_{t+1}]+[\Surplus_{1,t+1}+\Surplus_{2,t+2}/\Rfree_{t+2}]/\Rfree_{t+1} + \ldots \\
& = \Surplus_{2,t}+\bar{Z}_{t}+\bar{Z}_{t+1}/\Rfree_{t+1}+\bar{Z}_{t+2}/\Rfree_{t+1}\Rfree_{t+2}+\ldots
\end{aligned}
```

which again shows that the GIBC is consistent with any treatment of any particular generation; any pattern of generational accounts that satisfies the GIBC is feasible.

## Social Security and Generational Accounts

Consider an economy that initially has no government so that {math}`\Surplus_{1,t}=\Surplus_{2,t}=\Surplus_{2,t-1} = 0`. Now consider introducing a Pay As You Go (PAYG) Social Security system at date {math}`s`, which is to remain of constant size forever after introduction,

```{math}
\begin{aligned}
\Surplus_{2,t} & = -\Surplus_{1,t} \neq 0~~ \forall~t~\geq~s \\
\Surplus_{1,t+1} & = \Surplus_{1,t}.
\end{aligned}
```

Consider the generation born at time {math}`s-1`. It paid nothing into the Social Security system when young, yet gets {math}`\Surplus_{2,s}` out when old. Its generational account is therefore

```{math}
\begin{aligned}
\bar{Z}_{s-1} & = \Surplus_{1,s-1}+\Surplus_{2,s}/\Rfree_{s} \\
& = 0+\Surplus_{2,s}/\Rfree_{s}
\end{aligned}
```

so this generation benefits from the introduction of SS because it paid no taxes yet receives benefits.

:::{margin}
Since {math}`\Surplus_{2,s}` is a neg number, they are better off than without SS.
:::

The GA's for succeeding generations are

```{math}
:label: eq:SScost

\begin{aligned}
\bar{Z}_{t} & = \Surplus_{1,t}+\Surplus_{2,t+1}/\Rfree_{t+1} \\
& = \Surplus_{1,t}(1-1/\Rfree_{t+1}) \\
& = \rfree_{t+1}\Surplus_{1,t}/\Rfree_{t+1}
\end{aligned}
```

so future generations are worse off by this amount.

:::{margin}
Taxes are positive; effect on lifetime budget constraint is the negative of the expression on RHS of {eq}`eq:SScost`. Next revert to class notes for discussion of Ponzi Schemes.
:::

The reason the introduction of Social Security makes future generations worse off is that without SS they could have invested the amount {math}`\Surplus_{1,t}` and earned interest on it of {math}`\rfree_{t+1}\Surplus_{1,t}` in period 2. Now the money is taken away from them when young and returned *without interest* when old. Thus, the loss is precisely the loss in interest income on {math}`\Surplus_{1,t}` in period {math}`t+1`, discounted back to the present.

Note that if there is zero population growth, the foregoing analysis all holds in per-capita terms as well, so that the per-capita change in generational accounts from introducing Social Security is

```{math}
\bar{z}_{t} = \rfree_{t+1}\surplus_{1,t}/\Rfree_{t+1}
```

### Effects of Population Growth

If there is perpetual population growth, it is possible to finance a positive rate of return on Social Security contributions. Define

:::{margin}
Note that the definition of {math}`\surplus_{2,t+1}` is slightly different from usual because we divide by {math}`L_{t}` rather than {math}`L_{t+1}`.
:::

```{math}
:label: eq:zdef

\surplus_{1,t} = \Surplus_{1,t}/L_{t}
```

and assume there is constant population growth, {math}`\PopGro=L_{t+1}/L_{t}`. If we assume that Social Security taxes per capita are constant, then we can achieve a positive rate of return on Social Security contributions equal to the growth rate of population:

```{math}
\begin{aligned}
\surplus_{2,t+1} & = \Surplus_{2,t+1}/L_{t} \\
& = -\Surplus_{1,t+1}/L_{t} \\
& = -\left(\frac{\Surplus_{1,t+1}}{L_{t+1}}\right)\left(\frac{L_{t+1}}{L_{t}}\right) \\
& = -\surplus_{1,t+1}\PopGro = -\surplus_{1,t}\PopGro.
\end{aligned}
```

Not only does this prove that it is *possible* for the Social Security system to pay a rate of return equal to the rate of population growth - it proves that the *only* rate of return that is consistent with constant per-capita taxes on the young is a rate of return of {math}`\PopGro`.

:::{margin}
It is not only possible, but *necessary* to pay a positive return in an economy with perpetual population growth.
:::

### Effects of Productivity Growth and Population Growth

Suppose there is wage growth {math}`{\WGro}` betwen {math}`t` and {math}`t+1`, and suppose that workers contribute a constant *percentage* of their incomes to the Social Security system, {math}`\surplus_{1,t} = \zeta \Wage_{1,t}`. In this case it is possible to earn a rate of return on SS contributions equal to the product of the growth factor for wages and the growth factor for population:

```{math}
\begin{aligned}
\surplus_{1,t} & = \zeta \Wage_{1,t} \\
\Wage_{1,t+1} & = {\WGro}\Wage_{1,t} \\
\surplus_{2,t+1} & = -\Surplus_{1,t+1}/L_{t} \\
& = -(\Surplus_{1,t+1}/L_{t+1})(L_{t+1}/L_{t}) \\
& = -\zeta \underbrace{\Wage_{1,t+1}}_{= {\WGro} \Wage_{1,t}} \PopGro \\
& = -\zeta \Wage_{1,t}{\WGro} \PopGro \\
& = -\surplus_{1,t} {\WGro}\PopGro
\end{aligned}
```

so viewed from the perspective of the young generation in period {math}`t`, their Social Security contributions are returned to them larger by a factor of {math}`{\WGro}\PopGro` than what they paid in; the effective rate of return is therefore {math}`{\WGro}\PopGro`.

### Generational Accounts in a Growing Economy

Now consider the per-capita generational accounts in an economy with constant population growth and constant wage growth and a Social Security system that imposes a constant tax of {math}`\zeta` on the wages of the young:

```{math}
\begin{aligned}
\bar{z}_{t} & = \surplus_{1,t}+\surplus_{2,t+1}/\Rfree_{t+1} \\
& = \zeta \Wage_{1,t}- {\WGro}\PopGro \zeta \Wage_{1,t}/\Rfree_{t+1} \\
& = \zeta \Wage_{1,t}\left(1 - {\WGro}\PopGro/\Rfree_{t+1}\right) \\
& = \zeta \Wage_{1,t}\left(\frac{\Rfree_{t+1} - {\WGro}\PopGro}{\Rfree_{t+1}}\right).
\end{aligned}
```

Note that this expression will be *negative* if {math}`{\WGro}\PopGro>\Rfree_{t+1}`, meaning that the introduction of a Social Security system with a positive tax rate {math}`\zeta` actually *improves* the lifetime budget constraint! This is another way of seeing that an economy is *dynamically inefficient* if the return factor for capital {math}`\Rfree` is less than the product of the population growth and productivity growth factors. (Or, using approximations, the rate of return is less than the sum of the population growth rate and the productivity growth rate).

:::{admonition} Scraps/draft material
:class: dropdown

It will often be convenient to write generation accounts in per-capita terms rather than in aggregate terms. Thus define

```{math}
\begin{aligned}
\surplus_{1,t} & = \Surplus_{1,t}/L_{t} \\
\surplus_{2,t+1} & = \Surplus_{2,t+1}/L_{t+1}.
\end{aligned}
```
:::
