"""
Problem: Meeting Rooms II

Given an array of meeting time intervals
where intervals[i] = [start, end],

return the minimum number of conference rooms required.

Example:

Input:

[[0,30],[5,10],[15,20]]

Output:

2
"""

import heapq


def min_meeting_rooms(intervals):

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    heap = []

    heapq.heappush(heap, intervals[0][1])

    for start, end in intervals[1:]:

        if start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)


# Test Cases

print(min_meeting_rooms([[0,30],[5,10],[15,20]]))

print(min_meeting_rooms([[7,10],[2,4]]))

print(min_meeting_rooms([[1,5],[2,6],[4,8],[9,10]]))

print(min_meeting_rooms([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]))