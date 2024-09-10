import cv2,sys
import numpy as np
import matplotlib.pyplot as plt
import myLib_hist

# opencv폴더에 임계처리 문서 확인하기 
# 유튜브 강의에도 있었음 


src = cv2.imread('data2/apple_th.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
myLib_hist.histogram_gray(src)
# threshold 함수를 이용해서 흑과 백으로 나눈다 
# 이미지 이진화 
ret, src_th = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY)   # 반환값이 튜플임
print(ret)

#cv2.threshold(src, thresh, maxval, type) 입력이미지, 임계값, 임계값이상일때 적용할 값, 임계값 유형

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
cv2.waitKey()
cv2.destroyAllWindows()