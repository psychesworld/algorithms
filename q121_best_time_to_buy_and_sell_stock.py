#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (48.86%)
# Likes:    3579
# Dislikes: 162
# Total Accepted:    664.3K
# Total Submissions: 1.4M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        iterator = iter(prices)
        min_buy_price = next(iterator)
        max_profit = 0
        for price in iterator:
            profit = price - min_buy_price
            if profit > max_profit:
                max_profit = profit
            if price < min_buy_price:
                min_buy_price = price
        return max_profit


class BruteForceSolution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(len(prices) - 1):
            buy_price = prices[i]
            for sell_day in range(i + 1, len(prices)):
                sell_price = prices[sell_day]
                profit = sell_price - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


# @lc code=end
