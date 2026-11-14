# The book's package files

Every release of the book's Python package, `intertemporal-choice`, one wheel each, with `releases.txt` listing
them. The site serves them at https://intertemporal-choice.github.io/packages/.

Only `code/release_package.py` writes this branch, from the workflow, and only by adding a wheel and its line. A
file here is never changed or deleted, and the branch is never force-pushed: posted answer keys install these
files by their addresses. Install a release by its address, never by name, since the name is not on PyPI.
