import numpy as np
import cv2

#video capture web cam function
capture = cv2.VideoCapture(0) # '0' for 1 webcam

#if you want to load a video
#capture = cv2.VideoCapture('file name.mp4')

#while loop infinite untill user press key to quit
#ret means return and don't use return as variable
# as it is a keyword in python
#cap.read() will return the frame
while True:
    ret, frame = capture.read()
    #display the frame
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyWindowWindows()