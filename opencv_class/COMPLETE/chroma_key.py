import cv2,sys
import numpy as np


# 동영상불러오기
filename1 = 'data2/woman.mp4'
filename2 = 'data2/raining.mp4'
cap1 = cv2.VideoCapture(filename1)
cap2 = cv2.VideoCapture(filename2)

hmin = 50
hmax = 70
smin = 150
smax = 255
def on_trackbar(pos):
    global hmin,hmax,smin
    hmin = cv2.getTrackbarPos('H_min', 'Frame')
    hmax = cv2.getTrackbarPos('H_max', 'Frame')
    smin = cv2.getTrackbarPos('S_min', 'Frame')
    # smax = cv2.getTrackbarPos('S_max', 'Frame')
    

if not cap1.isOpened():
    sys.exit('video1 open failed')
    
if not cap2.isOpened():
    sys.exit('video2 open failed')

framesize1 = (int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)))
framesize2 = (int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(framesize1,framesize2)


# 초당 프레임수
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

print(fps1,fps2)

# 총 프레임수 
framecount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
framecount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# 초당 몇 프레임 : 1번 동영상을 기준으로 
delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False

cv2.namedWindow('Frame')
cv2.createTrackbar('H_min', 'Frame', 46, 60, on_trackbar)
cv2.createTrackbar('H_max', 'Frame', 60, 80, on_trackbar)
cv2.createTrackbar('S_min', 'Frame', 150, 255, on_trackbar)
cv2.setTrackbarPos('H_min', 'Frame',hmin)
cv2.setTrackbarPos('H_max', 'Frame',hmax)
cv2.setTrackbarPos('S_min', 'Frame',smin)


on_trackbar(0)

ret1, frame1 = cap1.read()
hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
framecount1 = 0
while True:
    ret1,frame1 = cap1.read()
    if ret1 == False:
        break
    
    # 1번 영상이 읽혀졌고 합성시도를 할때만 2번 영상을 불러온다. 
    if do_composite:
        ret2,frame2 = cap2.read()
        if ret2 == False:
            break
        
    # hsv 색공간에서 영역을 검출해서 합성
    # hsv : hue(색)/saturation(채도)/value(명도)
    # 한 바이트로 색을 표현한다. 
    # 날씨나 시간에 따라 색이 달라진다.
    # 자율주행 시스템에서 신호등 색을 rgb 만으로 표현하는건 어려운 일이다.

        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # h : 50~70, s : 150~255, v : 0~255
        mask = cv2.inRange(hsv, (hmin,smin,0),(hmax,smax,255))
        framecount1 +=1
        if(framecount1%30 == 0):
            print(hmin,hmax,smin,smax)
        cv2.copyTo(frame2, mask, frame1)
    
    cv2.imshow('Frame', frame1)
    key = cv2.waitKey(100)
    
    
    # 스페이스 바를 눌렀을때 do_composite를 반전
    if key == ord(' '):
        do_composite = not do_composite
    # esc가 입력되면 종료
    elif key == 27:
        break
        
cap1.release()
cap2.release()

cv2.destroyAllWindows()