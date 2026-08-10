# Phase XV / WP-002 — Handheld storage headroom

**PHYSICAL_EXECUTION_FREEZE ACTIVE** — digital NPI only. No fab, no purchase, no flash, no assemble.

## Defect

`NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001`

Preferred SoM **RM121-D8E32** (32GB marketed eMMC) is operationally unsafe if the full Phase XIV handheld-reduced MLP profile (games/AI/offline/user media) is forced onboard after format/usable overhead.

## WP-002 decision: Outcome A

**32 GB system-only eMMC + supported expansion (microSD; USB optional tertiary).**

| Option | Verdict |
|---|---|
| **A — System eMMC + expansion policy** | **SELECTED** — closes defect pending independent V1 |
| B — Larger onboard eMMC/UFS module SKU | **Rejected** — not in `EXACT_MPN_MATRIX` / NX5 brief (do not invent) |
| C — Class E architecture CR (e.g. carrier NVMe remux) | **Not required to close** — deferred spike only |

## Deliverables

| Artifact | Purpose |
|---|---|
| `HANDHELD_STORAGE_CAPACITY_MODEL.json` | Slot A/B/recovery/logs/caches/games/AI/WAIKE/Archive/reserves + expansion placement |
| `HANDHELD_STORAGE_POLICY.md` | Reserves, warnings, reclamation, eviction, offline-pack, fail-closed rules |
| `HANDHELD_STORAGE_GROWTH_30_90_180.json` | 30/90/180-day growth on eMMC + microSD |
| `HANDHELD_STORAGE_DEFECT_CLOSURE.json` | Decision record (A/B/C) |
| `simulate_handheld_storage_e2e.py` | Fill/update/save/cleanup E2E simulation (no silent data loss) |
| `tests/test_wp002_handheld_storage.py` | Implementer tests |

## Honesty bounds

- Approved NX5 alternates in-repo are **smaller** eMMC SKUs (`RM121-D8E16` / `D8E8` / `D8E0`), not larger.
- Frozen Handheld storage path is **on-module eMMC + microSD**, not carrier NVMe.
- This package does **not** authorize purchase or lift the freeze.
- Implementer does **not** self-certify V1 (`VP-002-RESULT.json` is verifier-owned).
