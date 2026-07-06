"""
Problem: Clone Graph

Return a deep copy of an undirected graph.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


def clone_graph(node):
    if not node:
        return None

    copies = {}

    def dfs(current):
        if current in copies:
            return copies[current]

        copy = Node(current.val)
        copies[current] = copy

        for neighbor in current.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


# Build Graph
node1 = Node(1)
node2 = Node(2)

node1.neighbors.append(node2)
node2.neighbors.append(node1)

clone = clone_graph(node1)

print(clone.val)
print(clone.neighbors[0].val)