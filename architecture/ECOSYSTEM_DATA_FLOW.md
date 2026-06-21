# Ecosystem Data Flow

```mermaid
flowchart LR
  WAIKE[WAIKE / gunnchAI3k] --> OS[gunnchOS device OS]
  EdgeIO[Edge-IO nodes] --> OS
  OS --> S[Student 14.5]
  OS --> H[Handheld Hybrid]
  OS --> D[DS-XL Coder]
  OS --> W[Wearables Arena]
  H --> Steam[Steam / gaming path]
  S --> Media[Streaming / media path]
  D --> Local[Offline learning path]
```

See also [DATA_FLOW_AND_CONNECTOR_MAP.md](DATA_FLOW_AND_CONNECTOR_MAP.md).

This repository is moving from EVT-0 concept toward EVT-1 prototype RFQ package. It is not a final schematic package, not certified hardware, not FCC/CE approved, not DVT/PVT complete, and not a manufacturing release.
