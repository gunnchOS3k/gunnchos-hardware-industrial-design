# Test plan — DS-XL Coder (digital)

**Role:** local create/deploy  
**Status:** `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA`  
**Physical:** `PHYSICAL_PENDING` — this plan is digital review + future EVT execution, not a passing lab report.

## Digital checks (this repository)

- [x] Schematic + PCB present (`device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_sch`, `device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_pcb`)
- [x] This-run ERC/DRC recorded under `artifacts/supervisor_ready_eda/kicad/ds_xl_coder/` (0 errors; warnings classified in `WARNING_DISPOSITION.csv`)
- [x] Assembly BOM copied to `digital_release/BOM.csv`
- [x] Firmware manifest `firmware/manifests/ds_xl_coder_firmware_manifest.yaml`
- [ ] Manufacturer ICT/flying-probe vectors — `UNRES-SIGNED-FW-BIN` / CM reply
- [ ] Impedance coupon vs stackup — `UNRES-IMPEDANCE-SI`

## Factory / QC (existing, not executed)

Follow `device_designs/ds_xl_coder/manufacturing/QC_CHECKLIST.md` and `device_designs/ds_xl_coder/manufacturing/PROGRAMMING.md`. Do not tick physical boxes from this pass.

## Device-specific

- Local create/deploy: two independent useful displays required for the product role. Dual-eDP pin-accurate test blocked on EXT-DSXL-DUAL-EDP.
- Fallback: single-display degraded mode is documented in DISPLAY_TOPOLOGY.json; it is not the pass criterion for the differentiator.

## Non-claims

Not EVT/DVT/PVT PASS. Not FCC/CE/USB-IF. Not RFQ sent.
