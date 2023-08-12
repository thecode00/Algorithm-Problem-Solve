// https://leetcode.com/problems/jump-game-ii/

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int time = 1, left = 0, right = nums[0];
        if (nums.size() <= 1)
        {
            return 0;
        }
        while (right < nums.size() - 1)
        {
            time += 1;
            int maxJump = 0;
            for (int i = left; i <= right; i++)
            {
                maxJump = max(maxJump, i + nums[i]);
            }
            left = right;
            right = maxJump;
        }
        return time;
    }
};
