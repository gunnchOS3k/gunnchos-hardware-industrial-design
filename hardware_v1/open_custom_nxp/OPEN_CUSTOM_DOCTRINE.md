# NXP open-custom engineering doctrine

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Track

`OPEN_ENGINEERING_MAINLINE = NXP_IMX95_OPEN_CUSTOM`

## Purpose (what this lane proves)

- custom BGA application-processor integration
- memory design
- power design
- PCIe / USB
- display / camera / audio
- EC / controller integration
- security / boot / recovery
- custom board fabrication
- manufacturing
- EVT / DVT methodology
- efficiency

## Explicit non-equivalence to PRODUCT_MAINLINE (AMD x86)

NXP i.MX95 is **not** claimed equivalent to AMD Ryzen Embedded x86 for:

- Windows desktop compatibility
- x86 software compatibility
- PC gaming
- Ryzen-class CPU / GPU performance
- USB4 unless separately implemented

## NDA policy

Prefer authoritative **public** NXP collateral. Do not accept NDAs via Cursor.
If a document forbids redistribution, commit metadata / URL / hash only — never the binary.

## Physical honesty

No physical pass claims. `READY_FOR_FAB` remains false until real EDA + public rules are applied.
