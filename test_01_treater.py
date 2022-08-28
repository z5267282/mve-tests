from subprocess import CalledProcessError
import pytest

import mve.src.treater as treater

def test_edit_good():
    try:
        output_name = 'test.mp4'
        treater.edit_video('videos/03.mp4', output_name, '2', '4')
    except CalledProcessError as c:
        assert False, str(c)
