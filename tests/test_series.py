from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

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
    expected = 4

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_4():
    #Arrange
    n = 4
    expected = 7

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_5():
    #Arrange
    n = 5
    expected = 11

    #Act
    actual = lucas(n)

    #Assert
    assert expected == actual

def test_lucas_return_correct_number_for_6():
    #Arrange
    n = 6
    expected = 18

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

# sum_series Function Tests:

def test_sum_series_return_fibonacci_sequence_3():
    #Arrange
    n = 3
    expected = 2

    #Act
    actual = sum_series(n)

    #Assert
    assert expected == actual

def test_sum_series_return_fibonacci_sequence_4():
    #Arrange
    n = 4
    expected = 3

    #Act
    actual = sum_series(n)

    #Assert
    assert expected == actual

def test_sum_series_return_fibonacci_sequence_6():
    #Arrange
    n = 6
    expected = 8

    #Act
    actual = sum_series(n)

    #Assert
    assert expected == actual

def test_sum_series_return_lucas_sequence_3():
    #Arrange
    n = 3
    a = 2
    b = 1
    expected = 4

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_return_lucas_sequence_4():
    #Arrange
    n = 4
    a = 2
    b = 1
    expected = 7

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_return_lucas_sequence_6():
    #Arrange
    n = 6
    a = 2
    b = 1
    expected = 18

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_special_case_2_3():

    #Arrange
    n = 1
    a = 2
    b = 3
    expected = 3

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_special_case_3_2():

    #Arrange
    n = 0
    a = 3
    b = 2
    expected = 3

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_custom_sequence_6():

    #Arrange
    n = 6
    a = 1
    b = 2
    expected = 21

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_custom_sequence_5():

    #Arrange
    n = 5
    a = 2
    b = 4
    expected = 26

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_custom_sequence_8():

    #Arrange
    n = 2
    a = 3
    b = 5
    expected = 8

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_custom_sequence_9():

    #Arrange
    n = 9
    a = 2
    b = 6
    expected = 246

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_custom_sequence_special_5():

    #Arrange
    n = 5
    a = -2
    b = 6
    expected = 24

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual

def test_sum_series_return_correct_number_for_minus_input_2():
    #Arrange
    n = -2
    a = 2
    b = 6
    expected = "n has to be a positive integer"

    #Act
    actual = sum_series(n, a, b)

    #Assert
    assert expected == actual