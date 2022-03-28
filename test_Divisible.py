import Divisible

import pytest

@pytest.fixture   # fixture is not a function. so, dont use () after that !!!
def input():
    x = 40
    return x


@pytest.mark.skip(reason="No Need")
def test_divisible_by_5(input):

    # a = 35
    Res = Divisible.divisible_by_5(input)
    assert Res == True

def test_divisible_by_7(input):

    # a = 49
    Res = Divisible.divisible_by_7(input)
    assert Res == False   # Here we change True or False to get the test cases passes !!!

def test_divisible_by_9(input):

    # a = 45
    Res = Divisible.divisible_by_9(input)
    assert Res == False

def test_divisible_by_10(input):

    # a = 70
    Res = Divisible.divisible_by_10(input)
    assert Res == True