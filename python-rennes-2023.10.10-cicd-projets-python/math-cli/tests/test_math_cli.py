from subprocess import PIPE, run
from typing import List

from pytest import mark


@mark.parametrize(['command_parts', 'expected_result'], [
    (['factorial', '4'], '24'),
    (['fibonacci', '4'], '3'),
])
def test_math_cli(command_parts: List[str], expected_result: str):
    command = ['python', '-m', 'math_cli'] + command_parts
    result = run(command, stdout=PIPE, stderr=PIPE, text=True, check=True).stdout

    assert result == f'{expected_result}\n'
