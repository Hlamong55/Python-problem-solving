"""
Problem: Decode Ways

A message containing letters A-Z
is encoded as:

A -> 1
B -> 2
...
Z -> 26

Return the total number of ways
to decode a given string.

Example:

s = "226"

Output:
3

Explanation:

2 2 6
22 6
2 26
"""

def num_decodings(s):
    dp = {len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or
                    (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                dp[i] += dp.get(i + 2, 1)

    return dp[0]


# Test Cases
print(num_decodings("12"))     # 2
print(num_decodings("226"))    # 3
print(num_decodings("06"))     # 0