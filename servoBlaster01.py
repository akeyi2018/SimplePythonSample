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

DISTANCE = 0
address = 0x29
bus = smbus.SMBus(1)

def makeuint16(lsb,msb):
    return ((msb & 0xFF) << 8) | (lsb & 0xFF)

def readTOFSensor():
    try:
        val1 = bus.write_byte_data(address, 0x000, 0x01)
    except OSError as err:
        print("ERROR In Write address:[0]".format(err))
        time.sleep(0.5)
        return "OSERROR=1"
    cnt = 0
    while(cnt < 100):
        time.sleep(0.010)
        try:
            val = bus.read_byte_data(address, 0x0014)
        except OSError:
            time.sleep(0.5)
            return "OSERROR=2"
        if (val & 0x01):
            break
        cnt += 1

    if (val & 0x01):
        try:        
            data = bus.read_i2c_block_data(address, 0x14, 12)
        except OSError:
            time.sleep(0.5)
            return "OSERROR=3"
        global DISTANCE
        DISTANCE = makeuint16(data[11],data[10])
        if (DISTANCE > 0): 
            return (str(DISTANCE/10) + "cm")
        else:
            return("")
    else:
        return ("not ready")

def setServo():
    #print("Set servo")
    cmd = "sudo servod --p1pins=7,11,12,13"
    subprocess.call(cmd, shell=True)
    time.sleep(DELAY)

def clearServo():
    #print("clear all servo")
    cmd = "sudo killall servod"
    subprocess.call(cmd, shell=True)
    time.sleep(DELAY)

def pwm(pin, angle):
    #print("servo[" + str(pin) + "][" + str(angle) + "]")
    cmd = "%u=%u\n" % (pin,angle)
    with open("/dev/servoblaster", "wb") as f:
        f.write(cmd.encode())
        time.sleep(DELAY)

def turn(pin, angle):
    if (pin == 0):
        cmd = "P1-7=+%u\n" % (angle)
    elif (pin == 1):
         cmd = "P1-11=+%u\n" % (angle)
    elif (pin == 2):
         cmd = "P1-12=%u\n" % (angle)
    else:
         cmd = "P1-13=%u\n" % (angle)

    print(cmd)    
    with open("/dev/servoblaster", "wb") as f:
        f.write(cmd.encode())
        time.sleep(DELAY)
    

def right_ctl():
    start = 50
    end = 180
    setServo()
    for j in range(start,end, STEP):
        pwm(RIGHT_SERVO, j)
    
    for j in range(end,start,STEP*(-1)):
        pwm(RIGHT_SERVO, j)
    clearServo()

def right_down():
    start = 100
    end = 180
    setServo()
    for j in range(start,end, STEP):
        pwm(RIGHT_SERVO, j)
    clearServo()

def right_up():
    start = 100
    end = 180
    setServo()
    for j in range(end,start,STEP*(-1)):
        pwm(RIGHT_SERVO, j)
    clearServo()

def grip_ctl():
    start = 120
    end = 230
    setServo()
    for j in range(start,end, STEP):
        pwm(GRIP_SERVO,j)
    
    for j in range(end,start,STEP*(-1)):
        pwm(GRIP_SERVO,j)
    clearServo()

def open_grip():
    setServo()
    for j in range(250,100,-10):
        pwm(GRIP_SERVO,j)
        
        
def close_grip():
    setServo()
    for j in range(100,250, 10):
        pwm(GRIP_SERVO,j)
    
def left_ctl():
    setServo()
    for j in range(50,150, STEP):
        pwm(LEFT_SERVO,j)
    
    for j in range(150,50,STEP*(-1)):
        pwm(LEFT_SERVO,j)
    clearServo()
    
def left_up():
    setServo()
    for j in range(150,50,STEP*(-1)):
        pwm(LEFT_SERVO,j)

def left_down():
    setServo()
    for j in range(50,150, STEP):
        pwm(LEFT_SERVO,j)

def base_ctl():
    setServo()
    for j in range(105,200, STEP):
        pwm(BASE_SERVO,j)
    
    for j in range(200,105,STEP*(-1)):
        pwm(BASE_SERVO,j)
    clearServo()

def base_right():
    setServo()
    for j in range(105,200, STEP):
        pwm(BASE_SERVO,j)
    
    for j in range(200,105,STEP*(-1)):
        pwm(BASE_SERVO,j)
    clearServo()

def base_left():
    setServo()
    for j in range(170,80, STEP*(-1)):
        pwm(BASE_SERVO,j)
    clearServo()
    
def base_middle():
    setServo()
    for j in range(80,170, STEP):
        pwm(BASE_SERVO,j)
              
def catchAndturn():
    for i in range(1):
        base_middle()
        open_grip()
        left_down()
        print(readTOFSensor())
        close_grip()
        left_up()
        base_left()
        left_down()
        open_grip()
        left_up()
    clearServo()

def setneutral():
    setServo()
    for i in range(60,50,-1):
        pwm(LEFT_SERVO, i)
        #pwm(RIGHT_SERVO, 100)
    for i in range(50,150,5):
        pwm(BASE_SERVO, i)
        time.sleep(0.01)
    clearServo()

def mesureAndMove():
    setServo()
    time.sleep(0.5)
    for j in range(50,140, STEP):
        pwm(LEFT_SERVO,j)
        print(readTOFSensor())
    clearServo()

#setneutral()
for i in range(5):
    #catchAndturn()
    grip_ctl()
    print(i)
    
