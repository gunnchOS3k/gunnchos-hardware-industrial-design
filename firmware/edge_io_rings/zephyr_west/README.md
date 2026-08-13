# Ring Zephyr west workspace (HW-002)

nRF52840 / Zephyr remains the intended Ring MCU firmware path.

## Hard gate

```bash
./scripts/require_west_build.sh
```

- Requires `ZEPHYR_BASE`, Zephyr SDK, and `west`.
- **Soft-skip is forbidden** (non-zero exit if toolchain missing or build fails).
- Evidence lands in `artifacts/hw002/zephyr_west/`.

## Scope

- This workspace proves a real `west build` for `nrf52840dk/nrf52840`.
- Full sensor-fusion drivers remain in `edge-io-measurement-node` (`gate1_digital_fabrication/ring_firmware/`).
- Physical flash/boot is **not** claimed (`RING_PHYSICAL_BOOT_PENDING`).
