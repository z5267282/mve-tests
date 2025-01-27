import os

import pytest

from mve.src.config import Stateful


@pytest.fixture
def remaining() -> str:
    return os.path.join(
        os.environ['MVE_CONFIGS'],
        os.environ['CONFIG'],
        Stateful.REMAINING
    )
