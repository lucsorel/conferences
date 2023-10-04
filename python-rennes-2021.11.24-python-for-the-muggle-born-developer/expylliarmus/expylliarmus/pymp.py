
from pympler.asizeof import asizeof

def report_memory_usage(**kwargs):
    total = 0
    for name, variable in kwargs.items():
        size_bytes = asizeof(variable)
        print(f'{name}:', size_bytes, 'bytes')
        total += size_bytes
    print(f'total: {total} bytes')
