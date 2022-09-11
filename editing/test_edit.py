from subprocess import CalledProcessError

import edit
import pytest

# HELPERS

OUT = 'outputs'
def generate_out_name(name):
    global OUT
    return f'{OUT}/{name}.mp4'

SRC = '../videos/03.mp4'
def helper(name, start, end=None):
    output_name = generate_out_name(name)
    edit.edit_video(SRC, output_name, start, end)

BAD = generate_out_name('bad')
def bad_helper(start, end):
    with pytest.raises(CalledProcessError):
        edit.edit_video(SRC, BAD, start, end)

def test_good_seconds_start_end():
    helper('start end', '2', '4')

def test_good_timestamp():
    helper('2 timestamps', '00:22', '00:24')

def test_good_positive_second():
    helper('only start', '60')

def test_good_negative_end():
    helper('negative end', '-4')
