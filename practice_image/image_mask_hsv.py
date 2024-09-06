import cv2
import numpy as np
import sys

# 1. 들판 이미지 가져오기 
# 2. 트랙바 생성
# 3. 트랙바 함수로 min, max 값 추출하기 
# 4. 추출한 색을 inRange 함수에 넣어 mask영역 지정하기 
# 5. 기존 컬러에서 hsv로 변환

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    
    mask = cv2.inRange(hsv_src, (hmin,150,0), (hmax, 255,255))
    
    # 마스크 부분만 출력하기 
    # result = cv2.bitwise_and(src, src, mask=mask)
    
    # 마스크를 반전하여 특정 색상 범위만 제외한 마스크 생성
    mask_inv = cv2.bitwise_not(mask)
    
    # 마스크를 사용하여 특정 색상 제외한 새로운 이미지 생성
    result_inv = cv2.bitwise_and(src,src, mask=mask_inv)
    # src와 src의 and 연산 
    # 원본이미지에 영향을 주지 않음 

    cv2.imshow('Trackbar', mask)
    # cv2.imshow('result', result)
    cv2.imshow('result_inv',result_inv)
    return hmin,hmax
    
def mask_print():
    cv2.imshow()
    
src = cv2.imread('data2/cropland.png')

if src is None:
    sys.exit('Image load failed!')
    
    
hsv_src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow('src', src)

cv2.namedWindow('Trackbar')
# H_min이라는 이름의 트랙바를 'Trackbar' 창에 생성 
cv2.createTrackbar('H_min', 'Trackbar', 0, 180, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 180, on_trackbar)
on_trackbar(0)
# 0을 넣는 이유는 트랙바값이 아직 변하지 않았기 때문에 초기값을 임의로 설정함 
# 다른값으로 설정해도 상관없음 


key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
    sys.exit()

