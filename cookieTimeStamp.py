import picamera
import datetime
import time
from subprocess import call

d = datetime.datetime.today()

fpath = "{0}{1:02d}{2:02d}{3:02d}{4:02d}{5:02d}.jpg\
".format(d.year, d.month, d.day, d.hour,d.minute,d.second)

filename = "/home/pi/Desktop/" + fpath + ".jpg"
# Setup the camera such that it closes
print("About to take a picture")
with picamera.PiCamera() as camera:

    camera.start_preview()

    for i in range(100):
        camera.brightness = i
        time.sleep(0.2)
        
    #camera.resolution = (1280,720)
    #camera.capture(filename)
    
print("Picture taken")

timestamp = "{0}.{1:02d}.{2:02d} {3:02d}:{4:02d}:{5:02d}\
".format(d.year, d.month, d.day, d.hour,d.minute,d.second)

cmd = "/usr/bin/convert " + filename + " -pointsize 32 \
-fill blue -annotate +20+30 '" + timestamp + "' " + filename

#call([cmd],shell=True)
print("Picture has been timestamped.")
