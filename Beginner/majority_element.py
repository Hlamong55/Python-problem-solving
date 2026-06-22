"""
Problem: Majority Element

Given an array nums of size n,
return the majority element.

The majority element is the element that appears
more than n / 2 times.

Example 1:
nums = [3,2,3]

Output:
3
"""

def majority_element(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > len(nums) // 2:
            return num


# Test Cases
print(majority_element([3, 2, 3]))          # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majority_element([5, 5, 5, 1, 2]))   # 5