import sys
import cv2


# opencv 버전 확인
print('Hello OpenCV', cv2.__version__)

# image read함수 
# img = cv2.imread('data/lenna.bmp')
img_gray = cv2.imread('data/puppy.jpg', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread('data/puppy.jpg')
print(type(img_bgr))    #데이터 타입 : 넘파이(numpy.ndarray)

# 파일을 못찾아서 이미지를 못 읽어온 경우 
# 프로그램 종료 
if img_bgr is None or img_gray is None:
    print('Image load failed!')
    sys.exit()

# 창의 이름을 정의
cv2.namedWindow('image_bgr')
cv2.namedWindow('image_gray')

# 불러온 이미지를 창에 띄워준다.
# 'image'창에 읽어온 img 배열을 출력한다.
cv2.imshow('image_bgr', img_bgr)
cv2.imshow('image_gray', img_gray)

# 키 입력을 기다리는 함수 
cv2.waitKey() # 1초만 기다리고 모든창을 닫음
                  # 지연값 없으면 무한 대기 


# wait 키를 변수에 담아 다양하게 활용 
# 's'를 누르면 저장가능

# k = cv2.waitKey()

# if k == 27 : 
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('data/puppy_gray.jpg', img_gray)
#     print('Image saved!')

cv2.destroyAllWindows()




