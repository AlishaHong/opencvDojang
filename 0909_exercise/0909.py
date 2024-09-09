# 512x512 사이즈에서 원(마우스 오른쪽 버튼), 다각형(삼각형, 사각형 포함, 마우스 왼쪽 버튼)을 그리고 
# 리사이징 후 선 얼마나 뭉개지는지 관찰하기
# (마우스 콜백함수로 직접 그리기를 사용+다각형 그리기(교재 52페이지참조))
# 각각의 도형을 한번에 그릴수는 없으니 하나 그리고 저장하고 거기에 추가도형 그리는 방식으로 진행 
# 이후 다시 부드럽게 필터링 후 축소해서 관찰하기(CV2.INTER_AREA를 사용한것과 다른 interpoltion비교)

# shift : 그리기 모드 

import cv2
import numpy as np
import os.path


# 512x512 사이즈에서 원(마우스 오른쪽 버튼), 다각형(삼각형, 사각형 포함, 마우스 왼쪽 버튼)을 그리고


# 마우스 콜백함수 정의하기 
pts = []
filepath = '0909_exercise/draw.jpg'

# 마우스 콜백함수로 직접 그리기를 사용+다각형 그리기
def mouseCallback(event, x, y, flags, param):
    global canvas, pts
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(canvas, (x,y), 20, (0,0,255), 3, cv2.LINE_AA)
    elif event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            pts.append([x,y])
            print(pts)
        # elif not (flags & cv2.EVENT_FLAG_SHIFTKEY):
        else:
            numpy_pts = np.array(pts, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(canvas, [numpy_pts], isClosed=True, color=(0, 255, 0), thickness=3)
            pts = []  # 도형을 그린 후 좌표 초기화``
    cv2.imshow('canvas', canvas)
    cv2.imwrite('0909_exercise/draw.jpg',canvas)
    
    
    
# 리사이징 후 선 얼마나 뭉개지는지 관찰하기
# 이후 다시 부드럽게 필터링 후 축소해서 관찰하기(CV2.INTER_AREA를 사용한것과 다른 interpoltion비교)

def main():
    global canvas
    # 기존에 저장된 파일이 있다면 resize 작업 
    if os.path.exists(filepath):
        canvas = cv2.imread('0909_exercise/draw.jpg')
        
        # 확대본 확인하기 
        # dst_expand1 = cv2.resize(canvas,(0,0), fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
        # dst_expand2 = cv2.resize(canvas,(0,0), fx=2, fy=2, interpolation = cv2.INTER_NEAREST)    # 엣지 부분에 픽셀이 각진것이 많이 보인다.
        # dst_expand3 = cv2.resize(canvas,(0,0), fx=2, fy=2, interpolation = cv2.INTER_LANCZOS4)   # 얘가 제일 좋다고 함 
        # cv2.imshow('expand_cubic', dst_expand1)
        # cv2.imshow('expand_nearest', dst_expand2)
        # cv2.imshow('expand_lanczos', dst_expand3)
        
        
        # 축소 이미지 품질 확인 및 gaussian blur + cv2.INTER_AREA 축소 이미지 확인
        dst_reduce1 = cv2.resize(canvas,(0,0), fx=0.8, fy=0.8, interpolation = cv2.INTER_CUBIC)
        dst_reduce2 = cv2.resize(canvas,(0,0), fx=0.8, fy=0.8, interpolation = cv2.INTER_NEAREST)  # 축소해보니 많이 끊김
        dst_reduce3 = cv2.resize(canvas,(0,0), fx=0.8, fy=0.8, interpolation = cv2.INTER_LANCZOS4)    
        dst_best_reducing = cv2.resize(cv2.GaussianBlur(canvas,(0,0), 1), (0,0), fx = 0.8, fy = 0.8, interpolation = cv2.INTER_AREA)
        
        
        cv2.imshow('src', canvas)
        cv2.imshow('reduce_cubic', dst_reduce1)
        cv2.imshow('reduce_nearest', dst_reduce2)
        cv2.imshow('reduce_lancoz', dst_reduce3)
        cv2.imshow('best_reducing', dst_best_reducing)
        
        cv2.waitKey()

        cv2.imwrite('0909_exercise/reduce_cubic.jpg',dst_reduce1)
        cv2.imwrite('0909_exercise/reduce_nearest.jpg',dst_reduce2)
        cv2.imwrite('0909_exercise/reduce_lancoz.jpg',dst_reduce3)
        cv2.imwrite('0909_exercise/best_reducing.jpg',dst_best_reducing)
        
    else:
        # 저장된 파일이 없으면 빈 캔버스 만들기
        canvas = np.zeros((512,512,3), np.uint8) + 255
        cv2.namedWindow('canvas')
        # 콜백함수 지정
        cv2.setMouseCallback('canvas', mouseCallback, canvas)
        cv2.imshow('canvas', canvas)
        cv2.waitKey()


cv2.waitKey()
cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
