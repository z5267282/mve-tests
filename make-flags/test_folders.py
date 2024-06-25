import json
import pytest

import constants.options as options

def test_folders():
    with open('configs/fishing/config.json', 'r') as f:
        data = json.load(f)

    assert data[options.SOURCE] == ['..', '..', 'videos']
    assert data[options.RENAMES] == [".."]
    assert data[options.DESTINATION] == ["..", "..", "outputs"]

