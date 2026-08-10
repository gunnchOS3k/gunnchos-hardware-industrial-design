# Phase XV NPI — Handheld storage headroom

**PHYSICAL_EXECUTION_FREEZE ACTIVE** — digital NPI only. No fab, no purchase, no flash, no assemble.

## Defect

Ingested from field-kit Phase XV control-plane:

- `NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001.json`
- `HANDHELD_STORAGE_DECISION.json` (`OPERATIONALY_UNSAFE`)
- Companion field-kit DRAFT: https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/pull/54

Preferred SoM **RM121-D8E32** (32GB marketed eMMC) is operationally unsafe for the Phase XIV handheld-reduced profile once format/usable overhead is applied.

## Recommendation (evidence-backed)

See `HANDHELD_STORAGE_HEADROOM_RECOMMENDATION.json`.

| Option | Verdict |
|---|---|
| Larger onboard eMMC/UFS module SKU (≥64GB) | **Not available** in current `EXACT_MPN_MATRIX` / NX5 brief freeze (do not invent Radxa variants) |
| Expand carrier storage (NVMe/SATA remux) | Deferred architecture spike — mux/WWAN/USB3 trade study required |
| System-only eMMC + external/user-media policy | **Selected for EVT0 digital policy** — uses existing µSD ICD path |
| Further reduce OS/AI/games profile | Parallel software mitigation (device-os / field-kit) |

## Honesty bounds

- Approved NX5 alternates in-repo are **smaller** eMMC SKUs (`RM121-D8E16` / `D8E8` / `D8E0`), not larger.
- Frozen Handheld storage path is **on-module eMMC + microSD**, not carrier NVMe.
- This package does **not** authorize purchase or lift the freeze.
