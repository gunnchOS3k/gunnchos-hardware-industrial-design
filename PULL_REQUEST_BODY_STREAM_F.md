# Stream F — Mechanical / EVT-DVT-PVT / Certification / Manufacturing Prep

**Generated:** 2026-09-18T18:35:47Z

## Summary
- Section 15: per-SKU mechanical digital packages (enclosure, tolerances, connectors, service, thermal/vents, antenna keepouts, exploded, DFM/DFA, drawings)
- Section 16: executable EVT/DVT/PVT test packs + schemas; physical tokens remain false
- Section 17: SKU×market certification prep matrix (no certification claims)
- Section 18: CM RFQ templates, AVL, fab notes, AOI/X-ray, PFMEA, control plan, MES schemas (`RFQ_SENT=false`)

## Gates
| Gate | Status |
|---|---|
| `MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED` | TRUE |
| `PHYSICAL_VALIDATION_ENGINEERING_PREP_EXHAUSTED` | TRUE |
| `CERTIFICATION_ENGINEERING_PREP_EXHAUSTED` | TRUE |
| `MANUFACTURING_ENGINEERING_PREP_EXHAUSTED` | TRUE |

## Coordination
Does not modify Stream E KiCad/electrical paths. See `artifacts/digital_engineering_exhaustion/stream_f/STREAM_E_COORDINATION.md`.

## Test plan
- [ ] `make validate-stream-f`
- [ ] Confirm `RFQ_SENT=false`, no ergonomic/cert/physical PASS claims
- [ ] Owner-only actions listed in `artifacts/digital_engineering_exhaustion/stream_f/OWNER_ONLY_ACTIONS.md`
