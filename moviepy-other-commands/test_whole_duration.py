import os

from mve.src.helpers.video import get_duration


def test_duration():
    assert get_duration(
        os.path.join(os.environ['EDITS'], 'whole command.mp4')
    ) == 4
