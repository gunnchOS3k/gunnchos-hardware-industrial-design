# Custom-First Architecture Doctrine

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


> **Mainline = maximum practical customization and ownership of the platform.**
>
> **Simpler modular/COTS implementations become reference/control or experimental variants.**

This does **not** mean designing CPU, cellular baseband, Wi-Fi, or closed PHY IP from scratch.
It means the mainline owns the **board around the silicon**.

## MAINLINE_CUSTOM

Production-intent Gen-1 path owns:

- motherboard / carrier PCB
- SoC package integration
- memory topology
- power tree / VRM / sequencing
- EC / supervisory MCU
- USB4 routing
- PCIe routing
- display routing
- NVMe
- Wi-Fi module integration
- optional cellular module integration
- audio, camera, sensors
- battery / BMS / charging
- TPM / root of trust
- firmware interfaces
- recovery/debug
- thermal solution
- antenna placement
- industrial/mechanical integration
- DFM/DFT/serviceability

Primary compute mainline: **gunnchOS Platform Core v1** (AMD Ryzen Embedded 8000 FP7r2 BGA custom motherboard family).

## REFERENCE_CONTROL

Simpler COTS platforms exist to provide:

- known-good comparison
- software validation
- bring-up isolation
- performance baseline
- driver/reference behavior
- fallback if custom board slips

They do **not** define the final product architecture.

Examples:

- ADLINK COM-HPC Mini mMTL + Mini Base → `REFERENCE_CONTROL_MODULAR_X86`
- COTS TB4/USB4 dock → `REFERENCE_CONTROL_DOCK`
- nRF54L15 DK → `REFERENCE_CONTROL_RING`

## EXPERIMENTAL_VARIANT

Alternative architectures may be better for specific SKUs, but can only replace mainline after measured comparison evidence.

Fail-closed rules:

- COM-HPC cannot be marked production mainline
- COTS/reference-control evidence cannot mark custom-board pass
- AMD custom pin/power/DDR collateral cannot be invented
- CPB0 cannot be READY_FOR_FAB without net-accurate vendor collateral + real EDA
- experimental variant cannot silently promote
- public package family equality ≠ pin compatibility without vendor confirmation

## HW1D track qualifiers

Ambiguous bare “mainline” is retired for control-plane language.

- `PRODUCT_MAINLINE` = `AMD_CUSTOM_X86` (this doctrine’s custom Platform Core path)
- `OPEN_ENGINEERING_MAINLINE` = `NXP_IMX95_OPEN_CUSTOM` (parallel no-NDA engineering lane)
- `GREENFIELD_EXPERIMENT` = `GXE` (integration contract only in this repo)
- `REFERENCE_CONTROL` = `COM_HPC_AND_COTS`

`MAINLINE_CUSTOM` in this document means **PRODUCT_MAINLINE** board ownership around AMD silicon.
