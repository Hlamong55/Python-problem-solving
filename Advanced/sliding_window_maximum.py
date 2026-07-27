"""
Problem: Sliding Window Maximum

You are given an array of integers nums,
and an integer k.

There is a sliding window of size k moving
from the left of the array to the right.

Return the maximum value in each window.

Example:

Input:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
[3,3,5,5,6,7]
"""

from collections import deque


def max_sliding_window(nums, k):

    if not nums:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):

        # Remove indices outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Store maximum after first full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test Cases

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(max_sliding_window([1], 1))
print(max_sliding_window([9,11], 2))
print(max_sliding_window([4,-2], 2))