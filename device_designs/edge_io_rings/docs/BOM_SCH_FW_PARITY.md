# Ring BOM ↔ schematic ↔ firmware parity (hardware ↔ edge-io)

Updated: 2026-08-08T20:15:00Z  
Hardware repo branch: `cursor/full-product-continuation-v-hardware-release`  
edge-io reference SHA: `fc617e831916362e77aa157d77d458e935dc4cfa`

PHYSICAL_EXECUTION_FREEZE ACTIVE — digital parity only.

## Sources
| Layer | Location |
|---|---|
| Hardware BOM | `device_designs/edge_io_rings/bom/assembly_bom.csv` |
| Hardware schematic | `device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch` |
| edge-io firmware pinout | `gate1_digital_fabrication/ring_firmware/dts/pinout.json` |
| edge-io board DT | `gate1_digital_fabrication/ring_firmware/boards/edge_io_ring/edge_io_ring.dts` |
| edge-io Zephyr smoke | `gate1_digital_fabrication/ring_firmware/zephyr_app/src/main.c` |

## Parity matrix

| MPN / function | In hardware BOM | In hardware KiCad Value | In edge-io pinout/DT | Firmware driver status | Verdict |
|---|---|---|---|---|---|
| nRF52840-QIAA-R | YES | YES (U1) | YES (mcu) | Zephyr west smoke build | **PARITY** |
| BMI270 | YES | YES (U2) | YES I2C `0x68` + INT P0.11 | Stub/DT only | **PARITY (DT)** |
| DRV2605L | YES | (BOM haptic driver) | YES I2C `0x5A` | Stub/DT only | **PARITY (DT)** |
| IQS7222A (cap touch) | YES | YES (U3) | **NO** | Missing | **GAP** → edge-io PR |
| DWM3001C (UWB) | YES (DNP OK) | YES DNP (U4) | **NO** | Missing | **GAP** (optional EVT) |
| BHI360 | YES alternate | YES DNP (U5) | **NO** | Missing | **GAP** (optional) |
| BMM350 | YES optional | YES DNP (U6) | **NO** | Missing | **GAP** (optional) |
| SE050C1HQ1 | YES | YES (U7) | **NO** | Missing | **GAP** → edge-io PR |
| npm1300-CAAA-R | YES | (power tree) | **NO** (only CHG_STATUS GPIO) | Partial | **PARTIAL** |
| Johanson 2450AT18A100 | YES | RF model | N/A antenna | N/A | BOM-only OK |
| I2C SDA/SCL | implied | nets MODELED | P0.26 / P0.27 | DT aliases | **PARITY** |
| CHG_STATUS | pogo/ESD path | MODELED | P0.02 | DT | **PARITY** |

## Honesty
- edge-io Zephyr app at reference SHA is a **west build smoke** (`printk` loop) — not full sensor fusion firmware.
- Hardware schematic still uses structural `Device:R` placeholders — Values track BOM MPNs; footprints incomplete → blocks `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE`.
- Pin numbers in edge-io are labeled EVT0 assumptions pending physical verify (`RING_PHYSICAL_BOOT_PENDING`).

## Recommended edge-io follow-up (second PR)
Branch suggestion: `cursor/full-product-continuation-v-ring-firmware-parity`
1. Extend `pinout.json` + DT with IQS7222A + SE050 I2C addresses (from datasheets) and reserved GPIOs.
2. Document DNP optional lines (DWM3001C, BHI360, BMM350) as `#if` stubs.
3. Align npm1300 CHG/INT bindings with hardware power tree.
4. Do **not** claim `RING_PHYSICAL_BOOT` under freeze.

## Tokens
- Claimed here: `RING_BOM_SCH_FW_PARITY_MATRIX_DOCUMENTED`
- Not claimed: full firmware feature parity / physical boot
