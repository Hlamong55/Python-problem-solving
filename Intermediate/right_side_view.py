"""
Problem: Binary Tree Right Side View

Return the values of the nodes
you can see from the right side.

Example:

        1
       / \
      2   3
       \   \
        5   4

Output:
[1,3,4]
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def right_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if i == level_size - 1:
                result.append(node.value)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(right_side_view(root))