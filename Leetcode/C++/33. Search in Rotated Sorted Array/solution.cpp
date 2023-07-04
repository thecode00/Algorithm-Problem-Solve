// https://leetcode.com/problems/search-in-rotated-sorted-array/

#include <vector>

using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int left = 0, right = nums.size() - 1;
        int mid;
        // Find index of most smallest element
        while (left < right)
        {
            /*
            Prevent overflow, left / 2 = left - (left / 2)
            mid = (left + right) / 2 -> left + (right - left) / 2
            */
            mid = left + (right - left) / 2;
            if (nums[mid] > nums[right])
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        int minIndex = left;
        left = 0;
        right = nums.size() - 1;
        while (left <= right)
        {
            mid = left + (right - left) / 2;
            int midPivot = ((mid) + minIndex) % nums.size();
            if (nums[midPivot] < target)
            {
                left = mid + 1;
            }
            else if (nums[midPivot] > target)
            {
                right = mid - 1;
            }
            else
            { // Found answer
                return midPivot;
            }
        }
        return -1; // Target not in nums
    }
};