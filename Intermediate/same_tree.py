"""
Problem: Same Tree

Given two binary trees,
check whether they are identical.

Example:

Tree 1:
    1
   / \
  2   3

Tree 2:
    1
   / \
  2   3

Output:
True
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_same_tree(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.value != q.value:
        return False

    return (
        is_same_tree(p.left, q.left)
        and
        is_same_tree(p.right, q.right)
    )


# Tree 1
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Tree 2
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print(is_same_tree(tree1, tree2))