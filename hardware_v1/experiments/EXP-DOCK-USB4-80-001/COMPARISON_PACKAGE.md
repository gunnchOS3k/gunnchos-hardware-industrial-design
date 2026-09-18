# Dock USB4 80 vs USB4 40

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-DOCK-USB4-80-001`
- Branch: `hardware/exp-dock-usb4-80`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
USB4 80 improves external display/storage UX enough to justify controller cost/SI risk

## Baseline (mainline)
JHL8440 USB4 40 + JHL9040R

## Variant
USB4 80-class controller (vendor TBD — PENDING_VENDOR_CONFIRMATION)

## Measurable comparison criteria
- `link_rate_gbps`
- `eye_margin`
- `bom_delta_usd`
- `cable_interop_pass_rate`

## Promotion gate
Measured eye margin at length L with owner cables; no mainline mix until DVT

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
