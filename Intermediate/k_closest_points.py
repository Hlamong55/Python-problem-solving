"""
Problem: K Closest Points to Origin

Given an array of points,
return the k closest points to the origin.

Example:

points = [[1,3],[-2,2]]
k = 1

Output:
[[-2,2]]
"""

import heapq

def k_closest(points, k):
    return heapq.nsmallest(
        k,
        points,
        key=lambda point: point[0]**2 + point[1]**2
    )


# Test Cases
print(k_closest([[1,3],[-2,2]], 1))
print(k_closest([[3,3],[5,-1],[-2,4]], 2))