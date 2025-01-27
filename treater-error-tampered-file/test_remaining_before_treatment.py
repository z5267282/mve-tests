import json


def test_remaining(remaining):
    with open(remaining) as f:
        data = json.load(f)

    assert data == ['01.mp4', '02.mp4', '03.mp4', '04.mp4']
