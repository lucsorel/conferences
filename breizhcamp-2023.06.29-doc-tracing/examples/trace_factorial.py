'''
cd examples
python -m trace --trace trace_factorial.py 3
python -m trace --count trace_factorial.py 2
python -m trace --listfuncs trace_factorial.py 2
'''

from sys import argv

def factorial(n: int) -> int:
    assert n > 0
    if n == 1:
        return 1
    return n * factorial(n - 1)

factorial(int(argv[1]))
