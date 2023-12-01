from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    C: List = []
    pa = None
    pb = None
    ia = 0
    ib = 0
    while ia < len(A) and ib < len(B):
        if pa is not None and pa == A[ia]:
            ia += 1
            continue
        if pb is not None and pb == B[ib]:
            ib += 1
            continue
        if A[ia] < B[ib]:
            pa = A[ia]
            ia += 1
        elif A[ia] > B[ib]:
            pb = B[ib]
            ib += 1
        elif A[ia] == B[ib]:
            C.append(A[ia])
            pa = A[ia]
            pb = B[ib]
            ia += 1
            ib += 1

    return C


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
