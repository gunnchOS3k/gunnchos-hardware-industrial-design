# CPB0-O stackup V1 (design intent — not fabricator-approved)

**Generated:** 2026-09-18T19:17:34Z  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## Decision

**14-layer** provisional stackup for 0.7 mm pitch BGA escape + LPDDR5 + multi-gigabit SerDes.

| Layer | Type | Copper | Role |
|---|---|---|---|
| L1 | SIGNAL | 0.5 oz finish | BGA escape, USB/PCIe breaks |
| L2 | GND | 1 oz | reference |
| L3 | SIGNAL | 0.5 oz | DDR byte lanes |
| L4 | GND | 1 oz | reference |
| L5 | SIGNAL | 0.5 oz | DDR CA/CLK |
| L6 | PWR | 1 oz | VDD_SOC / splits |
| L7 | PWR | 1 oz | VDDQ/VDD2H / analog |
| L8 | GND | 1 oz | reference |
| L9 | SIGNAL | 0.5 oz | PCIe/USB/ENET |
| L10 | GND | 1 oz | reference |
| L11 | SIGNAL | 0.5 oz | low-speed + MIPI |
| L12 | GND | 1 oz | reference |
| L13 | PWR | 1 oz | 3V3/1V8 planes |
| L14 | SIGNAL | 0.5 oz | bottom escape / test |

## Impedance classes (targets — confirm with fab)

- 50 Ω single-ended GPIO/clocks
- 90 Ω USB differential
- 85–100 Ω PCIe / Ethernet / MIPI (per interface standard + NXP guide when available)
- DDR: **values TBD pending UG10210**

## Via strategy

- Through-vias for power/GND; microvia L1-L2 / L14-L13 for BGA fanout as needed.
- Via-in-pad only under BGA with filled/capped note.
- Controlled-impedance coupon required on panel.

`CPB0_OPEN_STACKUP_DEFINED=true` (design stackup, not fab signoff).
