from captureTest import capture

a = capture()
p = a.captureTest(1001)

print(p[0])
print(p[1])

arm_list = [17, 18, 27, 22, 19, 26]
step = 10
mstep = -10
for i in range(50,10+mstep,mstep):
    print(i)
print("******")
for i in range(50,100+step,step):
    print(i)
