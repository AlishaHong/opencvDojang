import image_pre_processor as processor
import image_load_save as load_save
import numpy as np
import os

# 최종 실행 클래스
class MainController:
    def __init__(self, data_dir):
        self.loader_saver = load_save.ImageLoaderSaver(data_dir)
        self.processor = processor.ImagePreProcessor()

    # 이미지 처리 실행
    # 원하는 기능만 처리 가능
    def process_image(self, img_name, rotate_on=True, quadrants_on=True, random_crop_on=True, sb_on=True):
        img = self.loader_saver.load_image(img_name)
        
        if rotate_on:
            for angle in range(0, 361, 20):
                rotated_img = self.processor.rotate(img, angle)
                rotated_img_224 = self.processor.resize_image224(rotated_img)
                self.loader_saver.save_image(rotated_img_224, img_name, f'rotate_{angle}')
        
        if quadrants_on:
            quadrants = self.processor.crop_into_quadrants(img)
            for i, quadrant in enumerate(quadrants):
                cropped_img_224 = self.processor.resize_image224(quadrant)
                self.loader_saver.save_image(cropped_img_224, img_name, f'quadrant_{i+1}')

        if random_crop_on:
            for i in range(5):
                cropped_img = self.processor.random_crop(img)
                self.loader_saver.save_image(cropped_img, img_name, f'random_crop_{i+1}')

        if sb_on:
            for saturation in np.arange(0.4, 1.1, 0.1):
                for brightness in np.arange(0.4, 1.1, 0.1):
                    adjusted_img = self.processor.adjust_brightness_and_saturation(img, saturation, brightness)
                    self.loader_saver.save_image(adjusted_img, img_name, f'sb_{saturation:.1f}_{brightness:.1f}')
                    

# 메인함수
def main():
    data_path = os.path.join(os.getcwd(), '0912_exercise/data')
    controller = MainController(data_path)

    for img_name in controller.loader_saver.get_image_list():
        controller.process_image(img_name, sb_on=False, quadrants_on=True)

if __name__ == "__main__":
    main()