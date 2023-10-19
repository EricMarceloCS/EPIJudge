from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:

    if len(num1) == 1 and num1[0] == 0:
        return [0]
    if len(num2) == 1 and num2[0] == 0:
        return [0]
    m = []
    b = []
    n1 = False
    n2 = False
    if num1[0] < 0:
        n1 = True
        num1[0] = -num1[0]
    if num2[0] < 0:
        n2 = True
        num2[0] = -num2[0]

    k = 0
    for i in range(len(num1) - 1, -1, -1):
        sm = []
        for t in range(k):
            sm.insert(0, 0)
        for j in range(len(num2) - 1, -1, -1):
            sm.insert(0, num1[i] * num2[j])
        m.append(sm)
        k += 1

    for i in range(len(m)):
        while len(m[i]) < len(m[-1]):
            m[i].insert(0, 0)
    for c in range(len(m[0]) -1, -1, -1):
        s = 0
        for r in range(len(m)):
            s += m[r][c]
        b.insert(0, s)

    for i in range(len(b) - 1, 0, -1):
        b[i - 1] += b[i] // 10
        b[i] = b[i] % 10
    while b[0] >= 10:
        b.insert(0, b[0] // 10)
        b[1] = b[1] % 10
    if n1 ^ n2:
        b[0] = -b[0]
    return b


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
