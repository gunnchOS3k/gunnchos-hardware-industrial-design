# RP0-B vendor access packet

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## Purpose
Exact materials still needed before **custom** fabrication. No credentials. No NDA acceptance by Cursor.

## PICMG / ADLINK
| Material | Access | Owner action | Blocks RP0-A? | Blocks RP0-B? |
|---|---|---|---|---|
| COM-HPC Mini authoritative pin assignment / base spec for custom carrier | public overview may exist; full pin/net for custom often member/vendor | obtain PICMG/ADLINK design collateral | no | yes |
| ADLINK selected-module user manual (`COM-HPC-mMTL-155H-32G`) | account/login likely | request/download | no | yes |
| Reference carrier schematics/layout where permitted | vendor / NDA possible | request permissioned package | no | yes |
| Connector mechanical model | often public CAD / vendor | download | no | yes |
| Carrier design guide | vendor | request | no | yes |

## Intel dock silicon
| Material | Access | Owner action | Blocks RP0-A? | Blocks RP0-B? |
|---|---|---|---|---|
| JHL8440 design collateral (pin-accurate) | NDA likely | vendor support / NDA path | no | yes |
| JHL9040R design collateral (pin-accurate) | NDA likely | vendor support / NDA path | no | yes |
| Reference schematic/layout | NDA / account | request | no | yes |
| PD/controller integration requirements | mixed public/vendor | collect app notes | no | yes |
| Firmware/NVM programming collateral | vendor | request | no | yes |
| Thunderbolt/USB4 design & certification requirements | public + cert labs | plan cert path | no | yes (for cert) |

## If owner declines RP0-A order
`NEXT_GATE=ACQUIRE_RP0_B_VENDOR_COLLATERAL`
