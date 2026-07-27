"""
Problem: LRU Cache

Design a data structure that follows the constraints
of a Least Recently Used (LRU) cache.

Implement:

get(key)
put(key, value)

Both operations must run in O(1).

Example:

cache = LRUCache(2)

cache.put(1,1)
cache.put(2,2)

cache.get(1) -> 1

cache.put(3,3)

cache.get(2) -> -1
"""


class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        if key in self.cache:

            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node

        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]


cache = LRUCache(2)

cache.put(1,1)
cache.put(2,2)

print(cache.get(1))

cache.put(3,3)

print(cache.get(2))

cache.put(4,4)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))