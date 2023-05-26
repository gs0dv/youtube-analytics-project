"""Тесты с использованием pytest для модуля channel"""
from src.channel import Channel

channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
highload = Channel('UCwHL6WHUarjGfUM_586me8w')


def test_print_info():
    assert isinstance(channel.print_info(), str) == True


def test_str():
    assert str(channel) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


def test_add():
    assert channel + highload == 100500


def test_sub():
    assert channel - highload == -48500


def test_gt():
    assert (channel > highload) == False


def test_ge():
    assert (channel >= highload) == False


def test_lt():
    assert (channel < highload) == True


def test_le():
    assert (channel <= highload) == True


def test_eq():
    assert (channel == highload) == False
