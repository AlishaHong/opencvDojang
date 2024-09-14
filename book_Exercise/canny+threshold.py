import cv2
import numpy as np

# 이미지를 읽어옵니다.
img = cv2.imread('data2/road.png', cv2.IMREAD_GRAYSCALE)

# 가우시안 블러를 적용하여 노이즈를 제거합니다.
blurred_img = cv2.GaussianBlur(img, (5, 5), 1.4)  # 커널 크기는 (5, 5), 표준 편차는 1.4로 설정

# 이진화를 적용합니다.
ret, img_bin = cv2.threshold(blurred_img, 200, 255, cv2.THRESH_OTSU)

# Canny 엣지 검출을 적용합니다 (이진화된 이미지에서).
edges = cv2.Canny(img_bin, 100, 200)

# 원본 이미지, 블러 처리된 이미지, 이진화된 이미지, 그리고 Canny 엣지 결과를 보여줍니다.
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', blurred_img)
cv2.imshow('Binary Image', img_bin)
cv2.imshow('Canny Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()