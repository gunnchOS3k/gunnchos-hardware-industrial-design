# Reference Platform 0

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Stage model
See `RP0_STAGE_MODEL.md`.

### RP0-A — COTS Integration Bench
ADLINK COM-HPC Mini Base + COM-HPC-mMTL-155H-32G + nRF54L15 DK (PCA10156) + COTS USB4 dock.
No custom fabrication. Procurement packet ready; **NOT_PURCHASED**.

### RP0-B — Custom gunnchOS Reference Carrier
Net-accurate custom carrier/dock/ring EVT electronics. Requires vendor pin/ball maps + EDA.

## Fab readiness
`REFERENCE_PLATFORM_0_READY_FOR_FAB=false` (= `RP0_B_CUSTOM_READY_FOR_FAB=false`)

COTS orderability does **not** set fab readiness.

## Owner next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT` — Cursor does not purchase.
If owner declines: `NEXT_GATE=ACQUIRE_RP0_B_VENDOR_COLLATERAL`
