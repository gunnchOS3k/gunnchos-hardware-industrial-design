# CPB0-Open PRD (NXP open-custom learning board)

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Intent
Debug-friendly open-custom learning board on i.MX95 for board-level ownership without AMD NDA.

## Must prove
BGA fanout, LPDDR class memory, PMIC/sequencing, PCIe/USB, display/camera hooks, EC, secure boot path, DFT/bring-up.

## Must not claim
Product performance parity with AMD PRODUCT_MAINLINE; Windows/game readiness; USB4 unless separately designed.

## Fab readiness
`CPB0_OPEN_READY_FOR_FAB=false` until public design rules + real EDA exist.

