from subprocess import CalledProcessError

import edit
import pytest

# TESTS

# def test_good_seconds_start_end():
#     helper('start end', '4', '10')

# def test_good_timestamp():
#     helper('2 timestamps', '00:25', '00:30')

def test_good_positive_second():
    helper('only start', '60')

# def test_good_negative_end():
#     helper('negative end', '-4')

# HELPERS

def generate_out_name(name):
    OUT = 'outputs'
    return f'{OUT}/{name}.mp4'

def helper(name, start, end=None):
    SRC = '../videos/03.mp4'
    output_name = generate_out_name(name)
    edit.edit_video(SRC, output_name, start, end)
