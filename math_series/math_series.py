def fibonacci(n):
    """Function that returns value of the given index from Fibonacci sequence """
    previous = 0
    current = 1
    
    try:
        for i in range(n):
            previous, current = current, previous + current
        return previous
    except TypeError:
        return ("Input should be a one integer")

def lucas(n):
    """Function that returns value of the given index from Lucas sequence"""
    previous = 2
    current = 1
    try:
        for i in range(n):
            previous, current = current, previous + current
        return previous
    except TypeError:
        return ("Input should be a one integer")


def sum_series(n, previous = 0, current = 1):
    """Function that returns value of the given index from Custom fibonacci-like sequence"""
    try:
        for i in range(n):
            previous, current = current, previous + current
        return previous
    except TypeError:
        return ("Input allows only integers")
