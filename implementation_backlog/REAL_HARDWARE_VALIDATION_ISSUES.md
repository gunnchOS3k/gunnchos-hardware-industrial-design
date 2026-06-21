# Real Hardware Validation Issues

Issue-ready tasks for non-simulatable validation. Evidence gates: `os_compatibility_evidence/`.

## Physical board boot log collection
- **Purpose:** Prove firmware handoff on silicon
- **Evidence:** `os_compatibility_evidence/OS_BOOT_LOG_PLACEHOLDER.md`
- **Acceptance:** Boot log committed, validator updated
- **Boundary:** Does not claim certification

## USB-C DP Alt Mode dock validation
- **Purpose:** Validate dock/external display contract on hardware
- **Evidence:** dock test log in os_compatibility_evidence/
- **Acceptance:** Hotplug events captured
- **Boundary:** Simulation pass does not substitute

## TPM/secure boot hardware validation
- **Purpose:** Validate production secure boot path
- **Evidence:** secure_boot/results/ + lab signoff
- **Acceptance:** Measured boot on real TPM
- **Boundary:** Test keys in repo are non-production

(See also: battery, thermal, HLK-style, Edge-IO, WAIKE, DVT/PVT items.)
