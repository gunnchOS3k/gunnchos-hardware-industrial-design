# student_14_5 — firmware package index (STREAM-C-PKT-001)

| Item | Status | Honesty |
|---|---|---|
| Source | EXTERNAL_REPO | `gunnchos-device-os` primary |
| Binary in this repo | NOT_PRESENT | freeze |
| ACPI / DT public descriptors | DIGITAL | `firmware/descriptors/` |
| COM-HPC Mini 400-pin net-accurate map | EXTERNAL_NDA | **Not invented** — BLOCKED_NDA |
| On-target Student firmware | PHYSICAL_PENDING + BINARY_BLOB | Not claimed |
| Factory test mode | DIGITAL_STUB | `manufacturing/student_14_5/` |
| Image-fit coupling | N/A (handheld Outcome A is separate SKU) | — |

### Public harness notes (non-NDA)

- Boot / power-state / thermal contracts: `firmware/interfaces/*_contract.yaml`.
- Do not claim pin-accurate COM-HPC fanout in public package.
- Digital package complete token stays **false** until NDA map + on-target path close.
