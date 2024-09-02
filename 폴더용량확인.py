import shutil

diskLabel = 'C:\\Users\\user\\Desktop\\REPOSITORY\\opencvDojang'
total, used, free = shutil.disk_usage(diskLabel)

print(total)
print(used)
print(free)

import os 

print(os.scandir('C:/Users/user/Desktop/REPOSITORY/opencvDojang'))


import os
from os.path import join, getsize
for root, dirs, files in os.walk('C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'):
    result = "%s : %.f MB in %d files." % (
        os.path.abspath(root),
        sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0), 
        len(files))
    print(result)
    folder_size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)
    print(sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0))
    
    
    if folder_size >= 5:
        print(files)
        oldest_file = files[0]
        print("Oldest file is: ", files[0])
        os.remove('C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox/' + oldest_file)




# import os
# from os.path import join, getsize

# # 'C:/Users/user/Desktop/REPOSITORY/opencvDojang' 폴더의 최상위 정보만 출력
# root_dir = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang'

# for root, dirs, files in os.walk(root_dir):
#     result = "%s : %.f MB in %d files." % (
#         os.path.abspath(root), 
#         sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0), 
#         len(files)
#     )
#     print(result)
#     break  # 첫 번째 결과만 출력하고 루프 종료





    for root, dirs, files in os.walk('C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'):
        folder_size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)

        print(folder_size)
        print(root)
        print(dirs)
        if folder_size >= 5:
            print(files)
            oldest_file = files[0]
            print("Oldest file is: ", files[0])
            os.remove('C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox/' + oldest_file)
            
            

path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'

for name in os.listdir(path):
    full_path = os.path.join(path, name)
    if os.path.getsize(full_path) > 5:
        os.remove(full_path)