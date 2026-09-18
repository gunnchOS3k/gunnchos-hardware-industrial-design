# Dock no-NDA digital path

**Generated:** 2026-09-18T18:37:46Z
**Campaign:** `STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION`
**Claim boundary:** digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps.


## Mainline digital path (public silicon)
| Block | Public direction |
|---|---|
| USB-C PD | TI TPS65994 / TPS25751 class dual-port PD controller |
| USB3 hub | VL817 / GL3523 class USB3 hub |
| DP Alt Mode | PD Alt Mode mux + DP redriver class (public datasheets) |
| Ethernet | RTL8153 / similar USB-ETH or discrete 2.5GbE PHY with public docs |
| Audio | USB audio codec class OR 3.5mm via USB audio bridge |
| ESD | TPD4E / USBLC6 class on exposed ports |
| MCU/EC | STM32G0 / RP2040 class dock manager firmware |
| Thermal | NTC + copper pour + optional fan tach |

## Experimental (not required for no-NDA exhaustion)
USB4 / Thunderbolt JHL8440 + JHL9040R — remains `EXPERIMENTAL` / NDA-blocked (`EXT-JHL*`).

Production-intent USB4 custom dock stays blocked; this package exhausts the **public** dock.
