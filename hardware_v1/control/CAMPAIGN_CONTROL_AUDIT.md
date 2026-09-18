# Hardware v1.0 campaign control audit

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Scope
Execute Hardware 1.0 mainline EVT architecture + isolated experimental comparison tracks.

## Doctrine checklist
| Rule | Status |
|---|---|
| One mainline design per decision | PASS (see decision ledger) |
| Experiments isolated; not mixed into main BOM | PASS |
| No LCD compromise flattening | PASS |
| No physical/cert/fab/RFQ-send claims | PASS |
| No frozen software RC1 baseline edits | PASS (`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`) |
| Extend existing PHYSICAL_PENDING evidence | PASS (reconcile map below) |
| Honest FAIL on missing Gerbers/quotes | PASS |

## Reconcile map (do not discard)
| Existing artifact | Role in Hardware v1 |
|---|---|
| `DIGITAL_MANUFACTURING_READINESS.md` | retained / indexed |
| `DIGITAL_TO_PHYSICAL_HANDOFF.md` | retained / indexed |
| `device_designs/student_14_5/digital_release/INDEX.json` | retained / indexed |
| `device_designs/ds_xl_coder/digital_release/INDEX.json` | retained / indexed |
| `device_designs/handheld_hybrid/digital_release/INDEX.json` | retained / indexed |
| `device_designs/edge_io_rings/digital_release/INDEX.json` | retained / indexed |
| `device_designs/dock/bom/assembly_bom.csv` | retained / indexed |
| `device_designs/student_14_5/bom/assembly_bom.csv` | retained / indexed |
| `manufacturing/EVT_DVT_PVT_PLAN.md` | retained / indexed |
| `docs/full_product_family/COM_HPC_FINAL_DECISION_CONT_IX.md` | retained / indexed |
| `docs/full_product_family/DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md` | retained / indexed |

## Branch architecture
- Mainline branch: `hardware/v1-mainline-ready-for-evt` → DRAFT PR to `main`
- Experiments branch from mainline; DRAFT PRs target mainline, not `main`
- Cursor must NOT merge
