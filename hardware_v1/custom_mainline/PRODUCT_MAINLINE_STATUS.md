# PRODUCT_MAINLINE status — AMD_CUSTOM_X86

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Track identity

`PRODUCT_MAINLINE = AMD_CUSTOM_X86` (gunnchOS Platform Core v1)

## Preserved HW1C architecture

| Device | Candidate | Status |
|---|---|---|
| Student 14.5 | Ryzen Embedded 8840U | Architecture-complete; vendor-gated implementation |
| Handheld Hybrid | Ryzen Embedded 8840U | Architecture-complete; vendor-gated implementation |
| DS-XL | Ryzen Embedded 8845HS | Architecture-complete; vendor-gated implementation |
| Custom Dock | USB4 40 Gen-1 | Architecture-complete; JHL ballmaps external |
| Custom Rings | nRF54L15 | Architecture-complete; CSP47 form-factor pending |

## Vendor access

`CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false`

This is an **honest external blocker** for physical/silicon integration.

It is **not** a reason the architecture/control-plane baseline (#68) cannot merge.

## Physical gates (remain false)

- `CPB0_SCHEMATIC_READY=false`
- `CPB0_PCB_READY=false`
- `CPB0_READY_FOR_FAB=false`
- `CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false`
- `HARDWARE_V1_READY_FOR_EVT_BUILD=false`

## Relationship to OPEN_ENGINEERING_MAINLINE

NXP open-custom advances board-learning / fab methodology in parallel.
It does **not** replace PRODUCT_MAINLINE performance/compatibility requirements.
