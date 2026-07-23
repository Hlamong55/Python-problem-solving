"""
Problem: Keyboard Row

Given an array of strings words,
return the words that can be typed
using letters of only one row of the keyboard.

Example:

Input:
["Hello","Alaska","Dad","Peace"]

Output:
["Alaska","Dad"]
"""


def find_words(words):

    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []

    for word in words:

        letters = set(word.lower())

        if letters <= row1 or letters <= row2 or letters <= row3:
            result.append(word)

    return result


# Test Cases

print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
print(find_words(["omk"]))
print(find_words(["adsdf", "sfd"]))