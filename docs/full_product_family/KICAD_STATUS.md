# KiCad status — Continuation VI

Updated: 2026-08-08T20:58:59Z

## Environment probe
```
which kicad-cli → not found (Cont VI authoring)
which kicad → not found
ls /Applications/KiCad* → none
```

## brew install (inherited Cont V)
`brew install --cask kicad` previously FAILED — Homebrew prefixes not writable.  
Evidence: `docs/full_product_family/evidence/BREW_KICAD_INSTALL_ATTEMPT.log`  
`EDMUND_ACTION_REQUIRED` remains until admin install completes.

## Resume path (Cont VI)
```bash
sudo chown -R "$(whoami)" /opt/homebrew /Users/gunnchos/Library/Logs/Homebrew
brew install --cask kicad
export PATH="/Applications/KiCad/KiCad.app/Contents/MacOS:$PATH"
make kicad-validate-family
# or:
bash scripts/run_family_kicad_cli.sh
```

Per native board under `device_designs/*/kicad/`:
1. `kicad-cli sch erc`
2. `kicad-cli pcb drc`
3. Gerber / drill / pos / STEP → `docs/full_product_family/evidence/kicad_cli/<product>/`
4. Replace `Device:R` placeholders with vendor symbols/footprints

Soft-skip when CLI absent (exit 0, `KICAD_CLI_ABSENT` meta). Static Cont VI validator remains mandatory.

## Tokens
- Claimed: `KICAD_CLI_RESUME_SCRIPTS_READY`, `EDMUND_ACTION_REQUIRED_KICAD_BREW_ADMIN`
- Not claimed: `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`
