# Owner action packet

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## What Cursor completed (digital)
- Mainline decision ledger (one design per decision)
- Contracts, PRDs, ICDs, DFMEA starter, EVT/DVT/PVT matrices
- BOM/AVL indexes without experimental mix
- Experiments registry + EXP-*-001 comparison packages
- Make validators `make hardware-v1-*`
- Honest gate tokens (see below)

## What Cursor did NOT do
- Send RFQs / purchase / contact suppliers
- Claim physical validation or certification
- Merge any PR
- Modify software RC1 baselines
- Fabricate Gerbers/ODB++/quotes/lead times

## Gate tokens
| Token | Value |
|---|---|
| `HARDWARE_V1_READY_FOR_EVT_BUILD` | `False` |
| `REFERENCE_PLATFORM_0_READY_FOR_FAB` | `False` |
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
`NEXT_OWNER_ACTION=QUOTE_AND_BUILD_REFERENCE_PLATFORM_0`

Digital mainline architecture + comparison tracks are packaged. Gates above remain FALSE until external pin maps / AVL confirmations / owner quote-build. Cursor will not send RFQs, purchase, or claim fab.

If owner declines quote/build: `NEXT_GATE=EXT-COM-HPC-400PIN`
