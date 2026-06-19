# gunnchOS3k Modular Console Ecosystem — Product Requirements Document

**Status:** EVT-1 alpha product requirements — **requires engineering review**.  
**Not claimed:** certified hardware, finished OS, mass-production readiness, regulatory approval.

---

## 1. Product vision

gunnchOS3k is a modular console ecosystem built to help students learn, build, play, create, collaborate, and stay connected across school, university, work, and community life.

The product is not only a gaming device. It is a student computer, coding console, media device, learning platform, research endpoint, and community-access tool.

The system must support:

* Four years of high school use
* Any university degree path
* STEM and computer science workloads
* Creative work
* Gaming and recreation
* Streaming and media
* Offline-first learning
* Low-cost education access
* Safe youth/community use
* Repairability and long-term ownership

---

## 2. Product line

### 2.1 Student 14.5"

A laptop-adjacent student console.

**Primary use cases:** schoolwork · coding · office/productivity · web research · WSL/Linux development · streaming media · Steam gaming · AI tutor · remote learning · university coursework

**Minimum target specification:**

| Spec | Target |
|------|--------|
| Display | 14.5" FHD+ or better |
| CPU/GPU | AMD/Intel mobile APU class |
| RAM | 16 GB min · 32 GB recommended |
| Storage | 512 GB NVMe min · 1 TB recommended |
| Wireless | Wi-Fi 6E min · Bluetooth 5.2+ |
| I/O | USB-C charging + display · HDMI or USB-C dock |
| AV | Webcam + microphone |
| Security | TPM 2.0 / secure boot capable (design target) |
| Repair | Replaceable battery target · repairable storage target |

**Operating system target:** Windows 11 base · gunnchOS shell/launcher · WSL2 · Steam · browser/media · School/Developer/Play/Research modes

### 2.2 Handheld Hybrid

A PSP/Switch-style portable console.

**Primary use cases:** Steam gaming · gunnchOS games · light coding · AI tutor · deploy target from DS-XL Coder · dock to TV/projector · LAN/venue play · media streaming

**Minimum target specification:**

| Spec | Target |
|------|--------|
| Display | 7–8" 1080p |
| SoC | APU for Steam indie + low/mid PC games |
| RAM / storage | 16 GB min · 512 GB NVMe min · microSD preferred |
| Controls | Hall-effect sticks · D-pad · ABXY · bumpers · triggers · gyro/IMU |
| Audio | Stereo speakers · headphone jack |
| I/O | USB-C video out · dock support |
| Wireless | Wi-Fi 6/6E · Bluetooth 5.2+ |
| Battery | 2–4 hr gaming · 6+ hr light media/learning |

**OS target:** Windows-first · Steam Big Picture / handheld launcher · gunnchOS overlay · controller-first · school/developer/play/research profiles · safe update rollback

### 2.3 DS-XL Coder

Dual-screen handheld for building, learning, and previewing.

**Primary use cases:** code on lower screen · preview on upper · game jam · Python/JS/HTML learning · local build/run · deploy to Student 14.5" and Handheld Hybrid · offline lessons · coding meetups

**Minimum target specification:**

| Spec | Target |
|------|--------|
| Displays | Dual 7" — lower touch + optional keyboard · upper live preview |
| RAM / storage | 8 GB min (16 GB rec) · 256 GB min (512 GB rec) |
| Wireless | Wi-Fi 6 · Bluetooth 5.2+ |
| I/O | USB-C data/charging · optional snap-on keyboard |
| Mechanical | Rugged hinge · student-safe case |

**OS target:** gunnchOS Coder Mode · local editor · local web preview · Python/JS templates · one-tap deploy · offline curriculum · optional Git/GitHub sync · no always-online requirement

### 2.4 Wearables and Arena Set

Future add-on for safe, physical, community play.

**Components:** bracelet/ring tracker · haptic glove · glasses/HUD concept · BLE/UWB or approved tracking · venue beacons · charging case · arena safety controls

**Safety constraints:** no unsafe lasers · no uncontrolled public deployment · venue marshal mode · youth safety policy · wireless compliance · no biometric surveillance by default

---

## 3. User personas

| Persona | Key needs |
|---------|-----------|
| **High school student** | homework · productivity · coding · tutoring · games · videos · safe comms · offline resources · durability |
| **University CS/STEM** | VS Code · Git · Python/Java/C++ · WSL · Docker where feasible · external monitor · GPU where feasible |
| **Non-STEM university** | writing · research · presentations · streaming · notes · AI tutor · affordable reliability |
| **Educator / mentor** | class mode · lesson deploy · student-safe controls · offline content · fleet visibility · privacy-respecting telemetry |
| **Community partner** | reliable devices · easy setup · youth policies · support/warranty model · non-surveillance analytics · low-cost deployment |

See [USER_PERSONAS.md](USER_PERSONAS.md).

---

## 4. Core product requirements

### 4.1 Education

Browser learning · PDF/office · video lectures · local files · offline lessons · AI tutor · coding kits · school restrictions · accessibility

### 4.2 Development

