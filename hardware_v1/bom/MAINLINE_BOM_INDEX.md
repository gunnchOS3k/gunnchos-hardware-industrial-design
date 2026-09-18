# Hardware v1 mainline BOM index

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## BOM classes (fail-closed)

| Class | File / location | May define product architecture? |
|---|---|---|
| `MAINLINE_CUSTOM` | `hardware_v1/bom/MAINLINE_CUSTOM_BOM.csv` | YES |
| `REFERENCE_CONTROL` | `hardware_v1/bom/REFERENCE_CONTROL_BOM.csv` | NO |
| `EXPERIMENTAL` | `hardware_v1/bom/EXPERIMENTAL_BOM_INDEX.md` + EXP packages | NO |
| `DEFERRED_GEN2` | experimental index / ledger | NO |

## Rule

- Mainline BOM must **not** contain COM-HPC module/baseboard as product architecture.
- COM-HPC may appear only under REFERENCE_CONTROL equipment.
- Experimental MPNs must not appear in mainline with qty>0.

## SKU mapping (custom mainline intent)

| SKU | Mainline compute | Notes |
|---|---|---|
| Student 14.5 | 8840U custom Student-MB-v1 | COM-HPC retained as reference control |
| DS-XL Coder | 8845HS custom DSXL-MB-v1 | one eDP + DDI preserved |
| Handheld | 8840U custom Handheld-MB-v1 | COM-HPC mule = reference only |
| Dock Gen-1 | CUSTOM_GUNNCHOS_DOCK_GEN1 | COTS dock = REFERENCE_CONTROL_DOCK |
| Rings | custom nRF54L15 | DK = REFERENCE_CONTROL_RING |

## AVL
See `hardware_v1/bom/AVL.md`. Unknown fields stay unknown.
