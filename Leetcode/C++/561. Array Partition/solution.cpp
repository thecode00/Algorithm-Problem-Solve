// https://leetcode.com/problems/array-partition/description/

#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int arrayPairSum(vector<int> &nums)
    {
        int total = 0;
        sort(nums.begin(), nums.end());
        for (int idx = 0; idx < nums.size(); idx += 2)
        {
            total += nums[idx];
        }
        return total;
    }
};