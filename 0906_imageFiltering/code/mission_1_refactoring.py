import cv2
import sys
import numpy as np

# 이미지 읽기 함수
def load_image(filepath):
    img = cv2.imread(filepath)
    if img is None:
        sys.exit('이미지를 불러올 수 없습니다.')
    return img

# 필터 적용 함수 (Median, Bilateral, Fast Denoising, Sharpening)

# 효과 없었음
def apply_median_blur(image, ksize):
    return cv2.medianBlur(image, ksize)

# 효과 없었음
def apply_bilateral_filter(image, d, sigmaColor, sigmaSpace):
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

# 1차 필터링 
def apply_fast_denoising(image, h, hForColor, templateWindowSize, searchWindowSize):
    return cv2.fastNlMeansDenoisingColored(image, None, h, hForColor, templateWindowSize, searchWindowSize)

# 샤프닝 
def apply_sharpening(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# 밝기 및 채도 조정 함수
def adjust_brightness_and_saturation(image, brightness_adjust=-20, saturation_scale=0.90, brightness_scale=0.65):
    # 밝기 조정 (BGR -> HSV 변환 후 처리)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    
    v = cv2.multiply(v, brightness_scale)
    s = cv2.multiply(s, saturation_scale)
    
    adjusted_hsv_image = cv2.merge([h, s, v])
    adjusted_bgr_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)
    
    return adjusted_bgr_image

# 결과 저장 함수
def save_image(filepath, image):
    cv2.imwrite(filepath, image)

# 메인 함수
def main():
    # 이미지 불러오기
    filepath = '0906_imageFiltering/data/01.png'
    src = load_image(filepath)

    # 다양한 필터링 적용
    dst_median = apply_median_blur(src, 5)
    dst_bilateral = apply_bilateral_filter(src, 10, 75, 75)
    fast_dst = apply_fast_denoising(src, 8, 8, 7, 21)

    # 샤프닝 필터 적용 (두 가지 커널 제공)
    kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    kernel_sharpening2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    sharpened_image_fast_dst = apply_sharpening(fast_dst, kernel_sharpening2)

    # 밝기 및 채도 조정
    final_image = adjust_brightness_and_saturation(sharpened_image_fast_dst)

    # 결과 저장
    save_image('0906_imageFiltering/data/mission1_complete.png', final_image)

    # 결과 출력
    cv2.imshow('Original', src)
    cv2.imshow('Median Blur', dst_median)
    cv2.imshow('Bilateral Filter', dst_bilateral)
    cv2.imshow('Fast Denoising', fast_dst)
    cv2.imshow('Sharpened Image', sharpened_image_fast_dst)
    cv2.imshow('Adjusted Brightness & Saturation', final_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()