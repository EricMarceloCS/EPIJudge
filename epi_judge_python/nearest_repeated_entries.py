from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # TODO - you fill in here.
    ht = {}
    min_dist = len(paragraph)

    for i in range(len(paragraph)):
        if paragraph[i] in ht:
            dist = i - ht.get(paragraph[i])
            if dist < min_dist:
                min_dist = dist
        ht[paragraph[i]] = i

    if min_dist == len(paragraph):
        return -1
    return min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
