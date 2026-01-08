# A Gentle Introduction to Intertemporal Choice

Lecture notes on consumption, saving, growth, and asset pricing for advanced masters and first-year PhD students in economics.

**Authors:** Christopher D. Carroll and Alan E. Lujan Solis

**Institution:** Johns Hopkins University

## About

These lecture notes introduce the foundations of modern macroeconomic theory. Starting from first principles, we develop the mathematical tools and economic intuition needed to understand how agents make decisions over time under certainty and uncertainty.

We derive results analytically while connecting theory to computational methods and empirical applications. Each topic proceeds from simple benchmark models to extensions that incorporate additional features.

The notes originated from Christopher Carroll's [graduate macroeconomics lecture notes](https://www.econ2.jhu.edu/people/ccarroll/public/lecturenotes/) at Johns Hopkins University. Alan Lujan teaches from these materials in the advanced macroeconomics sequence of JHU's masters economics program.

:::{tip} For Instructors
These materials are freely available under a CC-BY-4.0 license. Instructors at other institutions are welcome to use, adapt, and redistribute them for teaching.
:::

## Contents

### Consumption

From perfect foresight through OLG to buffer stock models:

- Perfect foresight consumption under CRRA and CARA utility
- The permanent income hypothesis and consumption smoothing
- Precautionary saving and buffer-stock behavior
- Risk premia and the effects of uncertainty
- Overlapping generations and lifecycle models
- Habits, hyperbolic discounting, and behavioral extensions

### Asset Pricing

Lucas, Mehra and Prescott, Blanchard, and others:

- CRRA and CARA portfolio allocation
- The consumption-based capital asset pricing model (C-CAPM)
- The equity premium puzzle
- Multi-asset portfolio optimization

### Growth

Models of economic growth:

- The Ramsey-Cass-Koopmans model
- Fiscal policy in growth models
- Decentralization and competitive equilibrium
- Endogenous growth (Romer, Lucas, Rebelo AK)
- Overlapping generations growth models

### Investment

From Keynes to imperfections:

- The Hall-Jorgenson neoclassical model
- Tobin's q and the marginal q model
- Capital market imperfections
- Investment and cash flow sensitivity

### DSGE Models

Dynamic stochastic general equilibrium frameworks:

- The Brock-Mirman stochastic growth model
- Real business cycle theory

### Mathematical Appendix

Derivations and methods useful for macroeconomics:

- Useful facts for graduate macroeconomics
- Aggregation methods
- Approximation techniques for lognormal distributions

## Building the Book

This book is built using [MyST Markdown](https://mystmd.org/). To build locally:

```bash
uv sync
uv run myst build --html
```

The live version is available at the project website.

## License

- Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- Code: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Acknowledgments

Development supported by the [Econ-ARK](https://econ-ark.org/) project with funding from the Alfred P. Sloan Foundation.

:::{seealso}
The [HARK](https://docs.econ-ark.org/) toolkit provides computational implementations of many models covered in these notes, including buffer-stock consumption, portfolio choice, and lifecycle models.
:::

## Citation

If you use these materials, please cite:

> Carroll, Christopher D. and Alan E. Lujan Solis. *A Gentle Introduction to Intertemporal Choice*. Johns Hopkins University. https://github.com/jhu-econ/intertemporal-choice
