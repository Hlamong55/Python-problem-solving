"""
Problem: Insert Interval

You are given an array of non-overlapping intervals sorted
by their starting times.

Insert a new interval into the intervals such that the
resulting intervals remain sorted and non-overlapping.

Example:

Input:

intervals = [[1,3],[6,9]]

newInterval = [2,5]

Output:

[[1,5],[6,9]]
"""


def insert(intervals, new_interval):

    result = []

    i = 0
    n = len(intervals)

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:

        result.append(intervals[i])

        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:

        new_interval[0] = min(new_interval[0], intervals[i][0])

        new_interval[1] = max(new_interval[1], intervals[i][1])

        i += 1

    result.append(new_interval)

    # Add remaining intervals
    while i < n:

        result.append(intervals[i])

        i += 1

    return result


# Test Cases

print(insert([[1,3],[6,9]], [2,5]))

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

print(insert([], [5,7]))

print(insert([[1,5]], [2,3]))

print(insert([[1,5]], [6,8]))