"""A complete export must not pass with a missing or swapped quartet identity."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _validator():
    path = ROOT / "scripts/validate_os_compatibility_handoff.py"
    spec = importlib.util.spec_from_file_location("validate_os_compatibility_handoff", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_mislabeled_quartet_identity_is_rejected() -> None:
    mod = _validator()
    payload = {field: "present" for field in mod.EXPORT_FIELDS}
    payload["device_id"] = "student_desk"
    payload["hardware_repo_device_name"] = "Student Desk"
    payload["os_repo_profile_name"] = "student_desk"

    errors = mod.export_identity_errors("student_14_5_os_export.yaml", payload)
    assert errors
    assert any("device_id='student_desk'" in err for err in errors)

    missing = {field: "present" for field in mod.EXPORT_FIELDS}
    del missing["device_id"]
    missing_errors = mod.export_identity_errors("wearables_arena_set_os_export.yaml", missing)
    assert missing_errors
    assert any("device_id=None" in err for err in missing_errors)

    for rel in mod.EXPORTS:
        data = mod.load_yaml(ROOT / rel)
        assert mod.export_identity_errors(rel, data) == []
