from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_
def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)
