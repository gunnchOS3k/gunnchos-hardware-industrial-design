# Composite structure — current

Nested parts of one first-party SKU as represented **digitally**. Example: Handheld Hybrid (public SoM pinout). Other SKUs share the same outer ports with different inner compute (COM-HPC or nRF or dock controllers).

```mermaid
flowchart TB
  subgraph handheld [handheld_hybrid digital composite]
    subgraph mech [Mechanical]
      SCAD[cad/openscad/handheld_hybrid.scad]
      STL[exports/stl/handheld_hybrid_placeholder.stl]
    end
    subgraph elec [Electrical]
      SCH[device_designs/handheld_hybrid/kicad]
      TREE[electrical/power_tree.yaml]
      BOM[bom/assembly_bom.csv]
      ICD[docs/som_carrier_icd.md]
    end
    subgraph fw [Firmware contracts]
      MAN[firmware/manifests/handheld_hybrid_firmware_manifest.yaml]
      IF[firmware/interfaces]
    end
    subgraph osx [OS export]
      YAML[os_compatibility/device_class_exports/handheld_hybrid_os_export.yaml]
    end
  end
  SOM[Radxa RM121-D8E32 BOM SoT]
  SOM --- ICD
  SCH --- TREE
  BOM --- SOM
  YAML --- MAN
```

Ports to the environment: USB-C (VBUS), debug UART, optional WWAN footprint, OS profile name `handheld_hybrid`. NDA COM-HPC internals are **not** part of this composite.
