# KiCad CLI — Wave A attempt

Updated: `2026-08-08T00:29:08Z`

**PHYSICAL_EXECUTION_FREEZE = ACTIVE**. No fab / purchase / flash.

## Token

`RING_KICAD_CLI_VALIDATION_PASS` — **NOT emitted** (CLI unavailable after install failure).

## Attempt

```text
brew install --cask kicad
```

- Cask fetched: **kicad 10.0.5**
- Failed moving Generic Artifact `demos` → `/Library/Application Support/kicad/demos`
- Exact error:
  `sudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helper`
  `sudo: a password is required`
- Homebrew purged the partial cask install afterward
- `kicad-cli` still absent (`command -v` / Applications search)

## Action required

```text
EDMUND_ACTION_REQUIRED: Approve the macOS administrator/install prompt for KiCad.
```

No `sudo chown` brew ownership repair was required for the formula fetch itself; the blocker is **OS admin password for `/Library/Application Support/kicad`**.

## Target board (when CLI available)

`gate1_digital_fabrication/edge_io_ring` (schematic + PCB EVT0) — ERC/DRC/Gerber/drill/position/BOM/netlist/STEP via `kicad-cli`.
