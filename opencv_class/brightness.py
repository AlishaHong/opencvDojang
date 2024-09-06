import cv2 
import numpy as np
import sys
import matplotlib.pyplot as plt

isColor = False

if not isColor:

# grayscale로 가져오기 
    src = cv2.imread('data2/candies.png', cv2.IMREAD_GRAYSCALE)
    print(src.shape)

    # 밝기 변화
    dst1 = cv2.add(src, 50) #브로드캐스팅 연산
    
    hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([dst1], [0], None, [256], [0,256])
    
    dst2 = src + 100    #오버플로우발생
    dst3 = np.clip(src+100, 0,255).astype(np.uint8)  #오버플로우발생
    dst4 = cv2.convertScaleAbs(src, alpha=1, beta=100)
    
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst3)
    cv2.imshow('dst4', dst4)
    
    plt.plot(hist1)
    plt.plot(hist2)
    
    
if isColor :
    src = cv2.imread('data/cat.jpg')
    
    dst1 = cv2.add(src, (100,100,100))    #채널별로 100씩 더해준다.
    dst2 = np.clip(src.astype(np.int16)+100, 0, 255).astype(np.uint8)   #오버플로우 발생하지 않으려면 src배열을 더 큰 int 16으로 형변환 한 후 연산한다.
    
    cv2.imshow('color_dst1', dst1)
    cv2.imshow('color_dst2', dst2)


plt.plot(hist1)
plt.plot(hist2)
plt.show()



cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()