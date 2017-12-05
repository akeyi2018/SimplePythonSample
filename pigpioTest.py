import sys
import time
import pigpio

NUM_GPIO = 26



pi = pigpio.pi()

if not pi.connected:
    exit()

pi.set_noise_filter(NUM_GPIO, 500, 2500)

pi.set_servo_pulsewidth(NUM_GPIO, 800)
time.sleep(0.5)
pi.set_servo_pulsewidth(NUM_GPIO, 1500)
time.sleep(0.5)
#pi.set_servo_pulsewidth(NUM_GPIO, 2300)
#time.sleep(0.5)
pi.set_servo_pulsewidth(NUM_GPIO, 0)



pi.stop
