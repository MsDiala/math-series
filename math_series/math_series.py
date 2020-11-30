def fibonacci(n): ##Function that returns value of the given index from Fibonacci sequence 
    '''
    Given an integer value n, this function returns the nth value of the Fibonacci Numbers.
    '''
    if isinstance(n, str):
        #The isinstance() function returns True if the specified object 
        #is of the specified type, otherwise False.
        raise TypeError("n must be an integer greater than or equal to 0.") # The raise keyword is used to raise an exception.
    elif n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif n == 0:
         fibonacciOfN = 0
         return  fibonacciOfN 
    elif n == 1 or n == 2:
         fibonacciOfN  = 1
         return  fibonacciOfN 
    elif n > 2:
        fibonacciOfN = fibonacci(n-1) + fibonacci(n-2)
        return  fibonacciOfN 


def lucas(n): ###Function that returns value of the given index from Lucas sequence
    '''
    Given an integer value n, this function returns the nth value of the Lucas Numbers.
    '''
    if n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif n == 0:
        lucasOfN = 2
        return lucasOfN
    elif n == 1:
        lucasOfN = 1
        return lucasOfN
    elif n >= 2:
        lucasOfN = lucas(n-1) + lucas(n-2)
        return lucasOfN


def sum_series(n, arg1=0, arg2=1): ###Function that returns value of the given index from Custom fibonacci-like sequence
    # pass
    '''
    Given an integer value n and two optional terms arg1 and arg2, this function returns the nth value of the user-specified Fibonacci or Lucas numbers (defaults to Fibonacci if no optional terms provarged).
    '''
    if n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif arg1 == 0 and arg2 == 1:
        fibonacciOfN = fibonacci(n)
        return fibonacciOfN
    elif arg1 == 2 and arg2 == 1:
        lucasOfN = lucas(n)
        return lucasOfN
    else:
        noSum = "Sorry, that sum is not defined."
        return noSum