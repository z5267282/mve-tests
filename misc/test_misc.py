import lib.view as view


def test_padded_min_sec():
    assert view.parse_timestamp('04-57') == '04:57'


def test_2_digit_min_single_sec():
    assert view.parse_timestamp('59-8') == '59:8'


def test_over_sec():
    assert view.parse_timestamp('5-60') is None


def test_over_hour():
    assert view.parse_timestamp('61-3') is None
