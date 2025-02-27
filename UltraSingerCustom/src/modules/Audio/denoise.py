"""Reduce noise from audio"""

import ffmpeg

from UltraSingerCustom.src.modules.console_colors import ULTRASINGER_HEAD, blue_highlighted


def ffmpeg_reduce_noise(input_file_path: str, output_file: str) -> None:
    """Reduce noise from vocal audio with ffmpeg."""

    # Denoise audio samples with FFT.
    # A description of the accepted parameters follows.

    # noise_reduction, nr
    #    Set the noise reduction in dB, allowed range is 0.01 to 97. Default value is 12 dB.
    # noise_floor, nf
    #    Set the noise floor in dB, allowed range is -80 to -20. Default value is -50 dB.
    # track_noise, tn
    #    Enable noise floor tracking. By default is disabled.
    #    With this enabled, noise floor is automatically adjusted.

    print(
        f"{ULTRASINGER_HEAD} Reduce noise from vocal audio with {blue_highlighted('ffmpeg')}."
    )
    try:
        (
            ffmpeg.input(input_file_path)
            .output(output_file, af="afftdn=nr=70:nf=-80:tn=1")
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as ffmpeg_exception:
        print("ffmpeg stdout:", ffmpeg_exception.stdout.decode("utf8"))
        print("ffmpeg stderr:", ffmpeg_exception.stderr.decode("utf8"))
        raise ffmpeg_exception
