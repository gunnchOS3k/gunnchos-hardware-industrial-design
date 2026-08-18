# Physical bring-up — Edge I/O Rings

**Status:** `PHYSICAL_PENDING`  
**Owner-only.** This agent does not power boards, flash devices, or copy modeled YAML volts into a measured log.

Family packet: `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md`.

## Preconditions

1. Fabricated/assembled unit matching a tagged hardware SHA — **not done from this repo**.
2. ESD-safe, current-limited PSU.
3. Firmware image hash from `firmware/manifests/edge_io_rings_firmware_manifest.yaml` (harness YAML is not a board image).
4. Modeled rails in `device_designs/edge_io_rings/electrical/power_tree.yaml` are **expected class only**.

## Role reminder

Body-area spatial input. BMI270 IMU is inertial; ADR-FP-008 requires ≥2 modalities before action. IMU-only absolute position is rejected.

## Do not

- Invent NDA pin probe points.
- Record YAML `volts` as measured.
- Claim FCC/CE/UN38.3 from this digital package.

## Rings
IMU samples are body-rate / orientation change. Do not log them as world-frame pose.
