# HW1B final report A–T

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## A. #68 starting/final head
Starting (expected): `bd65bc67b413597a7d5534bc8dddaa9d7513b0c3`  
Final: see git after push (must remain on `hardware/v1-mainline-ready-for-evt`, DRAFT #68).

## B. Blocker closure matrix
`hardware_v1/rp0b/BLOCKER_CLOSURE_MATRIX.md`

## C. nRF54L15 public blocker result
`UNRES_NRF54L15_FOOTPRINT_CLOSED=true` (QFN48/DK PCA10156 public files checksummed; CSP47 separate)

## D. FN990B40 AVL result
`UNRES_FN990B40_AVL_CLOSED=true` (exact MPN `FN990B40W01T010300`; DigiKey/Mouser scrape blocked → VERIFY_AT_PURCHASE)  
`PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true`

## E. COM-HPC public/COTS result
ADLINK `COM-HPC-mMTL-155H-32G` + Mini Base COTS path documented for RP0-A.

## F. Remaining COM-HPC vendor-gated data
`EXT_COM_HPC_400PIN_RP0_A_BLOCKING=false`  
`EXT_COM_HPC_400PIN_RP0_B_BLOCKING=true`

## G. DS-XL display architecture correction
One eDP + DDI/DP; `EXT_DSXL_DUAL_EDP_CLOSED=true` via `CLOSED_BY_ARCHITECTURE_CHANGE`.

## H. Intel dock public data result
Functional USB4 40 class retained; COTS dock path for RP0-A.

## I. Remaining dock NDA/vendor collateral
`EXT_JHL8440_BALLMAP_RP0_A_BLOCKING=false` / `..._RP0_B_BLOCKING=true`  
`EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING=false` / `..._RP0_B_BLOCKING=true`

## J. RP0-A architecture
COTS Integration Bench — no custom PCB.

## K. RP0-A procurement packet
`RP0_A_PROCUREMENT_BOM.csv` + `RP0_A_PROCUREMENT_GUIDE.md`

## L. Exact MPN list
`COM-HPC-mMTL-155H-32G`, `FN990B40W01T010300`, `nRF54L15-DK/PCA10156` (+ VERIFY_AT_PURCHASE accessories)

## M. RP0-A bring-up matrix
`RP0_A_BRINGUP_MATRIX.csv` — all rows `UNTESTED_PENDING_PHYSICAL`

## N. RP0-B custom-fab blockers
400-pin map, JHL8440/9040R ballmaps, owner custom fab auth, complete EDA

## O. Experiment PR status
#69–#76 remain DRAFT targeting mainline; refresh after #68 head advances

## P. Validation results
See `make hardware-v1-validate` / `make hardware-v1-all`

## Q. Updated gates
See `hardware_v1/GATES.json`

## R. Software RC1 firewall
`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`

## S. Owner action packet
`hardware_v1/OWNER_ACTION_PACKET.md`

## T. Exactly one next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT`
