"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Time Complexity: O(N)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock = prices[0]
        for price in prices:
            if price > stock:
                profit += price - stock
            stock = price
        return profit
