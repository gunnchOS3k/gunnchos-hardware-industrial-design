from pathlib import Path
import subprocess
import sys


def test_device_id_aliases():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "firmware"))
    from _device_util import normalize_device_id  # noqa: E402

    assert normalize_device_id("student_14") == "student_14_5"
    assert normalize_device_id("student-14-5") == "student_14_5"
    assert normalize_device_id("wearables_arena") == "wearables_arena_set"


def test_qemu_all_devices():
    root = Path(__file__).resolve().parents[1]
    for device in ("student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"):
        r = subprocess.run(
            [sys.executable, "firmware/qemu/run_device_profile_vm.py", "--dry-run", "--device", device],
            cwd=root,
        )
        assert r.returncode == 0, device


def test_capsule_json_manifest_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "firmware/capsule_update/sample_capsule_manifest.json").exists()
    r = subprocess.run([sys.executable, "firmware/capsule_update/verify_capsule_manifest.py"], cwd=root)
    assert r.returncode == 0
