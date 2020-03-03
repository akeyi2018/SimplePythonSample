import os.path
from subprocess import call

filepath1 = "/home/pi/zippy/kurumi/peanuts_"
filepath2 = "/home/pi/zippy/kurumi/kurumi_"

#check number of 1000 
def CheckPath():
    for ct in range(1,1000):
        num = '{0:04d}'.format(ct)
        tmp = filepath2 + num + ".jpg"
        if os.path.exists(tmp) == True:
            pass
        else:
            return tmp

for ct in range(169,450):
    num = '{0:04d}'.format(ct)
    tmp = filepath1 + num + ".jpg"
    tmp2 = CheckPath()
    if os.path.exists(tmp) == True:
        cmd = "cp " + tmp + " " + tmp2
        call([cmd],shell=True)
        print(tmp2)
    else:
        pass
