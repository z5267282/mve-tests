import json
import os

from mve.src.constants.treatment_format import EDITS, EDIT_ORIGINAL, \
    EDIT_NAME, EDIT_TIMES, EDIT_TIMES_START, EDIT_TIMES_END


def test_tampered():
    treatment = os.environ['TREATMENT_FILE']
    with open(treatment) as t:
        session = json.load(t)
        assert session[EDITS] == [
            {
                EDIT_ORIGINAL: '01.mp4',
                EDIT_NAME: 'bad.mp4',
                EDIT_TIMES: {
                    EDIT_TIMES_START: '5',
                    EDIT_TIMES_END: 'fire'
                }
            },
            {
                EDIT_ORIGINAL: '02.mp4',
                EDIT_NAME: 'good.mp4',
                EDIT_TIMES: {
                    EDIT_TIMES_START: '3',
                    EDIT_TIMES_END: '6'
                }
            },
            {
                EDIT_ORIGINAL: '03.mp4',
                EDIT_NAME: 'worse.mp4',
                EDIT_TIMES: {
                    EDIT_TIMES_START: '40',
                    EDIT_TIMES_END: 'earth'
                }
            }
        ]
