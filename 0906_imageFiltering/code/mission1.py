import cv2,sys
import numpy as np


# 최종 : 
# fast_dst2 = cv2.fastNlMeansDenoisingColored(fast_src,None,8,8,7,21)
# sharpened_image_fast_src2_kernel2= cv2.filter2D(fast_dst2, -1, kernel_sharpening2)
# 명도/채도 조절



# median blur - 별로

src = cv2.imread('0906_imageFiltering/data/01.png')

if src is None:
    sys.exit('이미지를 불러올 수 없습니다.')
    
    
dst = cv2.medianBlur(src, 5)
dst1 = cv2.medianBlur(src, 3) 


# cv2.imshow('원본', src)
# cv2.imshow('dst_5', dst)
# cv2.imshow('dst_3', dst1)



# bilateral  별로 

bilateral_src = cv2.imread('0906_imageFiltering/data/01.png')

if src is None:
    sys.exit('image load failed')

bilateral_dst1 = cv2.bilateralFilter(bilateral_src,-1,10,5)
bilateral_dst2 = cv2.bilateralFilter(bilateral_src,10,75,75)
bilateral_dst3 = cv2.bilateralFilter(bilateral_src, 5,10,5)


# cv2.imshow('bilateral_src',bilateral_src)
# cv2.imshow('bilateral_dst1',bilateral_dst1)
# cv2.imshow('bilateral_dst2',bilateral_dst2)
# cv2.imshow('bilateral_dst3',bilateral_dst3)



# fastNlMeansDenoisingColored()
# 하늘 부분은 노이즈가 잘 제거된듯 보이지만 
# 하늘 외 부분들이 너무 블러처리되어 있음 

fast_src = cv2.imread('0906_imageFiltering/data/01.png')

fast_dst1 = cv2.fastNlMeansDenoisingColored(fast_src,None,10,10,7,21)
fast_dst2 = cv2.fastNlMeansDenoisingColored(fast_src,None,8,8,7,21)
fast_dst3 = cv2.fastNlMeansDenoisingColored(fast_src,None,5,5,7,21)

# cv2.imshow('fast_src',fast_src)
# cv2.imshow('fast_dst1',fast_dst1)
# cv2.imshow('fast_dst2',fast_dst2)
# cv2.imshow('fast_dst3',fast_dst3)


# 지피티가 알려준 커널(심하게 날카로운 느낌)
kernel_sharpening = np.array([[-1, -1, -1], 
                              [-1,  9, -1], 
                              [-1, -1, -1]])

# setosa 커널 참조
kernel_sharpening2 = np.array([[0, -1, 0], 
                              [-1,  5, -1], 
                              [0, -1, 0]])

# sharpening
sharpened_image_fast_src = cv2.filter2D(fast_src, -1, kernel_sharpening)
sharpened_image_fast_src1 = cv2.filter2D(fast_dst1, -1, kernel_sharpening)
sharpened_image_fast_src2 = cv2.filter2D(fast_dst2, -1, kernel_sharpening)
sharpened_image_fast_src3 = cv2.filter2D(fast_dst3, -1, kernel_sharpening)  
sharpened_image_fast_src3_kernel2= cv2.filter2D(fast_dst3, -1, kernel_sharpening2)
sharpened_image_fast_src2_kernel2= cv2.filter2D(fast_dst2, -1, kernel_sharpening2)  #얘가 제일 맘에듬 


# 밝기를 조금만 어둡게 
final_image = cv2.add(sharpened_image_fast_src2_kernel2, (-20,-20,-20)) 

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(sharpened_image_fast_src2_kernel2, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h, s, v = cv2.split(hsv_image)

# 채도/명도 값 줄이기
v = cv2.multiply(v, 0.65)
s = cv2.multiply(s, 0.90)

# 채널 병합 (H, S, V)
adjusted_hsv_image = cv2.merge([h, s, v])

# HSV -> BGR 변환
adjusted_bgr_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)


# 저~장
cv2.imwrite('0906_imageFiltering/data/mission1_complete.png', adjusted_bgr_image)


# 결과출력
cv2.imshow('sharpened_image_fast_src1', sharpened_image_fast_src1)
cv2.imshow('sharpened_image_fast_src2', sharpened_image_fast_src2)
cv2.imshow('sharpened_image_fast_src3', sharpened_image_fast_src3)
cv2.imshow('sharpened_image_fast_src3_kernel2', sharpened_image_fast_src3_kernel2)
cv2.imshow('sharpened_image_fast_src2_kernel2', sharpened_image_fast_src2_kernel2)  #얘가 제일 맘에듬 
cv2.imshow('Adjusted Saturation', adjusted_bgr_image)

cv2.waitKey()
cv2.destroyAllWindows()