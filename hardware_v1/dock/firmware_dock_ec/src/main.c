#include <stdint.h>
/* Bare-metal / Zephyr portability stub — PD IRQ + hub reset + thermal poll */
volatile uint32_t dock_ticks;
int main(void) {
  for (;;) { dock_ticks++; }
  return 0;
}
