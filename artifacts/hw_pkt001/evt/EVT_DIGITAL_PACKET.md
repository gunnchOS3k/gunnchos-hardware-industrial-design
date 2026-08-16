# EVT Digital Packet — STREAM-C-PKT-001

Honesty boundary: digitally executable work only. No physical fab/flash/assemble. No invented NDA pin maps. `SHIPPING_IMAGE=false`. `PRODUCTION_RELEASE_CLAIMED=false`. `HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE=false`.

## Digitally executable (this packet)

| Item | Status | Evidence |
|---|---|---|
| KiCad ERC (0 errors) on handheld_hybrid, edge_io_rings, dock, student_14_5, ds_xl_coder | RAN | `artifacts/hw_pkt001/kicad_cli/*/erc.json` |
| KiCad DRC (0 errors) same products | RAN | `artifacts/hw_pkt001/kicad_cli/*/drc.json` |
| BOM / firmware manifest / power budget validators | PASS | `artifacts/hw_pkt001/DIGITAL_VALIDATORS.json` |
| Handheld image-fit remeasure vs device-os `a1e11ef…` | PASS_PRODUCTION_INTENT_DIGITAL_FIT (digital CLOSE) | `artifacts/hw_pkt001/VP_IMAGE_FIT_REMEASURE.json` |
| Test-points CSV present or honest PLACEHOLDER | PRESENT | `manufacturing/*/test_points.csv` |
| Public firmware package descriptors / harness notes | DEEPENED | `manufacturing/*/firmware/PACKAGE_INDEX.md` |
| Ring Zephyr west digital build (prior HW-002) | EARNED (digital only) | `artifacts/hw002/zephyr_west/` |

## PHYSICAL_PENDING

- Fab / purchase / assemble / flash (PHYSICAL_EXECUTION_FREEZE ACTIVE)
- ICT fixture bring-up and real test-point probing
- Ring physical boot / multimodal tracking
- On-target Student / DS-XL / Dock firmware bring-up
- Manufacturer DFM sign-off beyond digital DFM_PRECHECK
- Physical eMMC flash proof of image-fit (digital margins ≠ silicon flash)

## EXTERNAL_NDA

- COM-HPC Mini 400-pin net-accurate map (PICMG/ADLINK) — Student / DS-XL
- Dual eDP COM-HPC pin map — DS-XL
- Intel JHL8440 / JHL9040R package ball maps — Dock
- Display panel exact MPNs + hinge bend OEM spec — DS-XL AVL
- Paste/reflow profile vendor values; some fastener torque OEM values

## Tokens (honest)

- Do **not** set `HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE=true` while NDA/on-target gaps remain
- Do **not** claim `SoA` / `STANDARDIZED_6G` / `COMPLIANT` / `PHYSICAL` PASS
- Conditional manufacturer tokens remain conditional on vendor collateral where noted in Cont IX blockers
