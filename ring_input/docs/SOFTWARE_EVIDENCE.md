# Software Evidence — Authenticated Ring Input

**evidence_class:** `SOFTWARE_SIMULATED`  
**physical_ring_claimed:** `false`  
**statuses:** `AUTHENTICATED_INPUT_PROTOCOL_PASS` · `RING_PHYSICAL_PROTOTYPE_PENDING`

## Source

Simulated sensor stream: `fixtures/simulated_sensor_stream.jsonl` and
`SimulatedSensorStream.generate()`.

This is **not** physical IMU capture from a ring prototype.

## Test results (local, uncommitted)

| Suite | Result |
|---|---|
| `gunnchos-hardware-industrial-design/ring_input/tests` | 17 passed |
| `edge-io-measurement-node/tests/test_ring_input_harness.py` | 3 passed |
| `gunnchos-device-os/tests/test_ring_input_adapter.py` | 7 passed |

Cases covered: valid accept; bad signature; unknown device; wrong target; replay;
stale; revoked; low-confidence destructive rejected; calibration mismatch;
offline paired; fallback available; key rotation; challenge-response failure.
