"""
Problem: Palindrome Pairs

Given a list of unique words,
return all pairs of distinct indices
(i, j) such that:

words[i] + words[j]
forms a palindrome.

Example:

Input:

["abcd","dcba","lls","s","sssll"]

Output:

[[0,1],[1,0],[3,2],[2,4]]
"""


def is_palindrome(text):

    return text == text[::-1]


def palindrome_pairs(words):

    word_map = {}

    for index, word in enumerate(words):
        word_map[word] = index

    result = []

    for i, word in enumerate(words):

        for j in range(len(word) + 1):

            prefix = word[:j]
            suffix = word[j:]

            if is_palindrome(prefix):

                reverse_suffix = suffix[::-1]

                if (
                    reverse_suffix in word_map and
                    word_map[reverse_suffix] != i
                ):
                    result.append(
                        [word_map[reverse_suffix], i]
                    )

            if (
                j != len(word) and
                is_palindrome(suffix)
            ):

                reverse_prefix = prefix[::-1]

                if (
                    reverse_prefix in word_map and
                    word_map[reverse_prefix] != i
                ):
                    result.append(
                        [i, word_map[reverse_prefix]]
                    )

    return result


# Test Cases

print(
    palindrome_pairs(
        ["abcd", "dcba", "lls", "s", "sssll"]
    )
)

print(
    palindrome_pairs(
        ["bat", "tab", "cat"]
    )
)

print(
    palindrome_pairs(
        ["a", ""]
    )
)