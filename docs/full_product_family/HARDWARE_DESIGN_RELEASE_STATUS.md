# Hardware design release status matrix

Updated: 2026-08-08T19:40:00Z  
Branch: `cursor/full-product-hardware-design-release`  
Base: `origin/main` @ `79b11aba3ca9d4db7051b6d5ccb3571e72503396`

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only.

| Product | Exact compute MPN | EDA native package | Mfg package | Drivers | Battery/Thermal/RF | KiCad CLI | CAD | Status token |
|---|---|---|---|---|---|---|---|---|
| Student 14.5 | ADLINK **COM-HPC-mMTL-155H-32G** | Carrier sch/PCB structure deepened | Yes (carrier) | Yes | Yes (MODELED) | ABSENT → EDMUND | OpenSCAD + STEP notes | `STUDENT_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| DS-XL Coder | Shared **COM-HPC-mMTL-155H-32G** | Dual-eDP carrier structure + ICD | Yes | Yes | Yes (MODELED) | ABSENT → EDMUND | OpenSCAD + STEP notes | `DS_XL_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Handheld Hybrid | Radxa NX5 **RM121-D8E32** | SoM carrier structure deepened | Yes | Yes | Sustained game models | ABSENT → EDMUND | OpenSCAD + STEP notes | `HANDHELD_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Edge I/O Rings | Nordic **nRF52840-QIAA-R** | Fusion-BOM-tracking KiCad + Fusion package | Yes (gate1+device) | Yes | Wearable models | ABSENT → EDMUND | Fusion package + OpenSCAD twin | `RINGS_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |
| Dock | Intel **JHL9040** (+ discretes) | Full digital PCB package (beyond skeleton) | Yes | Yes | Thermal/power; RF UWB opt | ABSENT → EDMUND | Enclosure params + SCAD | `DOCK_HARDWARE_DESIGN_RELEASE_CANDIDATE` — **not COMPLETE** |

## Family claim
- Claimed: `HARDWARE_DESIGN_RELEASE_CANDIDATE_PACKAGE_ALL_FIVE`
- **Not claimed:** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` (any product)
