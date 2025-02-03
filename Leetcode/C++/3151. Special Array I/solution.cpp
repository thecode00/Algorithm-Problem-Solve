// https://leetcode.com/problems/special-array-i/description

class Solution
{
public:
    bool isArraySpecial(vector<int> &nums)
    {
        for (int idx = 1; idx < nums.size(); idx++)
        {
            if ((nums[idx - 1] & 1) == (nums[idx] & 1))
            {
                return false;
            }
        }

        return true;
    }
};