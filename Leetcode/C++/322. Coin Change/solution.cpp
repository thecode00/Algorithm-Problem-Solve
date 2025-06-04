// https://leetcode.com/problems/coin-change/description/

class Solution
{
public:
    int coinChange(vector<int> &coins, int amount)
    {
        vector<int> dp(amount + 1);
        fill(dp.begin(), dp.end(), -1);
        dp[0] = 0;

        for (int idx = 1; idx <= amount; idx++)
        {
            for (auto coin : coins)
            {
                if (idx - coin >= 0)
                {
                    if (dp[idx - coin] == -1)
                    {
                        continue;
                    }
                    if (dp[idx] == -1)
                    {
                        dp[idx] = dp[idx - coin] + 1;
                    }
                    else
                    {
                        dp[idx] = min(dp[idx], dp[idx - coin] + 1);
                    }
                }
            }
        }

        return dp[amount];
    }
};