#!/usr/bin/env bash
# Require a real `west build` for the HW-002 ring Zephyr workspace.
# Soft-skip is forbidden: missing SDK/west/ZEPHYR_BASE exits non-zero.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HW_ROOT="$(cd "$ROOT/../../.." && pwd)"
EVIDENCE_DIR="${HW002_EVIDENCE_DIR:-$HW_ROOT/artifacts/hw002/zephyr_west}"
BOARD="${RING_ZEPHYR_BOARD:-nrf52840dk/nrf52840}"
BUILD_DIR="$ROOT/build/zephyr_west"

mkdir -p "$EVIDENCE_DIR" "$ROOT/build/out"

resolve_tool() {
  if [[ -z "${ZEPHYR_BASE:-}" ]]; then
    for cand in "$HOME/zephyr-workspace/zephyr" "/Users/gunnchos/zephyr-workspace/zephyr"; do
      if [[ -d "$cand" ]]; then export ZEPHYR_BASE="$cand"; break; fi
    done
  fi
  if [[ -z "${ZEPHYR_SDK_INSTALL_DIR:-}" ]]; then
    for cand in "$HOME/zephyr-workspace/zephyr-sdk-0.16.8" "/Users/gunnchos/zephyr-workspace/zephyr-sdk-0.16.8"; do
      if [[ -d "$cand" ]]; then export ZEPHYR_SDK_INSTALL_DIR="$cand"; break; fi
    done
  fi
  export ZEPHYR_TOOLCHAIN_VARIANT="${ZEPHYR_TOOLCHAIN_VARIANT:-zephyr}"

  WEST_BIN=""
  for cand in \
    "$ROOT/.toolchain/west-venv/bin/west" \
    "${EDGE_IO_RING_FW:-}/.toolchain/west-venv/bin/west" \
    "$HOME/.local/bin/west" \
    "$(command -v west || true)"; do
    if [[ -n "$cand" && -x "$cand" ]]; then WEST_BIN="$cand"; break; fi
  done

  # Prefer edge-io isolated west if present beside sibling repos.
  if [[ -z "$WEST_BIN" ]]; then
    SIB="$(cd "$HW_ROOT/.." && pwd)/edge-io-measurement-node/gate1_digital_fabrication/ring_firmware/.toolchain/west-venv/bin/west"
    if [[ -x "$SIB" ]]; then WEST_BIN="$SIB"; fi
  fi
}

resolve_tool

fail() {
  echo "RING_ZEPHYR_WEST_BUILD_FAIL: $*" | tee "$EVIDENCE_DIR/WEST_BUILD_FAIL.txt"
  cat > "$EVIDENCE_DIR/ZEPHYR_WEST_PROBE.json" <<EOF
{
  "generated_at_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "west_build_pass": false,
  "soft_skip": false,
  "board": "$BOARD",
  "blockers": ["$*"]
}
EOF
  exit 1
}

[[ -n "${ZEPHYR_BASE:-}" && -d "${ZEPHYR_BASE}" ]] || fail "ZEPHYR_BASE unset/missing — west build required"
[[ -n "${ZEPHYR_SDK_INSTALL_DIR:-}" && -d "${ZEPHYR_SDK_INSTALL_DIR}" ]] || fail "ZEPHYR_SDK_INSTALL_DIR unset/missing — west build required"
[[ -n "${WEST_BIN:-}" && -x "${WEST_BIN}" ]] || fail "west binary missing — install west in isolated venv; soft-skip forbidden"

export PATH="$(dirname "$WEST_BIN"):${PATH:-}"

{
  echo "HW-002 require_west_build"
  echo "ZEPHYR_BASE=$ZEPHYR_BASE"
  echo "ZEPHYR_SDK_INSTALL_DIR=$ZEPHYR_SDK_INSTALL_DIR"
  echo "WEST_BIN=$WEST_BIN"
  echo "BOARD=$BOARD"
  echo "APP=$ROOT/zephyr_app"
  "$WEST_BIN" --version
} | tee "$EVIDENCE_DIR/WEST_ENV.txt"

cd "$ROOT"
echo "west build board=$BOARD app=zephyr_app (hard-fail, no soft-skip)"
set +e
"$WEST_BIN" build -b "$BOARD" -d "$BUILD_DIR" zephyr_app 2>&1 | tee "$EVIDENCE_DIR/WEST_BUILD_LOG.txt"
rc=${PIPESTATUS[0]}
set -e
[[ $rc -eq 0 ]] || fail "west build exited $rc"

ELF="$BUILD_DIR/zephyr/zephyr.elf"
BIN="$BUILD_DIR/zephyr/zephyr.bin"
HEX="$BUILD_DIR/zephyr/zephyr.hex"
[[ -f "$ELF" ]] || fail "zephyr.elf missing after west build"

mkdir -p "$ROOT/build/out" "$EVIDENCE_DIR/out"
cp -f "$ELF" "$ROOT/build/out/hw002_ring_zephyr_nrf52840.elf"
cp -f "$ELF" "$EVIDENCE_DIR/out/hw002_ring_zephyr_nrf52840.elf"
[[ -f "$BIN" ]] && cp -f "$BIN" "$EVIDENCE_DIR/out/hw002_ring_zephyr_nrf52840.bin"
[[ -f "$HEX" ]] && cp -f "$HEX" "$EVIDENCE_DIR/out/hw002_ring_zephyr_nrf52840.hex"
(cd "$EVIDENCE_DIR/out" && shasum -a 256 hw002_ring_zephyr_nrf52840.* > SHA256SUMS)

python3 - <<PY
import json
from datetime import datetime, timezone
from pathlib import Path
ev = Path("$EVIDENCE_DIR")
elf = ev / "out" / "hw002_ring_zephyr_nrf52840.elf"
probe = {
  "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
  "west_build_pass": True,
  "soft_skip": False,
  "board": "$BOARD",
  "app": "firmware/edge_io_rings/zephyr_west/zephyr_app",
  "zephyr_base": "$ZEPHYR_BASE",
  "sdk": "$ZEPHYR_SDK_INSTALL_DIR",
  "elf_bytes": elf.stat().st_size if elf.exists() else None,
  "tokens": ["RING_ZEPHYR_WEST_BUILD_PASS"],
  "not_claimed": ["RING_PHYSICAL_BOOT", "HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE"],
  "blockers": [],
}
(ev / "ZEPHYR_WEST_PROBE.json").write_text(json.dumps(probe, indent=2) + "\n")
(ev / "RING_ZEPHYR_WEST_BUILD_PASS.md").write_text(
"""# RING_ZEPHYR_WEST_BUILD_PASS (HW-002)

Real \`west build\` succeeded for hardware-repo west workspace.

- Board: \`$BOARD\`
- App: \`firmware/edge_io_rings/zephyr_west/zephyr_app\`
- Soft-skip: **forbidden / not used**
- Physical flash/boot: **NOT claimed**

Evidence: \`artifacts/hw002/zephyr_west/\`
"""
)
print("RING_ZEPHYR_WEST_BUILD_PASS")
PY
