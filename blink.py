import webiopi, time

GPIO = webiopi.GPIO

LEDPIN = 20

def setup():
    GPIO.setFunction(LEDPIN, GPIO.OUT)
    
    
def loop():
    GPIO.digitalWrite(LEDPIN,1)
    time.sleep(0.5)
    GPIO.digitalWrite(LEDPIN,0)
    time.sleep(0.5)
    
def destroy():
    GPIO.digitalWrite(LEDPIN,0)

