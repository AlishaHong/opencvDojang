# 클래스별로 데이터 증식 조건이 다를수 있다! 
# 1. 배경 : 흰색책상, 나무색책상
# 2. 데이터 증식조건 
#   2.0. 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자.(이미지 사이즈는 224*224)
#           대상물 촬영을 어떻게 해야할지 확인
#   2.1. 회전(10~30도)범위 안에서 어느정도 각도를 넣어야 인식이 잘되는가?
#   2.2. hflip, vflip 도움이 되는가? 넣을 것인가?
#       물체에 따라서 회전하는 범위를 다르게 하는것이 좋다. ex 자동자는 뒤집힐 일이 별로 없음.. 
#   2.3. resize, crop : 가능하면 적용해보자. 
#   2.4. 파일명을 다르게 저장 cf) jelly_wood.jpg, jelly_white.jpg 
#           jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg, jelly_wood_resize.jpg 
#   2.5. 클래스 별로 폴더를 생성
#   2.6. 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약 
#   2.7. 최종 이미지 사이즈는 224*224


# 구성순서 
# 1. 촬영한다.
# 2. 이미지를 컴퓨터로 복사, resize 한다. 
# 3. 육안으로 확인, 이렇게 사용해도 되는가? 
# 4. 함수들을 만든다. rotate, hflip, vflip, resize, crop, 원본파일명을 읽어서 파일명을 생성하는 기능
#       파일명을 생성하는 기능은 모든 함수안에 넣으면 될듯(함수안의 함수)
# 5. 단일 함수 검증을 먼저한다.
# 6. 함수를 활용해서 기능 구현 
# 7. 테스트(경우의 수 전부 테스트해보기)
# 8. 데이터셋을 teachable machine 사이트에 올려서 테스트! (폴더로 넣을 수 있으니 이미지별로 폴더 생성)
    

import cv2
import numpy as np
import sys
import os
import glob
import random
import numpy as np



# jpg 원본 리스트 불러오기
# 강사님 리뷰때는 dataPath와 dataOrg는 전역변수로 뺐음 
# fileNames는 메인함수의 뺌 
# 클래스로 만들때도 편할 듯 
def getImageList():
    global dataPath
    dataPath = os.path.join(os.getcwd(), '0912_exercise\data')
    # print(dataPath)
    dataOrg = os.path.join(dataPath, 'dataOrg')
    # print(dataOrg)
    fileNames = glob.glob(os.path.join(dataOrg ,'*.jpg'))
    # print(fileNames)
    return fileNames
    
    
# 이미지 읽기
def load_image_by_name(imgName):
    fileNames = getImageList()
    # baseName = os.path.basename(imgName)
    # print(fileNames)
    for fileName in fileNames:
        if imgName in fileName:
            # print(fileName)
            img = cv2.imread(fileName)
            if img is None:
                sys.exit(f"{imgName} 파일이 없어요!")
            return img
    # sys.exit(f"{imgName} 파일이 없어요!")


# 이미지 사이즈 조절하기 
# 기본 사이즈(224*224)
def resize_image224(img, width=224, height=224):
    resized_img224 = cv2.resize(img, (width, height))
    return resized_img224

# 확장 사이즈(400*400)
def resize_image400(img, width=400, height=400):
    resize_image400 = cv2.resize(img, (width, height))
    return resize_image400


# 이미지 출력(리사이즈된 이미지) - 이제 출력은 필요없엉
def show_image(imgName):
    img = load_image_by_name(imgName)
    # resized_img224 = resize_image224(img)
    resized_img400 = resize_image400(img)
    return resized_img400


# 저장 경로 생성 함수
# (파일명에 따라서 저장폴더를 생성해주는 함수를 만들어 볼 예정)
# 리팩토링 완료
# keyboard하나 당 2개의 이미지가 존재함
# keyboard1_white/keyboard1_wood 
# '_' 문자로 앞뒤를 분리하여 앞의 단어를 기준으로 폴더를 생성하는 방식으로 코드를 수정함 
# _로 분리된 이미지명일 경우에만 유효함 

def make_save_path(imgName, pre_img_str):
    # imgName에서 "_" 앞의 텍스트를 폴더명으로 사용
    folder_name = imgName.split('_')[0]
    # 저장할 디렉터리 경로 생성
    data_pre_path = os.path.join(os.getcwd(), f'0912_exercise/data/{folder_name}')
    # 경로가 없으면 생성
    if not os.path.exists(data_pre_path):
        os.makedirs(data_pre_path)
    # 파일 경로 생성
    makeNewFileName = os.path.join(data_pre_path, f'{imgName}_{pre_img_str}.jpg')
    
    return makeNewFileName

