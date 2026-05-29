#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/cad/exports"
mkdir -p "$OUT"
if ! command -v openscad >/dev/null 2>&1; then
  echo "OpenSCAD not installed. Install: https://openscad.org/downloads.html"
  echo "Skipping STL export (non-fatal)."
  exit 0
fi
while IFS= read -r -d '' f; do
  base=$(basename "$f" .scad)
  rel=$(dirname "$f" | sed "s|$ROOT/cad/openscad/||")
  mkdir -p "$OUT/$rel"
  openscad -o "$OUT/$rel/${base}.stl" "$f"
  echo "Exported $OUT/$rel/${base}.stl"
done < <(find "$ROOT/cad/openscad" -name '*.scad' -print0)
