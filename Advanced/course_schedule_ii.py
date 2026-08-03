"""
Problem: Course Schedule II

There are numCourses courses you have to take,
labeled from 0 to numCourses - 1.

Some courses have prerequisites.

Return the order in which you should take the courses.

If it is impossible, return an empty list.

Example:

Input:

numCourses = 4

prerequisites =

[
    [1,0],
    [2,0],
    [3,1],
    [3,2]
]

Output:

[0,1,2,3]

(or [0,2,1,3])
"""

from collections import defaultdict, deque


def find_order(num_courses, prerequisites):

    graph = defaultdict(list)

    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:

        graph[prerequisite].append(course)

        indegree[course] += 1

    queue = deque()

    for course in range(num_courses):

        if indegree[course] == 0:

            queue.append(course)

    order = []

    while queue:

        current = queue.popleft()

        order.append(current)

        for neighbor in graph[current]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:

                queue.append(neighbor)

    if len(order) == num_courses:

        return order

    return []


# Test Cases

print(find_order(
    4,
    [[1,0],[2,0],[3,1],[3,2]]
))

print(find_order(
    2,
    [[1,0]]
))

print(find_order(
    2,
    [[0,1],[1,0]]
))