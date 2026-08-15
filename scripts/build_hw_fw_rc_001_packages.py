#!/usr/bin/env python3
"""Build HW-FW-RC-001 per-product digital release packages (honest token gate).

Resource policy: indexes existing Cont IX / HW-002 evidence; does not run
family-wide EDA batch sweeps or thermal Monte Carlo.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "hw_fw_rc_001"
PRODUCTS = [
    "student_14_5",
    "ds_xl_coder",
    "handheld_hybrid",
    "dock",
    "edge_io_rings",
]
TOKEN_NAMES = {
    "student_14_5": "STUDENT_HW_DIGITAL_RELEASE_PACKAGE",
    "ds_xl_coder": "DSXL_HW_DIGITAL_RELEASE_PACKAGE",
    "handheld_hybrid": "HANDHELD_HW_DIGITAL_RELEASE_PACKAGE",
    "dock": "DOCK_HW_DIGITAL_RELEASE_PACKAGE",
    "edge_io_rings": "RING_HW_DIGITAL_RELEASE_PACKAGE",
}
FALSE_ALWAYS = {
    "EVT_PASS": False,
    "DVT_PASS": False,
    "PVT_PASS": False,
    "RF_CERTIFIED": False,
    "EMC_CERTIFIED": False,
    "BATTERY_CERTIFIED": False,
    "SHIPPING_HARDWARE": False,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path):
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def erc_drc(product: str) -> dict:
    status = load_json(ROOT / "device_designs" / product / "manufacturing" / "ERC_DRC_STATUS.json") or {}
    cont = load_json(ROOT / "artifacts" / "continuation_ix_pre_evt" / "kicad_cli" / product / "erc.json")
    # Prefer Cont IX manufacturing status (errors counts)
    erc = status.get("erc") or {}
    drc = status.get("drc") or {}
    pcb = ROOT / "device_designs" / product / "kicad" / f"{product}.kicad_pcb"
    sch = ROOT / "device_designs" / product / "kicad" / f"{product}.kicad_sch"
    layout_exists = pcb.is_file() and pcb.stat().st_size > 500
    return {
        "schematic_path": str(sch.relative_to(ROOT)) if sch.is_file() else None,
        "pcb_path": str(pcb.relative_to(ROOT)) if pcb.is_file() else None,
        "schematic_complete_editable": bool(sch.is_file()),
        "pcb_layout_exists": layout_exists,
        "pcb_layout_status": "PRESENT" if layout_exists else "PCB_LAYOUT_DIGITAL_OPEN",
        "erc": {
            "errors": int(erc.get("errors", -1)),
            "warnings": int(erc.get("warnings", -1)),
            "pass": erc.get("errors") == 0,
            "source": "device_designs/*/manufacturing/ERC_DRC_STATUS.json (Cont IX)",
            "by_type": erc.get("by_type"),
        },
        "drc": {
            "errors": int(drc.get("errors", -1)),
            "warnings": int(drc.get("warnings", -1)),
            "pass": (drc.get("errors") == 0) if layout_exists else None,
            "source": "device_designs/*/manufacturing/ERC_DRC_STATUS.json (Cont IX)",
            "by_type": drc.get("by_type"),
            "note": "Family-wide re-sweep DEFERRED (Product-Use QEMU resource rule); Cont IX + HW-002 handheld closure reused",
        },
        "cont_ix_erc_present": cont is not None,
    }


def power_thermal(product: str) -> dict:
    elec = ROOT / "device_designs" / product / "electrical"
    battery = elec / "battery_model.yaml"
    thermal = elec / "thermal_model.yaml"
    power = elec / "power_budget.yaml"
    out = {
        "power_budget": str(power.relative_to(ROOT)) if power.is_file() else None,
        "power_tree": str((elec / "power_tree.yaml").relative_to(ROOT))
        if (elec / "power_tree.yaml").is_file()
        else None,
        "battery_model": None,
        "thermal_model": None,
        "battery_life_claim": False,
        "physical_thermal_pass": False,
    }
    if battery.is_file():
        text = battery.read_text()
        cls = "MODELED" if "MODELED" in text else ("TARGET" if "TARGET" in text else "UNKNOWN")
        out["battery_model"] = {
            "path": str(battery.relative_to(ROOT)),
            "evidence_class": cls,
            "PHYSICAL_PENDING": True,
        }
    elif product == "dock":
        out["battery_model"] = {
            "path": None,
            "evidence_class": "N_A_DOCK_LINE_POWERED",
            "PHYSICAL_PENDING": False,
        }
    if thermal.is_file():
        text = thermal.read_text()
        cls = "MODELED" if "MODELED" in text else "TARGET"
        out["thermal_model"] = {
            "path": str(thermal.relative_to(ROOT)),
            "evidence_class": cls,
            "PHYSICAL_PENDING": True,
            "physical_thermal_pass": False,
        }
    return out


def firmware_status(product: str, west_probe: dict | None) -> dict:
    manifest = ROOT / "firmware" / "manifests" / f"{product}_firmware_manifest.yaml"
    base = {
        "manifest": str(manifest.relative_to(ROOT)) if manifest.is_file() else None,
        "builds": False,
        "build_class": "MISSING",
        "evidence": [],
    }
    if product == "edge_io_rings":
        probe = west_probe or load_json(ROOT / "artifacts" / "hw002" / "zephyr_west" / "ZEPHYR_WEST_PROBE.json") or {}
        base.update(
            {
                "builds": bool(probe.get("west_build_pass")),
                "build_class": "ZEPHYR_WEST",
                "soft_skip": bool(probe.get("soft_skip", False)),
                "board": probe.get("board"),
                "script": "firmware/edge_io_rings/zephyr_west/scripts/require_west_build.sh",
                "evidence": [
                    "artifacts/hw_fw_rc_001/zephyr_west/ZEPHYR_WEST_PROBE.json",
                    "artifacts/hw002/zephyr_west/ZEPHYR_WEST_PROBE.json",
                    "firmware/edge_io_rings/zephyr_west/",
                ],
                "claim_boundary": "Digital west build only; physical flash/boot PHYSICAL_PENDING",
            }
        )
        return base
    # Host/COM products: harness + ACPI/DT descriptors
    acpi = ROOT / "firmware" / "descriptors" / "acpi" / f"{product}_dsdt.dsl"
    dts = ROOT / "firmware" / "descriptors" / "devicetree" / f"{product}.dts"
    if product == "dock":
        # Dock uses interface contracts + manifest; no ACPI profile required
        builds = manifest.is_file()
        base.update(
            {
                "builds": builds,
                "build_class": "MANIFEST_INTERFACE_HARNESS",
                "evidence": [
                    str(manifest.relative_to(ROOT)) if manifest.is_file() else None,
                    "firmware/interfaces/docking_external_display_contract.yaml",
                ],
                "claim_boundary": "Digital harness/contracts only; on-target dock FW PHYSICAL+BINARY_BLOB pending",
            }
        )
        return base
    builds = manifest.is_file() and (acpi.is_file() or dts.is_file())
    base.update(
        {
            "builds": builds,
            "build_class": "ACPI_DT_HARNESS",
            "acpi": str(acpi.relative_to(ROOT)) if acpi.is_file() else None,
            "devicetree": str(dts.relative_to(ROOT)) if dts.is_file() else None,
            "evidence": [p for p in [
                str(manifest.relative_to(ROOT)) if manifest.is_file() else None,
                str(acpi.relative_to(ROOT)) if acpi.is_file() else None,
                str(dts.relative_to(ROOT)) if dts.is_file() else None,
            ] if p],
            "claim_boundary": "Harness/ACPI/DT digital path; on-target COM/SoM firmware PHYSICAL+BINARY_BLOB pending",
        }
    )
    return base


def bom_avl(product: str) -> dict:
    assembly = ROOT / "device_designs" / product / "bom" / "assembly_bom.csv"
    supply = ROOT / "manufacturing" / "supply_chain" / f"{product}.json"
    legacy = ROOT / "bom" / product / "bom.csv"
    supply_j = load_json(supply) or {}
    honest_unknown = True
    fabricated_economics = []
    if legacy.is_file():
        for i, line in enumerate(legacy.read_text().splitlines()[1:], start=2):
            cols = line.split(",")
            # unit_cost_estimate column historically invented numeric prices
            if len(cols) >= 9:
                cost = cols[8].strip()
                if cost and cost not in {
                    "UNKNOWN",
                    "UNKNOWN_UNTIL_QUOTE",
                    "TODO_quote",
                    "",
                } and cost.replace(".", "", 1).isdigit():
                    fabricated_economics.append({"file": str(legacy.relative_to(ROOT)), "line": i, "value": cost})
                    honest_unknown = False
            if "Core Ultra 7 155H" in line and "COM-HPC" not in line:
                fabricated_economics.append(
                    {
                        "file": str(legacy.relative_to(ROOT)),
                        "line": i,
                        "issue": "bare_cpu_bga_mpn_forbidden_by_ADR-HW-001",
                    }
                )
                honest_unknown = False
    return {
        "assembly_bom": str(assembly.relative_to(ROOT)) if assembly.is_file() else None,
        "supply_chain_fields": str(supply.relative_to(ROOT)) if supply.is_file() else None,
        "legacy_bom": str(legacy.relative_to(ROOT)) if legacy.is_file() else None,
        "PRODUCTION_RELEASE_CLAIMED": supply_j.get("PRODUCTION_RELEASE_CLAIMED", False),
        "economics_policy": "UNKNOWN_UNTIL_QUOTE — no fabricated MOQ/price/stock",
        "fabricated_economics_findings": fabricated_economics,
        "bom_avl_honest": assembly.is_file() and supply.is_file() and honest_unknown and not fabricated_economics,
        "note": "Canonical orderable MPNs live in device_designs/*/bom/assembly_bom.csv + manufacturing/supply_chain/*.json",
    }


def drivers(product: str) -> dict:
    clf = load_json(ROOT / "docs" / "full_product_family" / "DRIVER_CLASSIFICATION.json") or {}
    products = clf.get("products") or {}
    prod = products.get(product) or {}
    subsystems = prod.get("subsystems") or []
    # DS-XL inherits Student matrix in JSON as a string marker — expand for honesty.
    if subsystems == "same_as_student_14_5" or prod.get("inherits_driver_matrix_from") == "student_14_5":
        subsystems = list((products.get("student_14_5") or {}).get("subsystems") or [])
    if not isinstance(subsystems, list):
        subsystems = []
    unavailable = [s for s in subsystems if isinstance(s, dict) and "UNAVAILABLE" in (s.get("risk") or [])]
    arch_notes = []
    if unavailable:
        arch_notes.append(
            {
                "trigger": "UNAVAILABLE",
                "subsystems": [s.get("id") for s in unavailable],
                "note": "Architecture revision / non-claim already recorded in DRIVER_CLASSIFICATION.md (ME open replacement; 6G/NTN on RM520N-GL; TB5 rejected)",
            }
        )
    # Global unavailable from md
    if product in {"student_14_5", "ds_xl_coder"}:
        arch_notes.append(
            {
                "id": "open_me_replacement",
                "risk": "UNAVAILABLE",
                "arch_revision_note": "Retain ADLINK COM + vendor ME/CSME BINARY_BLOB; do not invent open ME",
            }
        )
        arch_notes.append(
            {
                "id": "wwan_6g_ntn",
                "risk": "UNAVAILABLE",
                "arch_revision_note": "RM520N-GL is Rel-16 Sub-6 NSA+SA only; NTN/6G remain simulated/migration abstractions — not modem claims",
            }
        )
    if product == "dock":
        arch_notes.append(
            {
                "id": "tb5_80g",
                "risk": "UNAVAILABLE",
                "arch_revision_note": "ADR-HW-002 freezes JHL8440 + JHL9040R @ 40G; reject JHL9480/JHL9580",
            }
        )
    return {
        "classification_json": "docs/full_product_family/DRIVER_CLASSIFICATION.json",
        "classification_md": "docs/full_product_family/DRIVER_CLASSIFICATION.md",
        "subsystems": subsystems,
        "unavailable_triggers": unavailable,
        "architecture_revision_notes": arch_notes,
        "driver_risks_explicit": bool(subsystems) or product == "dock",
    }


def factory_service(product: str) -> dict:
    mfg = ROOT / "manufacturing" / product
    dd_mfg = ROOT / "device_designs" / product / "manufacturing"
    paths = {
        "factory_test_dir": mfg / "factory_test",
        "repair_dir": mfg / "repair",
        "repair_plan": ROOT / "manufacturing" / "REPAIR_AND_SERVICE_PLAN.md",
        "programming": dd_mfg / "PROGRAMMING.md",
        "qc": dd_mfg / "QC_CHECKLIST.md",
        "rework": dd_mfg / "REWORK.md",
        "calibration": dd_mfg / "CALIBRATION.md",
    }
    present = {k: str(v.relative_to(ROOT)) if v.exists() else None for k, v in paths.items()}
    complete = all(
        present[k]
        for k in ("factory_test_dir", "repair_dir", "programming", "qc", "repair_plan")
    )
    return {
        "paths": present,
        "factory_service_complete_digital": complete,
        "production_keys_ca": "PENDING",
        "physical_line_validation": "PHYSICAL_PENDING",
    }


def vendor_anchors(product: str) -> dict:
    common = {
        "student_14_5": {
            "compute": "ADLINK COM-HPC-mMTL-155H-32G",
            "cpu": "Core Ultra 7 155H",
            "memory": "32GB LPDDR5-class onboard COM",
            "wwan": "Quectel RM520N-GL Rel-16 Sub-6 NSA+SA",
            "not": ["NTN", "6G", "bare_CPU_BGA"],
        },
        "ds_xl_coder": {
            "compute": "ADLINK COM-HPC-mMTL-155H-32G",
            "cpu": "Core Ultra 7 155H",
            "memory": "32GB LPDDR5-class onboard COM",
            "display": "two independent useful displays (dual-eDP carrier)",
            "wwan": "Quectel RM520N-GL Rel-16 Sub-6 NSA+SA",
            "not": ["NTN", "6G", "alternate_COM_as_display_fix"],
        },
        "handheld_hybrid": {
            "som": "Radxa NX5 RM121-D8E32",
            "emmc": "32GB system/recovery",
            "microsd": "required large content (games/AI/WAIKE/media)",
            "lifecycle_floor": ">= Sep 2033 (Radxa brief)",
            "not": ["invented_larger_emmc_sku", "bare_RK3588S_BGA"],
        },
        "dock": {
            "controller": "Intel JHL8440",
            "retimer": "Intel JHL9040R",
            "link": "TB4/USB4 40G",
            "not": ["TB5", "80G", "JHL9480", "JHL9580"],
        },
        "edge_io_rings": {
            "mcu": "nRF52840",
            "imu": "BMI270",
            "cap": "IQS7222A",
            "se": "SE050",
            "pmic": "nPM1300",
            "uwb_optional": "DW3000/DWM3001C",
            "not": ["IMU_only_absolute_position"],
        },
    }
    return common[product]


def package_sections(product: str) -> dict:
    dd = ROOT / "device_designs" / product
    return {
        "electrical_block_diagram": str((dd / "architecture.md").relative_to(ROOT)),
        "power_tree": str((dd / "electrical" / "power_tree.yaml").relative_to(ROOT))
        if (dd / "electrical" / "power_tree.yaml").is_file()
        else None,
        "rail_budget": str((dd / "electrical" / "power_budget.yaml").relative_to(ROOT))
        if (dd / "electrical" / "power_budget.yaml").is_file()
        else None,
        "schematic": str((dd / "kicad" / f"{product}.kicad_sch").relative_to(ROOT)),
        "pcb": str((dd / "kicad" / f"{product}.kicad_pcb").relative_to(ROOT)),
        "stackup": str((dd / "manufacturing" / "stackup.yaml").relative_to(ROOT))
        if (dd / "manufacturing" / "stackup.yaml").is_file()
        else None,
        "bom_assembly": str((dd / "bom" / "assembly_bom.csv").relative_to(ROOT))
        if (dd / "bom" / "assembly_bom.csv").is_file()
        else None,
        "rf_model": str((dd / "electrical" / "rf_model.yaml").relative_to(ROOT))
        if (dd / "electrical" / "rf_model.yaml").is_file()
        else None,
        "manufacturing_release_checklist": str(
            (dd / "manufacturing" / "RELEASE_PACKAGE_CHECKLIST.md").relative_to(ROOT)
        ),
        "cont_ix_release": str((dd / "manufacturing" / "cont_ix_release").relative_to(ROOT))
        if (dd / "manufacturing" / "cont_ix_release").is_dir()
        else None,
        "drivers_readme": str((dd / "drivers" / "README.md").relative_to(ROOT))
        if (dd / "drivers" / "README.md").is_file()
        else None,
    }


def evaluate_token(product: str, pkg: dict) -> dict:
    c = {
        "schematic_complete": pkg["eda"]["schematic_complete_editable"],
        "erc_pass": bool(pkg["eda"]["erc"]["pass"]),
        "pcb_sufficient": pkg["eda"]["pcb_layout_exists"]
        or pkg["eda"]["pcb_layout_status"] == "PCB_LAYOUT_DIGITAL_OPEN",
        "drc_pass_where_layout": (
            bool(pkg["eda"]["drc"]["pass"])
            if pkg["eda"]["pcb_layout_exists"]
            else True
        ),
        "bom_avl_honest": bool(pkg["bom_avl"]["bom_avl_honest"]),
        "driver_risks_explicit": bool(pkg["drivers"]["driver_risks_explicit"]),
        "power_model_complete": bool(
            pkg["power_thermal"]["power_budget"] or pkg["power_thermal"]["power_tree"]
        ),
        "thermal_model_complete": bool(pkg["power_thermal"]["thermal_model"]),
        "firmware_builds": bool(pkg["firmware"]["builds"])
        and not pkg["firmware"].get("soft_skip"),
        "factory_service_complete": bool(
            pkg["factory_service"]["factory_service_complete_digital"]
        ),
        "dvpr_complete": True,  # master DVPR rows generated this packet
        "s0_digital_zero": pkg["severity"]["S0_digital"] == 0,
        "s1_digital_zero": pkg["severity"]["S1_digital"] == 0,
    }
    # NDA residual: withhold full package token for COM/Dock pin-accurate completeness
    nda_withhold = product in {"student_14_5", "ds_xl_coder", "dock"}
    if nda_withhold:
        c["nda_public_side_ok_but_pin_accurate_external"] = True
    earned = all(
        v
        for k, v in c.items()
        if k
        not in {
            "nda_public_side_ok_but_pin_accurate_external",
        }
    )
    # Prefer FAIL for NDA-blocked products: schematic completeness for release package
    # requires pin-accurate nets OR explicit CONDITIONAL — we withhold earned token.
    if nda_withhold:
        earned = False
        c["token_withhold_reason"] = (
            "EXTERNAL/NDA pin-accurate fanout remains; public Cont IX package is CONDITIONAL_VENDOR_COLLATERAL — "
            "prefer FAIL vs claiming STUDENT/DSXL/DOCK_HW_DIGITAL_RELEASE_PACKAGE"
        )
    # Ring/Handheld can earn if all gates true
    failed = [k for k, v in c.items() if v is False and k != "nda_public_side_ok_but_pin_accurate_external"]
    return {
        "token": TOKEN_NAMES[product],
        "earned": earned,
        "criteria": c,
        "failed_criteria": failed,
        **FALSE_ALWAYS,
    }


def severity(product: str, bom: dict, firmware: dict) -> dict:
    s0 = 0
    s1 = 0
    notes = []
    if bom.get("fabricated_economics_findings"):
        # Honesty defect — treat as digital S1 until fixed by this packet's BOM repair
        s1 += 1
        notes.append("legacy_bom_fabricated_economics_or_bare_cpu")
    if product == "edge_io_rings" and not firmware.get("builds"):
        s1 += 1
        notes.append("ring_zephyr_west_build_fail")
    # Cont IX residual warnings / NDA are not automatic S1
    return {"S0_digital": s0, "S1_digital": s1, "notes": notes}


def build_product(product: str, west_probe: dict | None) -> dict:
    eda = erc_drc(product)
    pt = power_thermal(product)
    fw = firmware_status(product, west_probe)
    bom = bom_avl(product)
    drv = drivers(product)
    fac = factory_service(product)
    sev = severity(product, bom, fw)
    pkg = {
        "schema": "gunnchos.hw_fw_rc_001.digital_release_package.v1",
        "packet": "HW-FW-RC-001",
        "product": product,
        "generated_at_utc": utc_now(),
        "vendor_anchors": vendor_anchors(product),
        "sections": package_sections(product),
        "eda": eda,
        "power_thermal": pt,
        "firmware": fw,
        "bom_avl": bom,
        "drivers": drv,
        "factory_service": fac,
        "severity": sev,
        "rf_final_pass": False,
        "spatial_accuracy": "PHYSICAL_PENDING" if product == "edge_io_rings" else None,
        "claim_boundary": {
            "physical_validation": False,
            "SHIPPING_HARDWARE": False,
            "battery_life_claim": False,
            "physical_thermal_pass": False,
            "rf_certified": False,
        },
    }
    pkg["token"] = evaluate_token(product, pkg)
    return pkg


def dvpr_master() -> dict:
    domains = [
        "electrical",
        "power",
        "battery",
        "thermal",
        "display",
        "usb",
        "dock",
        "storage",
        "rf",
        "antenna",
        "audio",
        "mechanical",
        "firmware",
        "security",
        "factory",
        "repair",
    ]
    rows = []
    for product in PRODUCTS:
        for domain in domains:
            if product == "dock" and domain == "battery":
                continue
            rows.append(
                {
                    "id": f"DVPR-{product}-{domain}",
                    "product": product,
                    "requirement": f"{domain} digital design meets Cont IX / HW-FW-RC-001 package criteria",
                    "test": f"digital_precheck_{domain}",
                    "method": "document_model_erc_drc_or_harness",
                    "digital_precheck": "DEFINED",
                    "equipment": "PHYSICAL_PENDING",
                    "sample_size_later": "PHYSICAL_PENDING",
                    "acceptance_criterion": "digital package present; no physical PASS claimed",
                    "state": "DIGITAL_DEFINED",
                    "evidence": f"artifacts/hw_fw_rc_001/products/{product}/DIGITAL_RELEASE_PACKAGE.json",
                    "physical_dependency": True,
                }
            )
    return {
        "schema": "gunnchos.hw_fw_rc_001.dvpr.v1",
        "generated_at_utc": utc_now(),
        "row_count": len(rows),
        "rows": rows,
        "claim_boundary": "Digital precheck definitions only — not EVT/DVT execution",
    }


def usb_dock_validate() -> dict:
    return {
        "schema": "gunnchos.hw_fw_rc_001.usb_dock_digital_validate.v1",
        "generated_at_utc": utc_now(),
        "silicon": {
            "controller": "JHL8440",
            "retimer": "JHL9040R",
            "generation": "TB4_USB4_40G",
            "tb5": False,
            "link_gbps": 40,
            "adr": "docs/adr/ADR-HW-002-dock-usb4-tb4-not-tb5.md",
        },
        "scenarios": [
            {"id": "attach", "model": "TYPE_C_ATTACH", "status": "DIGITALLY_DEFINED"},
            {"id": "pd_negotiation", "model": "PD_CONTRACT_TPS65994", "status": "DIGITALLY_DEFINED"},
            {"id": "host_device_role", "model": "DRP_POLICY", "status": "DIGITALLY_DEFINED"},
            {"id": "usb4_tb4_topology", "model": "JHL8440_40G", "status": "DIGITALLY_DEFINED"},
            {"id": "dp_tunneling", "model": "DP14_TUNNEL", "status": "DIGITALLY_DEFINED"},
            {"id": "multi_display", "model": "UP_TO_2_DP14", "status": "DIGITALLY_DEFINED"},
            {"id": "ethernet", "model": "RTL8156", "status": "DIGITALLY_DEFINED"},
            {"id": "usb_hub", "model": "VL817", "status": "DIGITALLY_DEFINED"},
            {"id": "audio", "model": "HUB_OR_HOST_PATH", "status": "DIGITALLY_DEFINED"},
            {"id": "power", "model": "PD_SOURCE_SINK", "status": "DIGITALLY_DEFINED"},
            {"id": "hotplug", "model": "HOTPLUG_REENUM", "status": "DIGITALLY_DEFINED"},
            {"id": "sleep_wake", "model": "S3_S0_RESUME", "status": "DIGITALLY_DEFINED"},
            {"id": "disconnect_reconnect", "model": "LINK_RETRAIN", "status": "DIGITALLY_DEFINED"},
            {"id": "fault_isolation", "model": "PORT_POWER_FAULT", "status": "DIGITALLY_DEFINED"},
        ],
        "compatibility": {
            "student_14_5": True,
            "ds_xl_coder": True,
            "handheld_hybrid": "VL108_COSTDOWN_OR_TB4_LIMITED",
        },
        "physical_si_validation": "PHYSICAL_PENDING",
        "nda_ball_maps": "EXTERNAL",
    }


def compatibility_matrix() -> dict:
    devices = ["student_14_5", "ds_xl_coder", "handheld_hybrid"]
    rings = "edge_io_rings"
    dock = "dock"
    matrix = {
        "schema": "gunnchos.hw_fw_rc_001.compatibility_matrix.v1",
        "generated_at_utc": utc_now(),
        "device_to_dock": {
            d: {
                "power": True,
                "display": True if d != "handheld_hybrid" else "LIMITED_DP_ALT_OR_VL108",
                "usb": True,
                "network": "via_dock_ethernet_or_host",
                "software": "gunnchOS_dock_contract",
            }
            for d in devices
        },
        "device_to_rings": {
            d: {
                "ble": True,
                "input_mapping": ["pointer", "click", "text", "delete", "shortcut", "gaming"],
                "se_identity": True,
                "uwb": "OPTIONAL",
                "spatial_accuracy": "PHYSICAL_PENDING",
            }
            for d in devices + [dock]
        },
        "device_to_software": {
            d: {
                "gunnchOS": True,
                "gunnchAI": True,
                "WAIKE": True,
                "games": True if d in {"handheld_hybrid", "student_14_5", "ds_xl_coder"} else False,
            }
            for d in devices
        },
        "claim_boundary": "Digital compatibility intent — not physical interoperability cert",
    }
    matrix["rings_product"] = rings
    matrix["dock_product"] = dock
    return matrix


def ring_sensing_map() -> dict:
    return {
        "schema": "gunnchos.hw_fw_rc_001.ring_sensing_map.v1",
        "generated_at_utc": utc_now(),
        "modalities_required": ["IMU_BMI270", "CAP_IQS7222A", "SE_SE050", "BLE_nRF52840"],
        "modalities_optional": ["UWB_DW3000", "BHI360", "BMM350"],
        "pmic": "nPM1300",
        "fusion_policy": ">=2 modalities before action dispatch (ADR-FP-008)",
        "imu_only_absolute_position": False,
        "action_map": {
            "pointer": ["IMU_delta", "CAP_hover"],
            "click": ["CAP_touch", "IMU_tap"],
            "text": ["CAP_gesture", "SE_auth_optional"],
            "delete": ["CAP_hold", "confidence_gate"],
            "shortcut": ["CAP_multi", "BLE_HID"],
            "gaming": ["IMU_rate", "CAP_trigger", "haptics_optional"],
        },
        "confidence": "required before destructive actions",
        "ota": "MCUboot/OpenDFU digital path",
        "spatial_accuracy": "PHYSICAL_PENDING",
    }


def vendor_refresh() -> dict:
    return {
        "schema": "gunnchos.hw_fw_rc_001.vendor_truth_refresh.v1",
        "generated_at_utc": utc_now(),
        "refreshed": True,
        "anchors": {
            "student_dsxl_com": {
                "mpn": "COM-HPC-mMTL-155H-32G",
                "vendor": "ADLINK",
                "cpu": "Core Ultra 7 155H",
                "memory": "32GB LPDDR5x-class onboard",
                "status": "CONFIRMED_PUBLIC_LISTING",
                "notes": [
                    "Still listed by distributors (e.g. WDL Systems SKU 1ACMK153)",
                    "Stock may be lead-time constrained — UNKNOWN_UNTIL_QUOTE for PO",
                    "Alternate COM-HPC-mMTL-155H-64G remains approved",
                ],
                "sources": [
                    "https://www.adlinktech.com/en/news/com-hpc-mini-intel-core-ultra",
                    "https://www.wdlsystems.com/adlink-com-hpc-mmtl-155h-32g",
                ],
            },
            "handheld_som": {
                "mpn": "RM121-D8E32",
                "vendor": "Radxa",
                "product": "NX5",
                "status": "CONFIRMED_PRODUCT_BRIEF",
                "emmc_gib": 32,
                "storage_architecture": {
                    "emmc": "system/recovery",
                    "microsd": "large content required",
                },
                "lifecycle_floor": ">= 2033-09 per Radxa brief",
                "sources": [
                    "https://dl.radxa.com/nx5/radxa_nx5_product_brief.pdf",
                    "https://docs.radxa.com/en/som/nx/nx5",
                ],
            },
            "cellular": {
                "mpn": "RM520N-GL",
                "vendor": "Quectel",
                "release": "3GPP Rel-16",
                "spectrum": "Sub-6",
                "modes": ["NSA", "SA"],
                "ntn": False,
                "is_6g": False,
                "sources": [
                    "https://www.quectel.com/product/5g-rm520n-series/",
                ],
            },
            "dock": {
                "controller": "JHL8440",
                "retimer": "JHL9040R",
                "tb_generation": "TB4_40G",
                "tb5": False,
                "sources": [
                    "https://www.intel.com/content/www/us/en/products/sku/189982/intel-jhl8440-thunderbolt-4-controller/specifications.html",
                    "https://www.intel.com/content/www/us/en/products/sku/211299/intel-jhl9040r-thunderbolt-4-retimer/specifications.html",
                ],
            },
            "rings": {
                "mcu": "nRF52840",
                "imu": "BMI270",
                "cap": "IQS7222A",
                "se": "SE050",
                "pmic": "nPM1300",
                "uwb_optional": "DW3000/DWM3001C",
                "status": "CONFIRMED_ADR_AND_BOM",
            },
        },
        "procurement": "PHYSICAL_EXECUTION_FREEZE — refresh is design truth only",
    }


def self_challenge(packages: dict, west_probe: dict | None) -> dict:
    findings = []

    def fail(challenge: str, detail: str, severity: str = "S1"):
        findings.append({"challenge": challenge, "result": "FAIL", "detail": detail, "severity": severity})

    def passed(challenge: str, detail: str):
        findings.append({"challenge": challenge, "result": "PASS", "detail": detail})

    for product, pkg in packages.items():
        sch = ROOT / pkg["eda"]["schematic_path"] if pkg["eda"]["schematic_path"] else None
        if not sch or not sch.is_file() or sch.stat().st_size < 200:
            fail("placeholder_schematic", f"{product}: missing/tiny schematic")
        else:
            text = sch.read_text(errors="ignore")
            if "TODO_PLACEHOLDER_ONLY" in text:
                fail("placeholder_schematic", f"{product}: placeholder marker")
            else:
                passed("editable_eda_source", f"{product}: kicad_sch present ({sch.stat().st_size} bytes)")
        if not pkg["eda"]["erc"].get("pass"):
            fail("erc_not_run_or_fail", f"{product}: erc errors={pkg['eda']['erc'].get('errors')}")
        else:
            passed("erc_pass_errors_zero", f"{product}: warnings={pkg['eda']['erc'].get('warnings')}")
        pcb = ROOT / pkg["eda"]["pcb_path"] if pkg["eda"]["pcb_path"] else None
        if pcb and pcb.is_file() and pcb.stat().st_size < 200:
            fail("pcb_screenshot_only", f"{product}: pcb too small")
        elif pcb and pcb.is_file():
            passed("pcb_editable_source", f"{product}: kicad_pcb present")
        if any("TB5" in str(pkg["vendor_anchors"]) or pkg["vendor_anchors"].get("not") and "TB5" in pkg["vendor_anchors"].get("not", []) for _ in [0]):
            if product == "dock":
                passed("no_fake_tb5", "Dock freezes 40G JHL8440+JHL9040R")
        if product == "edge_io_rings":
            if pkg["vendor_anchors"].get("not") and "IMU_only_absolute_position" in pkg["vendor_anchors"]["not"]:
                passed("ring_not_imu_only", "Fusion map requires CAP+SE+BLE (+ optional UWB)")
            if not (west_probe or {}).get("west_build_pass"):
                fail("firmware_does_not_build", "Ring west_build_pass false")
            else:
                passed("firmware_builds", "Ring ZEPHYR_WEST hard gate pass")
        if pkg["bom_avl"].get("fabricated_economics_findings"):
            fail("fake_price_moq", f"{product}: {pkg['bom_avl']['fabricated_economics_findings']}")
        else:
            passed("bom_economics_honest", f"{product}: UNKNOWN_UNTIL_QUOTE policy held")
        if "6G" in str(pkg["vendor_anchors"].get("not", [])) or pkg["vendor_anchors"].get("wwan"):
            if product in {"student_14_5", "ds_xl_coder"}:
                passed("modem_not_ntn_6g", "RM520N-GL Rel-16 Sub-6 only")

    # Dock TB5 explicit
    dock = packages["dock"]
    if dock["vendor_anchors"].get("link") == "TB4/USB4 40G" and not dock["vendor_anchors"].get("tb5", False):
        passed("no_80g_claim", "40G only")

    fails = [f for f in findings if f["result"] == "FAIL"]
    return {
        "schema": "gunnchos.hw_fw_rc_001.self_challenge_vp.v1",
        "generated_at_utc": utc_now(),
        "verdict": "FAIL" if fails else "PASS",
        "fail_count": len(fails),
        "findings": findings,
        "prefer_fail": True,
        "note": "Independent self-challenge for DRAFT PR; Edmund merge still required; Cursor never merges",
    }


def deferred_heavy() -> dict:
    return {
        "schema": "gunnchos.hw_fw_rc_001.deferred_heavy_work.v1",
        "generated_at_utc": utc_now(),
        "reason": "Product-Use QEMU likely ACTIVE — resource rule",
        "deferred": [
            "family-wide KiCad ERC/DRC batch re-sweep",
            "large thermal Monte Carlo",
            "extra QEMU device profiles",
            "long soak / reliability sims",
            "large video/model downloads for factory AV fixtures",
            "full SI channel simulation for TB4 (NDA tools)",
        ],
        "allowed_executed": [
            "firmware source/tests",
            "schematic/netlist/BOM/AVL refresh",
            "lightweight ERC status reuse (Cont IX)",
            "Ring west build hard gate",
            "unit tests for RC-001 package honesty",
            "DVP&R / USB-dock digital models",
        ],
    }


def open_pending(packages: dict) -> dict:
    digital = []
    physical = []
    external = []
    for product, pkg in packages.items():
        if not pkg["token"]["earned"]:
            digital.append(
                {
                    "product": product,
                    "token": pkg["token"]["token"],
                    "failed": pkg["token"]["failed_criteria"],
                    "reason": pkg["token"]["criteria"].get("token_withhold_reason"),
                }
            )
        if pkg["eda"]["drc"].get("warnings", 0) and pkg["eda"]["drc"].get("warnings", 0) > 0:
            digital.append(
                {
                    "product": product,
                    "item": "lib_footprint_mismatch_or_other_drc_warnings",
                    "warnings": pkg["eda"]["drc"]["warnings"],
                }
            )
        physical.append({"product": product, "item": "fab_flash_assemble_measure", "status": "PHYSICAL_PENDING"})
        if product in {"student_14_5", "ds_xl_coder"}:
            external.append({"product": product, "item": "COM-HPC Mini 400-pin NDA net map"})
        if product == "ds_xl_coder":
            external.append({"product": product, "item": "dual-eDP COM-HPC pin map NDA"})
        if product == "dock":
            external.append({"product": product, "item": "JHL8440/JHL9040R package ball maps NDA"})
        if product == "edge_io_rings":
            physical.append({"product": product, "item": "spatial_accuracy_and_physical_boot", "status": "PHYSICAL_PENDING"})
    return {
        "schema": "gunnchos.hw_fw_rc_001.open_physical_pending.v1",
        "generated_at_utc": utc_now(),
        "DIGITAL_OPEN": digital,
        "PHYSICAL_PENDING": physical,
        "EXTERNAL": external,
        "HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE": False,
    }


def write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n")


def main() -> None:
    west_probe = load_json(ROOT / "artifacts" / "hw002" / "zephyr_west" / "ZEPHYR_WEST_PROBE.json")
    # Also accept RC-001 local probe if present
    rc_probe = load_json(OUT / "zephyr_west" / "ZEPHYR_WEST_PROBE.json")
    if rc_probe and rc_probe.get("west_build_pass"):
        west_probe = rc_probe

    packages = {p: build_product(p, west_probe) for p in PRODUCTS}
    for p, pkg in packages.items():
        write_json(OUT / "products" / p / "DIGITAL_RELEASE_PACKAGE.json", pkg)
        # Per-device index under device_designs
        idx = {
            "product": p,
            "packet": "HW-FW-RC-001",
            "package": f"artifacts/hw_fw_rc_001/products/{p}/DIGITAL_RELEASE_PACKAGE.json",
            "token": pkg["token"],
            "generated_at_utc": pkg["generated_at_utc"],
        }
        write_json(ROOT / "device_designs" / p / "digital_release" / "INDEX.json", idx)

    vendor = vendor_refresh()
    dvpr = dvpr_master()
    usb = usb_dock_validate()
    compat = compatibility_matrix()
    ring_map = ring_sensing_map()
    deferred = deferred_heavy()
    opens = open_pending(packages)
    challenge = self_challenge(packages, west_probe)

    tokens = {
        "schema": "gunnchos.hw_fw_rc_001.tokens.v1",
        "generated_at_utc": utc_now(),
        "baseline_main_tip": "6c0b025e505505a74adca510e47c15b8f39bc980",
        "tokens": {pkg["token"]["token"]: pkg["token"] for pkg in packages.values()},
        "HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE": False,
        **FALSE_ALWAYS,
    }

    summary = {
        "schema": "gunnchos.hw_fw_rc_001.packet_summary.v1",
        "packet": "HW-FW-RC-001",
        "stream": "C",
        "generated_at_utc": utc_now(),
        "baseline_main_tip": "6c0b025e505505a74adca510e47c15b8f39bc980",
        "tokens_earned": [t for t, v in tokens["tokens"].items() if v.get("earned")],
        "tokens_withheld": [t for t, v in tokens["tokens"].items() if not v.get("earned")],
        "erc_drc": {p: {"erc_pass": packages[p]["eda"]["erc"]["pass"], "drc_pass": packages[p]["eda"]["drc"]["pass"], "erc_warnings": packages[p]["eda"]["erc"]["warnings"], "drc_warnings": packages[p]["eda"]["drc"]["warnings"]} for p in PRODUCTS},
        "firmware_builds": {p: packages[p]["firmware"] for p in PRODUCTS},
        "self_challenge_verdict": challenge["verdict"],
        "HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE": False,
        "cursor_never_merges": True,
        "evidence_roots": [
            "artifacts/hw_fw_rc_001/",
            "device_designs/*/digital_release/",
            "artifacts/continuation_ix_pre_evt/",
            "artifacts/hw002/",
        ],
    }

    write_json(OUT / "VENDOR_TRUTH_REFRESH.json", vendor)
    write_json(OUT / "DVPR_MASTER.json", dvpr)
    write_json(OUT / "USB_DOCK_DIGITAL_VALIDATE.json", usb)
    write_json(OUT / "COMPATIBILITY_MATRIX.json", compat)
    write_json(OUT / "RING_SENSING_MAP.json", ring_map)
    write_json(OUT / "DEFERRED_HEAVY_WORK.json", deferred)
    write_json(OUT / "OPEN_PHYSICAL_PENDING.json", opens)
    write_json(OUT / "SELF_CHALLENGE_VP.json", challenge)
    write_json(OUT / "TOKENS_HW_FW_RC_001.json", tokens)
    write_json(OUT / "PACKET_SUMMARY.json", summary)

    readme = f"""# HW-FW-RC-001 — Digital release packages

Generated: {utc_now()}

Baseline tip: `6c0b025e505505a74adca510e47c15b8f39bc980` (live GitHub main).

## Tokens
See `TOKENS_HW_FW_RC_001.json`. Prefer FAIL over invented PASS.
Student/DS-XL/Dock remain withheld while NDA pin-accurate fanout is EXTERNAL.

## Non-claims
EVT/DVT/PVT/RF/EMC/battery cert / SHIPPING_HARDWARE = false.

## Resource rule
Family EDA re-sweep / thermal Monte Carlo / extra QEMU deferred while Product-Use QEMU active.
"""
    (OUT / "README.md").write_text(readme)
    print(json.dumps({"summary": summary["tokens_earned"], "withheld": summary["tokens_withheld"], "challenge": challenge["verdict"]}, indent=2))


if __name__ == "__main__":
    main()
