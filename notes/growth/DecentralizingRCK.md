(sec:decentralizingrck)=

# Decentralizing the Ramsey/Cass-Koopmans Model
<!-- \newboolean{NumericalSolution} -->
<!-- \setboolean{NumericalSolution}{true} -->
<!-- \setboolean{NumericalSolution}{false} -->
<!-- \renewcommand{\cite}{\citeyearpar} -->

This section shows that under certain very special conditions the

behavior of an economy composed of distinct individual households will

replicate the social planner’s solution to the Ramsey/Cass-Koopmans

model.

## The Consumer’s Problem

Consider first the problem of an individual infinitely lived consumer

indexed by {math}`i` who has some predetermined set of expectations for

how the aggregate net interest rate {math}`\rfree_{t}` and wage rate {math}`\Wage_{t}` will

evolve.

At date {math}`t` household {math}`i` owns some capital {math}`\kap_{t,i}`, and can in principle also

borrow; designate the net debt of household {math}`i` in period {math}`t` as

{math}`\debt_{t,i}`; since we will be examining a perfect foresight solution with

perfect capital markets, the interest rate on debt must match the

rate of return on assets. This means that all that really matters is

the household's total net asset position,

:::{margin}
Each household can 'issue bonds' which is like borrowing; you promise to pay interest to the bondholder.
:::

```{math}
\begin{gathered}\begin{aligned}
        \wNet_{t,i} & =  \kap_{t,i} - \debt_{t,i}.
\end{aligned}\end{gathered}
```

Each household is endowed with one unit of labor, which it

supplies exogenously, earning a wage rate {math}`\Wage_{t,i}`.

:::{margin}
We will determine below how {math}`\Wage_{t}` is determined; take it as exogenous here.
:::

Each household solves:

```{math}
\max \int_{0}^{\infty} \uFunc(\cons_{t,i}) e^{-\timeRate t} dt
```

subject to the budget constraint

```{math}
\dot{\wNet}_{t,i} = \Wage_{t} + \rfree_{t} \wNet_{t,i} - \cons_{t,i}
.
```

Integrating the household’s dynamic budget constraint and assuming

a no-Ponzi-game transversality condition yields the

intertemporal budget constraint, which says that the present

discounted value of consumption must match the PDV of labor

income plus the current stock of net wealth:

```{math}
\begin{gathered}\begin{aligned}
        \mathbb{P}_{0,i}(\cons) & =  \mathbb{P}_{0,i}(\Wage)+\wNet_{0,i}.
\end{aligned}\end{gathered}
```

The formulas for these PDV’s are a bit awkward because they must

take account of the fact that interest rates are varying over time.

To make the formulas a bit simpler, define the compound interest factor

```{math}
\begin{gathered}\begin{aligned}
        \RCpnd_{t}^{-1} & =  \exp(-\int_{0}^{t} \rfree_{\tau} d\tau),
\end{aligned}\end{gathered}
```

which is simply the compound interest term needed to convert a value

at date {math}`t` to its PDV as of time 0.

With this definition in hand we can write the IBC as

```{math}
\begin{gathered}\begin{aligned}
        \int_{0}^{\infty} \cons_{t,i} \RCpnd^{-1}_{t} dt & =  h_{0,i}+ \wNet_{0,i}
\end{aligned}\end{gathered}
```

where {math}`h_{0,i}` is human wealth,

```{math}
:label: eq:humwealth

\begin{gathered}\begin{aligned}
        h_{0,i} & =  \int_{0}^{\infty} \Wage_{t} \RCpnd^{-1}_{t} dt. 
\end{aligned}\end{gathered}
```

Each household solves the standard optimization problem taking

the future paths of wages and interest rates as *given*. Thus

the Hamiltonian[^p637GulAXn]

