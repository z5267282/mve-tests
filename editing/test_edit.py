'''Note that neither `moviepy` nor `ffmpeg` can direclty check for errors.
Hence only working timestamps are tested'''

import mve.src.lib.edit as edit


OUT = 'outputs'
SRC = '../videos/03.mp4'

# TESTS


def test_good_seconds_start_end():
    helper('start end', '4', '10')


def test_good_timestamp():
    helper('2 timestamps', '00:25', '00:30')


def test_good_positive_second():
    helper('only start', '01:01')


def test_good_negative_end():
    helper('negative end', '-4')


# HELPERS


def generate_out_name(name):
    return f'{OUT}/{name}.mp4'


def helper(name, start, end=None):
    output_name = generate_out_name(name)
    print(start, end)
    edit.edit_video(False, 4, SRC, output_name, start, end)
