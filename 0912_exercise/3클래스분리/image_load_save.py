import os
import cv2
import sys

class ImageLoaderSaver:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.file_names = self.get_image_list()

    # 이미지 목록 가져오기
    def get_image_list(self):
        data_org = os.path.join(self.data_dir, 'dataOrg')
        return [os.path.basename(f) for f in os.listdir(data_org) if f.endswith('.jpg')]

    # 이미지 로드
    def load_image(self, img_name):
        img_path = os.path.join(self.data_dir, 'dataOrg', img_name)
        img = cv2.imread(img_path)
        if img is None:
            sys.exit(f"{img_name} 파일이 없습니다!")
        return img

    # 저장 경로 생성
    def make_save_path(self, img_name, pre_img_str):
        folder_name = img_name.split('_')[0]
        save_dir = os.path.join(self.data_dir, folder_name)
        os.makedirs(save_dir, exist_ok=True)
        return os.path.join(save_dir, f"{img_name}_{pre_img_str}.jpg")

    # 이미지 저장
    def save_image(self, img, img_name, pre_img_str):
        save_path = self.make_save_path(img_name, pre_img_str)
        cv2.imwrite(save_path, img)