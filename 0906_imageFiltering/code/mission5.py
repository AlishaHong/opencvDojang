import cv2,sys
import numpy as np


# 최종

# brightness 조절
# 명도/채도 조절

# 샤프닝 

src = cv2.imread('0906_imageFiltering/data/05.png')
src_hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

dst1 = cv2.add(src, (-50,-50,-50)) 
dst2 = cv2.add(src, (-30,-30,-30)) 
dst3 = cv2.add(src, (-10,-10,-10)) 

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(dst3, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h, s, v = cv2.split(hsv_image)

# 채도/명도 값 줄이기
v = cv2.multiply(v, 0.70)
s = cv2.multiply(s, 0.90)

# 채널 병합 (H, S, V)
adjusted_hsv_image = cv2.merge([h, s, v])

# HSV -> BGR 변환
adjusted_bgr_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)

# 저장
cv2.imwrite('0906_imageFiltering/data/mission5_complete.png', adjusted_bgr_image)

# 출력하기
cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('Adjusted Saturation', adjusted_bgr_image)

cv2.waitKey()
cv2.destroyAllWindows()