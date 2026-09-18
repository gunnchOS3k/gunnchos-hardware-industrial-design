# HW1D.1 final report A–P — Accepted-Main Rebind

**Generated:** 2026-09-18T18:12:00Z  
**Campaign:** `HW1D.1_ACCEPTED_MAIN_REBIND`  
**Claim boundary:** architecture/control-plane accepted-main rebind only — not physical pass, not certification, not fab, not purchase, not GXE execution.

## A. Preconditions
PR #68 **MERGED** via **Create a merge commit**. Parents: `9ee0ef2f688b2c18428bfabc316b23687a02988d` (previous main) + `14a96d3d14fad0430ea0d59bf88c20d74b9e587b` (tested head). Experiments #69–#79 remained DRAFT before retarget.

## B. Merge proof
Merge commit `e5f15d1f1b6ddefa73c0a6127bced8d784aae425` recorded in `HW1D1_MERGE_PROOF.json` / `.md`. Verdict: `MERGE_PROOF_PASS`.

## C. Tree equivalence
Tested head tree `eba38aad9c17ff03f7d6cb398d39b0c0987d4a71` == merge commit tree (identical). Material drift: **false**. Retarget authorized.

## D. Accepted-main validation
`make hardware-v1-validate` **PASS**; `make hardware-v1-all` **PASS** at merge tree (generator timestamp churn discarded to keep freeze hashes honest); gates/BOM/experiment isolation/experience-contract/no-physical/RC1 firewall **PASS**.

## E. Architecture freeze
Four-track freeze recorded with identities + SHA-256 hashes in `HW1D1_ARCHITECTURE_FREEZE.json` / `.md`. Accepted main SHA `e5f15d1f1b6ddefa73c0a6127bced8d784aae425`.

## F. Experiment retarget
#69–#79 base retargeted `hardware/v1-mainline-ready-for-evt` → `main`; all remain **DRAFT**; experiment-only BRANCH_CLAIM deltas; no polluted-branch refresh required. Matrix: `HW1D1_EXPERIMENT_RETARGET_MATRIX.*`. Verdict: `RETARGET_MATRIX_PASS`.

## G. PR #68 metadata hygiene
Body already matches `PULL_REQUEST_BODY_HW1D.md` claim boundary; merge-proof comment posted on #68.

## H. Physical gate preservation
All listed physical/fab/cert gates remain **false**; EVT/DVT/PVT/PHYSICAL/EXTERNAL pending remain **true**. No purchase/RFQ/fab/NDA.

## I. Software RC1 firewall
`SOFTWARE_RC1_BASELINES_UNTOUCHED=true` — no software v1.0 RC1 baseline modifications.

## J. Next lanes
- `NEXT_HARDWARE_ACTION=START_NXP_OPEN_CUSTOM_IMPLEMENTATION`
- `NEXT_GXE_ACTION=BUILD_FIRST_VERTICAL_SLICE_IN_RISCV_SIM` (separate workspace)
- `PARALLEL_AMD_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`
- `OPTIONAL_REFERENCE_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

## K. Experiments not merged
#69–#79 remain DRAFT / OPEN / unmerged.

## L. Evidence landing
Evidence on branch `hardware/hw1d1-accepted-main-rebind` as DRAFT follow-up PR (not self-merged).

## M. Four-track identities (frozen)
PRODUCT_MAINLINE=`AMD_CUSTOM_X86`; OPEN_ENGINEERING_MAINLINE=`NXP_IMX95_OPEN_CUSTOM`; GREENFIELD_EXPERIMENT=`GXE`; REFERENCE_CONTROL=`COM_HPC_AND_COTS`.

## N. What accepted main means
Architecture/control-plane baseline accepted — **not** hardware validated.

## O. Campaign result
`HW1D1_ACCEPTED_MAIN_REBIND_PASS=true`

## P. Printed tokens
```
HW1D1_ACCEPTED_MAIN_REBIND_PASS=true
MERGE_PROOF_PASS=true
TREE_EQUIVALENCE_PASS=true
ACCEPTED_MAIN_VALIDATION_PASS=true
ARCHITECTURE_FREEZE_RECORDED=true
EXPERIMENT_RETARGET_PASS=true
EXPERIMENT_ISOLATION_PASS=true
PHYSICAL_GATE_PRESERVATION_PASS=true
SOFTWARE_RC1_BASELINES_UNTOUCHED=true
PHYSICAL_HARDWARE_VALIDATED=false
CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false
HARDWARE_V1_READY_FOR_EVT_BUILD=false
CPB0_READY_FOR_FAB=false
CPB0_OPEN_READY_FOR_FAB=false
RFQ_SENT=false
GXE_IMPLEMENTED_IN_HARDWARE_REPO=false
PRODUCT_MAINLINE=AMD_CUSTOM_X86
OPEN_ENGINEERING_MAINLINE=NXP_IMX95_OPEN_CUSTOM
GREENFIELD_EXPERIMENT=GXE
REFERENCE_CONTROL=COM_HPC_AND_COTS
NEXT_HARDWARE_ACTION=START_NXP_OPEN_CUSTOM_IMPLEMENTATION
NEXT_GXE_ACTION=BUILD_FIRST_VERTICAL_SLICE_IN_RISCV_SIM
PARALLEL_AMD_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL
OPTIONAL_REFERENCE_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT
ACCEPTED_MAIN_SHA=e5f15d1f1b6ddefa73c0a6127bced8d784aae425
TESTED_PR68_HEAD=14a96d3d14fad0430ea0d59bf88c20d74b9e587b
```
