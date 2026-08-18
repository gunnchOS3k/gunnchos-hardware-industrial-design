# Traceability matrix — hardware industrial design

Every diagram element maps to a real path. Missing silicon evidence stays `PHYSICAL_PENDING`.

| Diagram element | Source path |
|---|---|
| Digital readiness | `DIGITAL_MANUFACTURING_READINESS.md` |
| EVT bring-up packet | `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md` |
| RFQ send packet | `docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md` |
| OpenSCAD | `cad/openscad/` |
| STL placeholders | `exports/stl/` |
| Family BOM CSVs | `bom/*.csv`, `device_designs/*/bom/assembly_bom.csv` |
| KiCad projects | `device_designs/{handheld_hybrid,student_14_5,ds_xl_coder,edge_io_rings,dock}/kicad/` |
| Power trees | `device_designs/*/electrical/power_tree.yaml` |
| Stackup | `device_designs/*/manufacturing/stackup.yaml` |
| ERC/DRC status (historical) | `device_designs/*/manufacturing/ERC_DRC_STATUS.json` |
| This-run EDA | `artifacts/supervisor_ready_eda/` |
| Handheld ICD | `device_designs/handheld_hybrid/docs/som_carrier_icd.md` |
| Firmware contracts | `firmware/interfaces/*.yaml` |
| Firmware manifests | `firmware/manifests/*.yaml` |
| Firmware/OS requirements | `firmware_os_interface/` |
| OS exports | `os_compatibility/device_class_exports/` |
| OS interface map | `os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md` |
| RFQ folders | `manufacturing/rfq/` |
| Validator | `scripts/validate_digital_manufacturing.py` |
| EDA check script | `scripts/run_supervisor_eda_checks.sh` |
| CI | `.github/workflows/ci.yml`, `hardware-package-ci.yml` |
| Power-state contract | `firmware/interfaces/power_state_contract.yaml` |
| Claim boundary | `product/CLAIM_BOUNDARY.md` |
