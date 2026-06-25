"""
Problem: Group Anagrams

Given an array of strings strs,
group the anagrams together.

An anagram is a word formed by rearranging
the letters of another word.

Example 1:
Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]
"""

from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# Test Cases
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))