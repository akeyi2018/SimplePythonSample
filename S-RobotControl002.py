from pynput import keyboard
from pynput.keyboard import Key, Listener
import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
    exit()
#Robot Arm No.1 ~ No.6
#camera holder
NUM_01 = 17
NUM_01_Defalt = 2300
NUM_01_Current = 2300

#middle arm
NUM_02 = 18
NUM_02_Defalt = 630
NUM_02_Current = 630

#upper arm
NUM_03 = 27
NUM_03_Defalt = 1400
NUM_03_Current = 1400

#right arm
NUM_04 = 22
NUM_04_Defalt = 600
NUM_04_Current = 600

#left arm
NUM_05 = 19
NUM_05_Defalt = 1400
NUM_05_Current = 1400

#Base Arm
NUM_06 = 26
NUM_06_Defalt = 1500
NUM_06_Current = 1500

def setup():
    #Base Arm
    pi.set_servo_pulsewidth(NUM_06, NUM_06_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_06, 0)
    time.sleep(0.2)
    #Camera Holder
    pi.set_servo_pulsewidth(NUM_01, NUM_01_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_01, 0)
    time.sleep(0.2)
    #middle arm
    pi.set_servo_pulsewidth(NUM_02, NUM_02_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_02, 0)
    time.sleep(0.2)
    #upper arm
    pi.set_servo_pulsewidth(NUM_03, NUM_03_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_03, 0)
    time.sleep(0.2)
    #right arm
    pi.set_servo_pulsewidth(NUM_04, NUM_04_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_04, 0)
    time.sleep(0.2)
    #left arm
    pi.set_servo_pulsewidth(NUM_05, NUM_05_Defalt)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_05, 0)
    time.sleep(0.2)
    print("prepare is ready")
    
def ctrl_NUM_06(angle):
    global NUM_06_Current
    pi.set_servo_pulsewidth(NUM_06, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_06, 0)
    NUM_06_Current = angle
    time.sleep(0.1)
    print(angle)

def ctrl_NUM_01(angle):
    global NUM_01_Current
    pi.set_servo_pulsewidth(NUM_01, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_01, 0)
    NUM_01_Current = angle
    time.sleep(0.1)
    print(angle)

def ctrl_NUM_02(angle):
    global NUM_02_Current
    pi.set_servo_pulsewidth(NUM_02, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_02, 0)
    NUM_02_Current = angle
    time.sleep(0.1)
    print(angle)

def ctrl_NUM_03(angle):
    global NUM_03_Current
    pi.set_servo_pulsewidth(NUM_03, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_03, 0)
    NUM_03_Current = angle
    time.sleep(0.1)
    print(angle)

def ctrl_NUM_04(angle):
    global NUM_04_Current
    pi.set_servo_pulsewidth(NUM_04, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_04, 0)
    NUM_04_Current = angle
    time.sleep(0.1)
    print(angle)

def ctrl_NUM_05(angle):
    global NUM_05_Current
    pi.set_servo_pulsewidth(NUM_05, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(NUM_05, 0)
    NUM_05_Current = angle
    time.sleep(0.1)
    print(angle)



def print_current_position():
    global NUM_01_Current, NUM_02_Current, NUM_03_Current
    global NUM_04_Current, NUM_05_Current, NUM_06_Current
    print("01:{0} *** 02:{1} *** 03:{2}".format(NUM_01_Current, NUM_02_Current, NUM_03_Current))
    print("04:{0} *** 05:{1} *** 06:{2}".format(NUM_04_Current, NUM_05_Current, NUM_06_Current))
def on_press(key):
    global NUM_06_Current
    
    try:
        if key.char == "l":
            angle = NUM_06_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_06(angle)
        elif key.char == "r":
            angle = NUM_06_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_06(angle)
        elif key.char == "q":
            angle = NUM_01_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_01(angle)
        elif key.char == "w":
            angle = NUM_01_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_01(angle)
        elif key.char == "a":
            angle = NUM_02_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_02(angle)
        elif key.char == "s":
            angle = NUM_02_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_02(angle)
        elif key.char == "z":
            angle = NUM_03_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_03(angle)
        elif key.char == "x":
            angle = NUM_03_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_03(angle)
        elif key.char == "e":
            angle = NUM_04_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_04(angle)
        elif key.char == "d":
            angle = NUM_04_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_04(angle)
        elif key.char == "c":
            angle = NUM_05_Current + 10
            if (angle > 2500):
                angle = 2500
            ctrl_NUM_05(angle)
        elif key.char == "v":
            angle = NUM_05_Current - 10
            if (angle < 500):
                angle = 500
            ctrl_NUM_05(angle)
        elif key.char == "p":
            print_current_position()
            
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        print_current_position()
        setup()
        return False

def Test01():

    pi.set_servo_pulsewidth(NUM_05, 1000)
    time.sleep(1)
    pi.set_servo_pulsewidth(NUM_05, 0)
    time.sleep(0.5)
    
    pi.set_servo_pulsewidth(NUM_04, 1400)
    time.sleep(1)
    pi.set_servo_pulsewidth(NUM_04, 0)
    time.sleep(0.5)
    
    pi.set_servo_pulsewidth(NUM_02, 1290)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_02, 0)
    time.sleep(0.5)

    global NUM_06_Current
    for i in range(9):
        angle1 = NUM_06_Current + 100
        pi.set_servo_pulsewidth(NUM_06, angle1)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(NUM_06, 0)
        time.sleep(0.1)
        NUM_06_Current = angle1


def Test02():
    global NUM_04_Current, NUM_05_Current

    for i in range(80):
        angle1 = NUM_05_Current - 10
        pi.set_servo_pulsewidth(NUM_05, angle1)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(NUM_05, 0)
        time.sleep(0.1)
        NUM_05_Current = angle1
        
        #angle2 = NUM_04_Current + 100
        #pi.set_servo_pulsewidth(NUM_04, angle2)
        #time.sleep(0.2)
        #pi.set_servo_pulsewidth(NUM_04, 0)
        #time.sleep(0.1)
        #NUM_04_Current = angle2

    for i in range(10):
        angle1 = NUM_05_Current - 10
        pi.set_servo_pulsewidth(NUM_05, angle1)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(NUM_05, 0)
        time.sleep(0.1)
        NUM_05_Current = angle1
        
        angle2 = NUM_04_Current + 10
        pi.set_servo_pulsewidth(NUM_04, angle2)
        time.sleep(0.2)
        pi.set_servo_pulsewidth(NUM_04, 0)
        time.sleep(0.1)
        NUM_04_Current = angle2
    
    #pi.set_servo_pulsewidth(NUM_02, 1290)
    #time.sleep(0.5)
    pi.set_servo_pulsewidth(NUM_02, 0)
    time.sleep(0.5)

    #pi.set_servo_pulsewidth(NUM_06, 2400)
    time.sleep(0.5)
    #pi.set_servo_pulsewidth(NUM_06, 0)
    time.sleep(0.5)
    
setup()
Test01()

with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    
pi.stop()    
