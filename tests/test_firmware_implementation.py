"""Firmware implementation tests at repo root."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]


def test_firmware_manifests_exist():
    for d in DEVICES:
        assert (ROOT / f"firmware/manifests/{d}_firmware_manifest.yaml").exists()


def test_firmware_descriptors_exist():
    for d in DEVICES:
        assert (ROOT / f"firmware/descriptors/acpi/{d}_dsdt.dsl").exists()
        assert (ROOT / f"firmware/descriptors/devicetree/{d}.dts").exists()


def test_qemu_profile_dry_run():
    r = subprocess.run(
        [sys.executable, "firmware/qemu/run_device_profile_vm.py", "--dry-run", "--device", "student_14_5"],
        cwd=ROOT,
    )
    assert r.returncode == 0


def test_capsule_manifest_verify():
    r = subprocess.run([sys.executable, "firmware/capsule_update/verify_capsule_manifest.py"], cwd=ROOT)
    assert r.returncode == 0


def test_dock_interface_contract():
    dock = ROOT / "firmware/interfaces/docking_external_display_contract.yaml"
    assert dock.exists()
    assert "docking_external_display" in dock.read_text()
