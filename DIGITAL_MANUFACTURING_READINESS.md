# Digital manufacturing readiness

**Repo:** `gunnchos-hardware-industrial-design`  
**Branch intent:** supervisor-ready DIGITAL packet (documentation, validators, EDA hygiene).  
**Family claim:** `PHYSICAL_PENDING` + `EXTERNAL_PENDING`.

This file lists every digital prerequisite that exists in-tree, every specification that cannot be verified from public design inputs, and the exact remaining physical / owner actions. It does **not** authorize fabrication, purchase, RFQ send, or certification.

## Status tokens (this pass)

| Token | Value | Meaning |
|---|---|---|
| `DIGITAL_MANUFACTURING_PACKET_PREPARED` | **TRUE** | Packets, UML, OS/hardware interface map, and validators exist |
| `DIGITAL_FABRICATION_PASS` | **FALSE** | Do not treat digital ERC/DRC or Gerber export as fab complete |
| `HANDHELD_HW_DIGITAL_RELEASE_PACKAGE` | earned in `device_designs/handheld_hybrid/digital_release/INDEX.json` | Public-pinout digital package; **not** EVT/DVT/PVT |
| `STUDENT_HW_DIGITAL_RELEASE_PACKAGE` | **not earned** | COM-HPC pin-accurate fanout `EXTERNAL_PENDING` |
| `DSXL_HW_DIGITAL_RELEASE_PACKAGE` | **not earned** | COM-HPC + dual-eDP pin map `EXTERNAL_PENDING` |
| `DOCK_HW_DIGITAL_RELEASE_PACKAGE` | **not earned** | Intel JHL8440 / JHL9040R ball maps `EXTERNAL_PENDING` |
| `EDGE_IO_RINGS` digital EDA | recorded | nRF52840 public path; physical boot still `PHYSICAL_PENDING` |
| `PREMANUFACTURING_RELEASE_READY` (all SKUs) | **FALSE** | See `manufacturing/*/PREMANUFACTURING_READINESS.md` |
| `RFQ_SENT` | **FALSE** | Owner action only; Cursor does not send |
| `FCC` / `CE` / `USB-IF` | **not claimed** | Digital prep only (`docs/full_product_family/CERT_DIGITAL_PREP.md`) |
| `PHYSICAL_EVT` | `PHYSICAL_PENDING` | No assembled unit, no measured rails |

`PHYSICAL_PENDING` is **not** converted into `DIGITAL_PASS` for fabrication.

## Claim boundary

Safe digital claim: this repository holds EVT-oriented design sources (CAD, BOM, KiCad, firmware contracts, OS exports) and RFQ *packets* suitable for engineering review.

Not claimed: fabrication release, purchase authorization, RFQ_SENT, FCC/CE/UKCA/USB-IF/UN38.3, DVT/PVT, shipping hardware, invented NDA pin maps, invented electrical measurements.

## Digital prerequisites (exist in-tree)

### 1. Product / architecture

| Prerequisite | Path | Digital status |
|---|---|---|
| PRD | `product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md` | present |
| Claim boundary | `product/CLAIM_BOUNDARY.md` | present |
| EVT-1 acceptance | `product/EVT1_ACCEPTANCE_CRITERIA.md` | present |
| Architecture contract | `architecture/OS_HARDWARE_CONTRACT.md` | present |
| OS-facing contract | `docs/OS_HARDWARE_CONTRACT.md` | present |
| Manufacturing claim boundary | `docs/MANUFACTURING_CLAIM_BOUNDARY.md` | present |

### 2. CAD / mechanical

| Prerequisite | Path | Digital status |
|---|---|---|
| OpenSCAD family models | `cad/openscad/*.scad` | present (EVT-0/EVT-1 placeholder geometry) |
| Concept models | `cad/openscad/{student_14_5,handheld_hybrid,ds_xl_coder}/` | present |
| Common modules | `cad/openscad/common/*.scad` | present |
| STL placeholders | `exports/stl/*_placeholder.stl` | present; not first-article print |
| Export status | `exports/OPENSCAD_EXPORT_STATUS.md` | present |
| Mechanical targets | `mechanical_correctness/device_mechanical_targets.json` | documented, not physically proven |
| Printability | `printability/` | gate definitions only |

This-run OpenSCAD parse is recorded with KiCad in the electrical EDA subsection below. Parse success is **not** a certified mechanical drawing.

### 3. BOM / AVL

