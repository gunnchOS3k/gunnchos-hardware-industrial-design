# RP0-A dock validation path (COTS USB4)

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## Mainline Dock Gen-1 (unchanged intent)
USB4 40 Gb/s, USB PD EPR, 2.5 GbE, display, downstream USB, field-updatable controller.

## RP0-A approach
Use a commercially available USB4/TB4 dock/reference platform to validate gunnchOS USB4,
display, Ethernet, USB, suspend/resume, power-policy, and recovery.

## Hard boundary
- RP0-A COTS dock results **do not** prove / certify the custom gunnchOS dock PCB
- Capture VID/PID/controller/firmware when accessible during physical bring-up
- Ball maps remain vendor-gated for RP0-B

## Requirements-equivalence matrix (behavioral)
| Intended Dock v1 behavior | RP0-A COTS proxy | Equivalence class |
|---|---|---|
| USB4 host link | COTS USB4/TB4 dock uplink | BEHAVIORAL_PROXY |
| External display | COTS dock DP/HDMI | BEHAVIORAL_PROXY |
| 2.5 GbE | COTS dock Ethernet (note if 1G only) | PARTIAL_IF_1G |
| Downstream USB | COTS dock USB-A/C | BEHAVIORAL_PROXY |
| PD / power policy | Certified PD supply + meter | BEHAVIORAL_PROXY |
| Custom JHL8440 fanout | — | NOT_COVERED (RP0-B) |
| Custom JHL9040R retimer | — | NOT_COVERED (RP0-B) |

## Tokens
`EXT_JHL8440_BALLMAP_RP0_A_BLOCKING=false`
`EXT_JHL8440_BALLMAP_RP0_B_BLOCKING=true`
`EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING=false`
`EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING=true`
