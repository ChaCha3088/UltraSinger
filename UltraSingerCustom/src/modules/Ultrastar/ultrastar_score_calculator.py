"""Ultrastar score calculator."""

import librosa

from UltraSingerCustom.src.modules.console_colors import (
    ULTRASINGER_HEAD,
    blue_highlighted,
    cyan_highlighted,
    gold_highlighted,
    light_blue_highlighted,
    underlined,
)
from UltraSingerCustom.src.modules.Midi.midi_creator import create_midi_note_from_pitched_data
from UltraSingerCustom.src.modules.Ultrastar.ultrastar_converter import (
    get_end_time_from_ultrastar,
    get_start_time_from_ultrastar,
    ultrastar_note_to_midi_note,
)
from UltraSingerCustom.src.modules.Ultrastar.ultrastar_txt import UltrastarTxtValue
from UltraSingerCustom.src.modules.Pitcher.pitched_data import PitchedData

MAX_SONG_SCORE = 10000
MAX_SONG_LINE_BONUS = 1000


class Points:
    """Docstring"""

    notes = 0
    golden_notes = 0
    rap = 0
    golden_rap = 0
    line_bonus = 0
    parts = 0


def add_point(note_type: str, points: Points) -> Points:
    """Add calculated points to the points object."""

    if note_type == ":":
        points.notes += 1
    elif note_type == "*":
        points.golden_notes += 2
    elif note_type == "R":
        points.rap += 1
    elif note_type == "G":
        points.golden_rap += 2
    return points


class Score:
    """Docstring"""

    max_score = 0
    notes = 0
    golden = 0
    line_bonus = 0
    score = 0


def get_score(points: Points) -> Score:
    """Score calculation."""

    score = Score()
    score.max_score = points.parts
    score.notes = points.notes

    # notes / max_score를 소수 첫번째 자리에서 반올림
    score.score = round(score.notes / score.max_score * 100, 1)
    return score


def print_score(score: Score) -> None:
    """Print score."""

    print(
        f"{ULTRASINGER_HEAD} Total: {cyan_highlighted(str(score.score))}, notes: {blue_highlighted(str(score.notes))}, line bonus: {light_blue_highlighted(str(score.line_bonus))}, golden notes: {gold_highlighted(str(score.golden))}"
    )


def calculate_score(pitched_data: PitchedData, ultrastar_class: UltrastarTxtValue) -> (Score, Score):
    """Calculate score."""

    print(ULTRASINGER_HEAD + " Calculating Ultrastar Points")

    simple_points = Points()
    accurate_points = Points()

    reachable_line_bonus_per_word = MAX_SONG_LINE_BONUS / len(
        ultrastar_class.words
    )

    for i in enumerate(ultrastar_class.words):
        pos = i[0]
        if ultrastar_class.words == "":
            continue

        if ultrastar_class.noteType[pos] == "F":
            continue

        start_time = get_start_time_from_ultrastar(ultrastar_class, pos)
        end_time = get_end_time_from_ultrastar(ultrastar_class, pos)
        duration = end_time - start_time
        step_size = 0.09  # Todo: Whats is the step size of the game? Its not 1/bps -> one beat in seconds s = 60/bpm
        parts = int(duration / step_size)
        parts = 1 if parts == 0 else parts

        accurate_part_line_bonus_points = 0

        ultrastar_midi_note = ultrastar_note_to_midi_note(
            int(ultrastar_class.pitches[pos])
        )

        accurate_points.parts += parts

        for part in range(parts):
            start = start_time + step_size * part
            end = start + step_size
            if end_time < end or part == parts - 1:
                end = end_time
            pitch_note = create_midi_note_from_pitched_data(
                start, end, pitched_data
            )

            midi_note = librosa.note_to_midi(pitch_note)

            # 키 한개 차이는 okay!
            if abs(midi_note - ultrastar_midi_note) <= 1:
                accurate_points = add_point(
                    ultrastar_class.noteType[pos], accurate_points
                )

        if accurate_part_line_bonus_points >= parts:
            accurate_points.line_bonus += reachable_line_bonus_per_word

    return get_score(accurate_points)


def print_score_calculation(accurate_points: Score) -> None:
    """Print score calculation."""

    print(
        f"{ULTRASINGER_HEAD} {underlined('Accurate (octave high matches)')} points:"
    )
    print_score(accurate_points)
