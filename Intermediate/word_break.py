"""
Problem: Word Break

Given a string s and a dictionary of words,
return True if s can be segmented into
a sequence of dictionary words.

Example:

s = "leetcode"

wordDict = ["leet", "code"]

Output:
True
"""

def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:

            if s[i:i + len(word)] == word:
                dp[i] = dp[i + len(word)]

            if dp[i]:
                break

    return dp[0]


# Test Cases
print(word_break("leetcode", ["leet", "code"]))          # True
print(word_break("applepenapple", ["apple", "pen"]))     # True
print(word_break("catsandog",
                 ["cats", "dog", "sand", "and", "cat"])) # False