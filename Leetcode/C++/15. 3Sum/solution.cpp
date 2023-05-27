// https://leetcode.com/problems/3sum/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int idx = 0; idx < (nums.size() - 2); idx++)
        {
            // Skip duplicate triplets
            if (idx > 0 && nums[idx] == nums[idx - 1])
            {
                continue;
            }
            int left = idx + 1, right = nums.size() - 1;
            while (left < right)
            {
                int total = nums[idx] + nums[left] + nums[right];
                if (total > 0)
                {
                    right -= 1;
                }
                else if (total < 0)
                {
                    left += 1;
                }
                else // Found triplet
                {
                    vector<int> triplet = {nums[idx], nums[left], nums[right]};
                    result.push_back(triplet);
                    // Skip duplicate number
                    while (left < right && nums[left] == nums[left + 1])
                    {
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right - 1])
                    {
                        right -= 1;
                    }
                    left += 1;
                    right -= 1;
                }
            }
        }
        return result;
    }
};