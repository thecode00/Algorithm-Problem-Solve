// https://leetcode.com/problems/maximum-subarray/description/
// Time complexity: O(N)

#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        vector<int> dp;
        dp.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++)
        {
            if (dp.back() < 0)
            {
                dp.push_back(nums[i]);
            }
            else
            {
                dp.push_back(dp.back() + nums[i]);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};

class Solution // Kadane`s algorithm
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int maxSum = INT_MIN, curSum = 0;
        for (auto num : nums)
        {
            curSum = max(curSum + num, num);
            maxSum = max(maxSum, curSum);
        }
        return maxSum;
    }
};