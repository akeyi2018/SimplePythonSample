from pynput import keyboard
from pynput.keyboard import Key, Listener
import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
    exit()
#Robot Arm No.1 ~ No.6
arm_name = ["Camera Holder","middle","upper","right","left","base"]
arm_list = [17, 18, 27, 22, 19, 26]
arm_def_position = [2300, 630, 1400, 600, 1400, 1500]
arm_cul_position = [2300, 630, 1400, 600, 1400, 1500]

def ctrl_direct(Motor_num, position):
    pi.set_servo_pulsewidth(Motor_num, position)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(Motor_num, 0)
    time.sleep(0.2)

def setup():
    print("preparing...")
    for i in range(len(arm_list)):
        ctrl_direct(arm_list[i], arm_def_position[i])
    print("prepare is ready")

def speed(angle, currentval):
    val = abs(angle - currentval)
    if val > 900:
        times = 100
    elif val > 90:
        times = 10
    else:
        times = 1
    if (angle > currentval):
        step = 1*times
    else:
        step = -1*times
    return step

def move_Motor(arm_num, angle, speed):
    for i in range(arm_cul_position[arm_num], angle+speed, speed):
        pi.set_servo_pulsewidth(arm_list[arm_num], i)
        time.sleep(0.02)
    pi.set_servo_pulsewidth(arm_list[arm_num], 0)
    print(arm_name[arm_num] + " moved :" + str(arm_cul_position[arm_num]) + "->" + str(angle))

def angle_ctrl(arm_num, angle):
    global arm_cul_position
    step = speed(angle, arm_cul_position[arm_num])
    move_Motor(arm_num, angle, step)
    arm_cul_position[arm_num] = angle
    
def Test02():           
    angle_ctrl(4, 900)
    angle_ctrl(3, 1050)
    angle_ctrl(1, 990)

def OriginalPosition():
    for i in range(5,-1,-1):
        angle_ctrl(i, arm_def_position[i])
    
def print_current_position():
    for i in range(len(arm_name)):
        print(arm_name[i] + "'s current position : " + str(arm_cul_position[i]))
        
def on_press(key):
    global NUM_06_Current
    move_step = 50
    try:
        
        if key.char == "q":
            angle = arm_cul_position[0] + move_step 
            if (angle > 2370):
                angle = 2370
            angle_ctrl(0, angle)
        elif key.char == "w":
            angle = arm_cul_position[0] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(0, angle)
        elif key.char == "a":
            angle = arm_cul_position[1] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(1, angle)
        elif key.char == "s":
            angle = arm_cul_position[1] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(1, angle)
        elif key.char == "z":
            angle = arm_cul_position[2] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(2, angle)
        elif key.char == "x":
            angle = arm_cul_position[2] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(2, angle)
        elif key.char == "e":
            angle = arm_cul_position[3] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(3, angle)
        elif key.char == "r":
            angle = arm_cul_position[3] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(3, angle)
        elif key.char == "d":
            angle = arm_cul_position[4] + move_step
            if (angle > 2500):
                angle = 2500
            angle_ctrl(4, angle)
        elif key.char == "f":
            angle = arm_cul_position[4] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(4, angle)
        elif key.char == "c":
            angle = arm_cul_position[5] + move_step 
            if (angle > 2500):
                angle = 2500
            angle_ctrl(5, angle)
        elif key.char == "v":
            angle = arm_cul_position[5] - move_step 
            if (angle < 500):
                angle = 500
            angle_ctrl(5, angle)
        elif key.char == "p":
            print_current_position()
            
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        print_current_position()
        OriginalPosition()
        return False

setup()

with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
    
pi.stop()    
