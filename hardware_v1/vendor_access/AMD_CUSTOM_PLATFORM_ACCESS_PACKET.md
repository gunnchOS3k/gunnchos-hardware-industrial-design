# AMD custom platform access packet

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


`CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false` — Cursor does not submit/accept NDAs or partner agreements.

## Required collateral categories

| Artifact | Classification | Notes |
|---|---|---|
| Ryzen Embedded 8000 pinout | `NDA_REQUIRED` | blocks CPB0 nets |
| FP7r2 package/mechanical | `AMD_PARTNER_ACCESS` | or NDA_REQUIRED |
| power sequencing | `NDA_REQUIRED` |  |
| VRM requirements | `NDA_REQUIRED` |  |
| DDR5 routing/topology | `NDA_REQUIRED` |  |
| supported memory devices/topologies | `NDA_REQUIRED` |  |
| USB4 implementation guidance | `AMD_PARTNER_ACCESS` | may be NDA |
| PCIe implementation guidance | `AMD_PARTNER_ACCESS` |  |
| display/DDI/eDP guidance | `AMD_PARTNER_ACCESS` |  |
| clock/reset requirements | `NDA_REQUIRED` |  |
| boot/SPI requirements | `AMD_PARTNER_ACCESS` |  |
| platform security requirements | `AMD_PARTNER_ACCESS` |  |
| thermal design guidance | `PUBLIC` | partial public; detailed TBD |
| reference schematic | `NDA_REQUIRED` |  |
| reference board/layout | `NDA_REQUIRED` |  |
| signal-integrity constraints | `NDA_REQUIRED` |  |
| BIOS/UEFI / AGESA enablement path | `IBV_REQUIRED` | vendor-supported path |
| manufacturing/programming requirements | `AMD_PARTNER_ACCESS` |  |
| debug tools | `AMD_DEVELOPER_LOGIN` | tool access TBD |
| reference validation checklist | `AMD_PARTNER_ACCESS` |  |
| public product brief / OPN identity | `PUBLIC` | 8840U/8845HS OPNs cited as reference only |

## Owner steps (human only)

1. Create/login AMD Embedded Developer Hub account (owner).
2. Request Embedded partner/sales engagement for Ryzen Embedded 8000 custom board design access.
3. Complete any required NDA/partner workflow **as owner** (Cursor will not accept/sign).
4. Obtain pinout, package, power, DDR, USB4/PCIe/display, boot, SI, reference schematic/layout packages.
5. Inquire BIOS/IBV support path (AGESA / vendor UEFI) for selected OPNs.
6. Deposit non-public files only in an owner-controlled vault; do not invent contents into this public repo.

## Cursor boundary

- Does not invent restricted data
- Does not submit agreements
- Does not purchase silicon or eval boards
- Stops honestly if collateral cannot be obtained (does not silently revert COM-HPC to mainline)

`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`
