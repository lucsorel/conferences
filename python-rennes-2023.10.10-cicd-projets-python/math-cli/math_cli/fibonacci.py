def fibonacci(value: int) -> int:
    '''Optimistic implementation of the Fibonacci suite'''
    if value in (0, 1):
        return value

    return fibonacci(value - 1) + fibonacci(value - 2)
