# KiCad status — Continuation VI

Updated: 2026-08-08T21:01:04Z

## Environment probe (Cont VI mid-run)
```
/opt/homebrew/bin/kicad-cli → PRESENT (10.0.5)
```
Earlier Cont V brew install was blocked; Cont VI resume found CLI available and executed family validation.

## Family CLI run
```bash
bash scripts/run_family_kicad_cli.sh
# → KICAD_CLI_FAMILY_BEST_EFFORT
```
Evidence: `docs/full_product_family/evidence/kicad_cli/family_kicad_cli_meta.json`

| Product | ERC JSON | DRC JSON | Gerbers | STEP |
|---|---|---|---|---|
| handheld_hybrid | yes (violations expected) | yes | 11 | yes |
| dock | yes (violations expected) | no / failed | 0 | no |
| edge_io_rings | yes | yes | 11 | yes |
| student_14_5 | yes | yes | 17 | yes |
| ds_xl_coder | yes | yes | 17 | yes |

## Honesty
- ERC reports contain violations — structural `Device:R` placeholders lack pin geometry.
- **Not claimed:** `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`, `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE`.
- Student/DS-XL remain `*_BLOCKED_NDA` for pin-accurate COM-HPC nets regardless of CLI.

## Tokens
- Claimed: `KICAD_CLI_RESUME_SCRIPTS_READY`, `KICAD_CLI_FAMILY_BEST_EFFORT_RAN`
- Retained: `EDMUND_ACTION_REQUIRED_KICAD_BREW_ADMIN` historical note (install now present)
- Not claimed: `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`
