# CPB0-O display / camera / audio

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Primary display

| Field | Value |
|---|---|
| Interface | MIPI DSI (lane count PENDING_PINMUX) |
| Connector | FPC debug-friendly |
| Power sequencing | panel rails after MIPI PHY rails |
| Test endpoint | DSI test points + optional EVK-class panel adapter |
| Software | NXP Linux BSP display stack as control |

## Camera

| Field | Value |
|---|---|
| Interface | MIPI CSI (one path minimum) |
| Connector | FPC |
| Clocking | sensor MCLK from SoC clocking block |
| Test endpoint | CSI test points / known-good sensor module later |
| Software | V4L2 / NXP camera notes (some ANs account-gated) |

## Audio

| Field | Value |
|---|---|
| Interface | SAI / I2S to codec |
| I/O | headset jack and/or header |
| Supply | VDD_AUD_1P8 must be supplied (IMX95IEC) |

## Debug-friendly

All media connectors placed on board edge with silkscreen IDs; no claim of production HMI.
