import mve.src.helpers.video as video


SECONDS = 1 * 60 + 37


def test_duration():
    assert video.get_duration('../videos/01.mp4') == SECONDS
    assert video.get_duration('../videos/02.mp4') == SECONDS
    assert video.get_duration('../videos/03.mp4') == SECONDS
    assert video.get_duration('../videos/04.mp4') == SECONDS
