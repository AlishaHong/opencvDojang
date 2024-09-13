# 정규화 다시 해보기 


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
# 강의땐 minLoc과 maxLoc은 _ 처리 했었음

print('src:', minVal, maxVal, minLoc, maxLoc)   # 좌표였군

dst = cv2.normalize(img,None, 10, 200, cv2.NORM_MINMAX)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dst)

print('dst:', minVal, maxVal, minLoc, maxLoc) 

# 히스토그램을 그려보자! 
hist1 = cv2.calcHist(images=[img], channels = [0], mask = None, histSize= [256], ranges = [0,256])
hist2 = cv2.calcHist(images=[dst], channels = [0], mask = None, histSize= [256], ranges = [0,256])

hist1 = hist1.flatten()
hist2 = hist2.flatten()

plt.plot(hist1, label = 'src')
plt.plot(hist2, label = 'dst')

plt.legend()
plt.show()


cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()




