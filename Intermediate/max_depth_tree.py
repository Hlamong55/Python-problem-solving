"""
Problem: Maximum Depth of Binary Tree

Given the root of a binary tree,
return its maximum depth.

Example:

        3
       / \
      9   20
         /  \
        15   7

Output:
3
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


# Build Tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))