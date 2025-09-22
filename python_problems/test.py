from numb3rs import validate


def test_checkletters():
    assert validate("cat") == False
    assert validate("255.255.255.0") == True
    assert validate("255.255.255.0.3") == False


def test_range():
    assert validate("255.255.256.0") == False
    assert validate("333.55.22.666") == False

