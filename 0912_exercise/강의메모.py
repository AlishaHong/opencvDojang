import cv2,sys
import numpy as np
import os
from glob import glob
import shutils  #sh = shell 
from enum import Enum

# 클래스에 내장될 기능을 번호로 설정
class funcNum(Enum):
    
    resize = 1
    rotate = 2
    hflip = 3
    vflip = 4
    crop = 5
    

dataPath = os.path.join(os.getcwd(),'0912_exercise\data')
dataOrg = os.path.join(dataPath,'dataOrg')


# 파일 확장명이 여러개일때 
# img_type = ['jpg','png','gif','jpeg'] 이런식으로 리스트로 만들어서 전달하면 된다. 

# input : dataPath
# output : dataPath안의 jpg파일의 리스트를 가져온다.
# glob함수를 쓸땐 리스트를 직접 넣을 수 는 없고 for문 돌려야함 

# 파일을 가져오는 함수
def getFileList(dataPath):
# 확장자 여러개일때 
#def getFileList(dataPath, img_type):
    pass


# 이미지를 불러오는 함수
def readImg(imagePath):
    img = cv2.imread(imagePath)
    if img is None:
        sys.exit(f'Image load failed: {imagePath}')
    return img

img = readImg(dataPath)    
    
    
    
# 강제로 지우기 

classList = ['airPod', 'whitePen','blackPen','CarKey'] 
def createFolder():
    for classname in classList:
        # 기존에 폴더가 있으면 삭제하고 새로 생성
        # 폴더안에 파일이 존재하더라도 파일과 폴더를 모두 삭제 
        # if os.path.exists(os.path.join(dataOrg, classname)):
        #     shutils.rmtree(os.path.join(dataOrg, classname))
        # os.makedirs(os.path.join(dataOrg, classname))
        classPath = os.path.join(dataOrg, classname)
        shutils.rmtree(classPath)
        os.makedirs(classPath, exist_ok=True)



# DEBUG = True

# if DEBUG:
#     for fileName in fileNames:
#         print(fileName)

