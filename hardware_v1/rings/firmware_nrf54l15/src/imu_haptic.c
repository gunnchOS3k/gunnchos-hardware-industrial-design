#include <zephyr/kernel.h>
int rings_imu_haptic_init(void)
{
        /* IMU ≠ absolute pose — spatial input role preserved */
        return 0;
}
