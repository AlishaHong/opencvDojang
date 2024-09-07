import cv2, sys

isWEBCAM = False

# 원하는 녹화 시간 (초)
record_time = 10  # 예: 10초 동안 녹화

if isWEBCAM:
    cap = cv2.VideoCapture(0)
else:
    filename = 'data/vtest.avi'
    cap = cv2.VideoCapture(filename)

# 영상 저장할 때는 프레임 사이즈를 읽어와야 함
framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = cap.get(cv2.CAP_PROP_FPS)

# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 영상저장 생성자
out1 = cv2.VideoWriter('video1.mp4', fourcc, 20.0, framesize)
out2 = cv2.VideoWriter('video2.mp4', fourcc, 20.0, framesize, isColor=False)

# 총 녹화할 프레임 수 계산
total_frames_to_record = int(record_time * fps)
frames_recorded = 0

while True:
    ret, frame = cap.read()
    if not ret or frames_recorded >= total_frames_to_record:
        break

    # 저장
    out1.write(frame)

    # 그레이로 변경
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 저장
    out2.write(gray)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    frames_recorded += 1

    delay = int(1000 / fps)
    key = cv2.waitKey(delay)
    if key == ord('q'):
        break

cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()