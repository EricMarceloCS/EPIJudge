from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    ia = 0
    ib = 0
    while ia < len(A) and ib < len(B):
        if A[ia] == 0 and m <= 0:
            A[ia] = B[ib]
            ia += 1
            ib += 1
        elif A[ia] > B[ib]:
            A.insert(ia, B[ib])
            ia += 1
            ib += 1
            A.pop()
        else:
            m -= 1
            ia += 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
