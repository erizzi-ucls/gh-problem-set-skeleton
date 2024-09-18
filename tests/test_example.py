#!/usr/bin/python3
from skeleton.example import get_identity


def test_get_identity_1() -> None:
    ret = get_identity(10)
    assert ret == 10


def test_get_identity_2() -> None:
    ret = get_identity(1)
    assert ret == 1


def test_get_identity_3() -> None:
    ret = get_identity(1)
    assert ret == 1
