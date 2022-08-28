import timestamp

# get_duration()

def test_duration():
    assert timestamp.get_duration('../videos/03.mp4') == 75
    assert timestamp.get_duration('../videos/04.mp4') == 50
    # probably < 56.5
    assert timestamp.get_duration('../videos/05.mp4') == 56
    assert timestamp.get_duration('../videos/06.mp4') == 40

# timestamp_seconds()

def test_timestamp_seconds_sec():
    assert timestamp.get_timestamp_seconds('00:59') == 59

def test_timestamp_seconds_min():
    assert timestamp.get_timestamp_seconds('04:57') == 297

def test_timestamp_seconds_hour():
    assert timestamp.get_timestamp_seconds('01:10:32') == 4232

# check good time

def test_check_good_time_int():
    assert timestamp.check_good_time('../videos/03.mp4', '74')

def test_check_good_time_negative_int():
    assert timestamp.check_good_time('../videos/03.mp4', '-3')

def test_check_good_time_bad_int():
    assert not timestamp.check_good_time('../videos/03.mp4', '104')