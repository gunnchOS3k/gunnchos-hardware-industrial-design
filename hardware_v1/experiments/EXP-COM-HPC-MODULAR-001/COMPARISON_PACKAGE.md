# EXP-COM-HPC-MODULAR-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
COM-HPC modular product architecture vs custom motherboard mainline

## Hypothesis
COM-HPC modular path matches product goals with lower board complexity; measure whether giving up motherboard ownership is justified

## Baseline (mainline)
CUSTOM AMD Platform Core v1 (8840U/8845HS)

## Variant
ADLINK COM-HPC Mini mMTL + Mini Base REFERENCE_CONTROL_MODULAR_X86

## Metrics
- time_to_bringup
- bom_complexity
- thermal_skin_c
- usb4_behavior
- os_compat
- ownership_score
- schedule_risk

## Promotion gate
Measured evidence that modular path meets product goals AND owner explicitly accepts reduced motherboard ownership; cannot silently become mainline

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
