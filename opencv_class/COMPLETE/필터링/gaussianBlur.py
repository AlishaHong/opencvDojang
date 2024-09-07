import cv2, sys
import numpy as np


src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')

# 첫번째 인자 : 블러링할 이미지
# 두번째 인자 : 커널 사이즈
# 세번째 인자 : sigma(0으로 설정 시 자동으로 적절한 값 계산)
#(0,0)이 커널사이즈
dst1 = cv2.GaussianBlur(src,(0,0), 1)
dst3 = cv2.GaussianBlur(src,(0,0), 3)


cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst3',dst3)
cv2.waitKey()
cv2.destroyAllWindows()