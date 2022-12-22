# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


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
