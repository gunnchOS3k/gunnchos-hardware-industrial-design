# CPB0-O stackup requirements (draft)

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Candidate 12-layer class (DESIGN_TARGET)

| Layer | Intent |
|---|---|
| L1 | Sig HS + SMT |
| L2 | GND |
| L3 | Sig DDR/HS |
| L4 | GND |
| L5 | PWR shapes |
| L6 | PWR / GND |
| L7 | PWR shapes |
| L8 | GND |
| L9 | Sig DDR/HS |
| L10 | GND |
| L11 | Sig |
| L12 | Sig SMT |

## Impedance classes (targets TBD — fab + UG10210)

- 50 Ω SE
- 90 Ω USB diff
- 85–100 Ω PCIe/MIPI class (confirm)
- DDR class per design guide

No fab house assumed. Finalize after account-login design guide + fab capability notes.
