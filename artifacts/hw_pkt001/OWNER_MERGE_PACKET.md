# OWNER_MERGE_PACKET — STREAM-C-PKT-001

## Branch
`stream/hw-digital-exhaust-pkt001`

## Ask
Owner merge when ready. **Cursor does not merge.** Do not claim SHIPPING_IMAGE / PRODUCTION_RELEASE / HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE.

## What closed (digital only)
- `NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001` → CLOSED on device-os tip `a1e11efcb502ce053d755a2539c26d252e216226` (production-intent fit, margins > 0, non-stub)
- KiCad ERC/DRC: 0 errors on five products
- BOM / firmware manifest / power budget validators: PASS

## Still OPEN
- EXTERNAL_NDA pin maps (COM-HPC, dual eDP, JHL*)
- PHYSICAL freeze (fab/flash/ICT/ring boot)
- On-target Student/DS-XL/Dock firmware
- lib_footprint_mismatch warnings

## Evidence
- `artifacts/hw_pkt001/PACKET_SUMMARY.json`
- `artifacts/hw_pkt001/VP_IMAGE_FIT_REMEASURE.json`
- `artifacts/hw_pkt001/kicad_cli/CLI_RESULTS.json`
- `artifacts/continuation_ix_pre_evt/BLOCKERS_CONT_IX.json` (`stream_c_pkt001` note)

## PR
If GitHub API is unavailable, merge from this packet locally. Do not invent NDA/physical PASS.
