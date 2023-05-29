// https://leetcode.com/problems/product-of-array-except-self/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> answer;
        int mul = 1;
        for (int num : nums) // Multiple from left
        {
            answer.push_back(mul);
            mul *= num;
        }
        mul = 1;
        for (int idx = nums.size() - 1; idx >= 0; idx--) // Multiple from right
        {
            answer[idx] *= mul;
            mul *= nums[idx];
        }
        return answer;
    }
};