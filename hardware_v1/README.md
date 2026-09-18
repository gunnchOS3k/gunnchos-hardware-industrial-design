# Hardware v1.0 mainline package

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Start
1. `hardware_v1/control/CAMPAIGN_CONTROL_AUDIT.md`
2. `hardware_v1/decisions/DECISION_LEDGER.md`
3. `hardware_v1/GATES.md`
4. `hardware_v1/OWNER_ACTION_PACKET.md`
5. `make hardware-v1-validate`

## Claim boundary
Digital architecture + EVT preparation. Not physical validation, not certification, not fab release.

## HW1C custom-first pivot

**Generated:** 2026-09-18T16:48:39Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

- Product mainline compute: **gunnchOS Platform Core v1** (custom AMD Ryzen Embedded 8000 FP7r2)
- COM-HPC Mini path: **REFERENCE_CONTROL_MODULAR_X86** (RP0-A packet preserved)
- Learning board: **CPB0** (`hardware_v1/custom_mainline/cpb0/`)
- Doctrine: `hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md`
- Preferred owner action: `ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`

## HW1D four-track convergence

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.

- `PRODUCT_MAINLINE` = AMD_CUSTOM_X86
- `OPEN_ENGINEERING_MAINLINE` = NXP_IMX95_OPEN_CUSTOM
- `GREENFIELD_EXPERIMENT` = GXE (contract only)
- `REFERENCE_CONTROL` = COM_HPC_AND_COTS
- Merge-ready gate: `HW_ARCHITECTURE_BASELINE_MERGE_READY` (≠ physical EVT)
- Docs: `hardware_v1/convergence/`
