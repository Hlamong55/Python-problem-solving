"""
Problem: Number of Connected Components

Given n nodes and a list of edges,
return the number of connected components.

Example:

n = 5
edges = [
    [0,1],
    [1,2],
    [3,4]
]

Output:
2
"""

from collections import defaultdict


def count_components(n, edges):

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):

        if node in visited:
            return

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    components = 0

    for node in range(n):

        if node not in visited:
            dfs(node)
            components += 1

    return components


print(count_components(
    5,
    [
        [0,1],
        [1,2],
        [3,4]
    ]
))

print(count_components(
    5,
    [
        [0,1],
        [1,2],
        [2,3],
        [3,4]
    ]
))