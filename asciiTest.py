import cv2

a = ord("a")
print(a)


while True:
    img = cv2.imread("/home/pi/opencv-3.2.0/samples/data/lena.jpg")
    cv2.imshow("test",img)
    if cv2.waitKey(0) & 0xff == 27:
        print("end")
        break
cv2.destroyAllWindows()



    
