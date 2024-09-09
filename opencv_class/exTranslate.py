import cv2, sys
import numpy as np

src = cv2.imread('data/lenna.bmp')

if src is None:
    sys.exit('image load failed')

# 이미지의 이동 변환    x->200, y->100
aff = np.array([[1,0,200],[0,1,100]], dtype=np.float32)
dst = cv2.warpAffine(src, aff, (0,0))
    
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()


