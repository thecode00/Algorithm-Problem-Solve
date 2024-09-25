// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

function maxProfit(prices: number[]): number {
  let curPrice = prices[0],
    maxProfit = 0;

  for (const price of prices) {
    curPrice = Math.min(curPrice, price);
    maxProfit = Math.max(maxProfit, price - curPrice);
  }

  return maxProfit;
}