[^p637GulAXn]: See [](#sec:RamseyCassKoopmans) for the discounted Hamiltonian optimality conditions and [](#sec:HamiltonianVSDiscrete) for the intuition

    of the logic behind the Hamiltonian. is

```{math}
\Ham(\cons_{t,i},\wNet_{t,i},\lambda_{t,i}) = \uFunc(\cons_{t,i}) + (\rfree_{t}\wNet_{t,i}+\Wage_{t}-\cons_{t,i})\lambda_{t,i}
```

which implies that the first optimality condition is the usual {math}`\uP(\cons_{t,i}) = \lambda_{t,i}`.

The second optimality condition is

```{math}
\begin{gathered}\begin{aligned}
        \dot{\lambda}_{t,i} & =  \timeRate \lambda_{t,i} - (\partial \Ham/\partial \wNet) \\
        \dot{\lambda}_{t,i} & =  \timeRate \lambda_{t,i} - \lambda_{t,i} \rfree_{t} \\
        \dot{\lambda}_{t,i}/\lambda_{t,i} & =   (\timeRate - \rfree_{t})
\end{aligned}\end{gathered}
```

leading eventually to the usual first order condition for consumption:

```{math}
:label: eq:cdotindiv

\begin{gathered}\begin{aligned}
        \dot{\cons}_{t,i}/\cons_{t,i} & =  \CRRA^{-1}(\rfree_{t}-\timeRate) .
\end{aligned}\end{gathered}
```

Note (for future use) that the RHS of this equation does not contain

any components that are idiosyncratic: The consumption growth rate will

be identical for every household. The same is true of the expression

for human wealth, equation {eq}`eq:humwealth`.

## The Firm's Problem

Now we assume that there are many perfectly competitive small firms indexed by {math}`j`

:::{margin}
Because of the perfect competition and CRS assumptions, it doesn't matter exactly how many firms there are; firms are 'atomistic' like households; like HH's, they take {math}`\Wage_{t}` and {math}`\rfree_{t}` as given.
:::

in this economy, each of which has a production function identical to

the aggregate Cobb-Douglas production function. Perfect competition

implies that individual firms take the interest

rate {math}`\hat{\rfree}_{t}` and wage rate {math}`\hat{\Wage}_{t}` to be exogenous. Hence

firms solve

:::{margin}
Note that we are back to the Hall-Jorgensen model with no adjustment costs, so the firm problem has no important intertemporal dimension.
:::

```{math}
\max_{\{K_{t,j},L_{t,j}\}} \FFunc(K_{t,j},L_{t,j}) - \hat{\Wage}_{t}L_{t,j} - \hat{\rfree}_{t}K_{t,j}
```

where {math}`\hat{\rfree}_{t}` and {math}`\hat{\Wage}_{t}` are the rental rates for a unit

of capital and a unit of labor for one period. Note that, dividing by

{math}`L_{t,j}`, this is equivalent to

```{math}
\max_{\{ \kap_{t,j} \}} \underbrace{\kap_{t,j}^{\alpha}}_{\fFunc(\kap_{t,j})} - \hat{\Wage}_{t} - \hat{\rfree}_{t} \kap_{t,j}.
```

The first order condition for this problem implies that

```{math}
\begin{gathered}\begin{aligned}
        \fFunc^{\prime}(\kap_{t,j}) & =  \hat{\rfree}_{t}.
\end{aligned}\end{gathered}
```

Under perfect competition firms must make zero profits in equilibrium,

which means, by [Euler's Theorem](#fact:eulerstheorem), that:

```{math}
\begin{gathered}\begin{aligned}
        \fFunc(\kap_{t,j}) & =  \hat{\Wage}_{t}+\hat{\rfree}_{t}\kap_{t,j}.
\end{aligned}\end{gathered}
```

## Equilibrium At a Point in Time

Thus far, we have solved the consumer's and the firm's problems

from the standpoint of atomistic individuals. It is now time to

consider the behavior of an aggregate economy composed of consumers

and firms like these.

We assume that the population of households and firms is distributed

along the unit interval and the population masses sum to one,

as per [](#sec:Aggregation). Thus, aggregate assets at time {math}`t`

can be defined as the sum of the assets of all the individuals in the

economy at time {math}`t`,

```{math}
\begin{gathered}\begin{aligned}
  \WNet_{t} & =  \int_{0}^{1} \wNet_{t,i}  di
\end{aligned}\end{gathered}
```

while per capita assets are aggregate assets divided by aggregate population,

```{math}
\begin{gathered}\begin{aligned}
  \wNet_{t} & =  \WNet_{t}/1.
\end{aligned}\end{gathered}
```

Similarly, normalizing the population of firms to one yields

```{math}
\begin{gathered}\begin{aligned}
  \kap_{t} & =  K_{t}/1.
\end{aligned}\end{gathered}
```

Up to this point, we have allowed for the possibility that different

households might have different amounts of net worth. We now impose

the assumption that every household is identical to every other

household. This assumption rules out the presence of any debt in

equilibrium (if all households are identical, they cannot all be in

debt - who would they owe the money to?). Indeed, in this case, the

aggregate capital stock per capita will equal the aggregate level of

net worth, {math}`\kap_{t}=\wNet_{t}`.[^byRa82hkCt]

[^byRa82hkCt]: The results do not change if we permit differences in the levels of wealth across households, but

    this is because we are assuming CRRA utility, perfect certainty,

    perfect capital markets, and various other things. When any of

    these assumptions is relaxed, the distribution of assets does

    matter. For exploration of this more complex and realistic

    framework, see {cite:t}`carroll:brookings`, {cite:t}`aiyagari:ge`,

    {cite:t}`ksHetero`, {cite:t}`carrollRequiem`.

Thus, households’ expectations about {math}`\Wage_{t}` and

{math}`\rfree_{t}` determine their saving decisions, which in turn determine the

aggregate path of {math}`\kap_{t}`.

There is one important subtlety here, however. In writing the

consumer’s budget constraint, we designated {math}`\rfree_{t}` as the net amount

of income that would be generated by owning one more unit of net worth

(e.g.  capital). But if we have depreciation of the capital stock,

the net return to capital will be equal to the marginal product *minus*

depreciation. The discussion of the firm’s optimization problem did

not consider depreciation because the firms do not own any capital;

instead, they make a payment {math}`\hat{\rfree}_{t}` to the households for the

privilege of using the households’ capital. Thus the net increment to

a household’s wealth if the household holds one more unit of capital

will be

```{math}
\begin{gathered}\begin{aligned}
        \rfree_{t} & =  \hat{\rfree}_{t}-\depr.
\end{aligned}\end{gathered}
```

There is no depreciation of labor, so the labor market equilibrium

will be

```{math}
\begin{gathered}\begin{aligned}
        \Wage_{t} & =  \hat{\Wage}_{t}
\\        & =  \fFunc(\kap_{t})- \hat{\rfree}_{t}\kap_{t}      
.
\end{aligned}\end{gathered}
```

## The Perfect Foresight Equilibrium

We assume that every household knows the aggregate production

function, and understands the behavior of all the other households and

firms in the economy. Understanding all of this, suppose that

households have some set of beliefs about the future path of the

aggregate capital stock per capita {math}`\{\kap_{t}\}_{t=0}^{\infty}`. This

belief about {math}`\kap_{t}` will imply beliefs about wages and interest rates

as well {math}`\{\Wage_{t},\rfree_{t}\}_{t=0}^{\infty}`.

The final assumption is that the equilibrium that comes about in this

economy is the “perfect foresight equilibrium.” That is, consumers

have the sets of beliefs such that, if they have those beliefs and act

upon them, the actual outcome turns out to match the beliefs.

:::{margin}
It can be shown that in this model there is only one 'self-validating' set of beliefs. Some other models may have multiple sets of beliefs all of which satisfy the condition that if everybody shares those beliefs, they will come true. Interesting area of macro that Thomas has done some important work in.
:::

Note now that using the fact that {math}`\wNet_{t}=\kap_{t}` in the perfect foresight

equilibrium we can rewrite the household’s budget constraint as

```{math}
:label: eq:DecRCK-aggkdot

\begin{gathered}\begin{aligned}
        \dot{\kap}_{t} & =  \rfree_{t}\kap_{t} + \Wage_{t} - \cons_{t} %
\\  & =  (\hat{\rfree}_{t}-\depr)\kap_{t} + \Wage_{t} - \cons_{t} 
.
\end{aligned}\end{gathered}
```

Reproducing from {eq}`eq:cdotindiv`,

```{math}
:label: eq:cdotagg

\begin{gathered}\begin{aligned}
        \dot{\cons}_{t}/\cons_{t} & =  \CRRA^{-1}(\rfree_{t}-\timeRate) %
\\  & =  \CRRA^{-1}(\hat{\rfree}_{t}-\depr-\timeRate)   .
\end{aligned}\end{gathered}
```

Now compare these to the equations derived for the social planner’s

problem (with population growth and productivity growth zero) in a

previous section:

```{math}
:label: eq:kdotsp

\begin{gathered}\begin{aligned}
        \dot{\kap}_{t} & =  \fFunc(\kap_{t})-\depr \kap_{t}-\cons_{t}  \\
         & =  \hat{\rfree}_{t}\kap_{t}+\Wage_{t}-\depr \kap_{t}-\cons_{t}  \\
         & =  (\hat{\rfree}_{t}-\depr) \kap_{t}+\Wage_{t}-\cons_{t} 
\end{aligned}\end{gathered}
```

and

```{math}
:label: eq:cdotsp

\begin{gathered}\begin{aligned}
        \dot{\cons}_{t}/\cons_{t} & =  \CRRA^{-1}(\fFunc^{\prime}(\kap_{t})-\depr-\timeRate). 
\end{aligned}\end{gathered}
```

Since the equilibrium value of {math}`\hat{\rfree}_{t}=\fFunc^{\prime}(\kap_{t})`,

{eq}`eq:cdotsp` = {eq}`eq:cdotagg`. And {eq}`eq:DecRCK-aggkdot` is

identical to {eq}`eq:kdotsp`. Thus, aggregate behavior of this economy

is identical to the behavior of the social planner’s economy!

This is a very convenient result, because it means that if we are

careful about the exact assumptions we make we can often solve a

social planner’s problem and then assume that the solution also

represents the results that would obtain in a decentralized economy.

The social planner’s solution and the decentralized solution are the

same because they are maximizing the same utility function with

respect to the same factor prices ({math}`\rfree_{t}` and {math}`\Wage_{t}`).

When will the decentralized solution *not* match the social

planner’s solution? One important case is when there are

externalities in the behavior of individual households; another

possible case is where there is idiosyncratic risk but no aggregate

risk; basically, whenever the household’s budget constraint or utility

function differs in the right ways from the aggregate budget

constraint or the social planner’s preferences, there can be a

divergence between the two solutions.


:::{admonition} Scraps/draft material
:class: dropdown

```{math}
\begin{gathered}\begin{aligned}
        \int_{0}^{\infty} \uFunc(c) e^{-\timeRate t}
\end{aligned}\end{gathered}
```

subject to

```{math}
\begin{gathered}\begin{aligned}
        \dot{\kap} & =  \fFunc(\kap) - \cons - \tau.
\end{aligned}\end{gathered}
```

which has Hamiltonian representation

```{math}
\Ham(\kap,c,\lambda) = \uFunc(c) + \lambda(\kap^{\alpha} - \cons - \tau)
```

The first Hamiltonian optimization condition requires {math}`\partial
 H/\partial \cons = 0`:

```{math}
:label: eq:DecRCK-H1A

\begin{gathered}\begin{aligned}
        \cons^{-\CRRA} & =  \lambda   \\
        -\CRRA \cons^{-\CRRA-1}\dot{\cons} & =  \dot{\lambda} %
\end{aligned}\end{gathered}
```

The second Hamiltonian optimization condition requires:

```{math}
\begin{gathered}\begin{aligned}
        \dot{\lambda} & =  \timeRate\lambda - \lambda(\partial \Ham/\partial k)  \\
         & =  \timeRate\lambda - \lambda \fFunc^{\prime}(\kap)
\\      \dot{\lambda}/{\lambda} & =  (\timeRate-\fFunc^{\prime}(\kap))
\\  \dot{\cons}/\cons  & =  \CRRA^{-1}(\fFunc^{\prime}(\kap)-\timeRate).
\end{aligned}\end{gathered}
```

Thus, the {math}`\dot{\cons}=0` locus in the phase diagram is unchanged.

However, the {math}`\dot{\kap}` locus is shifted down by amount {math}`\tau =
 \sigma`.

Now what happens if the government does not face a balanced budget

requirement? Specifically, suppose {math}`\debt` is the level of government

debt, and the government's Dynamic Budget Constraint is

```{math}
\begin{gathered}\begin{aligned}
        \dot{d} & =  \sigma-\tau+r d
\end{aligned}\end{gathered}
```

The government's IBC will be the integral of the DBC:

```{math}
\begin{gathered}\begin{aligned}
        \debt_{0}+\int_{0}^{\infty}\sigma R   & =  \int_{0}^{\infty} \tau R   \\
        \debt_{0}+G_{0} & =  T_{0}
\end{aligned}\end{gathered}
```

The DBC of the representative family also changes. They can now own

either capital {math}`\kap` or government debt {math}`\debt`. If the family is to be

indifferent between the two forms of assets, the interest rate must be

the same.

```{math}
\begin{gathered}\begin{aligned}
        \cons + \dot{\wNet} & =  \Wage + \rfree \wNet - \tau  \\
        \wNet & =  \kap + \debt
\end{aligned}\end{gathered}
```

The assumption of labor augmenting technological progress was made

because it implies that in steady-state {math}`\dot{\cons}=0` and {math}`\dot{C}/C =
 \dot{Y}/Y = \dot{K}/K = \wGro`.

{math}`\dot{\cons}/\cons = 0` implies that at the steady-state value of {math}`\bar{\kap}`

```{math}
\begin{gathered}\begin{aligned}
        \fFunc^{\prime}(\bar{\kap}) & =  \timeRate+\popGro+\depr+\CRRA \wGro  \\
        \alpha \bar{\kap}^{\alpha-1} & =  \timeRate+\popGro+\depr+\CRRA \wGro  \\
        \bar{\kap} & =  \left(\frac{\timePref+\popGro+\depr+\CRRA \wGro}{\alpha}\right)^{\frac{1}{\alpha-1}}
\\      \bar{\kap} & =  \left(\frac{\alpha}{\timePref+\popGro+\depr+\CRRA \wGro}\right)^{\frac{1}{1-\alpha}}
\end{aligned}\end{gathered}
```

Thus, the steady-state capital/output ratio will be higher if capital

is more productive ({math}`\alpha` is higher), and will be lower if

consumers are more impatient, population growth is faster,

depreciation is higher, or technological progress is higher (assuming

\CRRA>1).
:::