from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    if not L1 and not L2:
        return None
    elif not L1:
        return L2
    elif not L2:
        return L1
    elif L1.data <= L2.data:
        R = L1
        L1 = L1.next
    else:
        R = L2
        L2 = L2.next

    Head = R
    while L1 and L2:
        if L1.data <= L2.data:
            R.next = L1
            L1 = L1.next
        else:
            R.next = L2
            L2 = L2.next
        R = R.next

    if L1:
        R.next = L1
    elif L2:
        R.next = L2

    return Head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
