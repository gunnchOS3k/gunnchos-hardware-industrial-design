# EXP-RINGS-INDUCTIVE-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
Inductive ring charge vs magnetic cradle contacts

## Hypothesis
Inductive charge improves durability/UX with acceptable efficiency and EMI

## Baseline (mainline)
Magnetic cradle pogo/contacts (custom ring mainline)

## Variant
Qi-class or proprietary inductive coil

## Metrics
- charge_efficiency_pct
- emi_delta_db
- wear_cycles
- alignment_fail_rate

## Promotion gate
Efficiency >=70% at EVT coil; EMI does not fail pre-scan relative to baseline

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
