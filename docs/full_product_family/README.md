# Full product hardware design release (Continuation IV)

Branch: `cursor/full-product-hardware-design-release`  
Base: `origin/main` @ `79b11aba3ca9d4db7051b6d5ccb3571e72503396`  
Updated: 2026-08-08T19:40:00Z

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Intent
Move beyond family **depth/skeleton** toward **HARDWARE_DESIGN_RELEASE_CANDIDATE** packages for all five products, with **exact orderable MPNs** (no vague COM-class strings, no fake CPU BGA).

## Products (five)
| Product | Hardware package | Exact compute MPN |
|---|---|---|
| Student 14.5 | `device_designs/student_14_5/` | ADLINK **COM-HPC-mMTL-155H-32G** + carrier |
| DS-XL Coder | `device_designs/ds_xl_coder/` | Shared COM + dual-eDP carrier |
| Handheld Hybrid | `device_designs/handheld_hybrid/` | Radxa NX5 **RM121-D8E32** + game carrier |
| Edge I/O Rings | `device_designs/edge_io_rings/` + gate1 | **nRF52840-QIAA-R** + fusion BOM; Fusion CAD package |
| Dock | `device_designs/dock/` + gate1 | **JHL9040** discrete PCB (beyond skeleton) |

## Cross-cutting index
- Exact MPN matrix: `EXACT_MPN_MATRIX.md`
- Procurement/lifecycle: `PROCUREMENT_LIFECYCLE.md`
- Release status (honest): `HARDWARE_DESIGN_RELEASE_STATUS.md`
- Release COMPLETE criteria: `RELEASE_CRITERIA.md`
- Driver classification: `DRIVER_CLASSIFICATION.md`
- Modem freeze + public verify: `MODEM_ARCHITECTURE_FREEZE.md`, `MODEM_RM520N_GL_PUBLIC_VERIFY.md`
- KiCad / EDMUND: `KICAD_STATUS.md`
- ADR: `docs/adr/ADR-HW-001-com-carrier-strategy.md`

## Tokens
See `TOKENS.md`. **No** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` claimed.
