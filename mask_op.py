import numpy as np
import cv2, sys

# 이미지 불러오기
src = cv2.imread('data2/airplane.bmp')
mask = cv2.imread('data2/mask_plane.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('data2/field.bmp')

# 마스크 연산
cv2.copyTo(src,mask,dst)

cv2.imshow('mask',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


