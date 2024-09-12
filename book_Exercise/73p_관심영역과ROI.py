import cv2
import numpy as np

# roi에 의한 블록 평균


# src = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('data/lena.jpg')
dst = np.zeros(src.shape, dtype=src.dtype)  # 원본과 사이즈와 타입이 같은 캔버스를 생성

N = 4 
# height, width = src.shape   # 그레이(채널값 못받음)
height, width, channels = src.shape    # 컬러

h = height // N 
w = width // N

for i in range(N):
    for j in range(N):
        y = i * h 
        x = j * w
        
        roi = src[y:y+h, x:x+w]
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0]  # 그레이스케일
        dst[y:y+h, x:x+w] = cv2.mean(roi)[:3]   # 컬러

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
