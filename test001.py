import RPi.GPIO as GPIO
import time

S = 23

span = 0.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(S,GPIO.OUT)

#while True:
GPIO.output(S,GPIO.HIGH)
time.sleep(3)
GPIO.output(S,GPIO.LOW)

GPIO.cleanup()