# 이미지 저장 함수
def save_image(img, imgName, pre_img_str):
    save_path = make_save_path(imgName, pre_img_str) 
    cv2.imwrite(save_path,img)

# rotate 함수
def rotate(img, angle):
    (h,w) = img.shape[:2]
    centerPt = (w//2, h//2)
    rot = cv2.getRotationMatrix2D(centerPt, angle, 1.0)   #center/angle/scale
    dst = cv2.warpAffine(img,rot,(w,h))
    return dst


# crop 함수
# 부분별로 잘라서 일부가 나와도 인식이 잘 되도록 학습하기 위한 이미지 생성
def crop_selectROI(imgName):
    img = show_image(imgName)
    roi = cv2.selectROI(img)
    if roi != (0,0,0,0):
        croped_img = img[roi[1]: roi[1]+roi[3],
                         roi[0]: roi[0]+roi[2]]
        return croped_img
        
# crop 함수 
# 4등분하기
def crop_into_quadrants(img,imgName):
        (h, w) = img.shape[:2]
        center_x, center_y = w // 2, h // 2

        quadrants = [
        # 네 등분으로 자르기(BY 진성)
        img[0:center_y, 0:center_x],
        img[0:center_y, center_x:w],
        img[center_y:h, 0:center_x],
        img[center_y:h, center_x:w]
        ]
        return quadrants


# 랜덤 크롭(편함!)
def random_crop(img, crop_size=(224, 224)):
    h, w = img.shape[:2]  # 이미지의 높이와 너비
    crop_h, crop_w = crop_size

    # 크롭할 이미지의 시작 좌표를 랜덤으로 선택
    if h > crop_h and w > crop_w:
        x = random.randint(0, w - crop_w)
        y = random.randint(0, h - crop_h)

        # 이미지 크롭
        cropped_img = img[y:y+crop_h, x:x+crop_w]
        return cropped_img
    else:
        sys.exit('error')


# 채도와 명도 조절해보기
def adjust_brightness_and_saturation(image, saturation_scale, brightness_scale):
    # 밝기 조정 (BGR -> HSV 변환 후 처리)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    
    v = cv2.multiply(v, brightness_scale)
    s = cv2.multiply(s, saturation_scale)
    
    adjusted_hsv_image = cv2.merge([h, s, v])
    adjusted_bgr_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)
    
    return adjusted_bgr_image


# 이미지 전처리 함수 모두 실행
def pre(imgName):
    resized_img = show_image(imgName)
    global cropped_img
    # rotate
    # rotate함수에 필요한 각도 리스트 
    angles = []
    for i in range(361):
        if i % 20 == 0:     # 이렇게 안해도..될듯  for i in range(0,361,20)
            angles.append(i)
            
    # angles 리스트의 모든 각도에 대해 돌려보자 
    for angle in angles:
        rotated_img = rotate(resized_img, angle)
        rotated_img_224 = resize_image224(rotated_img, width = 224, height = 224)
        save_image(rotated_img_224, imgName, f'rotate_{angle}')

    # 4등분하기
    quadrants = crop_into_quadrants(resized_img,imgName)
    for i, quadrant in enumerate(quadrants):
        cropped_img_224 = resize_image224(quadrant)
        save_image(cropped_img_224, imgName, f'quadrant_{i+1}')

    # 원하는 영역 자르기(selectROI)
    # 좀 더 디테일하게 이미지를 자르고 싶을 때 사용하자
    for i in range(2):
        cropped_img = crop_selectROI(imgName)
        cropped_img_224 = resize_image224(cropped_img)
        save_image(cropped_img_224, imgName, f'crop_{i+1}')
        cv2.imshow(f'crop_{i}', cropped_img_224)
        cv2.waitKey()
        cv2.destroyAllWindows()  

    # 이미지에서 랜덤 크롭  
    for i in range(20):  # 20개의 랜덤 크롭을 생성
        cropped_img = random_crop(resized_img)
        save_image(cropped_img, imgName, f'random_crop_{i+1}')  # 저장

    # 채도, 명도 조절
    saturation_scale = []
    brightness_scale = []
    for i in np.arange(0.4, 1.1, 0.1):  # 0.4에서 1.0까지 포함
        i = format(i, ".1f")  # 소수점 첫째 자리까지 문자열로 고정
        brightness_scale.append(float(i))
        saturation_scale.append(float(i))

    # 채도, 명도 조절하면서 rotate 결과값도 함께 for문! 모든 각도에서 채도 명도 조절 가능 (엄청 많이 나옴)
    for saturation in saturation_scale:
        for brightness in brightness_scale:
            for angle in angles:
                adjusted_img = adjust_brightness_and_saturation(rotated_img_224, saturation, brightness)
                save_image(adjusted_img, imgName, f'brightness_saturation_{saturation}_{brightness}_rotate_{angle}')
    



