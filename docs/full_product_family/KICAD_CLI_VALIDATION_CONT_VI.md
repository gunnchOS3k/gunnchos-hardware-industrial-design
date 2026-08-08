# Cont VI — KiCad CLI validation

```text
KICAD_INSTALLATION_PASS = TRUE
KICAD_CLI_DISCOVERY_PASS = TRUE
KICAD_CLI_VERSION = 10.0.5
KICAD_CLI = /opt/homebrew/bin/kicad-cli (Homebrew cask link)
RING_KICAD_CLI_VALIDATION_PASS = TRUE
```

Evidence: `artifacts/continuation_vi_kicad_validation/VALIDATION_SUMMARY.json`

Per board (ERC + DRC + Gerber + drill + PnP + STEP):
- student_14_5 — DRC load fixed (removed KiCad10-unknown setup key)
- ds_xl_coder — same
- handheld_hybrid — validated
- edge_io_rings — validated (`RING_KICAD_CLI_VALIDATION_PASS`)
- dock — DRC load fixed (odd 5-layer copper → 4-layer; In3 removed)

Honest release posture remains per-product (COM-HPC NDA may still block Student/DS-XL full design release).
