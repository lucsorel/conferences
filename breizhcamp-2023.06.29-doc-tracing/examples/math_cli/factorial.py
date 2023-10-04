from functools import reduce

from math_cli.validation import validate_positive_int

def factorial_reduce(value: int) -> int:
    '''Functional implementation of factorial'''
    value = validate_positive_int(value)
    if value == 1:
        return 1

    return reduce(lambda agg, index: agg * index, range(value, 1, -1), 1)
