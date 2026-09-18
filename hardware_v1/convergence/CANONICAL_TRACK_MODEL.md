# Canonical four-track model

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Rule

Do **not** use the word “mainline” without a track qualifier.

| Track qualifier | Identity | Role |
|---|---|---|
| `PRODUCT_MAINLINE` | `AMD_CUSTOM_X86` | Best product-performance / x86 compatibility target |
| `OPEN_ENGINEERING_MAINLINE` | `NXP_IMX95_OPEN_CUSTOM` | No-NDA custom-board learning + fabrication path |
| `GREENFIELD_EXPERIMENT` | `GXE` | Experience-first experimental ecosystem (integration contract only here) |
| `REFERENCE_CONTROL` | `COM_HPC_AND_COTS` | Known-good control / fault isolation |

## PRODUCT_MAINLINE — AMD_CUSTOM_X86

- Student / Handheld: Ryzen Embedded 8840U candidates
- DS-XL: Ryzen Embedded 8845HS candidate
- Custom motherboards, Dock, Rings remain product-intent
- Vendor collateral pending is an **external** blocker, not an architecture-merge blocker

## OPEN_ENGINEERING_MAINLINE — NXP_IMX95_OPEN_CUSTOM

- Public NXP collateral path under `hardware_v1/open_custom_nxp/`
- Proves BGA AP integration, memory/power/PCIe/USB/display/camera, EC, security/boot, fab/EVT methodology
- Explicitly **not** product-equivalent to AMD x86 for Windows/gaming/Ryzen-class performance

## GREENFIELD_EXPERIMENT — GXE

- Defined only via `GXE_HARDWARE_INTEGRATION_CONTRACT.md` in this repo
- No GXE implementation executed here

## REFERENCE_CONTROL — COM_HPC_AND_COTS

- RP0-A COTS procurement packet, COM-HPC architecture, COTS Dock, nRF54L15 DK
- Optional owner order only; not PRODUCT_MAINLINE

Machine-readable: `CANONICAL_TRACK_MODEL.json`
