from gpiozero import Servo, Button
from time import sleep

flg = 0
button = Button(20, hold_time = 0.1)

def setServoState(flg):
    servo = Servo(18)
    if flg == 0:
        servo.min()
    else:
        servo.max()
    sleep(0.2)

while True:
    button.wait_for_press()
    if flg == 0:
        flg = 1
    else:
        flg = 0
    setServoState(flg)