| SKU | Assembly BOM | Notes |
|---|---|---|
| Handheld Hybrid | `device_designs/handheld_hybrid/bom/assembly_bom.csv` | SoM **RM121-D8E32** frozen; several connectors `AVL_PENDING` |
| Student 14.5 | `device_designs/student_14_5/bom/assembly_bom.csv` | COM-HPC MPN named; pin-accurate fanout blocked |
| DS-XL Coder | `device_designs/ds_xl_coder/bom/assembly_bom.csv` | shared COM-HPC; dual-eDP AVL open |
| Edge I/O Rings | `device_designs/edge_io_rings/bom/assembly_bom.csv` | nRF52840-QIAA-R public |
| Dock | `device_designs/dock/bom/assembly_bom.csv` | JHL8440 topology; package balls NDA |
| Legacy four-class CSVs | `bom/{student_14,handheld_hybrid,ds_xl_coder,wearables_arena}_bom.csv` | EVT-1 schema |

Master index: `bom/MASTER_BOM.md`. Unknown vendor fields must stay unknown (`scripts/validate_supply_chain_fields.py`).

### 4. Electrical / KiCad

| SKU | Schematic | PCB | Power tree (MODELED / PUBLIC_DOCS) | Stackup |
|---|---|---|---|---|
| Handheld | `device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch` | `.kicad_pcb` | `device_designs/handheld_hybrid/electrical/power_tree.yaml` | `device_designs/handheld_hybrid/manufacturing/stackup.yaml` |
| Student | `device_designs/student_14_5/kicad/student_14_5.kicad_sch` | `.kicad_pcb` | `device_designs/student_14_5/electrical/power_tree.yaml` | `device_designs/student_14_5/manufacturing/stackup.yaml` |
| DS-XL | `device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_sch` | `.kicad_pcb` | `device_designs/ds_xl_coder/electrical/power_tree.yaml` | `device_designs/ds_xl_coder/manufacturing/stackup.yaml` |
| Rings | `device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch` | `.kicad_pcb` | `device_designs/edge_io_rings/electrical/power_tree.yaml` | `device_designs/edge_io_rings/manufacturing/stackup.yaml` |
| Dock | `device_designs/dock/kicad/dock.kicad_sch` | `.kicad_pcb` | `device_designs/dock/electrical/power_tree.yaml` | `device_designs/dock/manufacturing/stackup.yaml` |

Family system-block skeletons (not production schematics): `schematics/*/`.

Historical recorded ERC/DRC (2026-08-15 tip-accurate run, **not** this-run unless `artifacts/supervisor_ready_eda` matches):

| SKU | ERC errors | ERC warnings | DRC errors | DRC warnings | Source |
|---|---:|---:|---:|---:|---|
| handheld_hybrid | 0 | 461 | 0 | 39 (`lib_footprint_mismatch`) | `device_designs/handheld_hybrid/manufacturing/ERC_DRC_STATUS.json` |
| student_14_5 | 0 | 40 | 0 | 50 (dangling/silk/mismatch) | `device_designs/student_14_5/manufacturing/ERC_DRC_STATUS.json` |
| ds_xl_coder | 0 | 45 | 0 | 51 | `device_designs/ds_xl_coder/manufacturing/ERC_DRC_STATUS.json` |
| edge_io_rings | 0 | 27 | 0 | 22 | `device_designs/edge_io_rings/manufacturing/ERC_DRC_STATUS.json` |
| dock | 0 | 19 | 0 | 39 | `device_designs/dock/manufacturing/ERC_DRC_STATUS.json` |

Zero ERC/DRC **errors** is digital hygiene. Warnings remain. `si_simulation_performed: false` on handheld stackup. Cont IX Gerbers under `device_designs/*/manufacturing/cont_ix_release/` are engineering exports, **not** a manufacturing release. `pcb/GERBER_OUTPUT_STATUS.md` still correctly refuses a production-Gerber claim.

This-run CLI (`kicad-cli` 10.0.5, 2026-08-18T17:15:23Z) matches the historical error/warning counts above. Compact record: `artifacts/supervisor_ready_eda/kicad_cli_meta.json` via `scripts/run_supervisor_eda_checks.sh`. `DIGITAL_FABRICATION_PASS` remains **FALSE**.

This-run OpenSCAD parse (`/opt/homebrew/bin/openscad`): all seven listed `.scad` files `rc=0` (`artifacts/supervisor_ready_eda/openscad_meta.json`). Parse success is **not** a first-article print.

