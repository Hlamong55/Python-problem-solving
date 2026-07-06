"""
Problem: Course Schedule

Determine if it is possible to finish all courses.

Example:

numCourses = 2
prerequisites = [[1,0]]

Output:
True
"""

from collections import defaultdict


def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)

    for course, pre in prerequisites:
        graph[course].append(pre)

    visiting = set()
    visited = set()

    def dfs(course):
        if course in visiting:
            return False

        if course in visited:
            return True

        visiting.add(course)

        for pre in graph[course]:
            if not dfs(pre):
                return False

        visiting.remove(course)
        visited.add(course)

        return True

    for course in range(num_courses):
        if not dfs(course):
            return False

    return True


print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))