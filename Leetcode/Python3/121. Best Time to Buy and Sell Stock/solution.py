# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        propit: int = 0
        min_price: int = prices[0]
        for price in prices:
            if price > min_price:
                propit = max(propit, price - min_price)
            else:
                min_price = price
        return propit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        buy_price = prices[0]
        for idx in range(1, len(prices)):
            dp[idx] = max(prices[idx] - buy_price, dp[idx - 1])
            if buy_price > prices[idx]:
                buy_price = prices[idx]
        return dp[-1]


class Solution:  # Two pointer
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit
