import cv2
import numpy as np
import sys
import os
import glob
import random

class ImageProcessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.file_names = self.get_image_list()
        
    # jpg 원본 리스트 불러오기
    def get_image_list(self):
        data_org = os.path.join(self.data_dir, 'dataOrg')
        file_names = glob.glob(os.path.join(data_org, '*.jpg'))
        return file_names
    
    # 이미지 읽기
    def load_image_by_name(self, img_name):
        for file_name in self.file_names:
            if img_name in file_name:
                print(file_name)
                img = cv2.imread(file_name)
                if img is None:
                    sys.exit('Image load failed')
                return img
        sys.exit(f"{img_name} 파일이 없어요!")

    # 이미지 사이즈 조절하기 
    # 기본 사이즈(224*224)
    def resize_image224(self, img, width=224, height=224):
        return cv2.resize(img, (width, height))

    # 조금 더 큰 사이즈(400*400)
    def resize_image400(self, img, width=400, height=400):
        return cv2.resize(img, (width, height))
    
    # 저장 경로 생성 함수
    # 리팩토링 완료
    # keyboard하나 당 2개의 이미지가 존재함
    # keyboard1_white/keyboard1_wood 
    # '_' 문자로 앞뒤를 분리하여 앞의 단어를 기준으로 폴더를 생성하는 방식으로 코드를 수정함 
    # _로 분리된 이미지명일 경우에만 유효함 
    def make_save_path(self, imgName, pre_img_str):
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
    def save_image(self, img, img_name, pre_img_str):
        save_path = self.make_save_path(img_name, pre_img_str)
        cv2.imwrite(save_path, img)

    # rotate 함수
    def rotate(self, src, angle):
        (h, w) = src.shape[:2]
        center_pt = (w // 2, h // 2)
        rot = cv2.getRotationMatrix2D(center_pt, angle, 1.0)   # center/angle/scale
        return cv2.warpAffine(src, rot, (w, h))
            
    # crop 함수
    # 부분별로 잘라서 일부가 나와도 인식이 잘 되도록 학습하기 위한 이미지 생성
    def crop_selectROI(self, img):
        roi = cv2.selectROI(img)
        if roi != (0,0,0,0):
            croped_img = img[roi[1]: roi[1]+roi[3],
                            roi[0]:roi[0]+roi[2]]
            return croped_img       
          
    # crop 함수 
    # 4등분하기
    def crop_into_quadrants(self,img):
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
            
    # 랜덤 크롭(이미지보다 크롭 크기가 클 경우, 크롭 크기를 이미지 크기에 맞게 조정)
    def random_crop(self, img, crop_size=(224, 224)):
        h, w = img.shape[:2]  # 이미지의 높이와 너비
        crop_h, crop_w = crop_size

        # 이미지보다 크롭 크기가 클 경우 크롭 크기를 이미지 크기로 맞추기
        if crop_h > h or crop_w > w:
            crop_h = min(crop_h, h)
            crop_w = min(crop_w, w)

        # 크롭할 이미지의 시작 좌표를 랜덤으로 선택
        x = random.randint(0, w - crop_w)
        y = random.randint(0, h - crop_h)

        # 이미지 크롭
        cropped_img = img[y:y + crop_h, x:x + crop_w]
        return cropped_img

    # 채도와 명도 조절
    def adjust_brightness_and_saturation(self, image, saturation_scale, brightness_scale):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        
        v = cv2.multiply(v, brightness_scale)
        s = cv2.multiply(s, saturation_scale)
        
        adjusted_hsv_image = cv2.merge([h, s, v])
        return cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)

    # 전처리 과정 실행
    # 원하는 기능만 실행하도록 boolean값 줌 
    def process_image(self, img_name, rotate_on = True, quadrants_on = True, select_roi_on = True, random_crop_on = True, sb_on = True):
        img = self.load_image_by_name(img_name)
        resize_image224 = self.resize_image224(img)
        resize_image400 = self.resize_image400(img)
        
        
        # 회전 각도 적용
        if rotate_on:
            angles = range(0, 361, 20)
            for angle in angles:
                rotated_img = self.rotate(resize_image400, angle)
                rotated_img_224 = self.resize_image224(rotated_img, width=224, height=224)
                self.save_image(rotated_img_224, img_name, f'rotate_{angle}')

        # 4등분하기
        if quadrants_on:
            quadrants = self.crop_into_quadrants(resize_image400)
            for i, quadrant in enumerate(quadrants):
                cropped_img_224 = self.resize_image224(quadrant)
                self.save_image(cropped_img_224, img_name, f'quadrant_{i+1}')
            
        # 랜덤 크롭
        if random_crop_on:
            for i in range(20):
                cropped_img = self.random_crop(resize_image400)
                self.save_image(cropped_img, img_name, f'random_crop_{i+1}')

        # 좀 더 디테일하게 이미지를 자르고 싶을 때 사용하자
        if select_roi_on:
            for i in range(5):
                cropped_img = self.crop_selectROI(resize_image400)
                cropped_img_224 = self.resize_image224(cropped_img)
                self.save_image(cropped_img_224, img_name, f'crop_{i+1}')
                cv2.imshow(f'crop_{i+1}', cropped_img_224)
                cv2.waitKey()
                cv2.destroyAllWindows()  
            
        # 채도, 명도 조절
        if sb_on:
            saturation_scale = np.arange(0.4, 1.1, 0.1)
            brightness_scale = np.arange(0.4, 1.1, 0.1)

            for saturation in saturation_scale:
                for brightness in brightness_scale:
                    for angle in angles:
                        adjusted_img = self.adjust_brightness_and_saturation(rotated_img_224, saturation, brightness)
                        self.save_image(adjusted_img, img_name, f'brightness_saturation_{saturation:.1f}_{brightness:.1f}_rotate_{angle}')

# 메인 실행 함수
def main():
    data_path = os.path.join(os.getcwd(), '0912_exercise/data')
    processor = ImageProcessor(data_path)   # 객체 생성

    for file_name in processor.file_names:
        basename = os.path.basename(file_name)
        img_name, _ = os.path.splitext(basename)
        processor.process_image(img_name, sb_on = False, select_roi_on=False)
        # 필요하지 않은 기능은 Fasle로 바꿔서 전처리 기능을 실행하지 않음
if __name__ == "__main__":
    main()







# def main():
#     data_path = os.path.join(os.getcwd(), '0912_exercise/data')
#     processor = ImageProcessor(data_path)   # 객체 생성
    
#     # 각 이미지에 대한 전처리 실행
#     processor.process_image("keyboard1_white")
#     processor.process_image("keyboard1_wood")
#     processor.process_image("keyboard2_white")
#     processor.process_image("keyboard2_wood")
#     processor.process_image("keyboard3_white")
#     processor.process_image("keyboard3_wood")