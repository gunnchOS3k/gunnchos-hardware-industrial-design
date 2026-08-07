# KiCad validation report

Updated: 2026-08-07T23:09:47.984727Z

## Tooling

- kicad-cli path expected: `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`
- kicad-cli present: **False**
- Homebrew cask install blocked on sudo password in this environment

## Results

- Static ERC/DRC validator: **PASS** (`static_erc_drc_validator.py`)
- CLI ERC/DRC/Gerber: **KICAD_CLI_ABSENT** (soft-skip; CI fails only on static regressions when CLI absent)

## Status

```text
RING_DIGITAL_FABRICATION_PACKAGE_COMPLETE
KICAD_STATIC_ERC_DRC_PASS
KICAD_CLI_REVALIDATION_PENDING_HOST_INSTALL
RING_PHYSICAL_PROTOTYPE_PENDING
```
