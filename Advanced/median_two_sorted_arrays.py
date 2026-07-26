"""
Problem: Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2
of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(min(m,n))).

Example:

Input:
nums1 = [1,3]
nums2 = [2]

Output:
2.0
"""

def find_median_sorted_arrays(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x = len(nums1)
    y = len(nums2)

    low = 0
    high = x

    while low <= high:

        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float("inf") if partition_x == x else nums1[partition_x]

        max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float("inf") if partition_y == y else nums2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:

            if (x + y) % 2 == 0:
                return (
                    max(max_left_x, max_left_y)
                    + min(min_right_x, min_right_y)
                ) / 2

            return max(max_left_x, max_left_y)

        elif max_left_x > min_right_y:
            high = partition_x - 1

        else:
            low = partition_x + 1


# Test Cases

print(find_median_sorted_arrays([1,3],[2]))
print(find_median_sorted_arrays([1,2],[3,4]))
print(find_median_sorted_arrays([0,0],[0,0]))