import json
import os

from mve.src.constants.options import SOURCE, RENAMES, DESTINATION
from mve.src.config import Stateful


def test_config_paths_correctly_loaded():
    with open(os.path.join(
            os.environ['MVE_CONFIGS'], 'input-make', Stateful.CONFIG)
    ) as f:
        conf = json.load(f)

    assert conf[SOURCE] == ['..', 'videos']
    assert conf[RENAMES] == ['renames']
    assert conf[DESTINATION] == ['outputs']
