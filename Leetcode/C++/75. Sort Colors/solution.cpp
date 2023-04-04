// https://leetcode.com/problems/sort-colors/description/

#include <vector>

using namespace std;

class Solution // Quick sort
{
public:
    void sortColors(vector<int> &nums)
    {
        int pivot = 1;
        int small = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] < pivot)
            {
                swap(nums[i], nums[small++]);
            }
        }
        int big = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; --i)
        {
            if (nums[i] > pivot)
            {
                swap(nums[i], nums[big--]);
            }
        }
    }
};