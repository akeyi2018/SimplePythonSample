import webiopi
import wiringpi as pi, time

A = 17
B = 27
C = 22
D = 26
LED_BLUE = 20
LED_GREEN = 25
S_INPUT = 8

timespan = 0.001

def setup():
    pi.wiringPiSetupGpio()
    pi.pinMode(A, pi.OUTPUT)
    pi.pinMode(B, pi.OUTPUT)
    pi.pinMode(C, pi.OUTPUT)
    pi.pinMode(D, pi.OUTPUT)
    pi.pinMode(LED_BLUE, pi.OUTPUT)
    pi.pinMode(LED_GREEN, pi.OUTPUT)
    pi.pinMode(S_INPUT, 0)
    pi.wiringPiISR(S_INPUT, pi.INT_EDGE_BOTH, my_int())
    
    
def test001():    
    pi.digitalWrite(LED_BLUE,1)
    time.sleep(0.5)
    pi.digitalWrite(LED_BLUE,0)
    time.sleep(0.5)
    
def test002(ct):
    for i in range(ct):
        pi.digitalWrite(LED_BLUE,1)
        time.sleep(0.5)
        pi.digitalWrite(LED_BLUE,0)
        time.sleep(0.5)
   
def stop():
    print("stop")
    pi.digitalWrite(LED_BLUE,0)
    time.sleep(0.5)

def my_int():
   # test001()
   # print("Receiving...")
    return True

#@webiopi.macro
def roll():
    while True:
        if pi.digitalRead(S_INPUT) == pi.HIGH:
            test001()	    
		
#@webiopi.macro
def stop2():
    #pi.digitalWrite(S_INPUT, 1)
    while True:
        time.sleep(1)
        print(pi.digitalRead(S_INPUT))
        #pi.wiringPiISR(S_INPUT, pi.INT_EDGE_BOTH, my_int())
        #pi.wiringPiISR(S_INPUT, 2, my_int())
        #stop()

    print("stop....")

setup()
roll()
#stop2()




