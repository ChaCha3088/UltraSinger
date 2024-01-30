"""Ultrastar txt parser"""

from UltraSingerCustom.src.modules.console_colors import ULTRASINGER_HEAD
from UltraSingerCustom.src.modules.Ultrastar.ultrastar_converter import (
    get_end_time_from_ultrastar,
    get_start_time_from_ultrastar,
)
from UltraSingerCustom.src.modules.Ultrastar.ultrastar_txt import UltrastarTxtValue, UltrastarTxtTag, UltrastarTxtNoteTypeTag, FILE_ENCODING

def parse_ultrastar_txt(input_file: str) -> UltrastarTxtValue:
    """Parse ultrastar txt file to UltrastarTxt class"""
    print(f"{ULTRASINGER_HEAD} Parse ultrastar txt -> {input_file}")

    # 주목 원본 파일을 읽습니다.
    with open(input_file, "r", encoding=FILE_ENCODING) as file:
        txt = file.readlines()

    # 주목 UltrastarTxtValue 클래스를 생성합니다.
    ultrastar_class = UltrastarTxtValue()
    count = 0

    # Strips the newline character
    for line in txt:
        count += 1

        # 주목 #으로 시작하는 줄은 곡에 대한 정보를 담고 있습니다.
        if line.startswith("#"):
            if line.startswith(f"#{UltrastarTxtTag.ARTIST}"):
                ultrastar_class.artist = line.split(":")[1].replace("\n", "")
            elif line.startswith(f"#{UltrastarTxtTag.TITLE}"):
                ultrastar_class.title = line.split("-")[1].replace(" [Karaoke]", "").replace("\n", "")
            elif line.startswith(f"#{UltrastarTxtTag.MP3}"):
                ultrastar_class.mp3 = line.split(":")[1].replace("\n", "").replace(" [Karaoke]", "")
            elif line.startswith(f"#{UltrastarTxtTag.AUDIO}"):
                ultrastar_class.audio = line.split(":")[1].replace("\n", "")
            elif line.startswith(f"#{UltrastarTxtTag.VIDEO}"):
                ultrastar_class.video = line.split(":")[1].replace("\n", "")
            elif line.startswith(f"#{UltrastarTxtTag.GAP}"):
                ultrastar_class.gap = line.split(":")[1].replace("\n", "")
            elif line.startswith(f"#{UltrastarTxtTag.BPM}"):
                ultrastar_class.bpm = line.split(":")[1].replace("\n", "")

        # 주목 노트에 대한 정보를 담고 있습니다.
        elif line.startswith((
                f"{UltrastarTxtNoteTypeTag.FREESTYLE} ",
                f"{UltrastarTxtNoteTypeTag.NORMAL} ",
                f"{UltrastarTxtNoteTypeTag.GOLDEN} ",
                f"{UltrastarTxtNoteTypeTag.RAP} ",
                f"{UltrastarTxtNoteTypeTag.RAP_GOLDEN} ")):
            parts = line.split()
            # [0] F : * R G
            # [1] start beat
            # [2] duration
            # [3] pitch
            # [4] word

            ultrastar_class.noteType.append(parts[0])
            ultrastar_class.startBeat.append(parts[1])
            ultrastar_class.durations.append(parts[2])
            ultrastar_class.pitches.append(parts[3])
            ultrastar_class.words.append(parts[4] if len(parts) > 4 else "")

            # do always as last
            pos = len(ultrastar_class.startBeat) - 1
            ultrastar_class.startTimes.append(
                # 주목 시작 시간을 계산합니다.
                get_start_time_from_ultrastar(ultrastar_class, pos)
            )
            ultrastar_class.endTimes.append(
                # 주목 끝 시간을 계산합니다.
                get_end_time_from_ultrastar(ultrastar_class, pos)
            )
            # todo: Progress?

    return ultrastar_class
