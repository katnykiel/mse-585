# import libraries
from fireworks import LaunchPad
from atomate2.vasp.flows.core import DoubleRelaxMaker
from atomate2.vasp.powerups import update_user_incar_settings
from jobflow.managers.fireworks import flow_to_workflow
from pymatgen.core import Structure

lpad = LaunchPad.auto_load()

struct = Structure.from_file("vbr2.cif")

# create a double relaxation workflow
relax_flow = DoubleRelaxMaker(name=f"mse 585").make(struct)
gga_incar_updates = {
    "NCORE": 8,
    "GGA": "PE",
    "ENCUT": 550
}

relax_flow = update_user_incar_settings(relax_flow, gga_incar_updates)

# add the workflow to the launchpad
wf = flow_to_workflow(relax_flow) # type: ignore
for fw in wf.fws:
    fw.spec.update({
            "tags": [
                "mse-585-test"
            ]
        }
    )
lpad.add_wf(wf)