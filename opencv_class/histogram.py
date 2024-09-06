import cv2,sys
import numpy as np
import matplotlib.pyplot as plt

isColor = True
if not isColor :

    src1 = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('data2/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)
    if src1 is None:
        sys.exit('image loading failed')
        
    # 히스토그램 
    hist1 = cv2.calcHist([src1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([src2], [0], None, [256], [0,256])
    cv2.imshow('src1', src1)
    cv2.imshow('src2', src2)
    plt.plot(hist1)
    plt.plot(hist2)
    # print(type(hist1))   # numpy 배열
    plt.show()  

if isColor:
    src = cv2.imread('data/lena.bmp')
    
    if src is None:
        sys.exit('image loading failed')
    
    # 컬러 채널 분리 
    colors = ['b','g','r']
    bgr_planes = cv2.split(src)
    print(bgr_planes)
    for(p,c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p],[0],None,[256],[0,256])
        plt.plot(hist, color = c)
    print(len(bgr_planes))
    plt.show()
    
    cv2.imshow('src',src)
    

# 정규화를 함으로써 분산이 커졌고 이미지는 분산이 커지면 선명해진다!!!!!!! 

cv2.waitKey()
cv2.destroyAllWindows()