import os

from src.UltraSinger import UltraSinger
from src.MySettings import MySettings

# 1. 파일명 리스트를 입력받는다.
input_file_list = os.listdir("../youtubeFile")
output_file_list = os.listdir("../output")

# 2. 파일명 리스트를 순회하면서
for i, file in enumerate(input_file_list):
    # output 폴더에 있는 파일은 건너뛴다.
    file_name_without_ext = file.replace(".m4a", "")
    if file_name_without_ext in output_file_list:
        continue

    # 3. 파일명을 가지고 MySettings 객체를 생성한다.
    settings = MySettings("../youtubeFile/" + file, "../output")

    # 4. UltraSinger 객체를 생성한다.
    us = UltraSinger(settings)

    # 5. UltraSinger 객체의 run 메서드를 호출한다.
    us.run()