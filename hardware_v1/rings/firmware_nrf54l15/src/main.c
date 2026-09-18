#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(rings_main, LOG_LEVEL_INF);

extern int rings_ble_start(void);
extern int rings_imu_haptic_init(void);

int main(void)
{
        LOG_INF("gunnchOS rings nRF54L15 digital stub");
        (void)rings_imu_haptic_init();
        (void)rings_ble_start();
        while (1) {
                k_sleep(K_SECONDS(1));
        }
        return 0;
}
