import helpers.time_handlers as time_handlers
import lib.view as view

# timestamp_seconds()


def test_timestamp_seconds_sec():
    assert time_handlers.get_timestamp_seconds('00:59') == 59


def test_timestamp_seconds_min():
    assert time_handlers.get_timestamp_seconds('04:57') == 297


def test_timestamp_seconds_hour():
    assert time_handlers.get_timestamp_seconds('01:10:32') == 4232

# get_duration()


def test_duration():
    assert view.get_duration('../videos/01.mp4') == 97
    assert view.get_duration('../videos/02.mp4') == 97
    assert view.get_duration('../videos/03.mp4') == 97
    assert view.get_duration('../videos/04.mp4') == 97
