"""
Problem: Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's
bar heights where the width of each bar is 1, return the area of
the largest rectangle in the histogram.

Example:

Input:
heights = [2,1,5,6,2,3]

Output:
10

Explanation:

The largest rectangle has height 5 and width 2,
covering bars [5,6].
"""


def largest_rectangle_area(heights):

    stack = []  # (start_index, height)
    max_area = 0

    for i, h in enumerate(heights):

        start = i

        while stack and stack[-1][1] > h:

            index, height = stack.pop()

            max_area = max(max_area, height * (i - index))

            start = index

        stack.append((start, h))

    n = len(heights)

    while stack:

        index, height = stack.pop()

        max_area = max(max_area, height * (n - index))

    return max_area


# Test Cases

print(largest_rectangle_area([2,1,5,6,2,3]))
print(largest_rectangle_area([2,4]))
print(largest_rectangle_area([2,1,2]))
print(largest_rectangle_area([6,2,5,4,5,1,6]))