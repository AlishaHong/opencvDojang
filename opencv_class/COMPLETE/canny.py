# import cv2, sys
# import numpy as np


# src = cv2.imread('data2/road.png', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     sys.exit('image load failed')



# dst = cv2.Canny(src, 64,128)
# # 이미지, 임계선1 임계선2 


# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()



import cv2
import numpy as np

deNoise = False
# 이미지를 읽어옵니다.
img = cv2.imread('data2/road.png', cv2.IMREAD_GRAYSCALE)

# 블러처리도 함께 함 
if deNoise:
# 가우시안 블러를 적용하여 노이즈 제거
    blurred_img = cv2.GaussianBlur(img, (5, 5), 1.4)

    # Canny 엣지 검출 적용 (하한 임계값 100, 상한 임계값 200)
    edges = cv2.Canny(blurred_img, 100, 200)

    # 원본 이미지와 엣지 검출 결과를 보여줍니다.
    cv2.imshow('Original Image', img)
    cv2.imshow('Canny Edges', edges)
    
# 블러처리 x 
if not deNoise:
        # Canny 엣지 검출 적용 (하한 임계값 100, 상한 임계값 200)
    edges = cv2.Canny(img, 100, 200)

    # 원본 이미지와 엣지 검출 결과를 보여줍니다.
    cv2.imshow('Original Image', img)
    cv2.imshow('Canny Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()