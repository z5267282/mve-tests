import json
import os

from mve.src.constants.errors_format import ERRORS_VIDEOS, ERROR_FILE_NAME


def test_error_order():
    '''Should be 01, then 03'''

    with open(os.environ['ERROR_FILE'], 'r') as f:
        data = json.load(f)

    error_files = data[ERRORS_VIDEOS]
    assert len(error_files) == 2
    assert error_files[0][ERROR_FILE_NAME] == '01.mp4'
    assert error_files[1][ERROR_FILE_NAME] == '03.mp4'


def test_remaining_order(remaining):
    '''Now the remaining files should be:
    04.mp4 - this wasn't edited to begin with;
    01.mp4 - the first error file;
    03.mp4 - the second error file.'''
    with open(remaining) as f:
        data = json.load(f)

    assert data == ['04.mp4', '01.mp4', '03.mp4']
