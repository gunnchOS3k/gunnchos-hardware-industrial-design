#!/usr/bin/env bash
# Export OpenSCAD models to STL — requires OpenSCAD CLI
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/exports/stl"
SCAD_DIR="$ROOT/cad/openscad"
mkdir -p "$OUT"

if ! command -v openscad >/dev/null 2>&1; then
  echo "OpenSCAD not installed. See exports/OPENSCAD_EXPORT_STATUS.md"
  exit 1
fi

export_pairs=(
  "student_14:student_14.scad"
  "handheld_hybrid:handheld_hybrid.scad"
  "ds_xl_coder:ds_xl_coder.scad"
  "wearables_arena_set:wearables_arena_set.scad"
)

for pair in "${export_pairs[@]}"; do
  name="${pair%%:*}"
  scad="${pair##*:}"
  openscad -o "$OUT/${name}_placeholder.stl" "$SCAD_DIR/$scad"
  echo "Exported $OUT/${name}_placeholder.stl"
done
