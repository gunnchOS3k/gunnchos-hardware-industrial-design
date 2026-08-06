# Authenticated Ring Input — Claim Boundary

## Status

| Status key | Value |
|---|---|
| `AUTHENTICATED_INPUT_PROTOCOL_PASS` | Software protocol vertical slice validated via fixtures / simulated sensor stream |
| `RING_PHYSICAL_PROTOTYPE_PENDING` | No physical ring hardware is claimed or present |

## What this package IS

- Firmware-facing **protocol specification**, JSON schemas, and a **reference Python encoder/decoder**
- Pairing ceremony state machine, ephemeral session, challenge-response, anti-replay, revocation, and calibration-session contracts
- **Software evidence** from labeled simulated sensor fixtures (not field measurements)

## What this package is NOT

- Not a physical ring prototype, BOM, or EVT board
- Not proof that a ring exists, ships, or has been manufactured
- Not a claim of secure-element / TPM hardware attestation on a real device
- Not persistent storage of raw motion/IMU samples by default (audit logs omit raw motion)

## Evidence labels

All fixture streams under `fixtures/` are tagged `evidence_class: SOFTWARE_SIMULATED`.
Do not promote these results to physical PASS without a separate hardware bring-up package.
