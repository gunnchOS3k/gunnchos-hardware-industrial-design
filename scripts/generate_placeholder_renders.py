#!/usr/bin/env python3
"""Generate placeholder SVG renders for EVT-1 vendor package."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports" / "renders"
OUT.mkdir(parents=True, exist_ok=True)

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="240" viewBox="0 0 400 240">
  <rect width="400" height="240" fill="#f4f4f5"/>
  <text x="200" y="110" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#52525b">{label}</text>
  <text x="200" y="140" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#71717a">EVT-1 PLACEHOLDER RENDER</text>
  <text x="200" y="165" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#a1a1aa">Not a manufacturing drawing</text>
</svg>"""

DEVICES = {
    "student_14_placeholder.svg": "Student 14.5\"",
    "handheld_hybrid_placeholder.svg": "Handheld Hybrid",
    "ds_xl_coder_placeholder.svg": "DS-XL Coder",
    "wearables_arena_set_placeholder.svg": "Wearables/Arena Set",
}

for fname, label in DEVICES.items():
    (OUT / fname).write_text(SVG.format(label=label))
    print(f"Wrote exports/renders/{fname}")
