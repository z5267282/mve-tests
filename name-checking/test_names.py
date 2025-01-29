from mve.src.lib.view import correct_name_format


def test_letters_only():
    assert correct_name_format('heymate')


def test_with_space():
    assert correct_name_format('hey mate')


def test_with_underscores():
    assert correct_name_format('hey_mate')


def test_with_dots():
    assert correct_name_format('hey.mate')


def test_with_hyphens():
    assert correct_name_format('hey-mate')


def test_combined():
    assert correct_name_format("hey_mate on syd.ney - a new day")


def combined_with_numbers():
    assert correct_name_format("hey_mate on 29.01.2025 - a new day")


def test_forbidden():
    assert not correct_name_format('hey@mate')
    assert not correct_name_format("it's 2001")
    assert not correct_name_format("hey_mate & friend")
    assert not correct_name_format("[ wow ]")
