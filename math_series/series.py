
def fibonacci(n:int):
    """
    This function takes the parameter n and returns the return the (n)th value in the fibonacci series.
    return: int
    """
    #Special Cases
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return (fibonacci(n-1) + fibonacci(n-2))




# if __name__ == "__main__":
