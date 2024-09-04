# 컨셉은 webcam에서부터 들어오는 영상을 녹화
# 우리가 웹캠이 없으니(난 있음 ㅎ) 비디오 파일을 열어서 사용하는 것으로 대체 


import cv2,sys


isWEBCAM = True


if isWEBCAM:
    cap = cv2.VideoCapture(0)
    
else:
    filename = 'data/vtest.avi'
    cap = cv2.VideoCapture(filename)
    

while(True):
    
    # 한 프레임에 영상 읽어오기 
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    
    # 영상 저장할때는 프레임 사이즈를 읽어와야함
    framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # 코덱 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    # 영상저장 생성자
    out1 = cv2.VideoWriter('video1.mp4', fourcc, 20.0, framesize)
    out2 = cv2.VideoWriter('video2.mp4', fourcc, 20.0, framesize, isColor = False)
        
    
    while(True):
        ret, frame = cap.read()
        if not ret:
            break
        
        # 저장
        out1.write(frame)
        
        # 그레이로 변경
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 저장 
        out2.write(gray)
        
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
        
        delay =int(1000/fps)
        key = cv2.waitKey(delay)
        if key == ord('q'):
            break
        
    cap.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()