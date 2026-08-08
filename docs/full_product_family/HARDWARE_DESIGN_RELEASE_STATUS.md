# Hardware design release status matrix

Updated: 2026-08-08T20:15:00Z  
Branch: `cursor/full-product-continuation-v-hardware-release`  
Base: `origin/main` @ `7e1658e63052e7baa2e9f4ab58113a91e4165c72`

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only.

| Product | Exact compute MPN | EDA native package | Mfg package | Drivers | Battery/Thermal/RF | KiCad CLI | CAD | Status token |
|---|---|---|---|---|---|---|---|---|
| Student 14.5 | ADLINK **COM-HPC-mMTL-155H-32G** | Carrier sch/PCB + deepened mfg (Gerber/STEP/PnP plans) | Yes + ERC/DRC blocker JSON | Yes | Yes (MODELED) | ABSENT → EDMUND | OpenSCAD + STEP notes | `STUDENT_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| DS-XL Coder | Shared **COM-HPC-mMTL-155H-32G** | Dual-eDP carrier + ICD + mfg deepen | Yes | Yes | Yes (MODELED) | ABSENT → EDMUND | OpenSCAD + STEP notes | `DS_XL_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Handheld Hybrid | Radxa NX5 **RM121-D8E32** | SoM carrier + PUBLIC_PINOUT feasibility | Yes | Yes | Sustained game models | ABSENT → EDMUND | OpenSCAD + Radxa STP ref | `HANDHELD_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Edge I/O Rings | Nordic **nRF52840-QIAA-R** | Fusion-BOM KiCad + BOM↔FW parity matrix | Yes | Yes | Wearable models | ABSENT → EDMUND | Fusion package + OpenSCAD twin | `RINGS_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Dock | **JHL8440** + **JHL9040R** retimer | Corrected USB4/TB4 PCB package | Yes | Yes | Thermal/power; RF UWB opt | ABSENT → EDMUND | Enclosure params + SCAD | `DOCK_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |

## Family claim
- Claimed: `HARDWARE_DESIGN_RELEASE_CANDIDATE_PACKAGE_ALL_FIVE` (still)
- New Continuation V: `DOCK_ARCHITECTURE_FROZEN_USB4_TB4_NOT_TB5`, `COM_HPC_NX5_FEASIBILITY_PINOUT_CLASSIFIED`, `RING_BOM_SCH_FW_PARITY_MATRIX_DOCUMENTED`, component truth re-verify
- **Not claimed:** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` (any product)

## Why COMPLETE is not earned
1. `kicad-cli` absent (brew needs Edmund admin) → no ERC/DRC/Gerber/PnP/STEP
2. Structural `Device:R` placeholders remain (criteria #2)
3. COM-HPC full pinout still **NARROW_NDA**
4. Rings Fusion `.f3d` binary not authored; edge-io firmware gaps for IQS7222A/SE050/etc.
