# Power / boot state machine — current (contract)

States from `firmware/interfaces/power_state_contract.yaml` (S0, S3, S4, S5) plus harness boot paths from `firmware/manifests/*_firmware_manifest.yaml`. **Harness only. Not proven on silicon.**

```mermaid
stateDiagram-v2
  [*] --> S5: unpowered_or_off
  S5 --> S0: power_apply_modeled
  S0 --> S3: suspend_contract
  S3 --> S0: resume_contract
  S0 --> S4: hibernate_contract
  S4 --> S0: resume_from_disk_contract
  S0 --> S5: shutdown_contract
  S0 --> Recovery: recovery_requested
  Recovery --> S0: recovery_complete_harness
  S0 --> SafeMode: safe_mode_boot_contract
  SafeMode --> S0: continue_harness
```

Handheld / Student / DS-XL manifests list `uefi_standard_boot`, `recovery_boot`, `safe_mode_boot`. Capsule update is `simulated_only`. Dock and rings do not claim UEFI on this diagram.

Physical bring-up must record measured rails before treating S0 as `DEVICE_MEASURED`. See [sequence_bringup.md](sequence_bringup.md).
