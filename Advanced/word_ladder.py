"""
Problem: Word Ladder

Given two words (beginWord and endWord), and a dictionary wordList,
return the length of the shortest transformation sequence.

Rules:
- Only one letter can be changed at a time.
- Each transformed word must exist in wordList.

Example:

Input:
beginWord = "hit"
endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

Output:
5
"""

from collections import deque


def ladder_length(begin_word, end_word, word_list):

    word_set = set(word_list)

    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])

    while queue:

        word, steps = queue.popleft()

        if word == end_word:
            return steps

        for i in range(len(word)):

            for c in "abcdefghijklmnopqrstuvwxyz":

                new_word = word[:i] + c + word[i + 1:]

                if new_word in word_set:

                    word_set.remove(new_word)

                    queue.append((new_word, steps + 1))

    return 0


# Test Cases

print(
    ladder_length(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    )
)

print(
    ladder_length(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"]
    )
)