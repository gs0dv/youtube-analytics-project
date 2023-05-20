"""Тесты с использованием pytest для модуля channel"""
from src.channel import Channel

channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_print_info():
    assert isinstance(channel.print_info(), str) == True
