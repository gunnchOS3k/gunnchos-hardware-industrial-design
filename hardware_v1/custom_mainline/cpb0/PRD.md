# CPB0 — gunnchOS Custom Platform Board 0 PRD

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Purpose

Primary pre-product motherboard learning platform. Deliberately debug-friendly, not pretty.

## Primary SoC candidate

`AMD Ryzen Embedded 8845HS` (OPN ref `100-000001316E`)  
Fallback: `8840U` only if vendor-access constraints require it.

## Required subsystems

BGA SoC, DDR5, full power tree, VRM, EC, SPI flash, TPM, NVMe, Wi-Fi, optional cellular,
USB4, USB 3.x/2, display outputs (min one eDP + DDI/DP), audio, camera, I2C/SPI/UART/GPIO,
USB-C PD, fan control, current sensing, rail test points, JTAG/SWD/UART, POST/debug LEDs,
board-revision straps, recovery switch, firmware recovery header, external bench power,
battery emulator input, thermistor headers.

## Fab readiness

`CPB0_READY_FOR_FAB=false` until net-accurate AMD collateral and actual EDA outputs exist.
