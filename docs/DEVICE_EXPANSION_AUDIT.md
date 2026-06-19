# Device Expansion Audit

**Pass target:** EVT-1 hardware architecture package — not manufacturing release.

## Current state

This repo is currently **EVT-0 concept scaffold** with OpenSCAD assets, draft BOM docs, and compliance trackers. This pass moves toward **EVT-1 hardware package**, not final manufacturing readiness.

## CAD / OpenSCAD

| Item | Status |
|------|--------|
| `cad/openscad/student_14_5/` | present |
| Handheld / DS-XL / wearables CAD | partial / planned |

## Device specs

| Item | Status |
|------|--------|
| `docs/DEVICE_REQUIREMENTS.md` | draft |
| `product/PRD_*.md` | **added this pass** |

## BOM

| Item | Status |
|------|--------|
| Legacy BOM paths | partial |
| `bom/*.csv` per product line | **added** |

## Compliance

| Item | Status |
|------|--------|
| `docs/07_compliance/` | partial |
| `compliance/REGULATORY_MATRIX.md` | **added** |

## Gaps addressed this pass

| Gap | EVT-1 action |
|-----|----------------|
| Schematics | KiCad skeleton `.kicad_sch` per product |
| KiCad structure | `schematics/*/README.md` |
| Block diagrams | `architecture/SYSTEM_BLOCK_DIAGRAM.md` |
| PCB stack-up | `pcb/STACKUP_PLAN.md` |
| Connector map | `architecture/DATA_FLOW_AND_CONNECTOR_MAP.md` |
| Power tree | `architecture/POWER_TREE.md` |
| Battery/charger | `battery/` docs |
| Thermal | `thermal/` docs |
| CM quote package | `manufacturing/CM_QUOTE_PACKAGE_CHECKLIST.md` |
| DFM/DFT | `pcb/DFM_NOTES.md`, `DFT_NOTES.md` |
| EVT/DVT/PVT | `manufacturing/EVT_DVT_PVT_PLAN.md` |

## Not claimed

- certified hardware
- finished OS
- mass-production readiness
- regulatory approval
- finished Steam/media licensing
