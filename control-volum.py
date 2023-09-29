import cv2 as cv
import time
from subprocess import call
from cvzone.HandTrackingModule import HandDetector as HD

cap = cv.VideoCapture(2)#your cameras num
detector=HD(detectionCon=0.5,maxHands=1)#   if you want detact morthan one hand you shold edite maxhands num for example 2 or...

def handDetaction(frame):
    hand ,_ = detector.findHands(frame)
    if hand:
        hand1=hand[0]
        lmList = hand1['lmList']
        length,_,_=detector.findDistance(lmList[4][:-1],lmList[8][:-1],frame)
        toPersent(length)
    
def toPersent(num):
    maxNum=200
    persent1=num*100/maxNum
    persent=round(persent1)
    changeVolume(persent)

def changeVolume(num):
    valid = False
    current_time = time.time()
    current_time=round(current_time)
    if (5<num<100):
        if(current_time%2 is 0):
            while not valid:
                try:
                   num = int(num)
                   if (num <= 100) and (num >= 0):
                        call(["amixer", "-D", "pulse", "sset", "Master", str(num)+"%"])
                        print(f"volum is: {str(num)}%")
                        valid = True
                except ValueError:
                    pass
    elif(num<=5):
            while not valid:
                try:     
                    call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
                    print(f"volum is: 0%")
                    valid = True
                except ValueError:
                    pass
    else:
        while not valid:
                try:     
                    call(["amixer", "-D", "pulse", "sset", "Master", "100%"])
                    print(f"volum is: 100%")
                    valid = True
                except ValueError:
                    pass

while(1):
    _,frame = cap.read()
    handDetaction(frame)
    cv.imshow("hand ditaction",frame)#show on window
    keyexite = cv.waitKey(5) & 0xFF
    if keyexite == 27:
        break

cv.destroyAllWindows()
cap.release()

