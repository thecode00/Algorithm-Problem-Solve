// https://leetcode.com/problems/subsets/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> result;
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<int> subset;
        dfs(nums, subset, 0);
        return result;
    }

    // Ex. nums = {1, 2, 3}, result = {[]} -> {[], [1]} -> {[], [1], [1, 2]} -> ... -> {[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]}
    void dfs(vector<int> &nums, vector<int> &subset, int start)
    {
        result.push_back(subset);
        if (start >= nums.size())
        {
            return;
        }

        for (int index = start; index < nums.size(); index++)
        {
            subset.push_back(nums[index]);
            dfs(nums, subset, index + 1);
            subset.pop_back();
        }
    }
};