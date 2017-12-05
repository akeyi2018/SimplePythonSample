import time
import os
import smbus
import subprocess

STEP = 1
DELAY = 0.02


RIGHT_SERVO = 0
BASE_SERVO = 1
GRIP_SERVO = 2
LEFT_SERVO = 3

def setServo():
    #print("Set servo")
    cmd = "sudo servod --p1pins=7,11,12,13"
    subprocess.call(cmd, shell=True)
    time.sleep(DELAY)
    cmd = "echo 2=100 > /dev/servoblaster"
    subprocess.call(cmd, shell=True)
    time.sleep(DELAY)

def clearServo():
    #print("clear all servo")
    cmd = "sudo killall servod"
    subprocess.call(cmd, shell=True)
    time.sleep(DELAY)

def pwm(pin, angle):
    
    cmd = "%u=%u\n" % (pin,angle)
    with open("/dev/servoblaster", "wb") as f:
        f.write(cmd.encode())
        time.sleep(DELAY)

def pwm2(angle):
    
    cmd = "P1-12=+%u\n" % (angle)
    print(cmd)
    with open("/dev/servoblaster", "wb") as f:
        f.write(cmd.encode())
        time.sleep(DELAY)

def pwm3(angle):
    
    cmd = "P1-12=-%u\n" % (angle)
    print(cmd)
    with open("/dev/servoblaster", "wb") as f:
        f.write(cmd.encode())
        time.sleep(DELAY)
        
def grip_ctl():
    start = 120
    end = 230
    setServo()
    for j in range(130):
        pwm2(1)
        time.sleep(0.02)
    
    for j in range(130):
        pwm3(1)
        time.sleep(0.02)
    clearServo()

grip_ctl()
