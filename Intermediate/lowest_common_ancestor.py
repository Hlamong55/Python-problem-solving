"""
Problem: Lowest Common Ancestor of a BST

Given a BST,
find the lowest common ancestor of two nodes.

Example:

        6
      /   \
     2     8
    / \   / \
   0   4 7   9

p = 2
q = 8

Output:
6
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    while root:
        if p.value < root.value and q.value < root.value:
            root = root.left

        elif p.value > root.value and q.value > root.value:
            root = root.right

        else:
            return root


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

ancestor = lowest_common_ancestor(root, root.left, root.right)

print(ancestor.value)