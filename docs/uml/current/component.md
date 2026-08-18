# Component — current

Components are **files and packages in this repo**, plus the OS sibling contract. There is no factory API.

```mermaid
flowchart TB
  README[README.md]
  DMR[DIGITAL_MANUFACTURING_READINESS.md]
  PKT[docs/packets]
  UML[docs/uml]
  CAD[cad/openscad]
  BOM[bom + device_designs/*/bom]
  EDA[device_designs/*/kicad]
  PWR[device_designs/*/electrical]
  FW[firmware]
  FWI[firmware_os_interface]
  OSC[os_compatibility]
  RFQ[manufacturing/rfq]
  VAL[scripts/validate_digital_manufacturing.py]
  EDACHK[scripts/run_supervisor_eda_checks.sh]
  CI[.github/workflows]
  README --> DMR
  DMR --> PKT
  DMR --> CAD
  DMR --> BOM
  DMR --> EDA
  DMR --> FW
  OSC --> FWI
  OSC --> FW
  PWR --> EDA
  RFQ --> DMR
  VAL --> DMR
  VAL --> UML
  EDACHK --> EDA
  EDACHK --> CAD
  CI --> VAL
```

OS sibling: `gunnchos-device-os` consumes `os_compatibility/device_class_exports/` as profile mirrors only.
