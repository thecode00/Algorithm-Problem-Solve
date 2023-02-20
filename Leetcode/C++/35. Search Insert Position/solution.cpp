// https://leetcode.com/problems/search-insert-position/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int start = 0, end = nums.size() - 1;
        int mid;
        while (start <= end)
        {
            mid = start + (end - start) / 2;
            if (nums[mid] >= target)
            {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }
        return start;
    }
};