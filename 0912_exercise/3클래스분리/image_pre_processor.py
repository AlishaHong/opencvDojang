import cv2
import numpy as np
import random


# 이미지 전처리 클래스
class ImagePreProcessor:
    def __init__(self):
        pass

    # 이미지 리사이즈 (기본 사이즈 224x224)
    def resize_image224(self, img, width=224, height=224):
        return cv2.resize(img, (width, height))

    # 이미지 리사이즈 (400x400)
    def resize_image400(self, img, width=400, height=400):
        return cv2.resize(img, (width, height))

    # 이미지 회전
    def rotate(self, img, angle):
        (h, w) = img.shape[:2]
        center_pt = (w // 2, h // 2)
        rot = cv2.getRotationMatrix2D(center_pt, angle, 1.0)
        return cv2.warpAffine(img, rot, (w, h))

    # 이미지 네 등분
    def crop_into_quadrants(self, img):
        (h, w) = img.shape[:2]
        center_x, center_y = w // 2, h // 2
        quadrants = [
            img[0:center_y, 0:center_x],
            img[0:center_y, center_x:w],
            img[center_y:h, 0:center_x],
            img[center_y:h, center_x:w]
        ]
        return quadrants

    # 랜덤 크롭
    def random_crop(self, img, crop_size=(224, 224)):
        h, w = img.shape[:2]
        crop_h, crop_w = crop_size
        if crop_h > h or crop_w > w:
            crop_h = min(crop_h, h)
            crop_w = min(crop_w, w)

        x = random.randint(0, w - crop_w)
        y = random.randint(0, h - crop_h)
        return img[y:y + crop_h, x:x + crop_w]

    # 채도와 밝기 조절
    def adjust_brightness_and_saturation(self, img, saturation_scale, brightness_scale):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)
        s = cv2.multiply(s, saturation_scale)
        v = cv2.multiply(v, brightness_scale)
        adjusted_hsv = cv2.merge([h, s, v])
        return cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)