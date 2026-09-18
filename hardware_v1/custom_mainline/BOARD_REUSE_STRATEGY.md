# Board reuse strategy

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Shared

- Platform Core v1 schematic blocks
- EC firmware architecture
- boot policy / Secure Boot key management patterns
- bring-up instrumentation philosophy
- AVL classes for NVMe / Wi-Fi / optional cellular / TPM

## Product-specific

| Board | Drivers of divergence |
|---|---|
| Student-MB-v1 | 14.5" thermal/mechanical, serviceability, battery capacity |
| Handheld-MB-v1 | compactness, controls, vapor chamber, M.2 2230 if packaging permits |
| DSXL-MB-v1 | dual-display eDP+DDI, higher sustained power, cooling |
| CPB0 | oversized debug headers, rail test points, bench power, battery emulator |

Do **not** force identical PCB dimensions across products.
