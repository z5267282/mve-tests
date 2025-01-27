import mve.src.helpers.video as video

import os


def test_duration():
    assert video.get_duration(os.path.join(
        os.environ['EDITS'], 'fix of 01.mp4')) == 3
    assert video.get_duration(os.path.join(
        os.environ['EDITS'], 'fix of 03.mp4')) == 5
