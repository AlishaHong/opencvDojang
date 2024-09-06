import cv2, sys
import numpy as np


src = cv2.imread('data2/noise.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')



dst = cv2.medianBlur(src, 3)    # 효과적
dst1 = cv2.bilateralFilter(src,10,50,50)
# 이미지, 커널크기 


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()