def fibonacci_recurse(value: int) -> int:
    '''Recursive implementation of the Fibonacci suite'''

    if value <= 1:
        return value

    return fibonacci_recurse(value - 1) + fibonacci_recurse(value - 2)
