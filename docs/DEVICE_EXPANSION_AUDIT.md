# Device Expansion Audit

**Pass target:** EVT-1 hardware architecture package — not manufacturing release.

## Current state

This repo is currently **EVT-0 concept scaffold** with OpenSCAD assets, draft BOM docs, and compliance trackers. This pass moves toward **EVT-1 hardware package**, not final manufacturing readiness.

## CAD / OpenSCAD

| Item | Status |
|------|--------|
| `cad/openscad/student_14_5/` | present |
| Handheld / DS-XL / wearables CAD | partial / planned |

## Device specs

| Item | Status |
|------|--------|
| `docs/DEVICE_REQUIREMENTS.md` | draft |
| `product/PRD_*.md` | **added this pass** |

## BOM

| Item | Status |
|------|--------|
| Legacy BOM paths | partial |
| `bom/*.csv` per product line | **added** |

## Compliance

| Item | Status |
|------|--------|
| `docs/07_compliance/` | partial |
| `compliance/REGULATORY_MATRIX.md` | **added** |

## Gaps addressed this pass (PRD full expansion)

| Gap | EVT-1 action |
|-----|----------------|
| Full PRD §1–12 | `product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md` |
| Personas / performance / MVP / claim boundary | `product/*.md` |
| Hardware acceptance criteria §6.3 | `docs/HARDWARE_ACCEPTANCE_CRITERIA.md` |
| Approved vendor list | `bom/APPROVED_VENDOR_LIST.md` |
| COPPA/CIPA in compliance matrix | `compliance/REGULATORY_MATRIX.md` |
| Device comparison matrix | `architecture/DEVICE_COMPARISON_MATRIX.md` |

## Not claimed

- certified hardware
- finished OS
- mass-production readiness
- regulatory approval
- finished Steam/media licensing
