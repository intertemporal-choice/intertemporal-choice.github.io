"""Re-execute the Fisher notebook in place so its stored outputs and ipywidgets state
match the current source. Regenerate whenever the code changes.

The stored state is NOT what the site shows before a reader starts a kernel. mystmd
carries the widget state into the built page and never mounts the ipywidgets embed
manager, so a reader sees the text/plain repr until they press the power button AND
run all. The state still has to be current, because it is
what a kernel-less consumer of the .ipynb file itself (nbviewer, GitHub, a local Jupyter)
renders.
"""

import logging
from pathlib import Path

import nbformat
from nbclient import NotebookClient

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

path = Path("content/consumption/FisherTwoPeriod.ipynb")
nb = nbformat.read(path, as_version=4)

# 600s per cell, up from 120s: each interact() cell solves the HARK model when it is
# instantiated, and 120s proved too tight on a cold kernel.
client = NotebookClient(nb, timeout=600, kernel_name="python3", allow_errors=False)
client.execute()
nbformat.write(nb, path)

state = nb.metadata.get("widgets", {}).get("application/vnd.jupyter.widget-state+json", {})
outputs = [
    m for m in state.get("state", {}).values() if m.get("model_name") == "OutputModel"
]
images = [
    key
    for m in outputs
    for out in m.get("state", {}).get("outputs", [])
    for key in (out.get("data") or {})
]
log.info("widget models stored: %d", len(state.get("state", {})))
log.info("Output widgets: %d, embedded mime types: %s", len(outputs), sorted(set(images)))
