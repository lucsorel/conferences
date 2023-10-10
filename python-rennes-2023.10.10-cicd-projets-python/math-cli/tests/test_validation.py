from typing import Any, Type

from pytest import mark, raises

from math_cli.validation import validate_positive_int


@mark.parametrize(['value'], [
    (0, ),
    (1, ),
    (2, ),
    (5, ),
    (10, ),
    (100, ),
])
def test_validate_positive_int_valid_cases(value: int):
    assert validate_positive_int(value) == value


@mark.parametrize(
    ['value', 'error_class', 'error_message'], [
        (None, ValueError, 'the value must not be None'),
        ('1', TypeError, 'value must be an integer, got a str'),
        (True, TypeError, 'value must be an integer, got a bool'),
        (False, TypeError, 'value must be an integer, got a bool'),
        (1., TypeError, 'value must be an integer, got a float'),
        (-1, ValueError, 'value must be a positive integer, got -1'),
        (-2, ValueError, 'value must be a positive integer, got -2'),
    ]
)
def test_validate_positive_int_invalid_cases(value: Any, error_class: Type, error_message: str):
    with raises(error_class) as error:
        validate_positive_int(value)

    assert str(error.value) == error_message
