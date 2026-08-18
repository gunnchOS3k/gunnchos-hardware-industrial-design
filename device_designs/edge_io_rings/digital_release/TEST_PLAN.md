# Test plan — Edge I/O Rings (digital)

**Role:** spatial input (IMU ≠ absolute pose)  
**Status:** `DIGITAL_RELEASE_READY`  
**Physical:** `PHYSICAL_PENDING` — this plan is digital review + future EVT execution, not a passing lab report.

## Digital checks (this repository)

- [x] Schematic + PCB present (`device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch`, `device_designs/edge_io_rings/kicad/edge_io_rings.kicad_pcb`)
- [x] This-run ERC/DRC recorded under `artifacts/supervisor_ready_eda/kicad/edge_io_rings/` (0 errors; warnings classified in `WARNING_DISPOSITION.csv`)
- [x] Assembly BOM copied to `digital_release/BOM.csv`
- [x] Firmware manifest `firmware/manifests/edge_io_rings_firmware_manifest.yaml`
- [ ] Manufacturer ICT/flying-probe vectors — `UNRES-SIGNED-FW-BIN` / CM reply
- [ ] Impedance coupon vs stackup — `UNRES-IMPEDANCE-SI`

## Factory / QC (existing, not executed)

Follow `device_designs/edge_io_rings/manufacturing/QC_CHECKLIST.md` and `device_designs/edge_io_rings/manufacturing/PROGRAMMING.md`. Do not tick physical boxes from this pass.

## Device-specific

- Spatial input: IMU (BMI270) + capacitive (IQS7222A) fusion per ADR-FP-008. **IMU ≠ absolute pose.**
- SWD Tag-Connect + OpenDFU digital path. Physical flash/boot is `PHYSICAL_PENDING`.

## Non-claims

Not EVT/DVT/PVT PASS. Not FCC/CE/USB-IF. Not RFQ sent.
