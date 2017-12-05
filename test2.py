import wiringpi as pi, time
import webiopi

servo_pin = 23
waittime = 0.03

pi.wiringPiSetupGpio()

pi.pinMode(servo_pin, pi.OUTPUT)
pi.softPwmCreate(servo_pin, 0, 50)


def moveleft(pin):
    for i in range(27, 5, -1):
        time.sleep(waittime)
        pi.softPwmWrite(pin, i)

def moveright(pin):
    for i in range(5, 27, 1):
        time.sleep(waittime)
        pi.softPwmWrite(pin, i)

for i in range(3):
    moveleft(servo_pin)
    moveright(servo_pin)
    
pi.softPwmWrite(servo_pin, 0)
