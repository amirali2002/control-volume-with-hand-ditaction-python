import cv2 as cv
import time
from subprocess import call
import os
from cvzone.HandTrackingModule import HandDetector as HD
#mediapipe
maxNum=200
cap = cv.VideoCapture(0)#your cameras num
detector=HD(detectionCon=0.5,maxHands=1)#   if you want detact morthan one hand you shold edite maxhands num for example 2 or...
while(1):
    _,frame = cap.read()
    hand , img = detector.findHands(frame)
    if hand:
        hand1 = hand[0]
        lmList = hand1['lmList']
        length,info,_=detector.findDistance(lmList[4][:-1],lmList[8][:-1],frame)
        persent1=length*100/maxNum
        persent=round(persent1)
        valid = False
        current_time = time.time()
        current_time=round(current_time)
        if (persent<100):
            if(current_time%2 is 0):
                while not valid:
                    try:
                        persent = int(persent)
                        if (persent <= 100) and (persent >= 0):
                            call(["amixer", "-D", "pulse", "sset", "Master", str(persent)+"%"])
                            #os.system("cls")
                            print(f"volum is: {str(persent)}%")
                            valid = True
                    except ValueError:
                        pass
    cv.imshow("hand ditaction",frame)#show on window
    keyexite = cv.waitKey(5) & 0xFF
    if keyexite == 27:
        break

cv.destroyAllWindows()
cap.release()

