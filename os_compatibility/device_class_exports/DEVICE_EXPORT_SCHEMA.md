# Device Export Schema

Hardware-side export manifests under `device_class_exports/` are the source of truth for device-class assumptions consumed by gunnchos-device-os `hardware_compat/device_profiles/`.

## Required fields

- `device_id`, `hardware_repo_device_name`, `os_repo_profile_name`
- Capability blocks: `display`, `input`, `audio`, `camera_mic`, `network`, `storage`, `memory`, `battery`, `thermal`, `ports`, `dock`, `sensors`, `controller`, `keyboard`, `touch`, `accessibility`
- OS mapping: `supported_modes`, `unsupported_modes`, `supported_journey_presets`, `supported_app_packs`
- Feature flags: `developer_features`, `gaming_media_features`, `creator_features`, `research_features`, `school_library_features`, `guardian_features`, `offline_features`
- Boot/firmware: `boot_expectations`, `recovery_expectations`, `firmware_interface_expectations`, `power_management_expectations`, `thermal_management_expectations`
- Evidence: `known_gaps`, `required_real_hardware_evidence`, `claim_boundary`, `source_artifacts`

## Sync rule

When hardware I/O, power, thermal, or product docs change, update the export YAML and notify OS repo to refresh profile mirrors.
