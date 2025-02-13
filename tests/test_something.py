import pytest

from scratch import hello

def test_something():
    assert hello() == "Hello from scratch!"