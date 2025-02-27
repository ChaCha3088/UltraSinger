"""Separate vocals from audio"""

import subprocess

from UltraSingerCustom.src.modules.console_colors import (
    ULTRASINGER_HEAD,
    blue_highlighted,
    red_highlighted,
)
from UltraSingerCustom.src.modules.os_helper import current_executor_path, move, path_join


def separate_audio(input_file_path: str, output_file: str, device="cpu") -> None:
    """Separate vocals from audio with demucs."""

    print(
        f"{ULTRASINGER_HEAD} Separating vocals from audio with {blue_highlighted('demucs')} and {red_highlighted(device)} as worker."
    )

    separated_path = input_file_path.split(".")[0] + "/" + "separated"

    # Model selection?
    # -n htdemucs_ft
    subprocess.run(
        ["demucs", "-d", device, "--two-stems=vocals", "--float32", input_file_path, "-o", separated_path]
    )
    # separated_folder = path_join(current_executor_path(), "separated")
    separated_folder = separated_path
    move(separated_folder, output_file)
