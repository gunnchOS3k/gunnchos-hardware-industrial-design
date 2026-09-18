# RP0-A procurement guide

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## Purpose
Exact owner-facing COTS bring-up kit list. Cursor does **not** purchase.

## Status tokens
| Token | Value |
|---|---|
| `RP0_A_COTS_PROCUREMENT_PACKET_READY` | `true` |
| `RP0_A_READY_TO_ORDER` | `true` |
| `physical_purchase_status` (all rows) | `NOT_PURCHASED` |
| `price` / `stock` / `lead_time` | `VERIFY_AT_PURCHASE` |

## BOM
See `RP0_A_PROCUREMENT_BOM.csv` (29 line items).

## Exact MPN anchors (verified where noted)
- Compute module: `COM-HPC-mMTL-155H-32G`
- Cellular optional: `FN990B40W01T010300`
- Rings DK: `nRF54L15-DK` / `PCA10156`

## Order of operations
1. Order required compute + storage + Wi-Fi + cooling + PSU
2. Order rings DK + sensing/charge prototype parts
3. Order COTS USB4 dock + cables + displays + lab meters
4. Optionally order FN990 + development antennas
5. Do **not** order custom carrier/dock/ring PCBs until RP0-B pin-accurate files exist

## Preferred next action
`NEXT_OWNER_ACTION=ORDER_RP0_A_COTS_BRINGUP_KIT`
