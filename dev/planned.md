# Planned changes to the book

Each entry is a deferred ruling: a change to make to the book's material once its trigger fires.
`code/check_planned.py` reads this file. The format and the triggers are in that script's
docstring. Every build checks this file and reports what is due as a warning, without blocking
the deploy. A sweep at the start of each term reads it again:

    python code/check_planned.py --root . dev/planned.md

Markers live here, not in `content/`: MyST publishes comments in a page's JSON and HTML, so a
marker in a chapter would be on the live site. This folder is never built, and the repository
split keeps it private. Until then it is public on GitHub, so it holds routine edits only.
Name the material by its title or label, never by a number.

PLANNED(when-merged econ-ark/DemARK#287 AND when-live https://econ-ark.github.io/DemARK/perfforesightcrra-convergence/; Chris 2026-10-07): In "Consumption Under Perfect Foresight and CRRA Utility", replace the two companion-notebook links at the top with links to DemARK's own site, not econ-ark.org: perfforesightcrra-convergence and perfforesightcrra-savingrate, with a clause each on what the notebook does. At the approximate perfect-foresight consumption function, add one sentence: the perfect-foresight consumption function is exact; the approximation treats r, ϑ and the return patience rate as small, and its error is distinct from the error of a numerical solution. One pull request for both.
  Target: content/consumption/PerfForesightCRRA.md: "Two companion notebooks in the Econ-ARK DemARK collection"
  Target: content/consumption/PerfForesightCRRA.md: ":label: eq:PFCRRA-capprox"
