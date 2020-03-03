import wiringpi as pi, time
import webiopi 


GPIO = webiopi.GPIO

led_pin = 20
waittime = 0.03

GPIO.setFunction(led_pin, GPIO.PWM)

ratio = 0.0
increase = 0.005

while True:
    GPIO.pwmWrite(led_pin, ratio)
    ratio += increase
    if 1.0 < ratio:
        ratio = 1.0
        increase = -increase
    if 0 > ratio:
        ratio = 0.0
        increase = -increase
    webiopi.sleep(0.01)
