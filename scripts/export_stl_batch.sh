#!/usr/bin/env bash
# Export OpenSCAD models to STL — requires OpenSCAD CLI
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/exports/stl"
mkdir -p "$OUT"

if ! command -v openscad >/dev/null 2>&1; then
  echo "OpenSCAD not installed. See exports/OPENSCAD_EXPORT_STATUS.md"
  exit 1
fi

declare -A MAP=(
  ["student_14"]="cad/openscad/student_14.scad"
  ["handheld_hybrid"]="cad/openscad/handheld_hybrid.scad"
  ["ds_xl_coder"]="cad/openscad/ds_xl_coder.scad"
  ["wearables_arena_set"]="cad/openscad/wearables_arena_set.scad"
)

for name in "${!MAP[@]}"; do
  scad="${MAP[$name]}"
  openscad -o "$OUT/${name}_placeholder.stl" "$ROOT/$scad"
  echo "Exported $OUT/${name}_placeholder.stl"
done
