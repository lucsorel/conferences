from pytest import mark

from math_cli.factorial import factorial


@mark.parametrize(['value', 'expected_factorial'], [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(value: int, expected_factorial: int):
    assert factorial(value) == expected_factorial
