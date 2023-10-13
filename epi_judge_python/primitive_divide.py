from test_framework import generic_test


def divide(x: int, y: int) -> int:
    p = 0
    v = y
    r = 1
    while x > v:
        v <<= 1
        p += 1
    r <<= p

    while x < v:
        v -= y
        r -= 1
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
