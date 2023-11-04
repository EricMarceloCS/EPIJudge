from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    d1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    d2 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
          8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    neg = False
    if num_as_string[0] == '-':
        neg = True
        b = 1
    else:
         b = 0

    p1 = 0
    p2 = 0
    n = 0
    r = ""
    for i in range(len(num_as_string)-1, b-1, -1):
        n += d1.get(num_as_string[i]) * b1 ** p1
        p1 += 1

    c = 0
    while c <= n:
        c = b2 ** p2
        p2 += 1

    c //= b2
    if neg:
        r += '-'
    while n > 0 or c > 0:
        d = n // c
        r += d2.get(d)
        n -= c * d
        c //= b2

    if r == "":
        return '0'
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
