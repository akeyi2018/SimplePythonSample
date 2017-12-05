import picamera

# Setup the camera such that it closes
print("About to take a picture")
with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.capture("/home/pi/Desktop/newimage.jpg")
print("Picture taken")

