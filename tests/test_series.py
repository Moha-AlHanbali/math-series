from math_series import __version__
from math_series.series import fibonacci, lucas

def test_version():
    assert __version__ == '0.1.0'

# Fibonacci Function Tests

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

def test_fibonacci_return_correct_number_for_3():
    #Arrange
    n = 3
    expected = 2

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_return_correct_number_for_4():
    #Arrange
    n = 4
    expected = 3

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_return_correct_number_for_5():
    #Arrange
    n = 5
    expected = 5

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_return_correct_number_for_6():
    #Arrange
    n = 6
    expected = 8

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_return_correct_number_for_minus_input_1():
    #Arrange
    n = -1
    expected = "n has to be a positive integer"

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual

def test_fibonacci_return_correct_number_for_minus_input_2():
    #Arrange
    n = -2
    expected = "n has to be a positive integer"

    #Act
    actual = fibonacci(n)

    #Assert
    assert expected == actual


# Lucas Function Tests

def test_lucas_returns_a_value():
    #Arrange
    n = 1
    expected = 1

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_special_case_0():
    #Arrange
    n = 0
    expected = 2

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_special_case_1():
    #Arrange
    n = 1
    expected = 1

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_special_case_2():
    #Arrange
    n = 2
    expected = 3

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_3():
    #Arrange
    n = 3
    expected = 2

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_4():
    #Arrange
    n = 4
    expected = 3

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_5():
    #Arrange
    n = 5
    expected = 5

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_6():
    #Arrange
    n = 6
    expected = 8

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_minus_input_1():
    #Arrange
    n = -1
    expected = "n has to be a positive integer"

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_minus_input_2():
    #Arrange
    n = -2
    expected = "n has to be a positive integer"

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual