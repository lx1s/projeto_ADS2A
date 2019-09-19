import pytest
from principal import somar
from principal import subtrair


def test_somar():
    assert somar(9+6)==15

def test_subtrair():
    assert subtrair(9-2)==7
