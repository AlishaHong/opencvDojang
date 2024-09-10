import cv2, sys
import numpy as np
from glob import glob
import os

# 완성
# 0. 파일 목록 읽기 *.jpg 리스트
# 1. 이미지 불러오기
# 2. 마우스 콜백함수 생성
# 3. 콜백 함수안에서 박스를 그리고 
# 박스 좌표를 뽑아낸다. 마우스좌표 2개
# 참고로 욜로에서는 박스의 중심좌표 (x,y), w, h
# 4. 이미지 파일명과 동일한 파일명으로(확장자만 떼고) txt 파일 생성
# 추가기능 0 박스를 잘못 쳤을 때 'c'를 누르면 현재파일의 박스 내용 초기화
# 추가 기능 화살표(->)를 누르면 다음 이미지 로딩되고(1~4 반복)
# 추추추추가기능 이미지를 c버튼으로 초기화 하지 않으면 
# 바운딩 박스가 다른 이미지를 보러 다녀와도 사라지지 않고 보존되어 있도록 
# 딕셔너리에 전체 boxes 들을 담아서 관리 



# 미완성
# 추가 기능 2 화살표 (<-) 눌렀을때 txt 파일이 있다면 박스를 이미지 위에 띄워주면


radius = 25


# 이미지를 한번에 불러와서 리스트화
def getImageList():
    global dataPath
# 현재 작업 디렉토리 확인
    basePath = os.getcwd()
    dataPath = os.path.join(basePath,'0910_exercise\images')
    print(dataPath)
    fileNames = glob(os.path.join(dataPath ,'*.jpg'))
    return fileNames



# 박스 그리기 
# 원본이미지에 그리지 않고 박스 그리는 레이어를 추가한다.
def drawROI(img, boxes):
    # 박스를 그릴 레이어를 생성 : cpy
    cpy = img.copy()
    line_c = (128,128,255)
    lineWidth = 2
    # print(ptList)
    # cv2.rectangle(cpy,corners[0],corners[1], line_c, lineWidth)
    for box in boxes:
        cv2.rectangle(cpy,tuple(box[0]),tuple(box[1]), line_c, lineWidth)
       
    
    # 원본이미지와 박스레이어를 합쳐서 한 그림인것처럼
    # alpha = 0.3 beta = 0.7 gamma = 0
    disp = cv2.addWeighted(img,0.3,cpy,0.7,0)
    return cpy


# 마우스 콜백함수 정의
def onMouse(event, x, y, flag, params):
    global startPt, img, ptList, cpy, boxes
    # 왼쪽 버튼을 눌렀을 때 시작 좌표를 담아
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt = (x,y)
        print(startPt)
    # 왼쪽버튼 키에서 손을 뗐을때 첫 좌표와 최종 좌표를 하나의 리스트에 담은뒤
    # 상위리스트(boxes)에 담아주고 drawROI 함수로 다 그려주기!
    # 그린 뒤에는 좌표 초기화 
    elif event == cv2.EVENT_LBUTTONUP:
        ptList = [startPt, (x,y)]  # startPt, endPt를 list로 저장
        boxes.append(ptList)
        print(boxes)
        cpy = drawROI(img, boxes)
        startPt = None
        cv2.imshow('label', cpy)
        
    # 박스 가이드라인(없어도 바운딩박스 만드는데에는 문제없음)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt:
            tempBox = [startPt, (x, y)]
            temp_img = drawROI(img, boxes + [tempBox])  # 기존 박스 + 임시 박스 그리기
            cv2.imshow('label', temp_img)
            
    #     if startPt:
    #         ptList=[startPt, (x,y)]
    #         boxes.append(ptList)
    #         cpy = drawROI(img, boxes)
    #         boxes.pop()
    #         print(boxes)
    #         cv2.imshow('label',cpy)
# 마우스가 눌리지 않으면 좌표값은 없음


boxes = []
all_boxes = {}  # 각 이미지의 박스를 저장할 딕셔너리
startPt = None
ptList = []
fileNames = getImageList()
image_load = True
index = 0
img = None


# 메인 함수
def main():
    global image_load, index, img, boxes, all_boxes

    # image_load가 true인 동안 반복
    while image_load:
        # 현재 이미지에 대해 박스가 있으면 로드, 없으면 빈 리스트로 초기화
        img = cv2.imread(fileNames[index])
        
        # 한번 그려진 뒤 초기화 되지않았다면 기존의 바운딩 박스들을 다시 보여줘!
        if fileNames[index] in all_boxes:
            boxes = all_boxes[fileNames[index]]
        # 없으면 박스 없는 이미지 보여줘
        else:
            boxes = []

        img = drawROI(img, boxes) 
        cv2.namedWindow('label')
        cv2.setMouseCallback('label', onMouse, [img])
        cv2.imshow('label', img)

        while True:
            key = cv2.waitKeyEx()
            if key == 27:  # ESC 키로 종료
                image_load = False
                break    
            elif key == ord('s'):  # 's' 키로 박스 저장
                filename, ext = os.path.splitext(os.path.basename(fileNames[index]))
                txtfilename = os.path.join(dataPath, filename + '.txt')
                with open(txtfilename, 'w') as f:
                    for box in boxes:
                        f.write(f'{box}')
                print(f'{filename}.txt 저장 완료!')
            elif key == ord('c'):  # 'c' 키로 박스 초기화
                boxes = []
                all_boxes[fileNames[index]] = []  # 현재 이미지의 박스 초기화
                cv2.imshow('label', img)
                print(f'{filename}.txt 초기화!')

            # 오른쪽 화살표
            elif key == 0x270000:
                # 현재 이미지의 박스를 저장하고 다음 이미지로 이동
                all_boxes[fileNames[index]] = boxes
                index += 1
                if index >= len(fileNames):
                    print('마지막 이미지입니다.')
                    index = len(fileNames) - 1
                else:
                    img = cv2.imread(fileNames[index])
                    boxes = all_boxes.get(fileNames[index],[])  # 다음 이미지에 저장된 박스를 불러옴
                    img_with_boxes = drawROI(img, boxes)
                    cv2.imshow('label', img_with_boxes)

            # 왼쪽 화살표
            elif key == 0x250000:
                # 현재 이미지의 박스를 저장하고 이전 이미지로 이동
                all_boxes[fileNames[index]] = boxes
                index -= 1
                if index < 0:
                    index = 0
                    print('첫번째 이미지입니다.')
                else:
                    img = cv2.imread(fileNames[index])
                    boxes = all_boxes.get(fileNames[index],[])  # 이전 이미지에 저장된 박스를 불러옴
                    img_with_boxes = drawROI(img, boxes)
                    cv2.imshow('label', img_with_boxes)
                    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()