VS Code · Git · Python · Node.js · C/C++ where feasible · WSL2 · local preview · one-tap deploy · GitHub export · templates · game jam workflows

### 4.3 Gaming

Steam · controller-first mode · gunnchOS games · local multiplayer · remapping · parental restrictions · storage management · cloud saves where licensed · offline where licenses allow

### 4.4 Media

YouTube · Netflix/Hulu via supported browser routes · speakers/headphones · external display · DRM/HDCP planning · school-safe controls

### 4.5 Security and privacy

Secure boot capable · TPM/root of trust · signed update plan · rollback · profiles/roles · encryption where feasible · privacy-preserving telemetry · no private packet capture · youth safety · parental controls · content reporting

### 4.6 Accessibility

Screen scaling · high contrast · keyboard nav · controller remapping · captions · color-blind UI · TTS planning · low-bandwidth/offline · repairability · affordability

---

## 5. Operating system requirements

See [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) — `gunnchos_device_os/` package.

### 5.1 OS strategy

**First operational version:** Windows 11 + gunnchOS launcher · WSL2 · Steam · browser/media · school/developer/play/research/coder profiles

**Future optional:** Linux/SteamOS-like handheld · education kiosk · recovery · developer images

### 5.2 Required OS modules (EVT-1 alpha)

| Module | Path |
|--------|------|
| Mode manager | `gunnchos_device_os/mode_manager.py` |
| App launcher | `gunnchos_device_os/launcher.py` |
| Profile manager | `gunnchos_device_os/profile_manager.py` |
| Parental/school controls | `gunnchos_device_os/parental_controls.py` |
| Telemetry consent | `gunnchos_device_os/telemetry_consent.py` |
| Updater | `gunnchos_device_os/updater.py` |
| Rollback | `gunnchos_device_os/rollback.py` |
| Device health | `gunnchos_device_os/device_health.py` |
| HAL | `gunnchos_device_os/hardware_abstraction.py` |
| Input mapper | `gunnchos_device_os/input_mapper.py` |
| Dock/display | `gunnchos_device_os/dock_manager.py` |
| Performance governor | `gunnchos_device_os/performance_governor.py` |
| Accessibility | `gunnchos_device_os/accessibility.py` |
| WAIKE integration | `gunnchos_device_os/waike_integration.py` |
| gunnchAI3k integration | `gunnchos_device_os/gunnchai_integration.py` |
| Steam integration | `gunnchos_device_os/steam_integration.py` |
| WSL/dev tools | `gunnchos_device_os/wsl_dev_tools.py` |

### 5.3 OS acceptance criteria

Documented in [gunnchos-device-os/docs/EVT1_OS_ACCEPTANCE_CRITERIA.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/docs/EVT1_OS_ACCEPTANCE_CRITERIA.md).

---

## 6. Hardware requirements

### 6.1 Hardware architecture

Each console: compute · RAM · storage · display · battery · charging · PMIC · Wi-Fi/BT · audio · input · USB-C · thermal · enclosure · service/repair plan

### 6.2 Manufacturing documentation

PRD · architecture · block diagrams · schematic drafts · PCB stack-up · connector map · BOM · vendor list · mechanical CAD · assembly · thermal · battery safety · regulatory matrix · DFM/DFT · EVT/DVT/PVT · CM quote · risk register

### 6.3 Hardware acceptance criteria

See [docs/HARDWARE_ACCEPTANCE_CRITERIA.md](../docs/HARDWARE_ACCEPTANCE_CRITERIA.md) — **manufacturing-candidate** gates, not met at EVT-1.

---

## 7. Product performance targets

See [PERFORMANCE_TARGETS.md](PERFORMANCE_TARGETS.md).

---

## 8. Software ecosystem

See [SOFTWARE_ECOSYSTEM.md](SOFTWARE_ECOSYSTEM.md).

---

## 9. Compliance and safety

FCC Part 15 · CE/UKCA · RoHS/REACH · UN 38.3 · IEC/UL review · module cert · charger safety · youth privacy · COPPA/CIPA awareness · open-source compliance · SBOM · security update policy

See [compliance/REGULATORY_MATRIX.md](../compliance/REGULATORY_MATRIX.md).

---

## 10. MVP scope

See [MVP_SCOPE.md](MVP_SCOPE.md).

---

## 11. First milestone — EVT-1 Alpha Device + OS Package

| Criterion | Status |
|-----------|--------|
| OS launcher + mode manager runnable locally | EVT-1 alpha |
| Hardware architecture + KiCad skeletons | EVT-1 package |
| PRD exists | this document |
| BOM + compliance + manufacturing checklist | EVT-1 package |
| Prototype vs certified clearly stated | yes |
| Demo walkthrough | see device-os `demo/` |

---

## 12. Core claim boundary

This project is moving from concept/EVT-0 toward **EVT-1**. It is **not** manufacturing-ready, certified, a finished OS, or a shipping consumer device.

**Safe claim after this pass:**

> gunnchOS3k has an EVT-1-ready product requirements package, OS alpha architecture, schematic/PCB documentation skeleton, and manufacturing-readiness roadmap for a modular student console ecosystem.
