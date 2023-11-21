from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    if len(A) == 0:
        return -1

    if A[0] == k:
        return 0

    lp = 0
    rp = len(A) - 1
    r = -1

    while lp < rp:
        m = lp + ((rp - lp) // 2)
        if A[m] == k:
            r = m
            break
        elif A[m] > k:
            rp = m - 1
        elif A[m] < k:
            lp = m + 1

    if lp == rp and A[lp] == k:
        r = lp
    elif lp == rp and A[lp] != k:
        return -1

    while True:
        if A[r-1] == k:
            r -= 1
        else:
            break

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
