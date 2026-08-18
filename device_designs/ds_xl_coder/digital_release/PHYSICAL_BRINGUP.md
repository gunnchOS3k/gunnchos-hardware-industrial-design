# Physical bring-up — DS-XL Coder

**Status:** `PHYSICAL_PENDING`  
**Owner-only.** This agent does not power boards, flash devices, or copy modeled YAML volts into a measured log.

Family packet: `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md`.

## Preconditions

1. Fabricated/assembled unit matching a tagged hardware SHA — **not done from this repo**.
2. ESD-safe, current-limited PSU.
3. Firmware image hash from `firmware/manifests/ds_xl_coder_firmware_manifest.yaml` (harness YAML is not a board image).
4. Modeled rails in `device_designs/ds_xl_coder/electrical/power_tree.yaml` are **expected class only**.

## Role reminder

Local creation and deployment workstation (learn-to-build). Dual independent useful displays; pin-accurate eDP2 is NDA.

## Do not

- Invent NDA pin probe points.
- Record YAML `volts` as measured.
- Claim FCC/CE/UN38.3 from this digital package.
