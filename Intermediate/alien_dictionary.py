"""
Problem: Alien Dictionary

There is a new alien language.

You are given a sorted list of words.

Return a string representing the correct
order of characters in the alien language.

If no valid ordering exists,
return an empty string.

Example 1:

Input:
["wrt","wrf","er","ett","rftt"]

Output:
"wertf"
"""

from collections import defaultdict, deque


def alien_order(words):

    graph = defaultdict(set)
    indegree = {}

    # Initialize all characters
    for word in words:
        for char in word:
            indegree[char] = 0

    # Build graph
    for i in range(len(words) - 1):

        first = words[i]
        second = words[i + 1]

        # Invalid case
        if (
            len(first) > len(second)
            and first.startswith(second)
        ):
            return ""

        for c1, c2 in zip(first, second):

            if c1 != c2:

                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1

                break

    queue = deque()

    for char in indegree:
        if indegree[char] == 0:
            queue.append(char)

    order = []

    while queue:

        char = queue.popleft()
        order.append(char)

        for neighbor in graph[char]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        return ""

    return "".join(order)


# Test Cases

print(alien_order(
    ["wrt", "wrf", "er", "ett", "rftt"]
))

print(alien_order(
    ["z", "x"]
))

print(alien_order(
    ["z", "x", "z"]
))