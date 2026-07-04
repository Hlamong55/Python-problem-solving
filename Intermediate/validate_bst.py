"""
Problem: Validate Binary Search Tree

Given the root of a binary tree,
determine if it is a valid Binary Search Tree (BST).

Example:

      2
     / \
    1   3

Output:
True
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root, left=float("-inf"), right=float("inf")):
    if root is None:
        return True

    if not (left < root.value < right):
        return False

    return (
        is_valid_bst(root.left, left, root.value)
        and
        is_valid_bst(root.right, root.value, right)
    )


# Test Tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))