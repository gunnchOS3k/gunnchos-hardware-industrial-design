"""Shared helpers for Cont IX."""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
BRANCH = "continuation-ix/pre-evt-hardware-lock"
BASE_SHA = "a710f35559252f36f0e6af7e025a5958df0906e3"
KICAD_CLI = Path("/opt/homebrew/bin/kicad-cli")
KICAD_FP = Path("/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints")
PRODUCTS = [
    "handheld_hybrid",
    "edge_io_rings",
    "dock",
    "student_14_5",
    "ds_xl_coder",
]


def root() -> Path:
    return Path(__file__).resolve().parents[2]


def art() -> Path:
    return root() / "artifacts/continuation_ix_pre_evt"


def docs() -> Path:
    return root() / "docs/full_product_family"


def release_docs() -> Path:
    return root() / "docs/release"


def deterministic_uuid(seed: str) -> str:
    h = hashlib.sha1(seed.encode()).hexdigest()
    return str(uuid.UUID(h[:32]))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, obj) -> None:
    write(path, json.dumps(obj, indent=2, sort_keys=False) + "\n")


def grid_mm(n: float) -> float:
    g = 1.27
    return round(n / g) * g


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
