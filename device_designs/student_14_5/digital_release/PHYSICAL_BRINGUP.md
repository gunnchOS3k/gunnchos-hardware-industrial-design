# Physical bring-up — Student 14.5

**Status:** `PHYSICAL_PENDING`  
**Owner-only.** This agent does not power boards, flash devices, or copy modeled YAML volts into a measured log.

Family packet: `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md`.

## Preconditions

1. Fabricated/assembled unit matching a tagged hardware SHA — **not done from this repo**.
2. ESD-safe, current-limited PSU.
3. Firmware image hash from `firmware/manifests/student_14_5_firmware_manifest.yaml` (harness YAML is not a board image).
4. Modeled rails in `device_designs/student_14_5/electrical/power_tree.yaml` are **expected class only**.

## Role reminder

Full-session learning/work at a desk. Not a gaming SKU.

## Do not

- Invent NDA pin probe points.
- Record YAML `volts` as measured.
- Claim FCC/CE/UN38.3 from this digital package.
