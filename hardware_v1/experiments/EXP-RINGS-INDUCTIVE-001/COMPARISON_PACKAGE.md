# Inductive ring charge vs magnetic cradle contacts

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-RINGS-INDUCTIVE-001`
- Branch: `hardware/exp-rings-inductive-charge`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
Inductive charge improves durability/UX with acceptable efficiency and EMI

## Baseline (mainline)
Magnetic cradle pogo/contacts

## Variant
Qi-class or proprietary inductive coil

## Measurable comparison criteria
- `charge_efficiency_pct`
- `emi_delta_db`
- `wear_cycles`
- `alignment_fail_rate`

## Promotion gate
Efficiency >=70% at EVT coil; EMI does not fail pre-scan relative to baseline

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
