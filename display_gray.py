# plt.imshow 함수에서 interpolation옵션
# cmap은 이미지가 컬러일경우 cmap 지정을 안해도 컬러로 출력
# cmap = "gray"

import cv2, sys
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('data/cat.jpg')
imgGray = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)
imgColor = cv2.imread('data/cat.jpg', cv2.IMREAD_COLOR)
print(imgGray.shape)    #(405,425)
print(imgColor.shape)   #(405,425,3)

plt.axis('off')
plt.imshow(imgGray, cmap = 'gray')  #cmap 생략하면 이상한 색의 고양이가 출력됨 
plt.show()

#interpolation 
#보간법 : 이미지를 확대하거나 축소할때 픽셀값을 계산하여 품질을 향상 
#nearest, bilinear, bicubic(부드러운 결과)
