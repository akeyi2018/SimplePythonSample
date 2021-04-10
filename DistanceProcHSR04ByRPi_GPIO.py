import time
import RPi.GPIO as GPIO

TRIG = 17
ECHO = 27
LED = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(LED, GPIO.OUT)

distance = 0

def reading(sensor):
    if sensor == 0:
        GPIO.output(TRIG,0)
        time.sleep(0.1)
        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)

        while GPIO.input(ECHO) == 0:
            soff = time.time()
        while GPIO.input(ECHO) == 1:
            son = time.time()

        timepassed = son - soff
        return timepassed * 17000
       # return timepassed * (331.50+0.606681*25)*100/2
    else:
        print ("Incorrect usonic() function varible.")

while True:
    distance = reading(0)
    if distance < 10:
        GPIO.output(LED,1)
    else:
        GPIO.output(LED,0)
    #print ("{:0.2f}cm".format(reading(0)))
    time.sleep(0.01)
