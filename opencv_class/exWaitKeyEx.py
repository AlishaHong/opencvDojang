import cv2, sys
import numpy as np

# 화살표를 누르면 원이 이동되는 어플
width, height = 512,512
# 초기에 원의 좌표와 반지름
x,y,R = 256,256,50

direction = 0 

#main 
while True:
    # 기본 waitKey + Extention 키 입력까지 받아들임(방향키나 함수키 등)
    key = cv2.waitKeyEx(30) #timeout = 30ms
    # 방향키 등의 특수키를 입력받을때 
    
    # 종료조건
    # if key == 0x1B: #esc키
    if key == 27:
        break
    
    
    # right key 
    elif key == 0X270000:
        direction = 0
        x += 10
    # down key 
    elif key == 0x280000:
        direction = 1
        y += 10
    # left key
    elif key == 0x250000:
        direction = 2
        x -= 10
    # up key 
    elif key == 0x260000:
        direction = 3
        y -= 10
    
    # 경계 확인 코드 넣으면 원이 이미지 밖으로 나가지 않음 
    
    # 빈 캔버스 생성
    img = np.zeros((width, height,3), np.uint8)+255
    # 원을 그린다. img에 (x,y)좌표에, 반지름 R로 빨간색으로 안을 채워서 -1 
    cv2.circle(img, (x,y), R, (0,0,255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()