# 이미지를 불러올때는 imread()
# 동영상을 불러올때는 VidioCapture()
import cv2,sys

filename = 'data/vtest.avi'

# 동영상의 해상도 width, height, frame수를 확인


# VideoCapture 클래스 객체 생성 + 생성자가 호출(파일열기)
cap = cv2.VideoCapture(filename)

# 카메라 열기
# cap = cv2.VideoCapture(0)
# cap.set(property_id, value) # 비디오 특정 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

# 파일의 정보를 가져오는 함수 
print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))  # 768
print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 576
print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))) # 795

framesize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(framesize)

# 동영상 이미지를 다 가져올때까지 반복
while(True): 
    # 동영상에서 한장의 이미지를 가져오기 
    # retval : 동영상에서 이미지를 가져올때 정상 동작했는지 여부 
    # frame : 이미지 한장
    # 동영상 코덱 디코딩도 포함
    
    retval, frame = cap.read() 
    # read = grab + retrieve
    
    
    # if not retval:
    if retval == False:
        break
    
    cv2.imshow('frame',frame)
    # 100ms대기(이 동영상은 초당 10프레임 짜리니까)
    key = cv2.waitKey(100)
    # 키 입력이 esc(27)이면 종료
    if key == 27:   #esc 키
        break
    
    # 동영상을 열었으면, 닫아야 한다.
if cap.isOpened():
    cap.release()   #열림해제


cv2.destroyAllWindows()


