import cv2 as cv

while(1):
    cap=cv.VideoCapture(0)#select your cams num for example 0 or 1 or...
    _,frame=cap.read()#read image from cam and replase in frame
    cv.imshow("cam",frame)#show pictare in a window with title
    if cv.waitKey(1) & 0xFF == ord('q'):#if press 'q' wile will break
      break