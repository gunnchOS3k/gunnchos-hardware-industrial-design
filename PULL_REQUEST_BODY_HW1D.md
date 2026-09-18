# HARDWARE 1.0D — Architecture / control-plane baseline (DRAFT #68)

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## What #68 establishes
- Canonical **four-track** hardware architecture control plane
- Experience-first co-design doctrine + Experience Contract schema
- AMD **PRODUCT_MAINLINE** architecture preserved
- NXP i.MX95 **OPEN_ENGINEERING_MAINLINE** architecture package (public collateral)
- GXE **integration contract** boundary (no GXE implementation in this repo)
- COM-HPC/COTS **REFERENCE_CONTROL** preserved
- Decision ledger reconciled with track qualifiers
- `HW_ARCHITECTURE_BASELINE_MERGE_READY` separated from physical EVT/fab/cert gates

## What #68 does **not** establish
- Physical hardware validation
- AMD vendor collateral acquisition
- CPB0 / CPB0-Open fab readiness
- NXP physical board existence
- GXE execution
- EVT / DVT / PVT / certification / manufacturing validation
- Software v1.0 RC1 baseline changes

## Four-track architecture
| Track | Identity |
|---|---|
| PRODUCT_MAINLINE | AMD_CUSTOM_X86 |
| OPEN_ENGINEERING_MAINLINE | NXP_IMX95_OPEN_CUSTOM |
| GREENFIELD_EXPERIMENT | GXE |
| REFERENCE_CONTROL | COM_HPC_AND_COTS |

## Merge meaning
Merging #68 means **architecture/control-plane accepted**, not **hardware validated**.

## Experiments
#69–#79 remain DRAFT experiments targeting this branch until post-merge rebind. Not merge-ready without promotion evidence.

## Pending external work
- AMD vendor collateral (external; does not block architecture merge)
- NXP open-custom implementation / design-guide access
- GXE implementation in separate workspace

## Preferred owner action
`NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT`

Do not merge via Cursor.
