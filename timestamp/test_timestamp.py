import mve.src.helpers.time_handlers as time_handlers


def test_timestamp_seconds_sec():
    assert time_handlers.get_timestamp_seconds('00:59') == 59


def test_timestamp_seconds_min():
    assert time_handlers.get_timestamp_seconds('04:57') == 297


def test_timestamp_seconds_hour():
    assert time_handlers.get_timestamp_seconds('01:10:32') == 4232
