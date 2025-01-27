import mve.src.helpers.video as video

import os


def test_duration():
    assert video.get_duration(os.path.join(
        os.environ['EDITS'], 'good.mp4')) == 3
