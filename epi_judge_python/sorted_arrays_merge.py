import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    r = []
    t = []
    for i in range(len(sorted_arrays)):
        t.extend(sorted_arrays[i])

    heapq.heapify(t)
    while len(t) > 0:
        r.append(heapq.heappop(t))

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