# 메인 함수 
def main():
    fileNames = getImageList()
    for filename in fileNames:
        basename = os.path.basename(filename)
        imgname, _ = os.path.splitext(basename)
        pre(imgname) #0이 파일명/1은 확장자
        

    
if __name__ == "__main__":
    main()
    
    
    

# 현재 2번 키보드 3번 키보드 분별에 문제가 있다. 
# 색상이 비슷한 키보드이기 때문에 구분하기 어려운데 심지어 웹캠의 화질이 좋지 않아서 색 구분을 할 수 없었다. 
# 이미지를 흐릿하게 만들어서 학습시키면 화질이 좋지않은 환경에서도 인식이 잘 되지 않을까 하는 기대를 가져본다! 

# 강사님의 캠으로 테스트해보았지만 화질이 좋아진다고해서 크게 성능이 향상되지는 않았다.
# 잘못 인식한 각도+색상 상태의 이미지를 캡쳐해서 추가로 학습시켜주니 잘 되서 허무했다. -> 과적합 위험
# 일단 그렇게 학습시킨 데이터들은 별도로 빼놓고 
# 채도와 명도를 조금씩 바꿔가면서 많은 데이터를 넣어봤지만 부족.. (무려 5000장인데..)

# 밝기만 조절해 볼 예정 
# 안되면 살짝씩 블러 처리를 해서 학습시켜 볼 예정 
# random croping도 마우스로 원하는 영역을 설정할 수 있다고 하는데 알아봐야겠다. 
# 우선은 우리 교재에 나온 selectROI 적용해봤는데 좀 귀찮다. 

# random gamma / rangom brightness / random erasing이건 뭐지! 
# 이호성님 블로그를 보니 별천지다







# 이미지 이름을 명시해야 했던 지난 함수 


# 저장 경로 생성 함수
# (파일명에 따라서 저장폴더를 생성해주는 함수를 만들어 볼 예정)
# def make_save_path(imgName, pre_img_str):
#     print(f'imgName : {imgName}')
#     # imgName에 포함된 키워드로 경로 설정
#     if 'keyboard1' in imgName:
#         folder_name = 'keyboard1'
#     elif 'keyboard2' in imgName:
#         folder_name = 'keyboard2'
#     elif 'keyboard3' in imgName:
#         folder_name = 'keyboard3'
#     else:
#         folder_name = 'others'
#     # 저장할 디렉터리 경로 생성
#     dataPrePath = os.path.join(os.getcwd(), f'0912_exercise/data/{folder_name}')
#     # 경로가 없으면 생성
#     if not os.path.exists(dataPrePath):
#         os.makedirs(dataPrePath)

#     # 파일 경로 생성
#     makeNewFileName = os.path.join(dataPrePath, f'{imgName}_{pre_img_str}.jpg')
#     return makeNewFileName


# 각 이미지에 대한 전처리 실행 함수 
# def keyboard1_white():
#     imgName = "keyboard1_white"
#     pre(imgName)
    
# def keyboard1_wood():
#     imgName = "keyboard1_wood"
#     pre(imgName)

# def keyboard2_white():
#     imgName = "keyboard2_white"
#     pre(imgName)

# def keyboard2_wood():
#     imgName = "keyboard2_wood"
#     pre(imgName)

# def keyboard3_white():
#     imgName = "keyboard3_white"
#     pre(imgName)

# def keyboard3_wood():
#     imgName = "keyboard3_wood"
#     pre(imgName)




# def main():
    # keyboard1_white()
    # keyboard1_wood()
    # keyboard2_white()
    # keyboard2_wood()
    # keyboard3_white()
    # keyboard3_wood()


    # pre('keyboard1_white')
    # pre('keyboard1_wood')
    # pre('keyboard2_white')
    # pre('keyboard2_wood')
    # pre('keyboard3_white')
    # pre('keyboard3_wood')