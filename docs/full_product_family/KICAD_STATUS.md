# KiCad status — Continuation V

Updated: 2026-08-08T20:15:00Z

## Environment probe
```
which kicad-cli → not found
which kicad → not found
ls /Applications/KiCad* → none
brew info --cask kicad → 10.0.5 (not installed)
```

## brew install attempt
```
brew install --cask kicad
```
**FAILED** — Homebrew prefixes not writable by user (`/opt/homebrew`, `~/Library/Logs/Homebrew`).  
Evidence: `docs/full_product_family/evidence/BREW_KICAD_INSTALL_ATTEMPT.log`

## EDMUND_ACTION_REQUIRED
```bash
sudo chown -R "$(whoami)" /opt/homebrew /Users/gunnchos/Library/Logs/Homebrew
brew install --cask kicad
export PATH="/Applications/KiCad/KiCad.app/Contents/MacOS:$PATH"
which kicad-cli
```
Then per product:
1. `kicad-cli sch erc`
2. `kicad-cli pcb drc`
3. Gerber / drill / pos / STEP per `device_designs/*/manufacturing/GERBER_EXPORT_PLAN.md`
4. Replace `Device:R` placeholders with vendor symbols/footprints

Work continued without stalling: mfg export plans + ERC/DRC blocker JSON checked in for all five.

## Tokens
- Claimed: `EDMUND_ACTION_REQUIRED_KICAD_BREW_ADMIN`
- Not claimed: `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`
