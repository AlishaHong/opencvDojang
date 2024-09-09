import cv2
import matplotlib.pyplot as plt


# 히스토그램 가져오기 
def histogram_gray(src):
    hist = cv2.calcHist([src], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()
    
    
    
