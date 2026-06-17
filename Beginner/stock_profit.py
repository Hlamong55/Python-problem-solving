"""
Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i]
is the price of a stock on the i-th day.

You want to maximize your profit by choosing:
- One day to buy
- One future day to sell

Return the maximum profit you can achieve.

If no profit is possible, return 0.

"""

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# Test Cases
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([2, 4, 1]))           # 2
print(max_profit([1, 2, 3, 4, 5]))     # 4