
def fibonacci(n:int):
    """
    This function takes the parameter (n), a positive integer value.
    It returns the return the (n)th value in the fibonacci series.
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
    This function takes the parameter (n), a positive integer value.
    It returns the return the (n)th value in the lucas series.
    n: int
    return: int
    """

    # Special Cases
    if n < 0:
        return ("n has to be a positive integer")
        
    if n == 0:
        return 2

    if n == 1:
        return 1

    if n == 2:
        return 3

    # Return Value
    return (lucas(n-1) + lucas(n-2))


def sum_series(n, a = 0, b = 1):
    """
        This function takes the parameters (n), a positive integer values and (a, b) , optional integer values. 
        It returns the return the (n)th value in the fibonacci series if (a = 0) and (b = 1).
        It returns the return the (n)th value in the lucas series if (a = 2) and (b = 1).
        It returns the return the (n)th value in a new series if (a and b) have different values.
        n: int
        a: int
        b: int
        retrun: int
    """
    # Fibonacci Case
    if a == 0 and b == 1:
       return fibonacci(n)
    
    # Lucas Case
    if a == 2 and b == 1:
       return lucas(n)

    # Special Cases
    if n < 0:
        return ("n has to be a positive integer")

    if n == 0:
        return a

    if n == 1:
        return b

    if n == 2:
        return a + b

    # Return Value
    return (sum_series(n-1, a, b) + sum_series(n-2, a, b))
    




# if __name__ == "__main__":
    # fibonacci(n)
    # lucas(n)
    # sum_series(n, a ,b)