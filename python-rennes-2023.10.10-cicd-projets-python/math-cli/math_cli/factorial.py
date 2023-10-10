def factorial(value: int):
    if value in (0, 1):
        return value
    else:
        return value * factorial(value - 1)
