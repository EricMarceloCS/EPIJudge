from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    nmv = None
    while tree is not None and tree.data != k:
        if tree.data > k and (nmv is None or tree.data < nmv.data):
            nmv = tree
        if k > tree.data:
            tree = tree.right
        elif k < tree.data:
            tree = tree.left

    if tree is not None and tree.right:
        tree = tree.right
        while tree is not None:
            nmv = tree
            tree = tree.left

    return nmv


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
