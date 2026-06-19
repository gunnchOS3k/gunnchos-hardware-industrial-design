# System Block Diagram

```mermaid
flowchart TB
  subgraph ecosystem [gunnchOS Ecosystem]
    S[Student 14.5]
    H[Handheld Hybrid]
    D[DS-XL Coder]
    W[Wearables Arena]
  end
  OS[gunnchOS Shell / Windows]
  S --> OS
  H --> OS
  D --> OS
  W -->|BLE| H
  OS --> Cloud[Optional sync]
  OS --> Local[Offline packs]
```
