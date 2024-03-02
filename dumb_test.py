import pytest
from myFunc import *


def test_isPrime():
    assert isPrime(5) == 'prime'
    assert isPrime(-16) == 'only a natural number can be prime'


def test_factorial():
    assert factorial(5) == 120
    assert factorial('bugaga') == 'Type Error'