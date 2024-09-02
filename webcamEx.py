import cv2 

# 카메라 열기
cap = cv2.VideoCapture(0)

print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# cap.set(property_id, value) # 비디오 특정 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)


while(True):
    ret,frame = cap.read()
    
    if ret == False:
        break
    
    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()

