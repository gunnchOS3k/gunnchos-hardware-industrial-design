# EDMUND_ACTION_REQUIRED — KiCad Homebrew install

Updated: 2026-08-08T20:15:00Z  
Repo: gunnchos-hardware-industrial-design  
Branch: `cursor/full-product-continuation-v-hardware-release`

## Why
`brew install --cask kicad` failed: `/opt/homebrew` and `~/Library/Logs/Homebrew` are not writable by the current user. Without admin ownership fix, `kicad-cli` cannot run ERC/DRC/Gerber/PnP/STEP.

## Required Edmund actions
```bash
sudo chown -R "$(whoami)" /opt/homebrew /Users/gunnchos/Library/Logs/Homebrew
brew install --cask kicad
export PATH="/Applications/KiCad/KiCad.app/Contents/MacOS:$PATH"
which kicad-cli
```

Then run per-product commands in `docs/full_product_family/KICAD_STATUS.md` and each `device_designs/*/manufacturing/GERBER_EXPORT_PLAN.md`.

## Evidence
`docs/full_product_family/evidence/BREW_KICAD_INSTALL_ATTEMPT.log`

Work did **not** stall: manufacturing export plans + blocker JSON checked in for all five products.
