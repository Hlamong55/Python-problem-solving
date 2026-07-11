"""
Problem: Palindrome Partitioning

Example:

Input:
"aab"

Output:
[['a','a','b'],['aa','b']]
"""

def partition(s):
    result = []

    def is_palindrome(text):
        return text == text[::-1]

    def backtrack(start, path):

        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):

            word = s[start:end]

            if is_palindrome(word):
                path.append(word)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])

    return result


print(partition("aab"))