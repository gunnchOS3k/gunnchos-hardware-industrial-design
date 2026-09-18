# CPB0-O PMIC / regulator architecture freeze

**Generated:** 2026-09-18T19:17:34Z  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## Architecture (frozen)

Public IMX95LPD5EVK-19 Quick Start Guide lists power management ICs: **PF09, PF5301, PF5302**.

| Role | Family / candidate | Evidence | Status |
|---|---|---|---|
| Multi-rail PMIC | **PF09** / preferred candidate **MPF0900AVNA1ES** (i.MX95, QM, HVQFN56) | nxp.com/products/PF09 part table; EVK QSG | Architecture frozen; **OTP variant not proven from EVK BOM** |
| Core / AVP rails | **PF5301**, **PF5302** | EVK QSG | Family frozen; exact OPNs VERIFY from EVK BOM |
| Input | 12 V class bench / adapter (EVK uses 12 V supply) | EVK QSG | Design target |

## Why not a “familiar” discrete tree

IMX95IEC states the power architecture expects a dedicated PMIC for all rails with BBSM-first sequencing (`NVCC_BBSM_1P8` first). Discrete improvisation is explicitly non-preferred.

## Gate

`NXP_OPEN_PMIC_ARCHITECTURE_FROZEN=true` for **architecture** (PF09+PF53x).  
Exact OTP programming file / EVK BOM line item remains an owner fetch (`pmic_otp_frozen=false`).
