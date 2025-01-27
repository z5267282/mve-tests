import json


def test_remaining(remaining):
    with open(remaining) as f:
        data = json.load(f)

    assert data == ['04.mp4']
