from UltraSingerCustom.src.UltraSinger import UltraSinger
from UltraSingerCustom.src.ScoreSettings import ScoreSettings

input_file = "./input/버즈-가시_INFO.txt"
audio_file = "./input/버즈-가시.mp3"
output_file = "./result"

settings = ScoreSettings("1", input_file, audio_file, output_file)
us = UltraSinger(settings)

score = us.analyze()
