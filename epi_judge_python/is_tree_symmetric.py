from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    rt = []
    lt = []
    if tree is None or (tree.left is None and tree.right is None):
        return True
    elif (tree.left is None and tree.right is not None) or (tree.left is not None and tree.right is None):
        return False
    elif tree.left.data != tree.right.data:
        return False
    else:
        lt.append(tree.left)
        rt.append(tree.right)

    while lt and rt:
        lr = lt.pop()
        rr = rt.pop()
        if (lr.left is not None and rr.right is None) or (lr.left is None and rr.right is not None):
            return False
        elif (lr.right is not None and rr.left is None) or (lr.right is None and rr.left is not None):
            return False

        if lr.left is not None and rr.right is not None:
            if lr.left.data == rr.right.data:
                lt.append(lr.left)
                rt.append(rr.right)
            else:
                return False

        if lr.right is not None and rr.left is not None:
            if lr.right.data == rr.left.data:
                lt.append(lr.right)
                rt.append(rr.left)
            else:
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
