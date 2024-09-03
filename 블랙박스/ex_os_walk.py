    
import os
from os.path import join, getsize


path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'

for root, dirs, files in os.walk(path):
    folder_size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)

    print(root)   
    print(dirs)     #하위폴더
    print(files)    
    
    

# os.path.islink(path)
# 바로가기 링크인지 확인함 

