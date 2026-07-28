"""
Problem:

Serialize and Deserialize Binary Tree

Convert a binary tree into a string and rebuild it.

Example:

        1
       / \
      2   3
         / \
        4   5

Serialized:

1,2,3,null,null,4,5,null,null,null,null
"""

from collections import deque


class TreeNode:

    def __init__(self, value):

        self.val = value
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):

        if not root:
            return ""

        result = []

        queue = deque([root])

        while queue:

            node = queue.popleft()

            if node:

                result.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)

            else:

                result.append("null")

        return ",".join(result)

    def deserialize(self, data):

        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))

        queue = deque([root])

        index = 1

        while queue:

            node = queue.popleft()

            if values[index] != "null":

                node.left = TreeNode(int(values[index]))

                queue.append(node.left)

            index += 1

            if values[index] != "null":

                node.right = TreeNode(int(values[index]))

                queue.append(node.right)

            index += 1

        return root


# Test

root = TreeNode(1)

root.left = TreeNode(2)

root.right = TreeNode(3)

root.right.left = TreeNode(4)

root.right.right = TreeNode(5)

codec = Codec()

serialized = codec.serialize(root)

print(serialized)

new_root = codec.deserialize(serialized)

print(codec.serialize(new_root))