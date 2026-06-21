"""Shared device ID normalization and YAML/JSON loading for firmware harness."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

CANONICAL_DEVICES = (
    "student_14_5",
    "handheld_hybrid",
    "ds_xl_coder",
    "wearables_arena_set",
)

ALIASES = {
    "student_14": "student_14_5",
    "student-14-5": "student_14_5",
    "student_14_5": "student_14_5",
    "handheld-hybrid": "handheld_hybrid",
    "handheld_hybrid": "handheld_hybrid",
    "ds_xl_coder": "ds_xl_coder",
    "ds-xl-coder": "ds_xl_coder",
    "wearables_arena_set": "wearables_arena_set",
    "wearables-arena-set": "wearables_arena_set",
    "wearables_arena": "wearables_arena_set",
}

DEFAULT_QEMU_PROFILES: dict[str, dict[str, str]] = {
    "student_14_5": {"machine": "q35", "firmware": "OVMF", "device_profile": "student_14_5"},
    "handheld_hybrid": {"machine": "q35", "firmware": "OVMF", "device_profile": "handheld_hybrid"},
    "ds_xl_coder": {"machine": "q35", "firmware": "OVMF", "device_profile": "ds_xl_coder"},
    "wearables_arena_set": {"machine": "q35", "firmware": "OVMF", "device_profile": "wearables_arena_set"},
}


def normalize_device_id(device_id: str) -> str | None:
    key = device_id.strip().lower().replace("-", "_")
    key = re.sub(r"_+", "_", key)
    if key in ALIASES:
        return ALIASES[key]
    if key.replace("_", "-") in ALIASES:
        return ALIASES[key.replace("_", "-")]
    return ALIASES.get(device_id.strip())


def load_structured(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        return data if isinstance(data, dict) else {}
    except ImportError:
        pass
    except Exception:
        pass
    if path.suffix == ".json":
        return json.loads(text)
    # Minimal YAML-ish fallback for simple key-value files
    if path.name.endswith(".yaml") or path.name.endswith(".yml"):
        return _parse_simple_yaml(text)
    return {}


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse simple nested YAML used by harness configs without PyYAML."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, root)]
    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        while stack and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if not val:
            parent[key] = {}
            stack.append((indent + 2, parent[key]))
        else:
            if val.lower() in ("true", "false"):
                parent[key] = val.lower() == "true"
            elif val.isdigit():
                parent[key] = int(val)
            else:
                parent[key] = val.strip('"').strip("'")
    return root


def load_qemu_profiles(profiles_yaml: Path, profiles_json: Path | None = None) -> dict[str, dict[str, str]]:
    profiles: dict[str, dict[str, str]] = dict(DEFAULT_QEMU_PROFILES)
    if profiles_yaml.exists():
        data = load_structured(profiles_yaml)
        for k, v in (data.get("profiles") or {}).items():
            canon = normalize_device_id(str(k)) or str(k)
            if isinstance(v, dict):
                profiles[canon] = {**profiles.get(canon, {}), **v, "device_profile": canon}
    if profiles_json and profiles_json.exists():
        data = json.loads(profiles_json.read_text())
        for k, v in (data.get("profiles") or {}).items():
            canon = normalize_device_id(str(k)) or str(k)
            if isinstance(v, dict):
                profiles[canon] = {**profiles.get(canon, {}), **v, "device_profile": canon}
    return profiles
