import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    _,frame = cap.read()
    cv.imshow("moz",frame)
    keyexite = cv.waitKey(5) & 0xFF
    if keyexite == 27:
        break

cv.destroyAllWindows()
cap.release()

