import cv2
import sys

filename = 'data/cat.jpg'

# 이미지를 불러오는 함수
img = cv2.imread(filename)
print(img.shape)
#(405, 425, 3)

if img is None: 
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('야옹이', cv2.WINDOW_NORMAL)    #창 크기를 조정할 수 있게 됨 
# 창을 전체 화면으로 설정
# cv2.setWindowProperty('야옹이', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#야옹이 창에 img 배열을 출력
cv2.imshow('야옹이',img)

# 이미지 저장
# cv2.imwrite('cat.png', img)

# 이미지 품질을 지정하여 저장 
cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 85])
cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])


while(True):
    inkey = cv2.waitKey(0)
    print(inkey)    # 아스키 테이블의 decimal 값이 출력된다. q키는 113 
    if inkey == ord('q'):
        cv2.destroyAllWindows()   # 모든 창 닫기 
        # cv2.destroyWindow('야옹이') #창 하나만 닫을때 
        break
        #loop 변수 없으면 break해도 된다. 
        
        
# cv2.destroyWindow('야옹이')