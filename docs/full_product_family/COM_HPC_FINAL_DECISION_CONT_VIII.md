# COM-HPC public-engineerability FINAL decision — Continuation VIII

Updated: 2026-08-09T19:46:44Z  
Branch: `continuation-viii/manufacturer-release-packages`  
Base: `c5b6afd6a792d367593867fc7533f413a5146db4`

## Decision
**Option B — `KEEP_ADLINK_AND_ACCEPT_NARROW_EXTERNAL_BLOCK`**

Mapped from Cont VIII A/B/C:
- **A** rejected (sunk-cost only)
- **C** preferred IF requirements still met — **not feasible** without breaking Ultra 7 155H + COM-HPC Mini ADR
- **B** selected with honest conditional/limited readiness

## Evidence summary
See `OPEN_DOCUMENTATION_ALTERNATIVE_AUDIT.md` + Cont VIII evaluation JSON.

## Readiness (Student / DS-XL)
- `manufacturer_ready` = **conditional**
- `adopter_ready` = **limited**
- `reproducible_ready` = **limited**

## Explicit
- Do not invent COM-HPC pin numbers
- Handheld / Ring / Dock not blocked by COM-HPC NDA
- Dock freeze remains USB4/TB4 (not TB5)
