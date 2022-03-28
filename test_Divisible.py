import Divisible


def test_divisible_by_5():

    a = 35
    Res = Divisible.divisible_by_5(a)
    assert Res == True

def test_divisible_by_7():

    a = 49
    Res = Divisible.divisible_by_7(a)
    assert Res == True

def test_divisible_by_9():

    a = 45
    Res = Divisible.divisible_by_9(a)
    assert Res == True

def test_divisible_by_10():

    a = 70
    Res = Divisible.divisible_by_10(a)
    assert Res == True