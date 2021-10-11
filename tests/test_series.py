from math_series import __version__
from math_series.series import fibonacci

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_returns_a_value():
    #Arrange
    n = 1
    expected = 1

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_special_case_0():
    #Arrange
    n = 0
    expected = 0

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_special_case_1():
    #Arrange
    n = 1
    expected = 1

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_special_case_2():
    #Arrange
    n = 2
    expected = 1

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual