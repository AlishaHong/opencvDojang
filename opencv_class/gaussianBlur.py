import cv2, sys
import numpy as np


src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')


dst1 = cv2.GaussianBlur(src,(0,0), 1)
dst3 = cv2.GaussianBlur(src,(0,0), 3)


cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst3',dst3)
cv2.waitKey()
cv2.destroyAllWindows()