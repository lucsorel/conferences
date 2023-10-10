from pytest import mark

from math_cli.fibonacci import fibonacci


@mark.parametrize(['value', 'expected_fibonacci'], [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_fibonacci(value: int, expected_fibonacci: int):
    assert fibonacci(value) == expected_fibonacci
