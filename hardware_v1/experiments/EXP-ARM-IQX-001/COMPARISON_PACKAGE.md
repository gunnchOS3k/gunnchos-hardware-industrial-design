# ARM IQX-class SoM vs COM-HPC Mini x86

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-ARM-IQX-001`
- Branch: `hardware/exp-arm-iqx`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
ARM SoM reduces idle power and BOM cost at equal desk productivity for Student/DS-XL

## Baseline (mainline)
COM-HPC-mMTL-155H-32G class

## Variant
ARM IQX-class SoM (vendor TBD — PENDING_VENDOR_CONFIRMATION)

## Measurable comparison criteria
- `idle_power_w`
- `sustained_compile_time_s`
- `thermal_skin_c`
- `bom_delta_usd_quote`
- `os_driver_gap_count`

## Promotion gate
All metrics meet or beat baseline on EVT mule sample n>=3 AND Device OS RC1 interface register shows zero P0 breaks

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
