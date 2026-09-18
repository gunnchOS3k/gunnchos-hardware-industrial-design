# nRF54L15 public package facts

**Generated:** 2026-09-18T18:37:46Z
**Campaign:** `STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION`
**Claim boundary:** digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps.


Sources: Nordic nRF54L15 product page + public datasheet package tables.

| Package | Size | Pins/balls | GPIO (public) | Ring role |
|---|---|---|---|---|
| QFN48 (QFAA) | 6×6 mm, 0.4 mm pitch | 48 | 31 | `RING_EVT_ELECTRICAL_PLATFORM` |
| CSP47 (CAAA) | 2.4×2.2 mm, 0.3 mm pitch | 47 | 32 | `RING_FORM_FACTOR_CANDIDATE` |
| QFN40 / QFN52 | public variants | — | — | cost/IO options |

Footprint used for EVT electrical: `gunnchos_production:QFN-48-1EP_6x6mm_P0.4mm` (JEDEC-class 6×6/0.4).

RF matching: follow Nordic PCA10156 DK hardware files (hashed in `devices/rings/NRF54L15_PACKAGE_STRATEGY.md`); values here are **placeholders**.
