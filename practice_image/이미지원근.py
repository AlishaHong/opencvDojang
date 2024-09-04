import cv2
import numpy as np

newspaper = cv2.imread('practice_image/newspaper.jpg')

# cv2.imshow('newspaper',newspaper)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

width, height = 640,230

# 그림판에서 좌표얻을 수 있음
img = np.array([[507,362],[1009,344],[1119,583],[449,581]], dtype = np.float32)
#왼쪽위 - 오른쪽위 - 오른쪽아래 - 왼쪽아래
dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)
#dst 배열은 변환 후 이미지에서 각 좌표가 어떻게 매핑될지를 나타냄


# 원근 변환 행렬계산 
matrix = cv2.getPerspectiveTransform(img,dst)
# 원근 변환 적용
result = cv2.warpPerspective(newspaper, matrix,(width,height))

cv2.imshow('src',newspaper)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()