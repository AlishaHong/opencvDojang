import cv2

# 마우스로 roi지정해서 출력해줌 쩐다 
# selectROI 함수 
# 결과값이 (0,0,0,0) 형태인데 
# 첫번째는 열 두번째는 행 세번째는 가로크기 네번째는 세로크기이다.

src = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)

print('roi = ' , roi)

if roi != (0,0,0,0):
    img = src[roi[1]: roi[1]+roi[3], 
              roi[0]:roi[0]+roi[2]]
    
    cv2.imshow('roi', img)
    cv2.waitKey()
    
cv2.destroyAllWindows()    