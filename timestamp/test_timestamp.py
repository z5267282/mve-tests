import timestamp

# get_duration()

def test_duration():
    assert timestamp.get_duration('../videos/01.mp4') == 22
    assert timestamp.get_duration('../videos/02.mp4') == 60
    assert timestamp.get_duration('../videos/03.mp4') == 68
    assert timestamp.get_duration('../videos/04.mp4') == 46

# timestamp_seconds()

def test_timestamp_seconds_sec():
    assert timestamp.get_timestamp_seconds('00:59') == 59

def test_timestamp_seconds_min():
    assert timestamp.get_timestamp_seconds('04:57') == 297

def test_timestamp_seconds_hour():
    assert timestamp.get_timestamp_seconds('01:10:32') == 4232
