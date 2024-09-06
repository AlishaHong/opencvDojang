import cv2,sys
import numpy as np


# 최종

# brightness 조절 후 
# fastNlMeansDenoisingColored로 노이즈 제거 
# 명도/채도 조절

src = cv2.imread('0906_imageFiltering/data/03.png')

dst1 = cv2.add(src, (10,10,10))
dst2 = cv2.add(src, (20,20,20))
dst3 = cv2.add(src, (30,30,30))

# cv2.imshow('brightness1', dst1)
# cv2.imshow('brightness2', dst2)
# cv2.imshow('brightness3', dst3)


# dst1번의 밝기가 마음에 들었음
# 여기에서 필터링을 하겠음 

fast_dst1 = cv2.fastNlMeansDenoisingColored(dst1,None,1,1,7,21) 

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(fast_dst1, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h, s, v = cv2.split(hsv_image)

# 채도/명도 값 줄이기
v = cv2.multiply(v, 0.75)
s = cv2.multiply(s, 0.90)

# 채널 병합 (H, S, V)
adjusted_hsv_image = cv2.merge([h, s, v])

# HSV -> BGR 변환
adjusted_bgr_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)



# 저장
cv2.imwrite('0906_imageFiltering/data/mission3_complete.png', adjusted_bgr_image)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('fast_dst1', fast_dst1)
cv2.imshow('Adjusted Saturation', adjusted_bgr_image)
cv2.waitKey()
cv2.destroyAllWindows()
