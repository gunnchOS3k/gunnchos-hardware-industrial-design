#!/usr/bin/env python3
from pathlib import Path

DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    out_dir = ROOT / "results/manufacturing"
    out_dir.mkdir(parents=True, exist_ok=True)
    for d in DEVICES:
        mfg = ROOT / "manufacturing" / d
        index = out_dir / f"{d}_package_index.md"
        index.write_text(
            f"""# Manufacturing package index — {d}

Status: **EVT-1 stub** — Gerbers/CPL after layout and DRC pass.

## Included
- `manufacturing/{d}/factory_test_procedure.md`
- `manufacturing/{d}/factory_test_script.py`
- `manufacturing/{d}/gerbers/` (placeholder)
- `electrical/{d}/kicad/` (schematic stub)

## Blockers for H3
- ERC pass
- DRC pass
- Gerber generation
- IPC-2581 export
""",
            encoding="utf-8",
        )
    print("Generated manufacturing package indexes")


if __name__ == "__main__":
    main()
