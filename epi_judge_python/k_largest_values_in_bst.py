from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []

    def in_order_traversal(tree: BstNode):

        if tree.left:
            in_order_traversal(tree.left)
            result.append(tree.data)
        else:
            result.append(tree.data)
        if tree.right:
            in_order_traversal(tree.right)

        return

    in_order_traversal(tree)
    result.reverse()
    return result[:k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
