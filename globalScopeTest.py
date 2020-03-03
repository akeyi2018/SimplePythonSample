arm = [2300, 630, 1400, 600, 1400, 1500]

def aaa(num, angle):
    global arm
    print (arm[num])
    arm[num] = angle

def bbb():
    aaa(1, 1000)

print(arm[1])
