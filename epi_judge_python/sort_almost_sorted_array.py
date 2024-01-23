import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # TODO - you fill in here.
    h = []
    result = []
    for num in itertools.islice(sequence, k):
        heapq.heappush(h, num)

    for num in sequence:
        low = heapq.heappushpop(h, num)
        result.append(low)

    while len(h) > 0:
        result.append(heapq.heappop(h))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
