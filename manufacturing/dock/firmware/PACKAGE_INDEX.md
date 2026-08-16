# dock — firmware package index (STREAM-C-PKT-001)

Firmware binaries live in sibling repos (`gunnchos-device-os`, dock controller / Thunderbolt collateral where licensed).
This hardware repo holds **public** harness descriptors only.

| Item | Status | Honesty |
|---|---|---|
| Source | EXTERNAL_REPO | Device-OS + vendor blobs |
| Binary in this repo | NOT_PRESENT | PHYSICAL_EXECUTION_FREEZE |
| Public USB-C / PD harness descriptor | DIGITAL | Documented under `firmware/interfaces/` docking contracts |
| JHL8440 / JHL9040R pin-accurate map | EXTERNAL_NDA | **Not invented** — BLOCKED_NDA |
| On-target flash / bring-up | PHYSICAL_PENDING | Not claimed |
| Factory test mode | DIGITAL_STUB | `manufacturing/dock/factory_test/` |
| Update / programming | Documented | `firmware_os_interface` / capsule stubs |

### Public harness notes (non-NDA)

- Enumerate USB4/TB host port power-role expectations via `firmware/interfaces/docking_external_display_contract.yaml` (contract-level, not ball map).
- Keep SI / retimer programming as BINARY_BLOB + NDA until vendor package lands.
- `HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE` remains **false** for dock while NDA ball maps + on-target path remain open.
