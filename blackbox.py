# 블랙박스 만들기

# 1. 60초에 동영상 한개가 생성되도록 한다.
# 파일명은 20240902-161903.avi

# 2. 폴더 생성은 날짜+현재시간
# 20240902-16 00분 ~ 59분
# 한시간마다 폴더 생성

# 3. 블랙박스 녹화 폴더가 3GB이면 가장 오래된 녹화 폴더 삭제 




# 1. 60초에 동영상 한개가 생성되도록 한다. 
# 파일명은 20240902-161903.avi


import cv2, sys
import time
import datetime
# 녹화 시작과 끝을 시간단위로 계산하기 위해 호출
from datetime import datetime, timedelta
import os
from os.path import join, getsize


record_time = 10  # 10초 동안 녹화

# 파일명 만들어주는 함수가 필요 
def create_filename():
    # 파일명으로 사용할 현재시각 불러오기 
    now = datetime.now()
    filename = now.strftime('%Y%m%d-%H%M%S') + '.avi'
    return filename

# videoCapture 클래스 객체 생성 및 호출 
cap = cv2.VideoCapture(0)

# 영상 크기 조절
cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)

# FPS 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)

# 총 녹화할 프레임 수 계산
total_frames_to_record = int(record_time * fps)



while(True):
    create_filename()
    # 영상 저장할때는 프레임 사이즈도 읽어온다.
    framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # 코덱설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 영상저장 생성자
    out = cv2.VideoWriter('blackbox/' + create_filename(), fourcc, fps, framesize)

    # 녹화된 프레임 변수 초기화
    frames_recorded = 0
    start_time = time.time()

    # 목표 녹화 프레임수가 녹화된 프레임수보다 큰 동안
    while frames_recorded < total_frames_to_record:
        ret,frame = cap.read()
        if not ret:
            break

        out.write(frame)
        frames_recorded += 1
        cv2.imshow('blackbox', frame)

        key = cv2.waitKey(30)
        if key == ord('q'):
            break

    if key == ord('q'):
        break
    

# while(True):
#     create_filename()
#     # 영상 저장할때는 프레임 사이즈도 읽어온다.
    
#     end_time = datetime.now() + timedelta(seconds = 10)
    
#     framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#     # 코덱설정
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     # 영상저장 생성자
#     out = cv2.VideoWriter('blackbox/' + create_filename(), fourcc, fps, framesize)

#     # endtime과 현재시간이 같을때 까지 반복
#     while (end_time - datetime.now()).total_seconds() > 0:
#         ret,frame = cap.read()
#         if not ret:
#             break

#         out.write(frame)
#         # frames_recorded += 1
#         cv2.imshow('blackbox', frame)

        
#         key = cv2.waitKey(30)
#         if key == ord('q'):
#             break
    # 녹화 시작한 시간과 끝나는 시간의 차가 11초가 될떄까지 반복하는것도 괜찮을듯 
    
    
    
    

    # 3. 현재 폴더의 용량이 5mb가 되면 가장 오래된 파일 지우기 

    # os.walk 함수(복잡한듯..)
    
    # for root, dirs, files in os.walk('C:/Users/user/Desktop/REPOSITORY/opeㅂcvDojang/blackbox'):
    #     folder_size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)

    #     print(folder_size)
    #     print(root)
    #     print(dirs)
    #     if folder_size >= 5:
    #         print(files)
    #         oldest_file = files[0]
    #         print("Oldest file is: ", files[0])
    #         os.remove('C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox/' + oldest_file)




    # os.listdir 함수
    path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'
    for name in os.listdir(path):
        folder_size = sum([getsize(join(path, name)) for name in os.listdir(path)]) / (1024.0 * 1024.0)
        print(folder_size)
        full_path = os.path.join(path, name)
        print(full_path)
        if folder_size > 5:
            oldest_file = os.listdir(path)[0]
            os.remove(path + '/' + oldest_file)

    if key == ord('q'):
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()






# / (1024.0 * 1024.0):
# 바이트 단위의 총 파일 크기를 메가바이트(MB) 단위로 변환합니다.
# 1MB는 1024 * 1024 바이트이므로, 이를 나누어 바이트를 MB로 변환합니다.