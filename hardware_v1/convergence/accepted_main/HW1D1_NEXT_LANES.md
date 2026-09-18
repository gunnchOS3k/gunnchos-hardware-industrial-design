# HW1D.1 — Next lanes (documented; not executed)

**Generated:** 2026-09-18T18:12:00Z  
**Campaign:** `HW1D.1_ACCEPTED_MAIN_REBIND`  
**Accepted main:** `e5f15d1f1b6ddefa73c0a6127bced8d784aae425`

## Preferred next actions

| Lane | Token | Notes |
|---|---|---|
| NXP open-custom | `NEXT_HARDWARE_ACTION=START_NXP_OPEN_CUSTOM_IMPLEMENTATION` | Continue under `hardware_v1/open_custom_nxp/`; public collateral; design-guide may be account-gated |
| GXE | `NEXT_GXE_ACTION=BUILD_FIRST_VERTICAL_SLICE_IN_RISCV_SIM` | **Separate workspace** — not in this hardware repo |
| AMD product mainline | `PARALLEL_AMD_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL` | External / collateral-gated; does not block architecture acceptance |
| Optional RP0-A | `OPTIONAL_REFERENCE_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT` | Owner optional; Cursor does not purchase |

## Explicit non-actions for this campaign

- Do not merge experiment PRs #69–#79
- Do not claim physical readiness
- Do not purchase / RFQ / fabricate / accept NDAs
- Do not modify software v1.0 RC1 baselines
- Do not execute GXE implementation inside this repo
