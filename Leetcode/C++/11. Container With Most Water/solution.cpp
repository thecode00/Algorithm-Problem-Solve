// https://leetcode.com/problems/container-with-most-water/

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0, right = height.size() - 1, maxWater = 0;
        while (left < right)
        {
            maxWater = max(maxWater, max(height[left], height[right]) * (right - left));
            if (height[left] > height[right])
            {
                right -= 1;
            }
            else
            {
                left += 1;
            }
        }
        return maxWater;
    }
};