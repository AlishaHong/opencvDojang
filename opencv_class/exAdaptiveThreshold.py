import cv2,sys
import myLib_hist
import matplotlib.pyplot as plt


import cv2,sys
import numpy as np
import matplotlib.pyplot as plt
import myLib_hist

# opencv폴더에 임계처리 문서 확인하기 
# 유튜브 강의에도 있었음 


src = cv2.imread('data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
myLib_hist.histogram_gray(src)
# threshold 함수를 이용해서 흑과 백으로 나눈다 
# 이미지 이진화 

# threshold
ret1, src_th = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY)
ret2, src_th_inv = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY_INV)
ret3, src_th_otsu = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



# 임계값을 이미지 전체에 적용하여 처리하기 때문에 하나의 이미지에 음영이 다르면 
# 일부 영역이 모두 흰색 또는 검정색으로 보여지게 됩니다.
# 이런 문제를 해결하기 위해서 이미지의 작은 영역별로 thresholding을 하는 것입니다. 
# 이때 사용하는 함수가 cv2.adaptiveThreshold() 입니다.

# adaptive threshold
# MEAN이 노이즈가 좀 심함
src_th_MEAN = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7) 
# 노이즈가 조금 덜함 
src_th_GAUSSIAN = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7) 

# 임계값 타입 
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV - BINARY 반대 
# cv2.THRESH_TRUNC - 임계값을 넘는 픽셀 값은 임계값으로 고정
# cv2.THRESH_TOZERO - THRESH_TOZERO와 반대
# cv2.THRESH_OTSU - 자동으로 최적의 임계값을 찾음


# 적응형 임계값 
# 배경색을 감안하여 살펴봐라~ 
# cv2.ADAPTIVE_THRESH_MEAN_C
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C


cv2.imshow('src', src)
cv2.imshow('src_th', src_th)
cv2.imshow('src_th_inv', src_th_inv)
cv2.imshow('src_th_otsu', src_th_otsu)
cv2.imshow('src_th_MEAN', src_th_MEAN)
cv2.imshow('src_th_GAUSSIAN', src_th_GAUSSIAN)

cv2.waitKey()
cv2.destroyAllWindows()