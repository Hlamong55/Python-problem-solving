"""
Problem: Coin Change

You are given an array of coin denominations
and a target amount.

Return the minimum number of coins
needed to make up that amount.

If it is not possible, return -1.

Example:

coins = [1,2,5]
amount = 11

Output:
3

Explanation:
11 = 5 + 5 + 1
"""

def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


# Test Cases
print(coin_change([1,2,5], 11))   # 3
print(coin_change([2], 3))         # -1
print(coin_change([1], 0))         # 0