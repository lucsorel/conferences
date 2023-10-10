from typing import Any


def validate_positive_int(value: Any) -> int:
    if value is None:
        raise ValueError('the value must not be None')

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f'value must be an integer, got a {value.__class__.__name__}')

    if value < 0:
        raise ValueError(f'value must be a positive integer, got {value}')

    return value
