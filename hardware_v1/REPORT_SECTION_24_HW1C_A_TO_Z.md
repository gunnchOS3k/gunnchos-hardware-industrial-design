# HW1C final report A–Z

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## A. #68 starting/final head
Starting (expected): `3730a98bb1285a86553cf4e38f5c7c6e4406a049` (no drift at preflight).  
Final: see git after push on `hardware/v1-mainline-ready-for-evt` (DRAFT #68).

## B. Architecture doctrine pivot
`hardware_v1/custom_mainline/CUSTOM_FIRST_ARCHITECTURE_DOCTRINE.md` — MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL_VARIANT.

## C. Mainline custom compute family
gunnchOS Platform Core v1 — AMD Ryzen Embedded 8000 FP7r2 BGA.

## D. Student SoC
8840U (`100-000001317E` public OPN ref) — PENDING_VENDOR_CONFIRMATION for pin/power/DDR.

## E. Handheld SoC
8840U same family; COM-HPC mule = REFERENCE_CONTROL only.

## F. DS-XL SoC
8845HS (`100-000001316E` public OPN ref) — pin compatibility with 8840U NOT assumed.

## G. CPB0 architecture
Debug-friendly Custom Platform Board 0; 8845HS preferred; digital package under `custom_mainline/cpb0/`; not fab-ready.

## H. AMD collateral needs
`hardware_v1/vendor_access/AMD_CUSTOM_PLATFORM_ACCESS_PACKET.md` — PUBLIC/LOGIN/PARTNER/NDA/IBV/UNKNOWN classifications; no invented restricted data.

## I. AMD owner-access steps
Developer Hub → partner/sales → NDA/partner workflow (owner only) → IBV/BIOS inquiry. Cursor does not submit agreements.

## J. Firmware ownership boundary
Vendor UEFI/AGESA mainline; Zephyr+MCUboot EC; coreboot/openSIL experimental only.

## K. Memory topology plan
UNFROZEN — CPB0 debug-friendly preference; product intents documented; `CUSTOM_DDR_TOPOLOGY_UNDERSTOOD=false`.

## L. COM-HPC reclassification
`REFERENCE_CONTROL_MODULAR_X86` — not product mainline.

## M. RP0-A status
Procurement packet preserved; `RP0_A_COTS_PROCUREMENT_PACKET_READY=true`; `RP0_A_READY_TO_ORDER=true`; optional order only.

## N. DS-XL X100 experiment
`EXP-DSXL-X100-001` package created.

## O. P100 AI experiment
`EXP-P100-AI-001` package created.

## P. Custom Dock mainline
`CUSTOM_GUNNCHOS_DOCK_GEN1` remains mainline; COTS dock = REFERENCE_CONTROL_DOCK.

## Q. Custom Ring mainline
Custom nRF54L15 ring remains mainline; DK = REFERENCE_CONTROL_RING.

## R. BOM class split
MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL / DEFERRED_GEN2 with fail-closed isolation.

## S. Knowledge map
`hardware_v1/custom_mainline/KNOWLEDGE_MAP.md`

## T. Learning gates
All understanding gates false where AMD collateral missing (see GATES.json).

## U. Complexity register
`hardware_v1/custom_mainline/CUSTOM_MAINLINE_COMPLEXITY_REGISTER.md`

## V. Existing experimental PR refresh
#69–#76 refreshed onto updated #68 head after push (DRAFT, unmerged).

## W. New experimental PRs
DRAFT PRs for COM-HPC modular / DSXL-X100 / P100-AI opened only with real packages (see campaign closeout).

## X. Validation
`make hardware-v1-validate` / `make hardware-v1-all` — see closeout log.

## Y. Remaining blockers
AMD custom collateral + EDA for CPB0; dock JHL ballmaps for pin-accurate custom dock; cellular antenna design pending; physical EVT/DVT/PVT pending.

## Z. Exactly one next owner action
`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`  
Optional: `OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

## Printed tokens
See `hardware_v1/GATES.json` / campaign closeout.
