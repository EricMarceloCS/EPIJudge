from test_framework import generic_test


def reverse(x: int) -> int:
    r = 0
    n = False
    if x < 0:
        n = True
        x = -x
    while x:
        r *= 10
        r += x % 10
        x //= 10
    if n:
        r = -r
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
