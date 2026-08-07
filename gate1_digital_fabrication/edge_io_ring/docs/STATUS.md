# Edge I/O Ring Digital Fabrication Status

Updated: `2026-08-07T23:11:41Z`

```text
RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE
RING_PHYSICAL_PROTOTYPE_PENDING
RING_KICAD_STATIC_ERC_DRC_PASS
KICAD_CLI_ABSENT
```

## KiCad validation
- Static ERC: **PASS** (`gunnchos_static_erc`)
- Static DRC: **PASS** (`gunnchos_static_drc`)
- kicad-cli: **KICAD_CLI_ABSENT** version=`None`
- Host install of KiCad cask skipped (requires sudo). CI soft-skips with `KICAD_CLI_ABSENT`.

## Included
- Component selection with real MPNs + alternates + datasheet URLs
- Schematic source + netlist + static ERC report
- PCB source + Gerbers + drills + pick-place + stack-up + static DRC report
- Mechanical OpenSCAD + STL export + interference check
- Cross-link to compiling firmware in edge-io-measurement-node

## Not claimed
- Physical ring existence
- Measured RF/battery/thermal
- Production manufacturing
- KiCad GUI-equivalent open of generated sexp (best-effort when CLI present)
