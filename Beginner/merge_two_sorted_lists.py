"""
Problem: Merge Two Sorted Lists

You are given two sorted lists.
Merge them into one sorted list and return the result.

"""

def merge_two_sorted_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


# Test Cases
list1 = [1, 2, 4]
list2 = [1, 3, 4]

print(merge_two_sorted_lists(list1, list2))

print(merge_two_sorted_lists([1, 5, 8], [2, 3, 7]))

print(merge_two_sorted_lists([], [1, 2, 3]))