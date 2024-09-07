# 이미지 불러오기 : 동일
# opencv 패키지의 툭성과 matplotlib패키지의 특성의 차이를 이해
# 이미지 출력하기 : cv2.imshow() -> plt.imshow()

import cv2
import sys
from matplotlib import pyplot as plt

filename = 'data/cat.jpg'

img = cv2.imread(filename)

if img is None:
    sys.exit("file is not found")

# opencv 모듈은 이미지를 읽어올때 컬러 스페이서의 순서 
# B,G,R 

# 채널 순서(컬러스페이스)를 바꿔줘야한다. 
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# matplotlib은 R,G,B로 사용 
plt.imshow(imgRGB)
# plt.axis('off') #눈금 지우기 
plt.show()