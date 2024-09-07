import numpy as np
import cv2, sys

# 이미지 불러오기
src = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('data2/cat.bmp')

# 알파채널 슬라이싱 (알파 채널만 추출)
mask = src[:,:,3]
print(mask.shape)

# 로고의 크기를 얻기
h, w = mask.shape[:2]
dst_crop = dst[10:10+h, 10:10+w]

# 마스크 연산
cv2.copyTo(src[:,:,:3], mask, dst_crop)  # 알파 채널이 아닌 RGB 채널을 대상으로 연산
#cv2.copyTo(src, mask, dst)

# 1. src - 스티커 같은거 
# 2. 원본이미지에서 스티커만 떼어내야 하므로 스티커를 제외한 부분만 계산
# 3. 스티커를 붙일 이미지 - 이미지의 영역중 스티커를 붙일 영역을 계산해둠
# 이미지 출력
cv2.imshow('logsrco', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

