import cv2, sys
import numpy as np
import matplotlib.pyplot as plt


# 이미지 로드 

img = cv2.imread('0906_imageFiltering/data/01.png')
if img is None: 
    sys.exit("이미지 로드 실패")
    
    
# 컬러 채널 분리 
colors = ['b','g','r']
split_img = cv2.split(img)
print(split_img)
for(p,c) in zip(split_img, colors):
    hist = cv2.calcHist([p],[0],None,[256],[0,256])
    plt.plot(hist, color = c)
print(len(split_img))
plt.title('color_split histogram')
plt.show()


# YCbCr 채널 
# 밝기 조절 시 그냥 add 하면 색이 틀어질 수 있다. 
# 밝기를 단순하게 증가시키면 특정 색상이 더 강하게 보일 수 있음
# YCbCr 채널 사용하기 

ycbcr_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
hist_ycbcr = cv2.calcHist([ycbcr_img],[0],None,[256],[0,256])
plt.plot(hist_ycbcr)
plt.title('ycbcr histogram')
plt.show()

# 분포가 앞쪽으로 엄청 쏠려있음 
# normalize 적용하기 
Y, Cb, Cr = cv2.split(ycbcr_img)
Y_norm = cv2.normalize(ycbcr_img, None, 0, 255, cv2.NORM_MINMAX)
# 정규화가 안된 것 처럼 보인다/
# add 해야할듯요 
# equalize 해도 됨(별로임)


Y_norm = cv2.add(Y, 50)
# Y만 떨어뜨려 놓은것을 cb와 cr과 합쳐야함 
ycbcr_norm_merge = cv2.merge([Y_norm, Cb, Cr])
ycbcr_norm_merge = cv2.cvtColor(ycbcr_norm_merge, cv2.COLOR_YCrCb2BGR)

hist_Y_norm = cv2.calcHist([ycbcr_norm_merge],[0],None,[256],[0,256])
plt.plot(hist_Y_norm)
plt.title('normalize histogram')
plt.show()

cv2.imshow('ycbcr_normalize_add',ycbcr_norm_merge)
cv2.imshow('ycbcr',ycbcr_img)
cv2.waitKey()
cv2.destroyAllWindows()
