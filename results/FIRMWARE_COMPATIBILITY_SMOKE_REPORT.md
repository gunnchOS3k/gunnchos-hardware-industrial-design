# Firmware Compatibility Smoke Report

Generated: 2026-06-21T22:29:53.903577+00:00

Overall: PASS

```json
{
  "validate_firmware_manifests": {
    "exit_code": 0,
    "output": "PASS firmware manifest validation"
  },
  "validate_firmware_descriptors": {
    "exit_code": 0,
    "output": "PASS firmware descriptor validation"
  },
  "validate_capsule_update_simulation": {
    "exit_code": 0,
    "output": "PASS capsule update simulation validation"
  },
  "validate_firmware_implementation": {
    "exit_code": 0,
    "output": "PASS firmware implementation validation"
  },
  "qemu_dry_run": {
    "exit_code": 0,
    "output": "{\n  \"status\": \"pass\",\n  \"device\": \"student_14_5\",\n  \"requested_device\": \"student_14_5\",\n  \"profile\": {\n    \"machine\": \"q35\",\n    \"firmware\": \"OVMF\",\n    \"device_profile\": \"student_14_5\"\n  },\n  \"qemu_available\": false,\n  \"mode\": \"dry_run\",\n  \"message\": \"OVMF-style harness validated (dry run)\"\n}"
  },
  "capsule_sim": {
    "exit_code": 0,
    "output": "{\n  \"status\": \"success\",\n  \"simulated_only\": true,\n  \"capsule_id\": \"gunnchos-capsule-sample\",\n  \"target_version\": \"0.1.1-harness\",\n  \"device_id\": \"student_14_5\",\n  \"reboot_required\": true,\n  \"message\": \"Simulated capsule staged \\u2014 no real firmware flashed\"\n}"
  }
}
```
