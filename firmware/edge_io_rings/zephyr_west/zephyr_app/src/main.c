/*
 * HW-FW-RC-001 / HW-002 Ring Zephyr west probe — nRF52840 digital build gate.
 * PHYSICAL_EXECUTION_FREEZE: not flashed to physical ring.
 *
 * Sensing policy (ADR-FP-008): NOT IMU-only absolute position.
 * Required modalities: BMI270 + IQS7222A + SE050 + BLE (nRF52840).
 * Optional: DW3000/DWM3001C UWB. Fusion requires >=2 modalities + confidence.
 * Full drivers remain in edge-io-measurement-node; this app proves west build.
 */
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/printk.h>

LOG_MODULE_REGISTER(hw_fw_rc001_ring_west, LOG_LEVEL_INF);

enum ring_modality {
	RING_MOD_IMU = 1 << 0,
	RING_MOD_CAP = 1 << 1,
	RING_MOD_SE = 1 << 2,
	RING_MOD_BLE = 1 << 3,
	RING_MOD_UWB = 1 << 4,
};

static bool ring_confidence_ok(uint32_t mods, int confidence_pct)
{
	/* Destructive actions require multi-modal presence + confidence gate. */
	const uint32_t required = RING_MOD_IMU | RING_MOD_CAP | RING_MOD_BLE;
	int bits = 0;

	for (uint32_t m = mods; m; m >>= 1) {
		bits += (int)(m & 1U);
	}
	return ((mods & required) == required) && (bits >= 2) && (confidence_pct >= 70);
}

int main(void)
{
	const uint32_t mods = RING_MOD_IMU | RING_MOD_CAP | RING_MOD_SE | RING_MOD_BLE;
	const int confidence = 80;

	LOG_INF("HW-FW-RC-001 ring Zephyr west probe (nRF52840 digital)");
	printk("RING_ZEPHYR_WEST_BUILD_PROBE_OK\n");
	printk("RING_FUSION_POLICY multimodal_not_imu_only\n");
	printk("RING_ACTION_MAP pointer,click,text,delete,shortcut,gaming\n");
	printk("RING_SPATIAL_ACCURACY PHYSICAL_PENDING\n");
	printk("RING_CONFIDENCE_GATE %s\n",
	       ring_confidence_ok(mods, confidence) ? "PASS_DIGITAL" : "FAIL");

	while (1) {
		k_msleep(1000);
	}
	return 0;
}
