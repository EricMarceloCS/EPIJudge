from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    m = 1
    r = 0
    for b in range(64):
        if y & m:
            r += x << b
        m <<= 1
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
