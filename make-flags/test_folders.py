import json
import pytest

def test_folders():
    with open('configs/fishing/config.json', 'r') as f:
        data = json.load(f)

    assert data["SOURCE"] == ['..', '..', 'videos']
    assert data["RENAMES"] == [".."]
    assert data["DESTINATION"] == ["..", "..", "outputs"]

