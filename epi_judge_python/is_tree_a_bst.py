from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def recurse(tree, low=float('-inf'), high=float('inf')) -> bool:
        if not tree:
            return True
        if tree.data < low or tree.data > high:
            return False
        else:
            return recurse(tree.left, low, tree.data) and recurse(tree.right, tree.data, high)

    return recurse(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
