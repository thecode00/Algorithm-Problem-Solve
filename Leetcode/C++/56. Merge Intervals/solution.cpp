// https://leetcode.com/problems/merge-intervals/

#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> result;
        for (auto &vec : intervals)
        {
            if (!result.empty() && vec[0] <= result.back()[1])
            {
                result.back()[1] = max(result.back()[1], vec[1]);
            }
            else
            {
                result.push_back(vec);
            }
        }
        return result;
    }
};