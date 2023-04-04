// https://leetcode.com/problems/longest-increasing-subsequence/description/

#include <algorithm>
#include <vector>

class Solution
{
public:
    int lengthOfLIS(std::vector<int> &nums)
    {
        std::vector<int> dp;
        for (int idx = 0; idx < nums.size(); idx++)
        {
            dp.push_back(1);
            for (int i = 0; i < idx; i++)
            {
                if (nums[i] < nums[idx])
                {
                    dp[idx] = std::max(dp[idx], dp[i] + 1);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};