from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    lp = len(perm) - 2
    rp = len(perm) - 1
    while rp >= 1:
        if perm[lp] < perm[rp]:
            break
        lp -= 1
        rp -= 1

    for i in range(len(perm) - 1, lp, -1):
        if perm[i] > perm[lp]:
            perm[i], perm[lp] = perm[lp], perm[i]
            break

    if rp == 0:
        return []
    perm[lp + 1:] = reversed(perm[lp + 1:])

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
