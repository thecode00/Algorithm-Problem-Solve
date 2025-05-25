// https://leetcode.com/problems/maximum-subarray/description/
// Time complexity: O(N)

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int maxSum = INT_MIN;
        int total = 0;

        for (auto num : nums)
        {
            total += num;

            if (maxSum < total)
            {
                maxSum = total;
            }
            if (total < 0)
            {
                total = 0;
            }
        }

        return maxSum;
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