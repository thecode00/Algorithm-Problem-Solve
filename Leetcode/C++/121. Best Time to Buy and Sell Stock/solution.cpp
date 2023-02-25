// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/904508417/

#include <vector>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int cur_stock = prices[0];
        int profits = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            if (cur_stock < prices[i])
            {
                profits = max(profits, prices[i] - cur_stock);
            }
            else
            {
                cur_stock = prices[i];
            }
        }
        return profits;
    }
};