Public handheld pinout ICD (no invented remux): `device_designs/handheld_hybrid/docs/som_carrier_icd.md`.

### 5. Firmware (harness only)

| Artifact | Path | Physical |
|---|---|---|
| Manifests | `firmware/manifests/*.yaml` | pending |
| Interface contracts | `firmware/interfaces/*_contract.yaml` | pending |
| ACPI / DT stubs | `firmware/descriptors/` | pending |
| Boot contracts | `firmware/boot/` | pending |
| QEMU/OVMF dry-run | `firmware/qemu/` | not board boot |
| Capsule simulation | `firmware/capsule_update/` | simulated_only |
| Ring Zephyr west | `firmware/edge_io_rings/zephyr_west/` | digital build ≠ physical boot |
| Firmware/OS reqs | `firmware_os_interface/` | pending |

See `firmware/CLAIM_BOUNDARY.md` and `firmware/IMPLEMENTATION_STATUS.md`.

### 6. OS / hardware interface

| Artifact | Path |
|---|---|
| Interface-level map (this pass) | `os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md` |
| High-level matrix | `os_compatibility/HARDWARE_TO_OS_TRACEABILITY.md` |
| Device-class YAML exports | `os_compatibility/device_class_exports/*.yaml` |
| Handoff | `os_compatibility/OS_COMPATIBILITY_HANDOFF.md` |
| Reciprocal OS repo | `gunnchos-device-os` `hardware_compat/` |

Exports are profile assumptions. They do **not** prove silicon boot.

### 7. RFQ packets (prepare ≠ send)

| SKU | Packet |
|---|---|
| Handheld | `manufacturing/rfq/handheld_hybrid/` + `device_designs/handheld_hybrid/manufacturing/RFQ_DIGITAL_PACKAGE.md` |
| Student | `manufacturing/rfq/student_14_5/` |
| DS-XL | `manufacturing/rfq/ds_xl_coder/` |
| Rings | `manufacturing/rfq/edge_io_rings/` |
| Dock | `manufacturing/rfq/dock/` |
| EVT-1 templates | `prototype_rfq/` |
| Owner send packet | `docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md` |

## Unresolved specifications (exact)

Do not invent values for these. Each remains open until a cited vendor/NDA/lab source exists.

| ID | Specification | SKUs | Why unresolved | Needed source |
|---|---|---|---|---|
| `UNRES-COM-HPC-400PIN` | COM-HPC Mini 400-pin net-accurate map | student_14_5, ds_xl_coder | Public docs insufficient | PICMG/ADLINK NARROW_NDA |
| `UNRES-COM-HPC-DUAL-EDP` | Dual eDP lane map on COM-HPC Mini | ds_xl_coder | Differentiator blocked | ADLINK NDA pin map |
| `UNRES-JHL8440-BALLS` | JHL8440 package ball map | dock | Topology public; balls NDA | Intel RDC NDA |
| `UNRES-JHL9040R-BALLS` | JHL9040R retimer ball map | dock | TB4 retimer fanout | Intel RDC NDA |
| `UNRES-DSXL-PANEL-MPN` | Exact dual-panel MPNs + hinge bend OEM spec | ds_xl_coder | AVL quotes pending | Panel OEM drawing |
| `UNRES-HH-DISPLAY-DIAGONAL` | Handheld display diagonal | handheld_hybrid | BOM `7in_1080p_120Hz_IPS` vs OS export / device-os profile `8.4` in | Single frozen panel MPN + mechanical drawing |
| `UNRES-HH-OS-EXPORT-STORAGE` | Handheld storage class in hardware OS export | handheld_hybrid | `os_compatibility/device_class_exports/handheld_hybrid_os_export.yaml` says `nvme` `min_gb: 512`; hardware SoT is on-module **32GB eMMC** + microSD (`DIGITAL_RELEASE_PACKAGE.json`, BOM RM121-D8E32) | Export aligned to SoT *or* explicit dual-track note; not invented NVMe |
| `UNRES-HH-OS-EXPORT-RAM` | Handheld RAM in hardware OS export | handheld_hybrid | Export `ram_gb: 12` vs SoM **8GB** LPDDR4X on RM121-D8E32 | Export aligned to SoM datasheet |
| `UNRES-STUDENT-RAM-EXPORT` | Student RAM in OS export | student_14_5 | Export `ram_gb: 8` vs named compute **COM-HPC-mMTL-155H-32G** | NDA/public module memory map |
| `UNRES-SODIMM-CONNECTOR-MPN` | Exact 260-pin SODIMM socket MPN + footprint | handheld_hybrid | BOM `AVL_PENDING` | Connector datasheet + KiCad footprint |
| `UNRES-HH-PANEL-MPN` | Exact 7in/8.4in panel MPN | handheld_hybrid | Placeholder description in BOM | Panel OEM |
| `UNRES-STICK-MPN` | Analog stick production MPN | handheld_hybrid | `AVL_PENDING` (ALPS candidate listed) | Vendor confirmation |
| `UNRES-BATTERY-CELL-MPN` | Exact pack/cell MPN | handheld, student, rings | MODELED packs | Cell OEM + UN38.3 report |
| `UNRES-PASTE-REFLOW` | Stencil/paste/reflow profile | all | Vendor process values | CM DFM reply |
| `UNRES-TORQUE` | Fastener torque OEM values | mechanical SKUs | Incomplete OEM | Mechanical drawing revision |
| `UNRES-IMPEDANCE-SI` | Coupon/SI proof vs stackup ohms | handheld (notes 90/85/100 Ω) | `si_simulation_performed: false` | SI tool run *or* CM coupon |
| `UNRES-SIGNED-FW-BIN` | Production signed firmware + fixture limits | all | Harness/simulated only | Signed image + ICT limits from CM |
| `UNRES-FLASH-LAYOUT` | Secure-update flash layout | OS contract | `docs/OS_HARDWARE_CONTRACT.md` TBD | EVT-1 firmware map on silicon |
| `UNRES-DOCK-0V8` | Dock `VDD_USB4` 0.8 V rail | dock | YAML `MODELED — package NDA` | Intel rail table under NDA |
| `UNRES-LIB-FOOTPRINT` | Residual `lib_footprint_mismatch` DRC warnings | family | Recorded, not cleared | Footprint library lock |
| `UNRES-DRC-DANGLING` | `track_dangling` / `silk_over_copper` | student, ds_xl, rings, dock | Recorded on those SKUs | Layout cleanup without inventing NDA nets |

