def validate_positive_int(value: int) -> int:
    if value <= 0:
        raise ValueError(f'Value must be a positive integer, got {value}.')

    return value
