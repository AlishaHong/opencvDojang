import sys
import cv2
import numpy as np

# hsv중에서 h와 s를 조절해보기
# 트랙바 함수

def on_trackbar(pos):
    hmin_red = cv2.getTrackbarPos('H_min_red', 'red')
    hmax_red = cv2.getTrackbarPos('H_max_red', 'red')
    hmin_yellow = cv2.getTrackbarPos('H_min_yellow', 'yellow')
    hmax_yellow = cv2.getTrackbarPos('H_max_yellow', 'yellow')
    hmin_green = cv2.getTrackbarPos('H_min_green', 'green')
    hmax_green = cv2.getTrackbarPos('H_max_green', 'green')
    # hmin_three = cv2.getTrackbarPos('H_min_three', 'three')
    # hmax_three = cv2.getTrackbarPos('H_max_three','three')
    # inRange 함수에 적용
    dst_red = cv2.inRange(hsv_red, (hmin_red,150,50), (hmax_red,255,255))
    cv2.imshow('red', dst_red)
    dst_yellow = cv2.inRange(hsv_yellow, (hmin_yellow,50,50), (hmax_yellow,255,255))
    cv2.imshow('yellow', dst_yellow)    
    dst_green = cv2.inRange(hsv_green, (hmin_green,50,50), (hmax_green,255,255))
    cv2.imshow('green', dst_green)
    
    print(dst_red,dst_yellow,dst_green)


red = cv2.imread('data2/red_light.jpg')
if red is None:
    sys.exit('red load failed!')

yellow = cv2.imread('data2/yellow_light.jpg')
if yellow is None:
    sys.exit('yellow load failed!')
    
green = cv2.imread('data2/green_light.jpg')
if green is None:
    sys.exit('green load failed!')
    
# 색상의 범위를 bgr에서 hsv로 변경

hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기위해 트랙바 창을 먼저 생성
cv2.namedWindow('red')
cv2.namedWindow('yellow')
cv2.namedWindow('green')

cv2.imshow('red',red)
cv2.imshow('yellow',yellow)
cv2.imshow('green',green)

# 트랙바를 생성
cv2.createTrackbar('H_min_red', 'red', 0, 180, on_trackbar)
cv2.createTrackbar('H_max_red', 'red', 0, 180, on_trackbar)
cv2.createTrackbar('H_min_yellow', 'yellow', 0, 180, on_trackbar)
cv2.createTrackbar('H_max_yellow', 'yellow', 0, 180, on_trackbar)
cv2.createTrackbar('H_min_green', 'green', 0, 180, on_trackbar)
cv2.createTrackbar('H_max_green', 'green', 0, 180, on_trackbar)
on_trackbar(0)


key = cv2.waitKey(0)
if key == 27 :
    sys.exit()
    
cv2.destroyAllWindows()


# 노란불은 가운데가 많이 밝아서 s도 함께 조절해야할것같다.
