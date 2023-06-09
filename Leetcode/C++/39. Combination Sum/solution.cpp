// https://leetcode.com/problems/combination-sum/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> result;
    vector<int> numbers;
    int targetSum, size;
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        targetSum = target;
        size = candidates.size();
        numbers = candidates;

        vector<int> comb;
        dfs(comb, 0, 0);
        return result;
    }

    void dfs(vector<int> &comb, int total, int start)
    {
        if (total == targetSum)
        {
            result.push_back(comb);
            return;
        }
        else if (total > targetSum) // Backtracking
        {
            return;
        }

        for (int index = start; index < size; index++)
        {
            // Search current index number after search to avoid affecting search results pop element
            comb.push_back(numbers[index]);
            dfs(comb, total + numbers[index], index);
            comb.pop_back();
        }
    }
};