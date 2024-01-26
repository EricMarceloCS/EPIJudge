from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    lower = 0
    upper = len(A) - 1
    mid = lower + (upper - lower) // 2

    if A[0] < A[upper]:
        return 0

    while lower <= upper:
        if mid == len(A) - 1 or A[mid - 1] > A[mid] < A[mid + 1]:
            break
        elif A[lower] > A[upper] > A[mid]:
            upper = mid
        elif A[lower] > A[upper] < A[mid]:
            lower = mid
        mid = lower + (upper - lower) // 2

        if lower == mid:
            if A[upper] < A[mid]:
                mid = upper
                break
            else:
                break
        elif upper == mid:
            if A[lower] < A[mid]:
                mid = lower
                break
            else:
                break

    return mid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
