# KiCad CLI validation report

Updated: 2026-08-07T23:37:53Z

**PHYSICAL_EXECUTION_FREEZE = ACTIVE** (conceptual until field-kit release). No physical claims.

## Target

- Token: `RING_KICAD_CLI_VALIDATION_PASS`
- Achieved: **False**

## Discovery (macOS host)

| Check | Result |
| --- | --- |
| `command -v kicad-cli` | absent |
| `find /Applications -path '*KiCad*.app/Contents/MacOS/kicad-cli'` | none |
| `mdfind 'kMDItemFSName == "kicad-cli"'` | empty |
| `brew list --cask \| grep -i kicad` | none |
| `brew info --cask kicad` | available, not installed (10.0.5) |

## Install attempt

```text
brew install --cask kicad
```

- Fetched cask **kicad 10.0.5**
- Failed while moving Generic Artifact `demos` → `/Library/Application Support/kicad/demos`
- Exact failure: `sudo: a terminal is required to read the password`
- Cask files purged by Homebrew after failure

### Blocker

```text
HUMAN_OS_AUTHORIZATION_REQUIRED
```

**Edmund instruction:** Approve the macOS administrator/install prompt.

After approval, re-run:

```bash
brew install --cask kicad
gate1_digital_fabrication/edge_io_ring/scripts/run_kicad_cli_validation.sh
```

## CLI validation (ERC / DRC / Gerber / drill / BOM / STEP / parity)

**Not run** — `kicad-cli` remains unavailable.

Committed static package still present under `gate1_digital_fabrication/edge_io_ring/` (schematic, PCB, Gerbers, drill, BOM). Static ERC/DRC remains the mandatory gate when CLI is absent.

## Status tokens

```text
RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE
KICAD_STATIC_ERC_DRC_PASS
HUMAN_OS_AUTHORIZATION_REQUIRED
KICAD_CLI_REVALIDATION_PENDING_HOST_INSTALL
RING_KICAD_CLI_VALIDATION_PASS   # NOT SET — blocked
RING_PHYSICAL_PROTOTYPE_PENDING
```
