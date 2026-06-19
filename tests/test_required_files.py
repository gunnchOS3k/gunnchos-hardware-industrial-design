from pathlib import Path


def test_files_exist():
    root = Path(__file__).resolve().parents[1]
    required = [
        "product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md",
        "product/PERFORMANCE_TARGETS.md",
        "product/USER_PERSONAS.md",
        "product/MVP_SCOPE.md",
        "product/CLAIM_BOUNDARY.md",
        "architecture/SYSTEM_BLOCK_DIAGRAM.md",
        "architecture/DEVICE_COMPARISON_MATRIX.md",
        "schematics/student_14/student_14_system_block.kicad_sch",
        "bom/student_14_bom.csv",
        "bom/APPROVED_VENDOR_LIST.md",
        "compliance/REGULATORY_MATRIX.md",
        "manufacturing/MANUFACTURING_READINESS_CHECKLIST.md",
        "docs/HARDWARE_ACCEPTANCE_CRITERIA.md",
    ]
    missing = [p for p in required if not (root / p).exists()]
    assert not missing, missing
