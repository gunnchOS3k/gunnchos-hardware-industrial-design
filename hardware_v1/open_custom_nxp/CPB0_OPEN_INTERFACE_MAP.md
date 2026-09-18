# CPB0-O interface ownership map

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Status

- Interface **ownership** (which subsystem owns which SoC interface class) is defined below from public IMX95IEC connectivity + CPB0-O PRD.
- **Ball-accurate pin/mux assignment is NOT complete.** CSV marks `unresolved=true` for every row until IMX95IEC package contact assignments + IMX95RM IOMUX are extracted.
- Therefore: **`NXP_PUBLIC_PINMAP_UNDERSTOOD=false`**.

Unresolved rows in `CPB0_OPEN_PINMUX_MAP.csv`: **26/26**.

## Ownership (CPB0-O)

| Interface class | Owner sheet | Destination | Notes |
|---|---|---|---|
| LPDDR5 x32 | 04_lpddr | on-board DRAM | Prefer EVK-like topology |
| PCIe0 x1 | 06_pcie_nvme | M.2 M-key NVMe | Gen3 |
| PCIe1 x1 | 07_wifi | M.2 E-key Wi-Fi | optional cellular uses separate M.2 B-key path |
| USB3 + USB2 | 09_usb | USB-C | No USB4 claim |
| 2× GbE | 10_ethernet | RJ45 magnetics/PHY | TSN capable silicon; product antenna N/A |
| 10 GbE | 10_ethernet | optional / DNP | 19×19 only |
| MIPI DSI | 11_display | FPC connector | primary display |
| MIPI CSI | 12_camera | FPC connector | one camera path |
| Audio SAI | 13_audio | codec + 3.5 mm / I2S header | |
| eMMC + FlexSPI | 05_boot_flash | eMMC + SPI NOR | boot media |
| UART/I2C/SPI/GPIO | 14_ec / 15_debug | EC + debug | |
| Clocks/reset/PMIC | 03_power / 16_clocks | PMIC + xtals | POR_B / PMIC_ON_REQ per IMX95IEC |
| Security/lifecycle | 08_security_boot | EdgeLock / fuses | no secure-boot pass claim |

## Required before pinmap token true

1. Extract package contact assignments for MIMX9596 VZ from IMX95IEC.
2. Map each CPB0-O net to ball + IOMUX from IMX95RM.
3. Zero unresolved rows for required CPB0 signals.
