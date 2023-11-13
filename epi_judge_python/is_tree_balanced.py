from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    q1 = [tree]
    q2 = []

    while len(q1) > 0:
        while len(q1) > 0:
            n1 = q1.pop(0)
            if n1:
                if n1.left and n1.right:
                    q2.append(n1.left)
                    q2.append(n1.right)
                elif not n1.left and n1.right:
                    if n1.right.left or n1.right.right:
                        return False
                elif n1.left and not n1.right:
                    if n1.left.left or n1.left.right:
                        return False
        while len(q2) > 0:
            n2 = q2.pop(0)
            if n2:
                if n2.left and n2.right:
                    q1.append(n2.left)
                    q1.append(n2.right)
                elif not n2.left and n2.right:
                    if n2.right.left or n2.right.right:
                        return False
                elif n2.left and not n2.right:
                    if n2.left.left or n2.left.right:
                        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
