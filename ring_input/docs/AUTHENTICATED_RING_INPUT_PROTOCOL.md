# Authenticated Ring Input Protocol

**Gate 1 Workstream B** · firmware / pairing facing  
**Statuses:** `AUTHENTICATED_INPUT_PROTOCOL_PASS` · `RING_PHYSICAL_PROTOTYPE_PENDING`

> This document specifies a software-validated protocol for authenticated ring-class input.
> It does **not** assert that a physical ring prototype exists.

## Protocol properties (normative)

| Property | Mechanism |
|---|---|
| Device identity | `device_id` bound to long-term device public key / shared secret material |
| User identity | `user_id` bound during pairing; carried in session claims |
| Pairing ceremony | Explicit multi-step state machine: `DISCOVER → CHALLENGE → VERIFY → CONFIRM → PAIRED` |
| Ephemeral session | `session_id` + session key derived after pairing; expires by TTL |
| Challenge-response | Host issues `challenge_nonce`; device returns HMAC over challenge + identities |
| Monotonic nonce / seq | Per-session `seq` increments by exactly 1; receiver rejects gaps/replays |
| Anti-replay | Sliding replay cache of `(device_id, session_id, seq)` with TTL |
| Integrity | HMAC-SHA256 over canonical payload (`mac`) |
| Source / target binding | `source_device_id` and `target_device_id` in every signed event |
| Freshness | `ts_ms` within `max_skew_ms` of receiver clock |
| Confidence | `confidence ∈ [0,1]`; destructive actions require `≥ min_confidence` |
| Surface / calibration id | `surface_id` + `calibration_id` must match active calibration session |
| Event type | Typed enum (`pointer_move`, `click`, `key_press`, `scroll`, `destructive_confirm`, …) |
| Permission scope | Session `permission_scope` allow-list; event rejected if outside scope |
| Low-confidence rejection | Destructive / privileged events below threshold are rejected |
| Lost-device revocation | Revocation registry by `device_id` (and optional `session_id`); immediate reject |
| Key rotation path | `rotate_session_key()` issues new session key version; old version rejected after grace |
| Audit logging | Structured audit events; **no persistent raw motion** by default |
| Offline operation | Paired devices operate without network using cached pairing + session material |
| Safe fallback | On auth failure / lost link, OS falls back to keyboard/touch; never silent accept |

## Message flow (software reference)

1. Pairing ceremony establishes device↔user↔host binding and stores pairing record offline.
2. Host issues challenge; device responds; ephemeral session opens.
3. Device encodes input events from sensor pipeline (here: **simulated** stream).
4. Receiver verifies identity, MAC, target, seq, freshness, revocation, calibration, confidence, scope.
5. Accepted events are forwarded to OS input adapter; rejected events are audited without raw IMU.

## Evidence class

Fixtures under `fixtures/` are labeled `SOFTWARE_SIMULATED`. Physical bring-up is tracked separately as `RING_PHYSICAL_PROTOTYPE_PENDING`.
