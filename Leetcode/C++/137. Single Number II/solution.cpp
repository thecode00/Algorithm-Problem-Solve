// https://leetcode.com/problems/single-number-ii/description/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        unordered_map<int, int> counter;
        // Count elements amount
        for (auto &num : nums)
        {
            counter[num] += 1;
        }

        int result = -1;
        // Find single number
        for (auto p : counter)
        {
            if (p.second == 1)
            {
                result = p.first;
                break;
            }
        }
        return result;
    }
};