from UltraSingerCustom.src.UltraSinger import UltraSinger
from UltraSingerCustom.src.BatchSettings import BatchSettings

# 3. 파일명을 가지고 MySettings 객체를 생성한다.
settings = BatchSettings("../youtubeFile" + "버즈-가시.m4a", "../output")

# 4. UltraSinger 객체를 생성한다.
us = UltraSinger(settings)

# 5. UltraSinger 객체의 run 메서드를 호출한다.
us.run()
