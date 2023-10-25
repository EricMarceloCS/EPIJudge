from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:

    p, g = 0, len(A) - 1
    i = 0
    while i <= p and i < g:
        p = max(p, i + A[i])
        i += 1

    return p >= g


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
