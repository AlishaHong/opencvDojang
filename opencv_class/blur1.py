import cv2, sys
import numpy as np


src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')

kernel_size = 3
kernel = (kernel_size , kernel_size)
# blur 처리
# 필터의 크기가 (3*3)/(5*5)
# 윈도우 크기가 커질수록 블러가 강하게 적용됨
# 연산량도 그만큼 늘어난다.
dst5 = cv2.blur(src, kernel)
dst3 = cv2.blur(src, kernel)

cv2.imshow('src',src)
cv2.imshow('dst5',dst5)
cv2.imshow('dst3',dst3)
cv2.waitKey()
cv2.destroyAllWindows()