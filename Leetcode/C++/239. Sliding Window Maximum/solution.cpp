// https://leetcode.com/problems/sliding-window-maximum/

#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        if (k == 1)
        {
            return nums;
        }
        vector<int> result;
        deque<int> window;

        for (int idx = 0; idx < nums.size(); idx++)
        {
            while (!window.empty() && nums[window.back()] < nums[idx]) // Delete number index that are smaller than the current number.
            {
                window.pop_back();
            }
            window.push_back(idx);
            if (window[0] == idx - k)
            {
                window.pop_front();
            }
            if (idx > k - 1)
            { // Window not yet filled
                result.push_back(window[0]);
            }
        }
        return result;
    }
};