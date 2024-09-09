import cv2, sys
import numpy as np



# 이미지 불러오기 
# 흰색 캔버스 생성 
# img = np.zeros((512,512,3), np.uint8) + 255
img = np.ones((512,512,3), np.uint8) * 255

# 마우스 콜백함수 구현
# 마우스에서 이벤트가 발생하면 호출되는 함수 
# 버튼 클릭, 마우스 좌표 이동 등 

pt1 = (0,0)
pt2 = (0,0)
def mouse_callback(event, x, y, flags, param):
     # 전역변수를 써도 되고 
    # img = param[0]    #뭔가 좀 이상함
    global img, pt1, pt2

    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)
        cv2.circle(img,pt1,5,(0,0,255), 3)
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x,y)
        cv2.circle(img,pt2,5,(0,0,255), 3)
        cv2.rectangle(img, pt1, pt2, (255,0,0), 3)
    cv2.imshow('img', img)

# 메인에서 setMouseCallback 함수를 실행하면서 콜백함수를 지정 
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback, img)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()





