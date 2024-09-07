import cv2
import sys
import numpy as np

# 이미지 불러오기
image = cv2.imread('data2/green_light.jpg')  # 불특정 이미지 파일 경로
if image is None:
    print('Image not found!')
    sys.exit()

# BGR에서 HSV로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 색상 범위 설정 (빨간색, 노란색, 초록색)
# 빨간색은 두 가지 범위로 나눠서 처리 (0-10, 170-180)

# hue값을 쉽게 찾기 위해 3색이 모두 담긴 신호등 이미지에서 트랙바를 사용함

lower_red1 = np.array([0, 150, 0])
upper_red1 = np.array([12, 255, 255])
lower_red2 = np.array([102, 150, 0])
upper_red2 = np.array([180, 255, 255])

lower_yellow = np.array([13, 150, 0])
upper_yellow = np.array([59, 255, 255])

lower_green = np.array([60, 150, 0])
upper_green = np.array([78, 255, 255])

# value 색이 선명한 녹색만 인정하겠다 싶으면 value 값을 제한하고 
# 희끄무리하던 거무튀튀하던 다 인정하고싶으면 0~255로 잡는다.

# 각 색상 범위에 대해 마스크 생성
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_red = mask_red1 + mask_red2  # 두 범위의 빨간색 마스크를 합침

mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# 각 마스크에서 255 값의 픽셀 수 계산
# countNonZero - 배열/이미지에서 0이 아닌 값의 개수를 세는 함수 
red_pixels = cv2.countNonZero(mask_red)
yellow_pixels = cv2.countNonZero(mask_yellow)
green_pixels = cv2.countNonZero(mask_green)

# 결과 출력
print(f"Red pixels: {red_pixels}")
print(f"Yellow pixels: {yellow_pixels}")
print(f"Green pixels: {green_pixels}")

# 가장 많은 픽셀을 가진 색상 찾기
if red_pixels > yellow_pixels and red_pixels > green_pixels:
    print("The image is mostly red.")
elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
    print("The image is mostly yellow.")
else:
    print("The image is mostly green.")

# 마스크 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Red Mask', mask_red)
cv2.imshow('Yellow Mask', mask_yellow)
cv2.imshow('Green Mask', mask_green)

key = cv2.waitKey(0)
if key == 27:
    sys.exit()

cv2.destroyAllWindows()
