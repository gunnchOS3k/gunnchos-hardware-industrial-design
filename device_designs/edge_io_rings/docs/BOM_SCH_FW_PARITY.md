# Ring BOM ↔ schematic ↔ firmware parity (Continuation VI)

Updated: 2026-08-08T20:58:59Z  
Hardware branch: `cursor/full-product-continuation-vi-eda-closure`  
edge-io reference baseline: `gate1_digital_fabrication/edge_io_ring/validation/baselines/pinout_baseline.json`

PHYSICAL_EXECUTION_FREEZE ACTIVE — digital parity only.

## Sources
| Layer | Location |
|---|---|
| Hardware BOM | `device_designs/edge_io_rings/bom/assembly_bom.csv` |
| Hardware schematic | `device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch` |
| In-repo pinout baseline | `gate1_digital_fabrication/edge_io_ring/validation/baselines/pinout_baseline.json` |
| Proposed DT overlay notes | this file §Proposed edge-io DT parity |

## Parity matrix

| MPN / function | Hardware BOM | Hardware KiCad Value | Baseline DT/pinout | Firmware status | Verdict |
|---|---|---|---|---|---|
| nRF52840-QIAA-R | YES | YES (U1) | YES MCU | Zephyr smoke | **PARITY** |
| BMI270 | YES | YES (U2) | I2C `0x68` + INT P0.11 | DT stub | **PARITY (DT)** |
| DRV2605LDGSR | YES | YES (U8) | I2C `0x5A` proposed | Stub | **PARITY (DT note)** |
| IQS7222A | YES | YES (U3) | I2C `0x44` class + RDY GPIO proposed | Missing in baseline | **GAP → edge-io** |
| DWM3001C | YES DNP | YES DNP (U4) | SPI reserved proposed | Optional | **GAP optional** |
| BHI360 | YES alt | YES DNP (U5) | — | Optional | **GAP optional** |
| BMM350 | YES opt | YES DNP (U6) | — | Optional | **GAP optional** |
| SE050C1HQ1 | YES | YES (U7) | I2C `0x48`/`0x1a` family proposed | Missing | **GAP → edge-io** |
| npm1300-CAAA-R | YES | YES (U9 Cont VI) | CHG_STATUS P0.02 exists | Partial | **PARTIAL→IMPROVED** |
| TLV75533PDBVR | YES | YES (U10 Cont VI) | power | N/A | **PARITY** |
| Johanson 2450AT18A100 | YES | YES (ANT1) | RF_ANT | N/A | **PARITY** |
| I2C SDA/SCL | implied | nets | P0.26 / P0.27 | DT | **PARITY** |

## Proposed edge-io DT parity (second PR — do not forge physical boot)

```
/* proposed overlay — addresses from public datasheets; GPIOs TBD with board bring-up */
&i2c0 {
  iqs7222a@44 { compatible = "azoteq,iqs7222a"; reg = <0x44>; /* CAP_RDY GPIO TBD */ };
  se050@48 { compatible = "nxp,se05x"; reg = <0x48>; };
  drv2605@5a { compatible = "ti,drv2605l"; reg = <0x5a>; };
  npm1300@6b { compatible = "nordic,npm1300"; reg = <0x6b>; };
};
```

GPIO freeze already in baseline: I2C P0.26/P0.27, IMU_INT P0.11, CHG_STATUS P0.02.  
New GPIOs for CAP_RDY / SE_IRQ / HAPTIC_TRIG remain **TBD_BOARD** — not invented.

## Honesty
- Structural `Device:R` placeholders remain → blocks `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE`.
- Cont VI aligned KiCad Values to BOM preferred PMIC/LDO MPNs.
- No `RING_PHYSICAL_BOOT` claim under freeze.

## Tokens
- `RING_EDA_DT_PARITY_NOTES_COMPLETE`
- `RING_BOM_SCH_FW_PARITY_MATRIX_DOCUMENTED` (updated)
- Not claimed: `RING_DESIGN_RELEASE_COMPLETE`, full firmware feature parity
