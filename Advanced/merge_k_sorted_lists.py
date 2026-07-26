"""
Problem: Merge K Sorted Lists

You are given an array of k sorted linked lists.

Merge all the linked lists into one sorted linked list
and return its head.

Example:

Input:
[
  [1,4,5],
  [1,3,4],
  [2,6]
]

Output:
[1,1,2,3,4,4,5,6]
"""

import heapq


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):

    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_list(head):

    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def merge_k_lists(lists):

    heap = []

    for index, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, index, node))

    dummy = ListNode()
    current = dummy

    while heap:

        value, index, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(
                heap,
                (node.next.val, index, node.next)
            )

    return dummy.next


# Test Cases

list1 = build_list([1, 4, 5])
list2 = build_list([1, 3, 4])
list3 = build_list([2, 6])

merged = merge_k_lists([list1, list2, list3])

print(print_list(merged))