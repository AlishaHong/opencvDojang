import cv2, sys
import numpy as np
import math

# wrapAffine 함수 매개변수 중 (0,0)의 의미
# (0,0) -> (row,col) : 변환후에 출력되는 배열의 크기 
# 이동변환 했을 때 이동한 이미지의 일부가 잘려서 보이지 않았다. 
# (0,0)를 줬다는 건 입력된 이미지와 같은 크기로 출력하겠다는 의미 -> 잘린부분 볼 수 없음
# 이동한만큼 높이 넓이에 더해주면 잘리지 않는다. 

# aff값을 적절한 행렬로 선언하여 대입해주면 변환 가능 



# 이동변환
def translate(src, x_move = 0,  y_move = 0):
    # 이미지의 이동 변환    x->200, y->100
    h,w = src.shape[:2]
    aff = np.array([[1,0,x_move],[0,1,y_move]], dtype=np.float32)
    # dst = cv2.warpAffine(src, aff, (0,0)) #입력 이미지 사이즈와 같은 사이즈의 출력이미지
    dst = cv2.warpAffine(src, aff, (h+y_move,w+x_move))     #이동한 만큼 커져서 가려지는 부분 없음
    print(dst.shape)    #(512,512,3 --> 562,562,3)
    return dst


# 전단변환
def shear_traslate(src, x_shear = 0, y_shear = 0):
    if x_shear > 0 and y_shear == 0: 
        aff = np.array([[1,x_shear,0],[0,1,0]], dtype = np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * x_shear), h))
    elif y_shear > 0 and x_shear == 0:
        aff = np.array([[1,0,0],[y_shear,1,0]], dtype = np.float32)
        h, w = src.shape[:2]    
        dst = cv2.warpAffine(src, aff, (w, h + int(h * y_shear)))
    return dst
        
        
# 확대/축소
def scale(src, x_scale, y_scale):
    h,w = src.shape[:2]
    aff = np.array([[x_scale,0,0],[0,y_scale,0]], dtype = np.float32)
    dst = cv2.warpAffine(src, aff, (int(w * x_scale), int(h * y_scale)))
    return dst


# 이미지 회전 함수 
# 방식과 기준점에 차이가 있음 
# rotate(좌상단좌표가 기준) --> 이미지는 좌상단이 시작점(원점)이다.
# 수학적으로는 좌측 하단이 (0,0) 원점이었음
def rotate(src, rad):
    aff = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0))
    return dst
    
    
# rotate2(중심좌표기준)
def rotate2(src, angle):
    h,w = src.shape[:2]
    centerPt = (w/2, h/2)
    rot = cv2.getRotationMatrix2D(centerPt, angle, 1)   #center/angle/scale
    dst = cv2.warpAffine(src,rot,(w,h))
    return dst




src = cv2.imread('data2/rose.bmp')
print(src.shape)    #(320,480,3)

if src is None:
    sys.exit('image load failed')


# print(src.shape)    #512,512,3
dst = translate(src, 50, 50)
dst1 = shear_traslate(src, 0.3, 0)
dst2 = shear_traslate(src, 0, 0.5)
dst3 = scale(src, 1.5, 1.5)
dst4 = cv2.resize(src,(1024,1024))
# 비율로 설정할때 
dst5 = cv2.resize(src,(0,0),fx=1.5, fy=1.5)


dst_rose1 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
dst_rose2 = cv2.resize(src,(0,0), fx=2, fy=2, interpolation = cv2.INTER_NEAREST)    # 엣지 부분에 픽셀이 각진것이 많이 보인다.
dst_rose3 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation = cv2.INTER_LANCZOS4)   # 얘가 제일 좋다고 함 


# rotation
angle = 20
rad = angle * math.pi/180
dst_rotate = rotate(src, rad)

#rotation2
dst_rotate2 = rotate2(src, 20)



# rotate2 출력 
cv2.imshow('src',src)
cv2.imshow('dst_rorate2', dst_rotate2)

# rotate 출력
# cv2.imshow('src', src)
cv2.imshow('dst_rotate', dst_rotate)

# 보간법 출력
# cv2.imshow('src', src)
# cv2.imshow('cubic', dst_rose1)
# cv2.imshow('nearest', dst_rose2)
# cv2.imshow('lanczos', dst_rose3)

# 변환 출력
# cv2.imshow('translate_이동변환', dst)
# cv2.imshow('shear_translate_x', dst1)
# cv2.imshow('shear_translate_y', dst2)
# cv2.imshow('scale', dst3)
# cv2.imshow('resize_해상도', dst4)
# cv2.imshow('resize_비율', dst5)


# 영상 축소시 픽셀이 손실될 수 있다. 
# 가장 효과적인 방법은 블러처리를 해서 작은 노이즈를 제거한 뒤 보간법에 cv2.INTER_AREA 를 적용하는 것이다. 
# INTER_AREA는 픽셀간의 영역을 평균내어 축소된 이미지를 만들어내서 고품질의 축소결과를 제공함 
# (무슨말인지를 모르겠음) - 영상축소에 특화된 보간법이라고 함 

cv2.waitKey()
cv2.destroyAllWindows()



# cv2.INTER_NEAREST -> 제일 별로였음
# cv2.INTER_AREA -> 축소시 제일 좋음 

# cv2.INTER_NEAREST (가장 가까운 이웃 보간법)
# 동작 방식: 새로운 픽셀 값을 계산할 때, 주변 픽셀 중에서 가장 가까운 픽셀 값 하나를 선택합니다. 
# 평균이나 복잡한 계산 없이 단순히 가장 가까운 픽셀의 값을 가져오기 때문에, 매우 빠른 방식입니다.
# 장점: 계산이 빠르고 간단합니다. 특히 실시간 애플리케이션이나 성능이 중요한 경우 유용할 수 있습니다.
# 단점: 이미지 축소나 확대 시 계단 현상이 발생할 수 있고, 경계가 거칠어지는 문제가 있습니다. 이미지 품질이 다소 떨어질 수 있습니다.




# cv2.INTER_AREA에서의 처리 방식:
# 축소할 픽셀 영역에서 각 픽셀 값을 더하고, 그 평균값을 계산합니다.
# (100 + 120 + 150 + 130) / 4 = 125
# 이 평균값이 새로운 축소된 픽셀 값으로 사용됩니다.
# 결과적으로, 이 영역을 축소하면 125라는 새로운 값이 됩니다.
