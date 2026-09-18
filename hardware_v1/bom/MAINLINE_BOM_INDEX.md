# Hardware v1 mainline BOM index

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Rule
Experimental MPNs must not appear in mainline BOM files.

## SKU → existing assembly BOM (reconciled)
| SKU | Path | Hardware v1 notes |
|---|---|---|
| Student 14.5 | `device_designs/student_14_5/bom/assembly_bom.csv` | COM-HPC Mini MTL retained; WWAN preferred class → Telit FN990B40 (Quectel alternate) |
| DS-XL Coder | `device_designs/ds_xl_coder/bom/assembly_bom.csv` | shared module; dual IPS |
| Handheld EVT mule | `hardware_v1/bom/handheld_evt_mule_bom.csv` | COM-HPC Mini mule (RM121 historical not mixed) |
| Dock Gen-1 | `device_designs/dock/bom/assembly_bom.csv` | USB4 40 only |
| Rings | `hardware_v1/bom/rings_mainline_bom.csv` | nRF54L15 class (nRF52840 historical retained separately) |

## AVL
See `hardware_v1/bom/AVL.md`. Unknown fields stay unknown.
