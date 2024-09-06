import cv2, sys
import numpy as np

#cartoon filter

src = cv2.imread('data/lena.bmp')

if src is None:
    sys.exit('image load failed')

dst = cv2.bilateralFilter(src,-1,10,5)
dst2 = cv2.bilateralFilter(src,10,75,75)
dst3 = cv2.bilateralFilter(src, 5,10,5)


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)

cv2.waitKey()
cv2.destroyAllWindows()