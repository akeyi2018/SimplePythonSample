import time
import os

STEP =2
DELAY = 0.02

def setServo(pin):
    print("Set servo[" + str(pin) + "]")
    cmd = "sudo servod --p1pins=" + str(pin)
    os.system(cmd)
    time.sleep(DELAY)

def clearServo():
    print("clear all servo")
    cmd = "sudo killall servod"
    os.system(cmd)
    time.sleep(DELAY)

def pwm(pin, angle):
    print("servo[" + str(pin) + "][" + str(angle) + "]")
    cmd = "echo " + str(pin) + "=" + str(angle) + "> /dev/servoblaster"
    os.system(cmd)
    time.sleep(DELAY)

def onecircle():
    i = 0
    servo_pin = 7
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,170, STEP):
              pwm(i,j)
    
        for j in range(170,50,STEP*(-1)):
              pwm(i,j)

def grip_ctl():
    i = 0
    servo_pin = 12
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,200, STEP):
              pwm(i,j)
    
        for j in range(200,50,STEP*(-1)):
              pwm(i,j)
    clearServo(servo_pin)

def open_grip():
    i = 0
    servo_pin = 12
    setServo(servo_pin)
    for ct in range(1):
        for j in range(100,50,-10):
              pwm(i,j)
    #clearServo(servo_pin)

def close_grip():
    i = 0
    servo_pin = 12
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,250, STEP):
              pwm(i,j)
    
    #clearServo(servo_pin)

def left_ctl():
    i = 0
    servo_pin = 13
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,170, STEP):
              pwm(i,j)
    
        for j in range(170,50,STEP*(-1)):
              pwm(i,j)
    clearServo(servo_pin)
def left_up():
    i = 0
    servo_pin = 13
    setServo(servo_pin)
    for ct in range(1):
        for j in range(140,50,STEP*(-1)):
              pwm(i,j)

def left_down():
    i = 0
    servo_pin = 13
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,140, STEP):
              pwm(i,j)

def base_ctl():
    i = 0
    # Base Pin Number
    servo_pin = 11
    setServo(servo_pin)
    for ct in range(1):
        for j in range(105,200, STEP):
              pwm(i,j)
    
        for j in range(200,105,STEP*(-1)):
              pwm(i,j)

def base_left():
    i = 0
    # Base Pin Number
    servo_pin = 11
    setServo(servo_pin)
    for ct in range(1):
        for j in range(105,50, STEP*(-1)):
              pwm(i,j)
    
def base_middle():
    i = 0
    # Base Pin Number
    servo_pin = 11
    setServo(servo_pin)
    for ct in range(1):
        for j in range(50,105, STEP):
              pwm(i,j)
              
def catchAndturn():
    for i in range(5):
        base_middle()
        open_grip()
        left_down()
        close_grip()
        left_up()
        base_left()
        open_grip()
    clearServo()

catchAndturn()
