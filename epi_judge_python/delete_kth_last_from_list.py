from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    p1 = L
    p2 = L
    i = 0
    while p1 is not None and i < k + 1:
        p1 = p1.next
        i += 1

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    if i == k:
        L = L.next
    else:
        p2.next = p2.next.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
