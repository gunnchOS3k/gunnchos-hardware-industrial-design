# CPB0-O EC / supervisory MCU architecture

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Decision

**Use a separate Zephyr-based EC / supervisory MCU** on CPB0-O for learning and future transfer to AMD product mainline EC patterns.

Preferred class: open, non-NDA MCU with good Zephyr support (exact MPN in BOM as candidate; verify at purchase).

## Responsibilities

- Power button debounce / ONOFF assist
- Rail enables / PG monitoring / fault LED
- Fan PWM / tach
- Battery emulator header (later BMS) — DC-in first
- Watchdog kick / reset request to PMIC path
- Board ID / inventory EEPROM
- Recovery strap drive
- Debug UART mux / status
- Thermal sensors (board)

## Interfaces

- I2C to PMIC + sensors
- GPIO to enables / PG / straps
- UART to host console share
- SWD for EC itself

## Non-claims

EC firmware is not a software RC1 deliverable. No physical bring-up asserted.
