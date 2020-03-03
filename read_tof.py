import smbus
import struct
import time

def makeuint16(lsb,msb):
    return ((msb & 0xFF) << 8) | (lsb & 0xFF)

def VL53L0x_decode_vcsel_period(vcsel_period_reg):
    vcsel_period_pclks = (vcsel_period_reg + 1) << 1
    return vcsel_period_pclks

address = 0x29

bus = smbus.SMBus(1)

val1 = bus.read_byte_data(address, 0x00c2)

print ("revisiong ID:" + hex(val1))

val1 = bus.read_byte_data(address, 0x00c0)

print("Device ID:" + hex(val1))

val1 = bus.read_byte_data(address, 0x0050)

print("PRE_RANGE_CONFIG_VCSEL_PERIOD:" + hex(val1))

val10 = VL53L0x_decode_vcsel_period(val1)

print("decode:" + str(val10))

val1 = bus.read_byte_data(address, 0x0070)
print("FINAL_RANGE_CONFIG_VCSEL_PERIOD:" + hex(val1))
val10 = VL53L0x_decode_vcsel_period(val1)
print("decode:" + str(val10))

val1 = bus.write_byte_data(address, 0x000, 0x01)

cnt = 0

while(cnt < 100):
    time.sleep(0.010)
    val = bus.read_byte_data(address, 0x0014)
    if (val & 0x01):
        break
    cnt += 1

if (val & 0x01):
    print("ready")
else:
    print("not ready")

data = bus.read_i2c_block_data(address, 0x14, 12)
print (data)
print ("ambient count " + str(makeuint16(data[7],data[6])))
print ("signal count " + str(makeuint16(data[9],data[8])))    
print ("distance " + str(makeuint16(data[11],data[10])))

devicerangestatusInternal = ((data[0] & 0x78) >> 3)
print (devicerangestatusInternal)

def read_tof():
    word_data = bus.read_word_data(0x29,0x00)
    #data = (word_data & 0xff00) >>8 | (word_data & 0xff) <<8
    #data = data >> 3
    return word_data

#this is original sample   
while True:
    inputVal = read_tof()
    print(str(inputVal))
    time.sleep(1)
