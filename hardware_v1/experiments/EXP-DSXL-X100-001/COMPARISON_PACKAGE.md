# EXP-DSXL-X100-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
DS-XL Ryzen AI Embedded X100-class vs 8845HS mainline

## Hypothesis
X100/X168i-class improves local AI/create workloads enough to justify LPDDR5X/PCB complexity and power

## Baseline (mainline)
Ryzen Embedded 8845HS Platform Core

## Variant
Ryzen AI Embedded X168i-class (PENDING_VENDOR_CONFIRMATION)

## Metrics
- cpu_perf
- gpu_perf
- npu_perf
- compile
- local_ai
- gaming
- power
- thermal
- lpddr5x_integration
- pcb_complexity
- cost
- battery_impact
- charger_requirement
- cooling
- longevity
- firmware
- compatibility

## Promotion gate
Physical comparison n>=3; do not promote without measured data

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
