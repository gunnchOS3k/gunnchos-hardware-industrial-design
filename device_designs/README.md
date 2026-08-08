# Device designs — hardware industrial design (family depth)

Updated: 2026-08-08T01:15:00Z  
Branch package: `docs/full_product_family/`

This repo owns **EDA / COM-carrier / PCB digital packages** for all five products.
Field-kit may hold umbrella product docs; prefer this repo for electrical sources.

| Product | Path | Integration |
|---|---|---|
| Student 14.5 | `student_14_5/` | COM + carrier (ADR-HW-001) |
| DS-XL Coder | `ds_xl_coder/` | Shared COM + dual eDP ICD |
| Handheld Hybrid | `handheld_hybrid/` | RK3588S SoM + game carrier |
| Edge I/O Rings | `edge_io_rings/` + gate1 | ADR-FP-008 fusion in EDA |
| Dock | `dock/` + gate1 | PCB package beyond skeleton |

Status: DIGITAL / MODELED. Never claim `GATE_2_PASS` or physical completion from these artifacts.
PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only
