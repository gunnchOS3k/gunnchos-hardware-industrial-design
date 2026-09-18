# Open-custom NXP i.MX95 package

**Generated:** 2026-09-18T18:55:43Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION` (extends HW1D architecture package)  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.

Track: `OPEN_ENGINEERING_MAINLINE = NXP_IMX95_OPEN_CUSTOM`  
Selected CPB0-O SoC: **MIMX9596AVZXN**

## Key entrypoints

| Doc | Purpose |
|---|---|
| `NXP0_STARTING_STATE.json` | Preflight / PR #80 baseline |
| `NXP0_GATES.json` | Honest gate tokens |
| `PUBLIC_COLLATERAL_INDEX.md` | Public collateral SoT |
| `CPB0_OPEN_SOC_SELECTION.md` | Exact OPN |
| `eda/cpb0_open/` | KiCad scaffold |
| `REPORT_SECTION_20_NXP0_A_TO_V.md` | Final report A–V |
| `OPEN_CUSTOM_DOCTRINE.md` | Non-equivalence to AMD PRODUCT_MAINLINE |

## Make targets

`make nxp-open-audit` · `make nxp-open-validate` · `make nxp-open-gates`


## NXP-2 (2026-09-18T22:17:56Z)

Collateral-unlock continuation from accepted main `56125d1738a437f413ee4418c51c2f3a82bcbac8`. Owner UG10210/EVK BOM missing — see `owner_collateral/NXP_OWNER_COLLATERAL_INDEX.md` and `REPORT_SECTION_NXP2_A_TO_Z.md`.
