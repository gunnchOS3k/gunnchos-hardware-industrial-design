# Placeholder / generic IC scan — Continuation VI

Updated: 2026-08-08T20:58:59Z

## Summary
```
{
  "ambiguous_or_MPN": 16,
  "Device:R structural placeholder": 143,
  "generic/undefined/fake": 4
}
```

Total hits: 163 (many are repeated Device:R structural placeholders).

## Actions taken (digitally resolvable)
- Handheld BOM: freeze preferred MPNs (remove `_or_` ambiguity in Values path)
- Dock: exact PD MPN; TB5 forbidden refs marked DNP
- Rings: KiCad Values → BOM preferred PMIC/LDO
- Handheld: PUBLIC_PINOUT net naming (no invented COM-HPC pins)

## Remaining (honest)
- `Device:R` remains until KiCad vendor libraries + CLI ERC/DRC
- Intel TB4 package pins + COM-HPC Mini pins remain NDA — **not faked**

See JSON companion for sample findings.
