# 화소접근 : 컬러영상 (bgr) / 채널접근

import cv2

img = cv2.imread('data/lena.jpg')
img[100,200] = [255,0,0]
print(img[100,200:210]) # 100,200은 블루로 변경되었고 그 외 부분은 원래 컬러값이 출력됨

img[100:400, 200:300] = [255,0,0]

# img[100:400, 200:300, 0] == 255 # b채널을 255 로 변경
# img[100:400, 300:400, 1] == 255 # g채널을 255 로 변경
# img[100:400, 400:500, 2] == 255 # r채널을 255 로 변경


cv2.imshow('img', img)
# cv2.imshow('img[100,200]', img[100,200])
cv2.waitKey()
cv2.destroyAllWindows()

