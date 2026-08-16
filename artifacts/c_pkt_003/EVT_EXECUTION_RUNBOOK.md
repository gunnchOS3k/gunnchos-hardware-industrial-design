# EVT Execution Runbook — C-PKT-003 (digital)

## Scope
Digitally executable EVT prep only. **No physical fab/flash/ICT.** Cursor never merges.

## Preconditions
1. Tip at hardware base `0e11dea8…` (or this branch).
2. Read `artifacts/c_pkt_003/FIRMWARE_GAP_MATRIX.json`.
3. Confirm NDA walls for Student / DS-XL / Dock — do not invent pin maps.

## Digital sequence (per device)
1. Open `artifacts/c_pkt_003/evt/<product>/EVT_DIGITAL_PACKET.md`.
2. Validate firmware manifest: `python scripts/validate_firmware_manifests.py` (if available in CI).
3. Run factory mock: `python artifacts/c_pkt_003/factory_hil/run_hil_mock.py --product <product>`.
4. Record results under `artifacts/c_pkt_003/factory_hil/results/`.
5. Update readiness only with evidence; never set `EVT_PHYSICAL_PASS`.

## Physical handoff (owner / lab — not this packet)
- Purchase / fab / assemble / flash
- ICT fixture bring-up against `manufacturing/*/factory_test/`
- On-target EVT0 measurements per `npi/evt0_measurement_readiness/`

## Tokens
- `EVT_DIGITAL_EXECUTION_INFRA_READY` may be true when packets + mocks + runbook exist.
- `*_FIRMWARE_DIGITAL_BUILD_PASS` only for real builds (Ring prior Zephyr west).
- `FACTORY_PHYSICAL_PASS` / `EVT_PHYSICAL_PASS` remain **false**.
