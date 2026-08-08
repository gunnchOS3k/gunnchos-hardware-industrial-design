# Full product hardware family depth

Branch: `cursor/full-product-hardware-family-depth`  
Base: `origin/main` @ `2ff20bedfe07d1a951872973155202c3b632e8b1`  
Updated: 2026-08-08T01:15:00Z

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Products (five)
| Product | Hardware package | Strategy |
|---|---|---|
| Student 14.5 | `device_designs/student_14_5/` | **COM module + carrier** (no fake proprietary CPU BGA) |
| DS-XL Coder | `device_designs/ds_xl_coder/` | Shared COM + dual-eDP carrier + second-display ICD |
| Handheld Hybrid | `device_designs/handheld_hybrid/` | RK3588S **SoM + carrier** sized for sustained game load |
| Edge I/O Rings | `device_designs/edge_io_rings/` + `gate1_digital_fabrication/edge_io_ring/` | Native EDA tracks ADR-FP-008 fusion BOM |
| Dock | `device_designs/dock/` + `gate1_digital_fabrication/dock/` | Discrete USB4/PD PCB package (beyond skeleton) |

## Cross-cutting
- Driver classification: `docs/full_product_family/DRIVER_CLASSIFICATION.md`
- Modem freeze: `docs/full_product_family/MODEM_ARCHITECTURE_FREEZE.md`
- Family status table: `docs/full_product_family/FAMILY_STATUS.md`
- KiCad status: `docs/full_product_family/KICAD_STATUS.md`
- COM/carrier amendment: `docs/adr/ADR-HW-001-com-carrier-strategy.md`

## Tokens claimed
- `HARDWARE_FAMILY_DEPTH_DIGITAL_PACKAGE`
- `STUDENT_COM_CARRIER_ARCHITECTURE_DOCUMENTED`
- `DS_XL_SECOND_DISPLAY_ICD_DOCUMENTED`
- `HANDHELD_SUSTAINED_GAME_LOAD_MODEL_DOCUMENTED`
- `RING_EDA_TRACKS_ADR_FP_008_FUSION_BOM`
- `DOCK_PCB_DIGITAL_PACKAGE_BEYOND_SKELETON`

## Tokens NOT claimed
- `GATE_2_PASS`, any `*_PHYSICAL_PROTOTYPE_COMPLETE`, fab/purchase, FCC/CE/USB-IF logos
- `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`, Gerber manufacture-ready
- Fake 6G modem certification / proprietary Ultra 7 BGA fanout designed in-house
