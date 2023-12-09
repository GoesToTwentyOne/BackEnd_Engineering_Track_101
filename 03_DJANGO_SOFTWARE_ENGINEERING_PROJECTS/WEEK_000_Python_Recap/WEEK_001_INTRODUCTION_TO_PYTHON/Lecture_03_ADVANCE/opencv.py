import cv2
from time import *
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    cv2.imshow('mycam',frame)
    cv2.waitKey(1)
    time.sleep(3)
    break
    
