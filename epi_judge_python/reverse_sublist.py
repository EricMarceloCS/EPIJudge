from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    if not L or start == finish:
        return L
    n1 = 1
    n2 = 1
    f = L
    while n2 != finish:
        f = f.next
        n2 += 1

    p = None
    c = L
    n = c.next
    rev = False
    while n1 <= finish:
        if n1 == start:
            c.next = f.next
            rev = True
            if p:
                p.next = f
        elif rev:
            c.next = p
        p = c
        c = n
        if n:
            n = n.next
        n1 += 1

    if start == 1:
        return p
    else:
        return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
