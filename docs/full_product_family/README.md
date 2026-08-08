# Full product hardware design release (Continuation V)

Branch: `cursor/full-product-continuation-v-hardware-release`  
Base: `origin/main` @ `7e1658e63052e7baa2e9f4ab58113a91e4165c72` (#47)  
Updated: 2026-08-08T20:15:00Z

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Intent
Close hardware design-release honesty gaps: **component truth**, COM/NX5 pinout classification, dock USB4/TB4 vs TB5 freeze, deepen native EDA/CAD/mfg packages, attempt KiCad install, ring BOM↔FW parity.

## Products (five)
| Product | Hardware package | Exact compute MPN |
|---|---|---|
| Student 14.5 | `device_designs/student_14_5/` | ADLINK **COM-HPC-mMTL-155H-32G** + carrier |
| DS-XL Coder | `device_designs/ds_xl_coder/` | Shared COM + dual-eDP carrier |
| Handheld Hybrid | `device_designs/handheld_hybrid/` | Radxa NX5 **RM121-D8E32** + game carrier |
| Edge I/O Rings | `device_designs/edge_io_rings/` + gate1 | **nRF52840-QIAA-R** + fusion BOM; Fusion CAD + FW parity matrix |
| Dock | `device_designs/dock/` + gate1 | **JHL8440** + **JHL9040R** retimer (USB4/TB4 40G; **not TB5**) |

## Cross-cutting index
- Component truth verify: `COMPONENT_TRUTH_VERIFY_CONTINUATION_V.md`
- Dock architecture freeze: `DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md`
- COM/NX5 feasibility: `COM_HPC_NX5_FEASIBILITY_PINOUT.md`
- Exact MPN matrix: `EXACT_MPN_MATRIX.md`
- Procurement/lifecycle: `PROCUREMENT_LIFECYCLE.md`
- Release status (honest): `HARDWARE_DESIGN_RELEASE_STATUS.md`
- Release COMPLETE criteria: `RELEASE_CRITERIA.md`
- Driver classification: `DRIVER_CLASSIFICATION.md`
- Modem freeze + public verify: `MODEM_ARCHITECTURE_FREEZE.md`, `MODEM_RM520N_GL_PUBLIC_VERIFY.md`
- KiCad / EDMUND: `KICAD_STATUS.md`
- ADRs: `docs/adr/ADR-HW-001-com-carrier-strategy.md`, `docs/adr/ADR-HW-002-dock-usb4-tb4-not-tb5.md`

## Tokens
See `TOKENS.md`. **No** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` claimed.
