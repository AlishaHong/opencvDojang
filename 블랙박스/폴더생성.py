import os
from datetime import datetime
import schedule

folder_path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'
now = datetime.now()

folder_name = now.strftime('%Y%m%d' + '-' + str(now.hour) + '시')


def make_folder():
    if not os.path.exists(os.path.join(folder_path,folder_name)):
        os.makedirs(os.path.join(folder_path,folder_name))
        print(f"'{folder_name}' 폴더가 생성되었습니다.")
    else:
        print(f"'{folder_name}' 폴더가 이미 존재합니다.")


# make_folder()   #폴더 생성됨

schedule.every().hour.do(make_folder)

len = len(os.listdir(folder_path))


print(os.listdir(folder_path)[len-1])

