# Post-merge plan — prepare only (do not execute)

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## After owner merges #68 with a merge commit

1. Verify accepted-main merge SHA and parents
2. Verify merge tree equals tested #68 head
3. Run accepted-main validators
4. Record accepted hardware-architecture freeze SHA
5. Retarget #69–#79 from `hardware/v1-mainline-ready-for-evt` to `main`
6. Ensure each experiment shows only its intended delta
7. Keep them DRAFT
8. Do not merge any experiment
9. Start NXP open-custom implementation lane and GXE v2 separately

## Expected next campaign

`HW1D.1_ACCEPTED_MAIN_REBIND`

## Execution status (HW1D.1)

Owner merged #68 with a merge commit (`e5f15d1f1b6ddefa73c0a6127bced8d784aae425`).  
HW1D.1 accepted-main rebind evidence is under `hardware_v1/convergence/accepted_main/`.  
Experiments #69–#79 were retargeted to `main` and kept DRAFT (not merged).

## Non-execution (historical prep note)

This file originally said Cursor must **not** merge #68 or retarget until the owner merges — that precondition is now satisfied.
