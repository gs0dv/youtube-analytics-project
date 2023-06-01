"""Тесты с использованием pytest для модуля playlist"""
import pytest

from src.playlist import PlayList


@pytest.fixture()
def pl():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_str(pl):
    assert str(pl) == "Moscow Python Meetup №81"


def test_repr(pl):
    assert repr(pl) == "PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')"


def test_total_duration(pl):
    duration = pl.total_duration
    assert str(duration) == "1:49:52"


def test_show_best_video(pl):
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"


def test_title(pl):
    assert pl.title == "Moscow Python Meetup №81"


def test_url(pl):
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
