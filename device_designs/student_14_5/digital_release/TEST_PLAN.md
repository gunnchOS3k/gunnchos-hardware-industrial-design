# Test plan — Student 14.5 (digital)

**Role:** sustained desk/work  
**Status:** `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA`  
**Physical:** `PHYSICAL_PENDING` — this plan is digital review + future EVT execution, not a passing lab report.

## Digital checks (this repository)

- [x] Schematic + PCB present (`device_designs/student_14_5/kicad/student_14_5.kicad_sch`, `device_designs/student_14_5/kicad/student_14_5.kicad_pcb`)
- [x] This-run ERC/DRC recorded under `artifacts/supervisor_ready_eda/kicad/student_14_5/` (0 errors; warnings classified in `WARNING_DISPOSITION.csv`)
- [x] Assembly BOM copied to `digital_release/BOM.csv`
- [x] Firmware manifest `firmware/manifests/student_14_5_firmware_manifest.yaml`
- [ ] Manufacturer ICT/flying-probe vectors — `UNRES-SIGNED-FW-BIN` / CM reply
- [ ] Impedance coupon vs stackup — `UNRES-IMPEDANCE-SI`

## Factory / QC (existing, not executed)

Follow `device_designs/student_14_5/manufacturing/QC_CHECKLIST.md` and `device_designs/student_14_5/manufacturing/PROGRAMMING.md`. Do not tick physical boxes from this pass.

## Device-specific

- Desk/work session path: internal eDP + keyboard/touch. COM-HPC pin-accurate USB/eDP tests blocked on EXT-COM-HPC-400PIN.
- Cellular: RM520N-GL Rel-16 only — not 6G, not NTN.

## Non-claims

Not EVT/DVT/PVT PASS. Not FCC/CE/USB-IF. Not RFQ sent.
