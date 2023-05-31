// https://leetcode.com/problems/daily-temperatures/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        vector<int> result = vector<int>(temperatures.size());
        vector<pair<int, int>> stack;
        for (int idx = 0; idx < temperatures.size(); idx++)
        {
            // Looking for past index that current index is warmer day
            while (!stack.empty() && stack.back().first < temperatures[idx])
            {
                int diff = idx - stack.back().second;
                result[stack.back().second] = diff;
                stack.pop_back();
            }
            stack.push_back({temperatures[idx], idx});
        }
        // No future day warmer temperatures
        while (!stack.empty())
        {
            result[stack.back().second] = 0;
            stack.pop_back();
        }
        return result;
    }
};