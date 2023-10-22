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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx - 1] < prices[idx]:
                profit += prices[idx] - prices[idx - 1]
        return profit
