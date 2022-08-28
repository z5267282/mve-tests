from subprocess import CalledProcessError

import edit
import pytest

# HELPERS

OUT = 'outputs'
def generate_out_name(name):
    global OUT
    return f'{OUT}/{name}.mp4'

SRC = '../videos/03.mp4'
def good_helper(name, start, end):
    try:
        output_name = generate_out_name(name)
        edit.edit_video(SRC, output_name, start, end)
    except CalledProcessError as c:
        assert False, str(c)

BAD = generate_out_name('bad')
def bad_helper(start, end):
    with pytest.raises(CalledProcessError):
        edit.edit_video(SRC, BAD, start, end)

# GOOD TESTS 

def test_good_seconds_start_end():
    good_helper('start end', '2', '4')

def test_good_timestamp():
    good_helper('2 timestamps', '00:22', '00:24')

def test_good_positive_second():
    good_helper('only start', '71', end=None)

def test_good_negative_end():
    good_helper('negative end', '-2', end=None)

# BAD TESTS

def test_bad_over_bounds():
    bad_helper('1:22', '1:24')
