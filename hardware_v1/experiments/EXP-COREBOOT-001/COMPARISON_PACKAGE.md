# coreboot vs vendor UEFI

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-COREBOOT-001`
- Branch: `hardware/exp-coreboot`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
coreboot improves auditability without breaking Device OS RC1 boot contract

## Baseline (mainline)
Vendor UEFI on COM-HPC

## Variant
coreboot + LinuxBoot or equivalent

## Measurable comparison criteria
- `secure_boot_chain_intact`
- `boot_time_s`
- `capsule_update_compat`
- `rc1_interface_breaks`

## Promotion gate
Zero P0 RC1 interface breaks; measured boot on EVT mule

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
