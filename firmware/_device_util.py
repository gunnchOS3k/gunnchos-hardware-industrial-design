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


def _absorb_profiles(source: dict[str, Any], supplied: dict[str, dict[str, str]]) -> bool:
    """Merge canonical profiles. Return True when a key cannot be normalized.

    A failed key is omitted. It is not stored under its raw name.
    """
    rejected = False
    for raw_key, value in (source.get("profiles") or {}).items():
        canon = normalize_device_id(str(raw_key))
        if canon is None or canon not in CANONICAL_DEVICES or not isinstance(value, dict):
            rejected = True
            continue
        supplied[canon] = {**supplied.get(canon, {}), **value, "device_profile": canon}
    return rejected


def load_qemu_profiles(profiles_yaml: Path, profiles_json: Path | None = None) -> dict[str, dict[str, str]]:
    """Load digital QEMU profiles for the Device Quartet.

    Defaults are digital placeholders for a canonical identity the file omits.
    They are not physical devices. If a key fails normalization, that key is
    dropped and defaults are not used to fill the quartet around it.
    """
    supplied: dict[str, dict[str, str]] = {}
    rejected = False
    if profiles_yaml.exists():
        rejected = _absorb_profiles(load_structured(profiles_yaml), supplied) or rejected
    if profiles_json and profiles_json.exists():
        rejected = _absorb_profiles(json.loads(profiles_json.read_text()), supplied) or rejected
    if rejected:
        return supplied
    profiles = {device_id: dict(profile) for device_id, profile in DEFAULT_QEMU_PROFILES.items()}
    for device_id, profile in supplied.items():
        profiles[device_id] = {**profiles.get(device_id, {}), **profile, "device_profile": device_id}
    return profiles
