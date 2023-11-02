from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix) == 0:
        return []
    s = []
    r_min, r_max = 0, len(square_matrix) - 1
    c_min, c_max = 0, len(square_matrix[0]) - 1
    while r_min <= r_max and c_min <= c_max:
        # Right
        r = r_min
        c = c_min
        while c <= c_max:
            s.append(square_matrix[r][c])
            if c == c_max:
                break
            c += 1
        # Down
        r_min += 1
        r = r_min
        while r <= r_max:
            s.append(square_matrix[r][c])
            if r == r_max:
                break
            r += 1
        # Left
        c_max -= 1
        c = c_max
        while c >= c_min:
            s.append(square_matrix[r][c])
            if c == c_min:
                break
            c -= 1
        # Up
        r_max -= 1
        r = r_max
        while r >= r_min:
            s.append(square_matrix[r][c])
            if r == r_min:
                break
            r -= 1
        c_min += 1

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
