import cv2,sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image is missing')
    

# 사용자 커널(=필터)를 생성 
# dst = cv2.filter2D(src, ddepth, kernel, anchor, delta, borderType)
# src: 입력 이미지입니다. 보통 numpy 배열로 표현됩니다.
# ddepth: 결과 이미지의 깊이(비트 단위)입니다. -1로 지정하면 입력 이미지와 동일한 깊이를 사용합니다.
# kernel: 필터링에 사용될 커널입니다. numpy 배열로 정의되며, 일반적으로 부동소수점 값으로 구성됩니다.

kernel3 = np.ones((3,3), dtype = np.float32)/9
kernel5 = np.ones((5,5), dtype = np.float32)/25
# emboss filter
kernel_emboss = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])

dst5 = cv2.filter2D(src,-1,kernel5)   #-1  입력영상과 동일한 데이터를 넣겠다는 의미 
print(kernel5)
dst3 = cv2.filter2D(src, -1, kernel3)
dst_emboss = cv2.filter2D(src, -1, kernel_emboss)

cv2.imshow('src',src)
cv2.imshow('dst5',dst5)
cv2.imshow('dst3', dst3)
cv2.imshow('dst_emboss',dst_emboss)
cv2.waitKey()
cv2.destroyAllWindows()