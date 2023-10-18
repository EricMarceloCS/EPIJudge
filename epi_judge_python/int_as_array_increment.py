from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    b = []

    while i >= 0 and A[i] == 9:
        b.insert(0, 0)
        i -= 1

    if i >= 0:
        b.insert(0, A[i] + 1)
        i -= 1

    while i >= 0:
        b.insert(0, A[i])
        i -= 1

    if A[0] == 9 and b[0] == 0:
        b.insert(0, 1)
    return b


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
