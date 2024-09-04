# 

import cv2,sys
from matplotlib import pyplot as plt

imgBGR1 = cv2.imread('data/lena.jpg')
imgBGR2 = cv2.imread('data/orange.jpg')
imgBGR3 = cv2.imread('data/apple.jpg')
imgBGR4 = cv2.imread('data/cat.jpg')

if imgBGR1 is None or imgBGR2 is None or imgBGR3 is None or imgBGR4 is None:
    sys.exit("image load is failed")

# 컬러스페이스 바꾸기 
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)  
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)  
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)  

figsize = (10,10)
# matplotlib의 plt.subplots으로 이미지를 출력 
fig, ax = plt.subplots(2,2, figsize = figsize)
print(fig,ax)
ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

ax[0][0].imshow(imgRGB1)
ax[0][1].imshow(imgRGB3)
ax[1][0].imshow(imgRGB4)
ax[1][1].imshow(imgRGB2)

# 창 이름 설정
fig.canvas.manager.set_window_title('Sample windows')
plt.show()

