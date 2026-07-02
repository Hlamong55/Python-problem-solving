"""
Problem: Min Stack

Design a stack that supports:

push()
pop()
top()
get_min()

All operations should run in O(1) time.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


# Test Cases
stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.get_min())  # -3

stack.pop()

print(stack.top())      # 0
print(stack.get_min())  # -2