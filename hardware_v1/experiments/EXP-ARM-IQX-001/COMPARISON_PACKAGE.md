# EXP-ARM-IQX-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
ARM IQX-class SoM vs custom AMD Platform Core v1

## Hypothesis
ARM SoM reduces idle power and BOM cost at equal desk productivity vs owned custom AMD motherboard

## Baseline (mainline)
CUSTOM AMD Platform Core v1 (8840U/8845HS)

## Variant
ARM IQX-class SoM (vendor TBD — PENDING_VENDOR_CONFIRMATION)

## Metrics
- idle_power_w
- sustained_compile_time_s
- thermal_skin_c
- bom_delta_usd_quote
- os_driver_gap_count
- ownership_score

## Promotion gate
All metrics meet or beat baseline on EVT sample n>=3 AND Device OS RC1 interface register shows zero P0 breaks; owner accepts reduced x86 ownership

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
