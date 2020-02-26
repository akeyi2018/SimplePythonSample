import VL53L0X

tof = VL53L0X.VL53L0X()

f = open("result.txt","w")

def Measure():
    tof.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)

    distance = tof.get_distance()

    if (distance > 0):
        f.write("%d cm", distance/10)
    
    tof.stop_ranging()

#write distance from sensor to result.txt in current folder. 
Measure()
