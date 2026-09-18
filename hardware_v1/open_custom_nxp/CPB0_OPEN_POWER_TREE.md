# CPB0-O power tree (public-collateral)

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Sources

- IMX95IEC § power architecture / recommended operating / absolute max rail names
- Sequence labels from IMX95IEC power-up diagrams (NVCC_BBSM first; PMIC_ON_REQ; POR_B)
- Exact PMIC OPN = pending EVK BOM / UG10210 account fetch (`PENDING_PUBLIC_REF_DESIGN`)

## Top-level

```
DC_IN 12V (DESIGN_TARGET) ──► buck/PMIC complex ──► SoC + DDR + I/O + M.2 + USB + media
                     └─► EC always-on rail (3.3V_AO DESIGN_TARGET)
```

## Rail classes (names from IMX95IEC; voltages DESIGN_TARGET / DATASHEET_CLASS)

| Rail | Class voltage | Classification | Supplies |
|---|---|---|---|
| NVCC_BBSM_1P8 | 1.8 V | DATASHEET_CLASS | BBSM; must power first / last |
| VDD_ARM | ~core | DATASHEET_CLASS | Cortex-A55 mix |
| VDD_SOC | ~core | DATASHEET_CLASS | SoC digital |
| VDD_ANA_0P8 / VDD_ANA_1P8 | 0.8 / 1.8 V | DATASHEET_CLASS | analog |
| VDD_DDR_0P8 | 0.8 V class | DATASHEET_CLASS | DDR PHY digital |
| VDD2H_DDR | 1.05 V (LPDDR5) / 1.1 V (LPDDR4X) | DATASHEET_CLASS | DDR PHY I/O |
| VDDQ_DDR | 0.5 V (LPDDR5) / 0.6 V (LPDDR4X) | DATASHEET_CLASS | DDR PHY I/O |
| VDD_USB_0P8/1P8/3P3 | PHY rails | DATASHEET_CLASS | USB |
| VDD_PCI_0P8/1P8 | PHY rails | DATASHEET_CLASS | PCIe |
| VDD_ETH_0P8/1P8 | PHY rails | DATASHEET_CLASS | Ethernet |
| VDD_MIPI_0P8/1P8 | PHY rails | DATASHEET_CLASS | MIPI |
| VDD_LVDS_1P8 | 1.8 V | DATASHEET_CLASS | LVDS (tie off if unused per datasheet) |
| VDD_AUD_1P8 | 1.8 V | DATASHEET_CLASS | audio |
| NVCC_GPIO_1P8 / 3P3 | I/O | DATASHEET_CLASS | GPIO banks |
| NVCC_SD2 | 1.8/3.3 | DATASHEET_CLASS | SD |
| 3V3_SYS / 5V_SYS | system | DESIGN_TARGET | M.2, fan, USB VBUS switch |
| VBUS_USBC | 5 V | DESIGN_TARGET | USB-C sink/source policy TBD |

## Unused PHY termination

IMX95IEC documents 10 kΩ to ground for unused PHY supply pins (USB/MIPI/PCI/ETH/LVDS classes). CPB0-O will either power used PHYs or terminate unused ones per datasheet — no invented currents.

## Measurement points (DFT)

Provide Kelvin-friendly test points on: DC_IN, 3V3_AO, NVCC_BBSM_1P8, VDD_SOC, VDD_ARM, VDD2H_DDR, VDDQ_DDR, 3V3_SYS, each M.2 power enable.

## Token

`NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD=true` — rail identity + high-level sequencing from public IMX95IEC. Detailed timing numbers remain subject to UG10210/EVK cross-check; currents are not fabricated.
