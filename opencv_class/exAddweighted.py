import cv2 
import numpy as np
import sys



src1 = cv2.imread('data2/airplane.bmp')
src2 = cv2.imread('data2/field.bmp')

alpha = 0.4
beta = 1 - alpha

dst1 = cv2.addWeighted(src1, alpha=alpha, src2= src2, beta=beta, gamma=0)    
# 알파와 베타값의 총 합은 1이어야 한다.
# 알파값을 줄이면 비행기가 투명해지고(alpha - 첫번째 이미지)
# 베타값을 줄이면 배경인 필드가 투명해진다.(beta - 두번째 이미지)
# 감마값 밝기 추가하는 상수 
    
cv2.imshow('img1', src1)
cv2.imshow('img2', src2)
cv2.imshow('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()