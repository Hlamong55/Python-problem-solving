"""
Problem: LFU Cache

Design and implement a data structure for a
Least Frequently Used (LFU) cache.

Implement:

get(key)
put(key, value)

If there is a tie,
remove the Least Recently Used item.

Example:

cache = LFUCache(2)

put(1,1)
put(2,2)

get(1) -> 1

put(3,3)

get(2) -> -1
get(3) -> 3
"""

from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity):

        self.capacity = capacity

        self.min_freq = 0

        self.key_to_val_freq = {}

        self.freq_to_keys = defaultdict(OrderedDict)

    def update_frequency(self, key):

        value, freq = self.key_to_val_freq[key]

        del self.freq_to_keys[freq][key]

        if not self.freq_to_keys[freq]:

            del self.freq_to_keys[freq]

            if self.min_freq == freq:

                self.min_freq += 1

        self.freq_to_keys[freq + 1][key] = None

        self.key_to_val_freq[key] = (value, freq + 1)

    def get(self, key):

        if key not in self.key_to_val_freq:

            return -1

        self.update_frequency(key)

        return self.key_to_val_freq[key][0]

    def put(self, key, value):

        if self.capacity == 0:

            return

        if key in self.key_to_val_freq:

            freq = self.key_to_val_freq[key][1]

            self.key_to_val_freq[key] = (value, freq)

            self.update_frequency(key)

            return

        if len(self.key_to_val_freq) == self.capacity:

            old_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)

            del self.key_to_val_freq[old_key]

            if not self.freq_to_keys[self.min_freq]:

                del self.freq_to_keys[self.min_freq]

        self.key_to_val_freq[key] = (value, 1)

        self.freq_to_keys[1][key] = None

        self.min_freq = 1


# Test Cases

cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))

cache.put(3, 3)

print(cache.get(2))
print(cache.get(3))

cache.put(4, 4)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))