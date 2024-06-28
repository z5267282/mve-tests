import json


def test_remaining():
    with open("configs/suffixes/remaining.json") as f:
        data = json.load(f)

        assert data == [
            "good.mp4",
            "SHOUTING.MP4",
            "apple.mov",
            "WINDOWS.MOV"
        ]
