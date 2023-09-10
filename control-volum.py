import cv2 as cv
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector as HD
#mediapipe
cap = cv.VideoCapture(0)#your cameras num
detector=HD(detectionCon=0.5,maxHands=1)#   if you want detact morthan one hand you shold edite maxhands num for example 2 or...
while(1):
    _,frame = cap.read()
    hand , img = detector.findHands(frame)
    if hand:
        hand1 = hand[0]
        lmList = hand1['lmList']
        length,info,_=detector.findDistance(lmList[4][:-1],lmList[8][:-1],frame)
        #40-300   0=40 100=260
        print(f"length: {str(length)}")
        #time.sleep(0.5)
    cv.imshow("hand ditaction",frame)#show on window
    keyexite = cv.waitKey(5) & 0xFF
    if keyexite == 27:
        break

cv.destroyAllWindows()
cap.release()

