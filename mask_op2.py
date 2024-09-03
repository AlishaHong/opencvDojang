import numpy as np
import cv2, sys

# 이미지 불러오기
logo = cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
src = cv2.imread('data2/cat.bmp')

# 알파채널 빼고 슬라이싱
logo = logo[:,:,3]  #알파 뺴기 
print(logo.shape)

# 알파채널만 슬라이싱
mask = logo[:,:,:-1]
print(mask.shape)

h,w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]

# 마스크 연산
cv2.copyTo(logo,mask,crop)


cv2.imshow('logo',logo)
cv2.imshow('mask',mask)
cv2.imshow('src',src)
cv2.waitKey(0)
cv2.destroyAllWindows()


