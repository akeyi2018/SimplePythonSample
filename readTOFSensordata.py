import smbus
import time

def makeuint16(lsb,msb):
    return ((msb & 0xFF) << 8) | (lsb & 0xFF)

address = 0x29
bus = smbus.SMBus(1)

def readTOFSensor():
    val1 = bus.write_byte_data(address, 0x000, 0x01)
    cnt = 0
    while(cnt < 100):
        time.sleep(0.010)
        val = bus.read_byte_data(address, 0x0014)
        if (val & 0x01):
            break
        cnt += 1

    if (val & 0x01):
        data = bus.read_i2c_block_data(address, 0x14, 12)
        distance = makeuint16(data[11],data[10])
        if (distance > 0): 
            return (str(distance/10) + "cm")
        time.sleep(66/1000000.00)
    else:
        return ("not ready")

#output 200 times of distance info.
for i in range(1,200):
    print(readTOFSensor())
    
