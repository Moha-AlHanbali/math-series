from math_series import __version__
from math_series.series import fibonacci

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_returns_a_value():
    #Arrange
    n = 1
    expected = 1

    #Act
    actual = fibonacci(1)

    #Assert
    assert expected == actual
