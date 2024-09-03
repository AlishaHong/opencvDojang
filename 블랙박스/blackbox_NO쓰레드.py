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
import schedule
import threading


record_time = 60  # 녹화시간

# 파일명 만들어주는 함수가 필요 
def create_filename():
    # 파일명으로 사용할 현재시각 불러오기 
    now = datetime.now()
    filename = now.strftime('%Y%m%d-%H%M%S') + '.avi'
    return filename


def make_folder():
    if not os.path.exists(os.path.join(folder_path,folder_name)):
        os.makedirs(os.path.join(folder_path,folder_name))
        print(f"'{folder_name}' 폴더가 생성되었습니다.")


# videoCapture 클래스 객체 생성 및 호출 
cap = cv2.VideoCapture(0)

# 영상 크기 조절
cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)
cap.set(cv2.CAP_PROP_FPS, 30)

# FPS 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)
# 총 녹화할 프레임 수 계산
total_frames_to_record = int(record_time * fps)
# 10초후 시간 계산
end_time = datetime.now() + timedelta(seconds = 10)

# 1분 타이머 스레드 함수
def timer_thread(stop_event):
    global recording
    time.sleep(60)  # 60초 (1분) 대기
    stop_event.set()  # 이벤트 설정 (녹화 중지)
    

while(True):
    # 녹화 중지 이벤트 생성
    stop_recording = threading.Event()

    # 타이머 스레드 생성 및 시작
    timer = threading.Thread(target=timer_thread, args=(stop_recording,))
    timer.start()
    
    create_filename()

    folder_path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'
    now = datetime.now()

    # 2. 폴더 생성은 날짜+현재시간
    # 20240902-16 00분 ~ 59분
    # 한시간마다 폴더 생성

    folder_name = now.strftime('%Y%m%d' + '-' + str(now.hour) + '시')

    # # 새폴더 만드는 함수
    # def make_folder():
    #     if not os.path.exists(os.path.join(folder_path,folder_name)):
    #         os.makedirs(os.path.join(folder_path,folder_name))
    #         print(f"'{folder_name}' 폴더가 생성되었습니다.")

    # 폴더가 없을 수 있으니 한개 만들기
    make_folder()
    
    # 정시마다 폴더 생성하기 
    schedule.every().hour.do(make_folder)
    
    
    # 가장 최근에 만들어진 파일(폴더) 확인하기 
    new_folder = max(os.listdir(folder_path), key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
    print(new_folder)
    
    
    # 영상 저장할때는 프레임 사이즈도 읽어온다.
    framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # 코덱설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 영상저장 생성자
    output_path = os.path.join(folder_path, new_folder, create_filename())
    out = cv2.VideoWriter(output_path + create_filename(), fourcc, fps, framesize)

    # 녹화된 프레임 변수 초기화
    frames_recorded = 0
    start_time = time.time()

    # 목표 녹화 프레임수가 녹화된 프레임수보다 큰 동안
    # while frames_recorded < total_frames_to_record:
    recording = True
    while recording:
        ret,frame = cap.read()
        if not ret:
            break

        out.write(frame)
        frames_recorded += 1
        cv2.imshow('blackbox', frame)

        key = cv2.waitKey(30)
        if key == ord('q'):
            break
        # 타이머 이벤트 확인 (1분 경과 여부)
        if stop_recording.is_set():
            recording = False    
    

    if key == ord('q'):
        break

    # 3. 현재 폴더의 용량이 5mb가 되면 가장 오래된 파일 지우기 
    # 용량 확인 주기 추가해야함 
    
    # os.listdir 함수
    path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'
    new_path = os.path.join(path, new_folder)
    for name in os.listdir(new_path):
        # 1MB는 1024 * 1024 바이트이므로, 이를 나누어 바이트를 MB로 변환
        folder_size = sum([getsize(join(new_path, name)) for name in os.listdir(new_path)]) / (1024.0 * 1024.0)
        if folder_size > 100:
            oldest_file = os.listdir(new_path)[0]
            os.remove(new_path+ '/' + oldest_file)

    # if key == ord('q'):
    #     sys.exit()
    
out.release()
cap.release()
cv2.destroyAllWindows()
