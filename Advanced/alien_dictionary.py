"""
Problem: Alien Dictionary

There is a new alien language that uses the English alphabet,
but the order of the letters is unknown.

You are given a sorted list of words according to the rules
of this language.

Return a string representing the characters in the correct
alien order.

If there are multiple valid orders, return any of them.
If the dictionary is invalid, return an empty string.

Example:

Input:
["wrt","wrf","er","ett","rftt"]

Output:
"wertf"
"""

from collections import defaultdict, deque


def alien_order(words):

    graph = defaultdict(set)
    indegree = {}

    # Initialize all unique characters
    for word in words:
        for char in word:
            indegree[char] = 0

    # Build graph
    for i in range(len(words) - 1):

        word1 = words[i]
        word2 = words[i + 1]

        min_len = min(len(word1), len(word2))

        # Invalid case
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""

        for j in range(min_len):

            if word1[j] != word2[j]:

                if word2[j] not in graph[word1[j]]:

                    graph[word1[j]].add(word2[j])
                    indegree[word2[j]] += 1

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

print(alien_order(["wrt","wrf","er","ett","rftt"]))

print(alien_order(["z","x"]))

print(alien_order(["z","x","z"]))

print(alien_order(["abc","ab"]))