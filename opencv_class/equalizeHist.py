import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')


# equalize
dst= cv2.equalizeHist(src)

# equalize 전 그래프
hist0 = cv2.calcHist([src], [0], None, [256], [0,256])
# eqaulize 후 그래프
hist1 = cv2.calcHist([dst], [0], None, [256], [0,256])



# normalize
pixMin, pixMax, _, _ = cv2.minMaxLoc(src)
# print(pixMin, pixMax) #113.0,213.0

# 이미지 정규화 0~255
dst1 = cv2.normalize(src,None,0,255,cv2.NORM_MINMAX)
pixMin, pixMax, _, _ = cv2.minMaxLoc(dst1)
print(pixMin, pixMax)   #0.0,255.0(정규화됨)
# normalize 후
hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])
hist3 = cv2.calcHist([src], [0], None, [256], [0,256])

cv2.imshow('normalize',dst1)
cv2.imshow('src',src)
cv2.imshow('equalize',dst)

plt.plot(hist0, label = 'src')
plt.plot(hist1, label = 'equalize')
plt.plot(hist2, label = 'normalize')
plt.legend()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()