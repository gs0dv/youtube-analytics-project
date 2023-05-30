"""Тесты с использованием pytest для модуля video"""
import pytest

from src.video import Video, PLVideo


@pytest.fixture()
def video_1():
    return Video('AWX4JnAnjBE')


@pytest.fixture()
def video_2():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video_1_str(video_1):
    assert str(video_1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_video_2_str(video_2):
    assert str(video_2) == 'MoscowPython Meetup 78 - вступление'


def test_video_1_repr(video_1):
    assert repr(video_1) == "Video('AWX4JnAnjBE')"


def test_video_2_repr(video_2):
    assert repr(video_2) == "PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')"
