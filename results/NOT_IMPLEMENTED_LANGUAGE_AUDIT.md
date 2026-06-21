# Not Implemented Language Audit

Hardware repo scan — stale language replaced with implementation artifacts or evidence gates.

| File | Phrase/context | Category | Replacement action | New implementation/evidence link |
|---|---|---|---|---|
| firmware_os_interface/*.md | requirements defined only | replace_with_implemented_artifact | Updated footers | firmware/, secure_boot/ |
| hardware_os_validation/*.md | real hardware validation not started | convert_to_vendor_lab_issue | Link evidence backlog | implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md |
| firmware/qemu (CI) | unknown device without PyYAML | replace_with_implemented_artifact | Device util + JSON fallback | firmware/_device_util.py |
| os_compatibility_evidence/* | placeholder only | keep_as_claim_boundary_but_link_evidence_gate | Keep | EVIDENCE_INTAKE_PROCESS.md |

Implemented harnesses: `firmware/`, `secure_boot/`, `component_selection/`, validators in `scripts/validate_*`.

Physical validation tracked in `implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md`.
