// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int cheapestPrice = prices[0];

        for (int idx = 0; idx < prices.length; idx++){
            cheapestPrice = Math.min(cheapestPrice, prices[idx]);
            profit = Math.max(profit, prices[idx] - cheapestPrice);
        }

        return profit;
    }
}