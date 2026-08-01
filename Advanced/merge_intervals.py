"""
Problem: Merge Intervals

Given an array of intervals where
intervals[i] = [start, end],

merge all overlapping intervals.

Example:

Input:

[[1,3],[2,6],[8,10],[15,18]]

Output:

[[1,6],[8,10],[15,18]]
"""


def merge(intervals):

    if not intervals:
        return []

    intervals.sort()

    merged = [intervals[0]]

    for current in intervals[1:]:

        last = merged[-1]

        if current[0] <= last[1]:

            last[1] = max(last[1], current[1])

        else:

            merged.append(current)

    return merged


# Test Cases

print(merge([[1,3],[2,6],[8,10],[15,18]]))

print(merge([[1,4],[4,5]]))

print(merge([[1,4],[5,6]]))

print(merge([[1,10],[2,3],[4,8]]))