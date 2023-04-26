import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import calci

def test_add():
    assert calci.add(2, 3) == 5
    assert calci.add(-1, 1) == 0
    assert calci.add(0, 0) == 0

def test_subtract():
    assert calci.subtract(5, 3) == 2
    assert calci.subtract(-1, 1) == -2
    assert calci.subtract(0, 0) == 0

def test_multiply():
    assert calci.multiply(2, 3) == 6
    assert calci.multiply(-1, 1) == -1
    assert calci.multiply(0, 0) == 0

def test_divide():
    assert calci.divide(6, 3) == 2
    assert calci.divide(-6, 3) == -2
    assert calci.divide(0, 5) == 0
    try:
        calci.divide(5, 0)
        assert False
    except ValueError:
        assert True
