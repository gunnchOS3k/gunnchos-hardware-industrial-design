# Test plan — Handheld Hybrid (digital)

**Role:** mobile/docked compute  
**Status:** `DIGITAL_RELEASE_READY`  
**Physical:** `PHYSICAL_PENDING` — this plan is digital review + future EVT execution, not a passing lab report.

## Digital checks (this repository)

- [x] Schematic + PCB present (`device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch`, `device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_pcb`)
- [x] This-run ERC/DRC recorded under `artifacts/supervisor_ready_eda/kicad/handheld_hybrid/` (0 errors; warnings classified in `WARNING_DISPOSITION.csv`)
- [x] Assembly BOM copied to `digital_release/BOM.csv`
- [x] Firmware manifest `firmware/manifests/handheld_hybrid_firmware_manifest.yaml`
- [ ] Manufacturer ICT/flying-probe vectors — `UNRES-SIGNED-FW-BIN` / CM reply
- [ ] Impedance coupon vs stackup — `UNRES-IMPEDANCE-SI`

## Factory / QC (existing, not executed)

Follow `device_designs/handheld_hybrid/manufacturing/QC_CHECKLIST.md` and `device_designs/handheld_hybrid/manufacturing/PROGRAMMING.md`. Do not tick physical boxes from this pass.

## Device-specific

- Mobile/docked compute: SoM USB/fastboot + HID MCU SWD. Docking is USB-C DP Alt Mode.
- Storage test must use 32 GiB eMMC A/B/recovery + microSD content, not an invented 512 GB NVMe.
- Gamepad HID is a latency workload on this compute device; it is not a generic gaming SKU.

## Non-claims

Not EVT/DVT/PVT PASS. Not FCC/CE/USB-IF. Not RFQ sent.
