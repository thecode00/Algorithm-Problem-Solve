// https://leetcode.com/problems/trapping-rain-water/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        int water = 0;
        int left = 0, right = height.size() - 1;
        int leftMax = height[left], rightMax = height[right];

        // left and right will meet max value of height
        while (left < right)
        {
            leftMax = max(leftMax, height[left]);
            rightMax = max(rightMax, height[right]);
            if (leftMax <= rightMax)
            {
                water += leftMax - height[left];
                left += 1;
            }
            else
            {
                water += rightMax - height[right];
                right -= 1;
            }
        }
        return water;
    }
};