import picamera
import time

# Setup the camera such that it closes
print("About to take a picture")
with picamera.PiCamera() as camera:
    camera.start_recording("/home/pi/Desktop/pythonVideo.h264")
    time.sleep(5)
    camera.stop_recording()
    #camera.capture("/home/pi/Desktop/newimage.jpg")
    
print("Picture taken")
