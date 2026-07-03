# PhD Application Readiness

## Repository role in the PhD portfolio

This repository defines the industrial design, mechanical specifications, firmware manifests, and hardware compatibility documentation for the Device Quartet — four affordable edge-device form factors used as research benchmarks for evaluating 6G service continuity.

The devices are research form factors, not finished commercial products. They define hardware constraints (compute, memory, energy, thermal, radio interfaces) that parameterize simulation and evaluation of service-continuity methods.

## Current status

**Concept-complete** — EVT-0 industrial design specifications, firmware manifests, device profiles, and OS compatibility exports exist for all four device families. Physical hardware validation is pending.

## What is complete

- Industrial design specifications for all four device form factors
- Firmware manifests for Student 14.5", Handheld Hybrid, DS-XL Coder, and Wearables/Arena Set
- Device profile YAML definitions with compute/energy/thermal parameters
- OS validation documentation for all four devices
- Mechanical validation specifications (dimensions, materials, thermal)
- Component selection documentation
- QEMU simulation profiles

## What is prototype-pending

- Physical EVT-0 hardware builds
- Thermal validation on physical units
- RF performance measurements
- Battery life validation under real workloads
- Manufacturing-ready schematics

## What is simulation-only

- All device workload evaluation (uses QEMU profiles and emulated constraints)
- Thermal modeling (parametric, not measured)
- Battery life estimation (modeled, not measured)
- RF performance (assumed from component datasheets)

## What is ethics-gated

- Any user testing with physical devices involving human participants
- Wearable/body-area device testing on humans
- Device deployment in schools or community settings

## Metrics contributed to the research plan

- Energy consumption per device class
- Thermal envelope limits
- Compute capacity (FLOPS/memory/storage budgets)
- Device form factor constraints for workload simulation
- Hardware parameters for device emulation

## Evidence available for faculty review

- Complete EVT-0 design documentation
- Device profile YAML files with quantified parameters
- Firmware manifests showing component architecture
- Mechanical specifications with dimensions and materials
- QEMU profiles enabling software simulation without hardware

## What must not be claimed yet

- Final commercial products are complete
- Manufacturing-ready hardware exists
- Physical prototypes have been tested
- RF performance has been validated
- Thermal performance has been measured on real devices
- Hardware is 6G-ready

## Simulation and prototype fallback

All four devices can be studied through:
1. QEMU firmware simulation profiles
2. Resource-constrained VMs mimicking device compute/memory
3. Commodity hardware with artificial constraints (tc/cgroups)
4. Workload trace replay under emulated device parameters

Physical hardware is NOT required for the PhD research to proceed.

## Ethics and permissions boundary

- Technical simulation and emulation: No ethics review needed
- Physical device testing by researcher only: Likely no review needed
- Device deployment with users: Ethics review required
- Wearable testing on humans: Ethics review required
- School/community deployment: Ethics and governance required

## Definition of application-ready

This repository is application-ready when:
- All four device form factors have documented research specifications
- Each device's compute/energy/thermal constraints are quantified
- Simulation substitutes are defined for each device
- The balanced device rule is documented and enforced
- No overclaims about hardware completion exist
