# Authenticated Ring Input Protocol (Gate 1 Workstream B)

Firmware-facing authenticated input protocol for a **future** I/O ring form factor.

**Statuses:** `AUTHENTICATED_INPUT_PROTOCOL_PASS` · `RING_PHYSICAL_PROTOTYPE_PENDING`

No physical ring is claimed. All runtime evidence here is from **simulated sensor streams / fixtures**.

## Layout

| Path | Role |
|---|---|
| `docs/AUTHENTICATED_RING_INPUT_PROTOCOL.md` | Normative protocol properties |
| `schemas/` | JSON schemas (event, pairing, session, calibration) |
| `python/authenticated_ring_input/` | Reference encoder/decoder, sender/receiver, replay cache, pairing SM, revocation, audit, latency |
| `fixtures/` | Positive test vectors, negative fixtures, simulated stream |
| `tests/` | Protocol unit/integration tests |

## Quick test

```bash
cd ring_input
PYTHONPATH=python pytest -q tests
```

## Cross-repo

- Measurement harness: `edge-io-measurement-node` → `src/edge_io_node/ring_input_harness`
- OS adapter: `gunnchos-device-os` → `ring_input/`
