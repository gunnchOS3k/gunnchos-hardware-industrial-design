# ERC status

**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`

## Recorded run (NXP-0)

- Tool: `kicad-cli` 10.0.5
- Command: `kicad-cli sch erc` on `cpb0_open.kicad_sch`
- Tool output: `Found 0 violations` on **placeholder-only** hierarchy (text notes, no SoC symbol/nets)

## Gate interpretation

`CPB0_OPEN_SCHEMATIC_ERC_PASS=false`

Zero violations on empty/placeholder sheets is **not** an ERC pass for a CPB0-O design. Pass requires a symbol-complete netlist for required sheets with zero errors after real connectivity is drawn.
