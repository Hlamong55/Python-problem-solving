"""
Problem: Valid Palindrome

Return True if the string is a palindrome.

Ignore spaces, punctuation,
and uppercase letters.

Example:

Input:
"A man, a plan, a canal: Panama"

Output:
True
"""


def is_palindrome(text):

    filtered = ""

    for ch in text:
        if ch.isalnum():
            filtered += ch.lower()

    left = 0
    right = len(filtered) - 1

    while left < right:

        if filtered[left] != filtered[right]:
            return False

        left += 1
        right -= 1

    return True


# Test Cases
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))