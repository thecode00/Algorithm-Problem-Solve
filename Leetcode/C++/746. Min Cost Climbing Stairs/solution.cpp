// https://leetcode.com/problems/min-cost-climbing-stairs/description/

#include <algorithm>
#include <vector>

class Solution
{
public:
    int minCostClimbingStairs(std::vector<int> &cost)
    {
        int prev = 0;
        int prev2 = 0;

        for (auto c : cost)
        {
            int cur = std::min(prev, prev2) + c;
            prev2 = prev;
            prev = cur;
        }

        return std::min(prev, prev2);
    }
};