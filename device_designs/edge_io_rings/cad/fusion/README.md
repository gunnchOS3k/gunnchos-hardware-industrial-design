# Rings — Fusion-native CAD package

Updated: 2026-08-08T19:40:00Z  
Token: `RING_FUSION_NATIVE_CAD_PACKAGE_DOCUMENTED`

## Native intent
Autodesk Fusion 360 is the **native** mechanical toolchain for Edge I/O Rings (band, inner PCB pocket, pogo faces, size grades).

## Package contents (this folder)
- `parameters.yaml` — parametric ring sizes / PCB pocket / antenna keepout
- `timeline.md` — Fusion timeline feature recipe (reproducible without binary)
- `export_manifest.yaml` — STEP/STL/3MF export targets
- `EDMUND_ACTION_REQUIRED.md` — Fusion app / `.f3d` binary authoring

## Twin
Open-source geometric twin remains at:
- `gate1_digital_fabrication/edge_io_ring/mechanical/edge_io_ring.scad`
- `cad/openscad/wearables/` concepts

PHYSICAL_EXECUTION_FREEZE — no print/fab.
