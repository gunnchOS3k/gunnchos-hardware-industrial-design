# Owner action packet

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## What Cursor completed (digital)
- Mainline decision ledger (one design per decision)
- HW1B RP0-A/B stage split + public-source blocker closures
- RP0-A COTS procurement BOM/guide + bring-up matrix
- RP0-B vendor access packet
- Contracts, PRDs, ICDs, DFMEA starter, EVT/DVT/PVT matrices
- Experiments registry + EXP-*-001 comparison packages
- Make validators `make hardware-v1-*`
- Honest gate tokens (see below)

## What Cursor did NOT do
- Send RFQs / purchase / contact suppliers / accept NDAs
- Claim physical validation or certification
- Merge any PR
- Modify software RC1 baselines
- Fabricate Gerbers/ODB++/quotes/lead times / invent ball maps

## Gate tokens
| Token | Value |
|---|---|
| `HARDWARE_V1_READY_FOR_EVT_BUILD` | `False` |
| `HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE` | `True` |
| `REFERENCE_PLATFORM_0_READY_FOR_FAB` | `False` (= `RP0_B_CUSTOM_READY_FOR_FAB`) |
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `True` |
| `RP0_A_READY_TO_ORDER` | `True` |
| `RP0_A_PHYSICAL_BUILD_PENDING` | `True` |
| `RP0_A_BRINGUP_PENDING` | `True` |
| `RP0_B_CUSTOM_READY_FOR_FAB` | `False` |
| `PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING` | `True` |
| `EVT_PENDING` | `True` |
| `DVT_PENDING` | `True` |
| `PVT_PENDING` | `True` |
| `PHYSICAL_HARDWARE_VALIDATED` | `False` |
| `CERTIFICATION_COMPLETE` | `False` |
| `MANUFACTURING_VALIDATED` | `False` |
| `DIGITAL_FABRICATION_PASS` | `False` |
| `RFQ_SENT` | `False` |
| `DIGITAL_ARCHITECTURE_PACKAGE_COMPLETE` | `True` |

## Preferred next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT`

RP0-A COTS procurement packet is ready. Cursor will not purchase. RP0-B custom fab remains blocked on vendor pin/ball maps. COTS orderability does not set READY_FOR_FAB.

If owner declines RP0-A order: `NEXT_GATE=ACQUIRE_RP0_B_VENDOR_COLLATERAL`
