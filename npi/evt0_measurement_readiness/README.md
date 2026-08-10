# WP-010 — EVT0 Fixture / Instrument / Evidence Readiness

**Role:** Implementer package (not VP-010 verifier).  
**Claim boundary:** DIGITAL readiness only. `PHYSICALLY_VALIDATED=false`.  
**Freeze:** `PHYSICAL_EXECUTION_FREEZE` — do not purchase, fab, or run physical EVT.

## Exit artifacts

| Artifact | Path |
|----------|------|
| Master test matrix | `EVT0_MASTER_TEST_MATRIX.json` |
| Instrument matrix | `EVT0_INSTRUMENT_MATRIX.json` |
| Fixture register | `EVT0_FIXTURE_REGISTER.json` |
| Bring-up sequence | `EVT0_BRINGUP_SEQUENCE.md` |
| Evidence schema | `EVT0_EVIDENCE_SCHEMA.json` |
| Safety plan | `EVT0_SAFETY_PLAN.md` |
| Device Lab bridge schema | `DEVICE_LAB_CALIBRATION_BRIDGE_SCHEMA.json` |
| Acquisition action list | `EVT0_ACQUISITION_ACTION_LIST.json` |
| E5 Golden Journey map | `EVT0_E5_GOLDEN_JOURNEY_MEASUREMENT_MAP.json` |
| Risk↔test traceability | `EVT0_RISK_TEST_TRACEABILITY.json` |
| Readiness token (implementer) | `READY_FOR_EVT0_MEASUREMENT_EXECUTION.json` |
| Independent VP-010 result | `independent_verifier/VP-010-RESULT.json` |

## Hardware baseline

Accepted Cont IX silk/rev: `0.6.0-cont-ix` (five-product family).

## Honesty

- No pre-populated physical PASS.
- VF4/VF5/VF6 remain PHYSICAL_PENDING (Device Lab).
- Expensive RF/SI gear classified RENT / EXTERNAL_LAB / VENDOR_DFM — not assumed purchased.
- Independent verifier owns V1 / `independent_verifier/VP-010-RESULT.json` (implementer must not self-certify V1).

## Validate

```bash
pytest -q tests/test_wp010_evt0_readiness.py
```
