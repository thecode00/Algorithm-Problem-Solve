// https://leetcode.com/problems/product-of-array-except-self/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> result;
        int mul = 1;

        for (int idx = 0; idx < nums.size(); idx++)
        {
            result.emplace_back(mul);
            mul *= nums[idx];
        }

        mul = 1;

        for (int idx = nums.size() - 1; idx >= 0; idx--)
        {
            result[idx] *= mul;
            mul *= nums[idx];
        }

        return result;
    }
};