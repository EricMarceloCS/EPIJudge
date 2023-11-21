import math

from test_framework import generic_test


def square_root(k: int) -> int:
    lp = 1
    rp = k

    while lp < rp:
        m = lp + ((rp - lp) // 2)
        rt = m ** 2
        if rt == k:
            return m
        elif rt < k:
            lp = m + 1
        elif rt > k:
            rp = m - 1

    while True:
        if lp ** 2 > k:
            lp -= 1
        else:
            break

    return lp


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
