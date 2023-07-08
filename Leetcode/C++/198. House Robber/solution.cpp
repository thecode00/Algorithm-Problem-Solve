// https://leetcode.com/problems/house-robber/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        vector<int> profit;

        for (int i = 0; i < nums.size(); i++)
        {
            if (i == 0)
            {
                profit.push_back(nums[i]);
            }
            else if (i == 1)
            {
                profit.push_back(max(nums[i], profit[i - 1]));
            }
            // Compare rob current house: nums[i] + profit[i - 2] and not rob current house: profit[i - 1]
            else
            {
                profit.push_back(max(nums[i] + profit[i - 2], profit[i - 1]));
            }
        }
        return profit.back();
    }
};

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() <= 2)
        {
            return *max_element(nums.begin(), nums.end());
        }
        vector<int> profit;
        profit.push_back(nums[0]);
        profit.push_back(max(nums[0], nums[1]));
        for (int i = 2; i < nums.size(); i++)
        {
            profit.push_back(max(nums[i] + profit[i - 2], profit[i - 1]));
        }

        return profit.back();
    }
};