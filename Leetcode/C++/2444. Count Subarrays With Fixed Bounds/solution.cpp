// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
// Ref: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/?orderBy=most_votes

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    long long countSubarrays(vector<int> &nums, int minK, int maxK)
    {
        long count = 0;
        int subArrayIndex = -1;
        int minKIndex = -1, maxKIndex = -1;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] < minK || nums[i] > maxK)
            {
                subArrayIndex = i;
            }
            if (nums[i] == minK)
            {
                minKIndex = i;
            }
            if (nums[i] == maxK)
            {
                maxKIndex = i;
            }
            if (minKIndex != -1 || maxKIndex != -1)
            {
                count += max(0, min(minKIndex, maxKIndex) - subArrayIndex);
            }
        }
        return count;
    }
};