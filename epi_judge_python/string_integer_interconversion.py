from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    neg = False
    r = []
    s = ''
    if x < 0:
        neg = True
        x *= -1

    if x == 0:
        return '0'

    while x > 0:
        v = x % 10
        x //= 10
        r.insert(0, str(v))

    if neg:
        s += "-"
    for i in range(len(r)):
        s += r[i]
    return s


def string_to_int(s: str) -> int:
    neg = False
    b = 0
    if s[0] == '-':
        neg = True
    if s[0] == '+' or s[0] == '-':
         b = 1
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    v = 0
    for i in range(b, len(s)):
        v *= 10
        v += d.get(s[i])

    if neg:
        v *= -1
    return v


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
