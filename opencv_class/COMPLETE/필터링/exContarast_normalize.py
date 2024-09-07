# cv2.normalize

import cv2,sys
import numpy as np

#대비 효과 


src = cv2.imread('data2/Hawkes.jpg')
# print(src.shape)    #컬러인점확인

gray_src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
# print(gray_src.shape) 

if src is None:
    sys.exit('Image load failed')

pixMin, pixMax, _, _ = cv2.minMaxLoc(gray_src)
# print(pixMin, pixMax) #113.0,213.0


# 이미지 정규화 0~255
dst = cv2.normalize(gray_src,None,0,255,cv2.NORM_MINMAX)
pixMin, pixMax, _, _ = cv2.minMaxLoc(dst)
print(pixMin, pixMax)   #0.0,255.0(정규화됨)

# 데이터 결과를 파일로 저장 
cv2.imwrite('data2/Hawkes_norm.jpg', dst)

# cv2.imshow('src',src)
cv2.imshow('gray_src',gray_src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

