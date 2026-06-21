# Hardware Compatibility Evidence Matrix (Hardware Repo)

| Gate | Required evidence | Current evidence | Status | Blocking? |
|------|-------------------|------------------|--------|-----------|
| OS profile export manifest | device_class_exports/*.yaml | Created this pass | documented | Yes |
| OS repo consumed profiles | hardware_compat/device_profiles/*.yaml | OS PR #27 merged | documented | Yes |
| Simulated OS compatibility | OS compatibility engine demos | OS-side simulated | simulated | Yes |
| Hardware-side validation plan | hardware_os_validation/ | Created this pass | documented | Yes |
| Real hardware boot | Boot logs in os_compatibility_evidence/ | Placeholder only | needs_real_hardware | Yes |
| Firmware/OS interface | firmware/ harness + firmware_os_interface/ | Harness implemented in CI | documented | Yes |
| HLK-style readiness | hlk_readiness/ | Plan only | documented | No |
| Real hardware compatibility | Lab signoff | Not started | blocked | Yes |

Production hardware-compatible release: **not claimed**.
