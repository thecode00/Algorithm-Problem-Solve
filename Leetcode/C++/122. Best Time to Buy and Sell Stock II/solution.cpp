// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int profit = 0, cur;
        for (int idx = 0; idx < prices.size() - 1; idx++)
        {
            // To track the continuous increase in price, assign cur to prices[idx].
            cur = prices[idx];
            if (prices[idx + 1] > cur)
            {
                profit += prices[idx + 1] - cur;
            }
        }
        return profit;
    }
};