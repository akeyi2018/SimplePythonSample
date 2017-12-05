from pynput import keyboard
from pynput.keyboard import Key, Listener
import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
    exit()
GRIPPER = 18
GRIPPER_POSITION = 1500

LEFT_ARM = 27
LEFT_ARM_POSITION = 500

BASE = 17
BASE_POSITION = 1000

def gotohome():
    pi.set_servo_pulsewidth(GRIPPER, 1500)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(GRIPPER, 0)
    time.sleep(0.2)
    pi.set_servo_pulsewidth(LEFT_ARM, 500)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(LEFT_ARM, 0)
    time.sleep(0.2)
    pi.set_servo_pulsewidth(BASE, 1000)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(BASE, 0)
    time.sleep(0.2)

def setup():
    pi.set_servo_pulsewidth(GRIPPER, GRIPPER_POSITION)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(GRIPPER, 0)
    time.sleep(0.2)
    pi.set_servo_pulsewidth(LEFT_ARM, LEFT_ARM_POSITION)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(LEFT_ARM, 0)
    time.sleep(0.2)
    pi.set_servo_pulsewidth(BASE, BASE_POSITION)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(BASE, 0)
    time.sleep(0.2)

def ctrl_Gripper(angle):
    global GRIPPER_POSITION
    pi.set_servo_pulsewidth(GRIPPER, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(GRIPPER, 0)
    GRIPPER_POSITION = angle
    print(angle)

def ctrl_LeftArm(angle):
    global LEFT_ARM_POSITION
    pi.set_servo_pulsewidth(LEFT_ARM, angle)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(LEFT_ARM, 0)
    LEFT_ARM_POSITION = angle
    print(angle)
    
def on_press(key):
    global GRIPPER_POSITION, LEFT_ARM_POSITION
    
    try:
        if key.char == "c":
            angle = GRIPPER_POSITION + 30
            if (angle > 2300):
                angle = 2300
            ctrl_Gripper(angle)
        elif key.char == "o":
            angle = GRIPPER_POSITION - 30
            if (angle < 500):
                angle = 500
            ctrl_Gripper(angle)
        elif key.char == "g":
            angle = LEFT_ARM_POSITION + 30
            if (angle > 1500):
                angle = 1500
            ctrl_LeftArm(angle)
            
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        
        return False

setup()
with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    
gotohome()
pi.stop()    

    


