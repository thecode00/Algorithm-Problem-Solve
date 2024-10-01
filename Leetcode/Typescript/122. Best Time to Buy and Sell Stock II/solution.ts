// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

function maxProfit(prices: number[]): number {
  let profit = 0;
  let stock = prices[0];

  for (const price of prices) {
    stock = Math.min(stock, price);

    if (price > stock) {
      profit += price - stock;
      stock = price;
    }
  }

  return profit;
}
