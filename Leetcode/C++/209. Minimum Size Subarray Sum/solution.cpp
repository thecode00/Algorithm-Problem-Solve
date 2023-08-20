// https://leetcode.com/problems/minimum-size-subarray-sum/

#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int left = 0, total = 0;
        int min_length = INT_MAX;
        for (int right = 0; right < nums.size(); right++)
        {
            total += nums[right];
            while (total >= target && left <= right)
            {
                min_length = min(min_length, right - left + 1);
                total -= nums[left];
                left += 1;
            }
        }
        return min_length == INT_MAX ? 0 : min_length;
    }
};