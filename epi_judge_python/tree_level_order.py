from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    r = []
    q1: List = [tree]
    q2: List = []

    while q1 or q2:
        l = []
        while q1:
            n = q1.pop(0)
            if n:
                if n and n.left:
                    q2.append(n.left)
                if n and n.right:
                    q2.append(n.right)
                l.append(n.data)

        if len(l) != 0:
            r.append(l)
        l = []

        while q2:
            n = q2.pop(0)
            if n:
                if n.left:
                    q1.append(n.left)
                if n.right:
                    q1.append(n.right)
                l.append(n.data)
        if len(l) != 0:
            r.append(l)

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