Cited NDA request list: `docs/full_product_family/EXTERNAL_VENDOR_COLLATERAL_REQUIRED_CONT_IX.md`.

## Exact remaining physical / owner actions

These cannot be completed by this agent.

1. **Owner reviews** this digital packet (`DIGITAL_MANUFACTURING_READINESS.md` + RFQ folders). Cursor does not approve spend.
2. **Owner sends RFQ** using `docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md`. Record vendor, date, document hash. Do not treat packet existence as send.
3. **CM DFM reply** — paste, stencil, X-ray, impedance coupons (`UNRES-PASTE-REFLOW`, `UNRES-IMPEDANCE-SI`).
4. **NDA collateral intake** — COM-HPC and Intel maps (`UNRES-COM-HPC-*`, `UNRES-JHL*`) by a human with portal access.
5. **Purchase / fab authorization** — owner PO. No fab from this repo.
6. **Assemble EVT unit(s)** matching a tagged hardware SHA.
7. **Lab ESD / power setup** — follow `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md`. Measure rails; do not copy modeled YAML volts as measured.
8. **Record bring-up evidence** — board ID, firmware hash, boot log, passing/failing test points under `artifacts/evt/` (create when physical).
9. **Battery / thermal / RF physical tests** — UN38.3, chamber, antenna; still `PHYSICAL_PENDING` / `EXTERNAL_PENDING`.
10. **Certification labs** — FCC Part 15, CE/UKCA, USB-IF, module listings ≠ end-product cert. Owner engages labs.
11. **DVT then PVT** — plans exist under `dvt/` and `pvt/`; execution is physical.
12. **Ring physical boot** — Zephyr west digital PASS does not substitute flashing a real nRF52840.

## What digital success looks like (this pass)

- Validators: `python3 scripts/validate_digital_manufacturing.py`
- Optional EDA: `bash scripts/run_supervisor_eda_checks.sh`
- Packets and UML present under `docs/packets/` and `docs/uml/`
- OS/hardware interface map present
- Status remains `PHYSICAL_PENDING` for fabrication and bring-up

## Related

- [PHYSICAL_EVT_BRINGUP_PACKET.md](docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md)
- [MANUFACTURER_RFQ_SEND_PACKET.md](docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md)
- [UML index](docs/uml/README.md)
- [OS/hardware interface traceability](os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md)
