# Driver / firmware matrix — five-product family

Updated: 2026-08-08T19:40:00Z

Classes: `UPSTREAM` | `OPEN_VENDOR` | `BINARY_BLOB` | `NDA_ONLY` | `UNAVAILABLE`

## Student 14.5 / DS-XL — ADLINK COM-HPC-mMTL-155H-32G (Ultra 7 155H on-module)
| Subsystem | Exact MPN / module | Classification | Firmware notes |
|---|---|---|---|
| CPU/iGPU/NPU | Ultra 7 155H on COM-HPC-mMTL | `BINARY_BLOB` + `UPSTREAM` | i915/xe + `linux-firmware`; NPU intel_vpu + FW |
| ME/CSE/CSME | on-module | `BINARY_BLOB` | Required; no open replacement |
| COM board mgmt | ADLINK SEMA / AMI UEFI | `BINARY_BLOB` / `OPEN_VENDOR` tools | Vendor BIOS; dual-BIOS option |
| Wi-Fi/BT | Intel BE200 | `BINARY_BLOB` + `UPSTREAM` | iwlwifi + FW |
| WWAN | Quectel RM520N-GL | `OPEN_VENDOR` + `BINARY_BLOB` | MBIM/QMI userspace; modem FW blob |
| eSIM/eUICC | GSMA SGP.22 path | `OPEN_VENDOR` / `NDA_ONLY` profiles | No compliance claim |
| TPM | SLB9672XQ2.0 | `UPSTREAM` | tpm_tis_spi |
| USB4 | on-COM USB4 / dock **JHL8440** (+ **JHL9040R** retimer) | `UPSTREAM` + `BINARY_BLOB` FW | thunderbolt stack @ **40G**; not TB5 |
| Audio | ALC256/ALC245 class | `UPSTREAM` | SOF/HDA |
| EC | ITE5570 or NPCX9 class | `OPEN_VENDOR` / `UPSTREAM` | ChromeEC or vendor EC FW |
| Touch / webcam | panel OEM / MIPI | `BINARY_BLOB` / `OPEN_VENDOR` | HID; libcamera preferred |

## Handheld Hybrid — Radxa NX5 RM121-D8E32 (RK3588S)
| Subsystem | Exact MPN | Classification | Firmware notes |
|---|---|---|---|
| CPU/GPU/NPU | RK3588S on NX5 | `OPEN_VENDOR` + `BINARY_BLOB` | Radxa/vendor kernel; Mali blob; NPU vendor SDK |
| Board FW | Radxa NX5 images | `OPEN_VENDOR` | Debian/Ubuntu/Android per Radxa Docs |
| Wi-Fi/BT | AP6275P / AIC8800D class | `BINARY_BLOB` / `OPEN_VENDOR` | Module-dependent |
| WWAN optional | RM520N-GL | same as Student | Thermal may force Wi-Fi-first |
| GPU Vulkan | Mali-G610 | `BINARY_BLOB` | Panfrost tracked, not sole claim |
| Gamepad MCU | STM32F103C8T6 class | `UPSTREAM` | HID |
| SE | SE050C1HQ1 | `OPEN_VENDOR` | Plug & Trust |

## Edge I/O Rings
| Subsystem | Exact MPN | Classification | Firmware notes |
|---|---|---|---|
| BLE MCU | nRF52840-QIAA-R | `UPSTREAM` | Zephyr/NCS preferred |
| SoftDevice (if used) | Nordic | `BINARY_BLOB` | Prefer Zephyr controller |
| IMU | BMI270 | `UPSTREAM` | IIO |
| Cap | IQS7222A | `OPEN_VENDOR` | Azoteq host notes |
| UWB | DWM3001C | `OPEN_VENDOR` + `BINARY_BLOB` | Qorvo portions |
| BHI360 | BHI360 | `OPEN_VENDOR` | BSX/SH2 |
| SE | SE050C1HQ1 | `OPEN_VENDOR` | Plug & Trust |
| PMIC | npm1300-CAAA-R | `OPEN_VENDOR` / `UPSTREAM` | Nordic nPM |

## Dock
| Subsystem | Exact MPN | Classification | Firmware notes |
|---|---|---|---|
| USB4/TB4 controller | **JHL8440** | `BINARY_BLOB` + `UPSTREAM` host | Goshen Ridge dock/peripheral @ 40G |
| TB4 retimer | **JHL9040R** | `BINARY_BLOB` | Hayden Bridge SI — not the controller |
| TB5 (rejected) | JHL9480 / JHL9580 | `UNAVAILABLE` for this freeze | Out of ADR-HW-002 scope |
| PD | TPS65994 | `OPEN_VENDOR` | TI config tools |
| Ethernet | RTL8156 | `UPSTREAM` | r8152 |
| USB hub | VL817 | n/a silicon | Host xHCI |
| UWB companion | DWM3001C | same as ring | ADR-FP-008 escape |

## Unavailable / rejected
- Open Ultra 7 ME replacement: `UNAVAILABLE`
- Fully open Mali-free sole GPU path: `UNAVAILABLE` as sole strategy
- 6G / NTN modem driver stack on RM520N-GL: `UNAVAILABLE`
