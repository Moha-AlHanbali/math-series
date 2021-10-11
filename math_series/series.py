
def fibonacci(n:int):
    """
    This function takes the parameter (n), a positive integer value, and returns the return the (n)th value in the fibonacci series.
    n: int
    return: int
    """

    # Special Cases
    if n < 0:
        return ("n has to be a positive integer")
        
    if n == 0:
        return 0

    if n <= 2:
        return 1

    # Return Value
    return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n:int):
    """
    This function takes the parameter (n), a positive integer value, and returns the return the (n)th value in the lucas series.
    n: int
    return: int
    """

    # Special Cases
    if n == 0:
        return 2

    if n == 1:
        return 1

    if n == 2:
        return 3

    return n







# if __name__ == "__main__":
#     fibonacci(n)