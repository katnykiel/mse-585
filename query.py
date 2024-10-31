from fireworks import LaunchPad
from jobflow import SETTINGS
from pymatgen.core import Structure
from kat.atomate2.utils import get_convex_hulls

store = SETTINGS.JOB_STORE

# connect to the job store (mongodb)
store.connect()
lpad = LaunchPad.auto_load()

docs = list(store.query(
    {
        "metadata.tags": {
            "$all": [
                "mse-585-test",
            ]
        },
        "name": "relax 1",
    }
))

for i, doc in enumerate(docs):
    struct = Structure.from_dict(doc["output"]["structure"]) # type: ignore

# Construct convex hulls
figs = get_convex_hulls(docs, write_results=True, show_unstable=0.5)
figs[0].show()  # type: ignore

figs[0].write_image("convex_hull.png", scale=3)  # type: ignore
pass

