#!/usr/bin/env python3
"""Generate placeholder render README or Blender PNGs if available."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RENDERS = ROOT / "cad" / "renders"
RENDERS.mkdir(parents=True, exist_ok=True)

try:
    import subprocess
    subprocess.run(["blender", "--version"], capture_output=True, check=True)
    has_blender = True
except Exception:
    has_blender = False

if not has_blender:
    (RENDERS / "README.md").write_text(
        "# Placeholder renders\n\nInstall Blender to auto-render STLs. "
        "Until then, use OpenSCAD preview or import STL into your CAD tool.\n"
    )
    print("Blender not found; wrote cad/renders/README.md")
else:
    print("Blender found; add batch render script in a future iteration.")
