import RPi.GPIO as GPIO
import time

S = 26

span = 0.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(S,GPIO.IN)

while True:
    i = GPIO.input(S)
    if i == 1:
        print("no input signal")
        time.sleep(0.1)
    elif i == 0:
        print("Got a signal")
        time.sleep(0.1)

GPIO.cleanup()
