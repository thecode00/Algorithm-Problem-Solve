// https://leetcode.com/problems/single-number/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        int result = 0;
        for (auto num : nums)
        {
            result ^= num;
        }
        return result;
    }
};