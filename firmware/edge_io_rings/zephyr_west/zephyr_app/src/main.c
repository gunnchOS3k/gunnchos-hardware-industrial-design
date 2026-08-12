/*
 * HW-002 Ring Zephyr west probe — nRF52840 digital build gate.
 * PHYSICAL_EXECUTION_FREEZE: not flashed to physical ring.
 * Full fusion drivers remain in edge-io-measurement-node; this app proves
 * hardware-repo west workspace can execute a real `west build`.
 */
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/printk.h>

LOG_MODULE_REGISTER(hw002_ring_west, LOG_LEVEL_INF);

int main(void)
{
	LOG_INF("HW-002 ring Zephyr west probe boot (nRF52840 digital)");
	printk("RING_ZEPHYR_WEST_BUILD_PROBE_OK\n");
	while (1) {
		k_msleep(1000);
	}
	return 0;
}
