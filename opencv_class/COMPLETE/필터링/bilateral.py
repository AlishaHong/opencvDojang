import cv2, sys
import numpy as np

#cartoon filter

src = cv2.imread('data/lena.bmp')

if src is None:
    sys.exit('image load failed')

# 양방향 필터(bilateral filter)를 적용
# d: 필터 직경 (필터링에 사용할 픽셀의 이웃 범위)
# sigmaColor: 색 공간에서의 필터 표준 편차 (색 차이가 클수록 멀리 있는 픽셀을 더 많이 고려)
# sigmaSpace: 좌표 공간에서의 필터 표준 편차 (좌표가 멀수록 더 적은 영향)

dst = cv2.bilateralFilter(src,d=-1,sigmaColor=10,sigmaSpace=5)
dst2 = cv2.bilateralFilter(src,d=10,sigmaColor=75,sigmaSpace=75)


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

cv2.waitKey()
cv2.destroyAllWindows()