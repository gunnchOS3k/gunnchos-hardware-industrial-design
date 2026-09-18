# Reference Platform 0 stage model

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## RP0-A — COTS Integration Bench
Purpose:
- physically exercise the mainline architecture without a custom PCB
- use commercially available reference/development platforms
- collect power, thermal, I/O, OS, driver, radio and workflow data
- unblock custom design decisions

No custom fabrication required.

## RP0-B — Custom gunnchOS Reference Carrier
Purpose:
- implement the net-accurate gunnchOS custom carrier/dock/ring EVT electronics
- requires vendor/PICMG pin maps and complete EDA outputs
- **only this stage may become READY_FOR_FAB**

## Tokens
| Token | Value | Meaning |
|---|---|---|
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `true` | Exact COTS kit list + guide exist; not purchased |
| `RP0_A_READY_TO_ORDER` | `true` | Owner may order; Cursor will not purchase |
| `RP0_A_PHYSICAL_BUILD_PENDING` | `true` | No physical kit assembled yet |
| `RP0_A_BRINGUP_PENDING` | `true` | Bring-up matrix rows remain untested |
| `RP0_B_CUSTOM_READY_FOR_FAB` | `false` | Pin-accurate custom package incomplete |
| `REFERENCE_PLATFORM_0_READY_FOR_FAB` | `false` | **Legacy alias of** `RP0_B_CUSTOM_READY_FOR_FAB` |

## Hard rules
- COTS orderability ≠ custom fab readiness
- Owner purchase authorization ≠ `READY_FOR_FAB`
- COTS dock behavioral results ≠ custom dock PCB certification
- nRF DK/QFN evidence ≠ wearable CSP47 validation
- Development antennas ≠ production antenna design
