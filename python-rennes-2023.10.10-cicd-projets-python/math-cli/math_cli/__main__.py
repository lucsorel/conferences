from typing import Any

from fire import Fire

from math_cli.factorial import factorial
from math_cli.fibonacci import fibonacci
from math_cli.validation import validate_positive_int


class Controller:
    '''Math commands.'''
    def factorial(self, value: Any):
        '''Computes the factorial of the given integer value.'''
        return factorial(validate_positive_int(value))

    def fibonacci(self, value: Any):
        '''Computes the fibonacci of the given integer value.'''
        return fibonacci(validate_positive_int(value))


if __name__ == '__main__':
    Fire(Controller)
