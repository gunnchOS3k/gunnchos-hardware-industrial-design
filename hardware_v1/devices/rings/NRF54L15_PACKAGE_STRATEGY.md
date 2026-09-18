# nRF54L15 package strategy

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## DEC-RINGS-001 split
| Token | Value |
|---|---|
| `RING_EVT_ELECTRICAL_PLATFORM` | `QFN48/DK reference` |
| `RING_FORM_FACTOR_CANDIDATE` | `CSP47` (WLCSP production-size candidate) |
| `DK_HARDWARE_ID` | `PCA10156` |

## RP0-A path
- Use **nRF54L15 DK** (PCA10156) with SoC in **QFN48** for firmware, sensor-fusion, power, BLE, and haptics bring-up.
- Use Nordic official reference layout / hardware files — do not hand-invent RF matching.
- Hardware files zip (not redistributed in-repo; license/size):
  - URL: `https://nsscprodmedia.blob.core.windows.net/prod/software-and-other-downloads/dev-kits/nrf54l15-dk/pca10156-nrf54l15-dk-1_0_0.zip`
  - sha256: `ed70a2233d009e7e4dd31a20f66527ef206b23bd357623850a9f3228a089e1d4`
  - bytes: `14098311`
  - version: `PCA10156-nRF54L15-DK 1.0.0`

## Wearable form-factor
- Keep **CSP47 / WLCSP** as compact Ring candidate.
- Require separate HDI/assembly feasibility gate before wearable board promotion.
- **nRF DK evidence cannot be called wearable-form-factor validation.**

## Blocker
`UNRES-NRF54L15-FOOTPRINT` → `CLOSED_PUBLIC_EVIDENCE` for RP0-A / digital reference.
