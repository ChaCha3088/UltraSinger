"""Pitcher module"""

import crepe
from scipy.io import wavfile

from modules.console_colors import ULTRASINGER_HEAD, blue_highlighted, red_highlighted
from modules.Pitcher.pitched_data import PitchedData


def get_pitch_with_crepe_file(
    filename: str, model_capacity: str, step_size: int = 10, device: str = "cpu"
) -> PitchedData:
    """Pitch with crepe"""

    print(
        f"{ULTRASINGER_HEAD} Pitching with {blue_highlighted('crepe')} and model {blue_highlighted(model_capacity)} and {red_highlighted(device)} as worker"
    )
    sample_rate, audio = wavfile.read(filename)

    return get_pitch_with_crepe(audio, sample_rate, model_capacity, step_size)


def get_pitch_with_crepe(
    audio, sample_rate: int, model_capacity: str, step_size: int = 10
) -> PitchedData:
    """Pitch with crepe"""

    # Info: The model is trained on 16 kHz audio, so if the input audio has a different sample rate, it will be first resampled to 16 kHz using resampy inside crepe.

    times, frequencies, confidence, activation = crepe.predict(
        audio, sample_rate, model_capacity, step_size=step_size, viterbi=True
    )

    return PitchedData(times, frequencies, confidence)

# 변경
def get_pitched_data_with_high_confidence(
    pitched_data: PitchedData, threshold=0.4
) -> PitchedData:
    """Get frequency with high confidence"""

    print("변경")

    new_pitched_data = PitchedData([], [], [])

    for i, time in enumerate(pitched_data.times):
        new_pitched_data.times.append(pitched_data.times[i])
        new_pitched_data.confidence.append(pitched_data.confidence[i])

        if pitched_data.confidence[i] > threshold and pitched_data.frequencies[i] <= 880:
            new_pitched_data.frequencies.append(pitched_data.frequencies[i])
        else:
            new_pitched_data.frequencies.append(0)

    return new_pitched_data

# 변경
def get_frequencies_with_high_confidence(
    frequencies: list[float], confidences: list[float], threshold=0.4
) -> list[float]:
    """Get frequency with high confidence"""

    conf_f = []
    for i, conf in enumerate(confidences):
        if frequencies[i] <= 880 and conf > threshold:
            conf_f.append(frequencies[i])

    if not conf_f:
        conf_f = frequencies

    return conf_f


class Pitcher:
    """Docstring"""
