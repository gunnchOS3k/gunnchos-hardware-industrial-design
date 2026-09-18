# Test points / DFT

**Generated:** 2026-09-18T18:37:46Z
**Campaign:** `STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION`
**Claim boundary:** digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps.


| TP | Net role | Purpose |
|---|---|---|
| TP_GND | GND | Fixture common |
| TP_VSYS | VSYS placeholder | Power bring-up |
| TP_UART_TX/RX | Debug UART | Console |
| TP_SWDIO/SWCLK | Debug | MCU/AP debug path |
| TP_BOOTCFG | Boot straps | Sample boot mode |

Fixtures: `fixtures/imx95_open_pogo_fixture.md`
