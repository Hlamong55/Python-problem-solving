"""
Problem: Encode and Decode Strings

Encode a list of strings into one string
and decode it back.

Example:

Input:
["hello", "world"]

Output:
Encoded: "5#hello5#world"
Decoded: ["hello", "world"]
"""

def encode(strings):
    result = ""

    for s in strings:
        result += str(len(s)) + "#" + s

    return result


def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])

        i = j + 1 + length

    return result


encoded = encode(["hello", "world"])
print(encoded)
print(decode(encoded))