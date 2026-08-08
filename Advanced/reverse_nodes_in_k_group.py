"""
Problem: Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes
of the list k at a time.

If the number of nodes is not a multiple of k,
the remaining nodes should stay unchanged.

Example:

Input:
1 -> 2 -> 3 -> 4 -> 5
k = 2

Output:
2 -> 1 -> 4 -> 3 -> 5
"""


class ListNode:

    def __init__(self, value=0, next_node=None):

        self.value = value
        self.next = next_node


def reverse_k_group(head, k):

    if head is None or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head

    group_previous = dummy

    while True:

        # Find the kth node
        kth = group_previous

        for _ in range(k):

            kth = kth.next

            if kth is None:
                return dummy.next

        group_next = kth.next

        # Reverse the current group
        previous = group_next
        current = group_previous.next

        while current != group_next:

            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        # Connect previous group with reversed group
        old_start = group_previous.next

        group_previous.next = kth

        group_previous = old_start


def create_linked_list(values):

    dummy = ListNode()

    current = dummy

    for value in values:

        current.next = ListNode(value)

        current = current.next

    return dummy.next


def print_linked_list(head):

    values = []

    current = head

    while current:

        values.append(str(current.value))

        current = current.next

    print(" -> ".join(values))


# Test Case 1

head1 = create_linked_list(
    [1, 2, 3, 4, 5]
)

head1 = reverse_k_group(head1, 2)

print_linked_list(head1)


# Test Case 2

head2 = create_linked_list(
    [1, 2, 3, 4, 5]
)

head2 = reverse_k_group(head2, 3)

print_linked_list(head2)


# Test Case 3

head3 = create_linked_list(
    [1, 2, 3, 4]
)

head3 = reverse_k_group(head3, 4)

print_linked_list(head3)


# Test Case 4

head4 = create_linked_list(
    [1, 2, 3, 4, 5]
)

head4 = reverse_k_group(head4, 1)

print_linked_list(head4)