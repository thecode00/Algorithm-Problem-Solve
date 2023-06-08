// https://leetcode.com/problems/combinations/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> result;
    vector<int> numbers;
    vector<vector<int>> combine(int n, int k)
    {
        for (int num = 1; num <= n; num++)
        {
            numbers.push_back(num);
        }
        vector<int> comb;
        dfs(comb, k, 0);
        return result;
    }

    void dfs(vector<int> &comb, int target, int start)
    {
        // If comb size = k add comb to result
        if (comb.size() == target)
        {
            result.push_back(comb);
            return;
        }

        for (int index = start; index < numbers.size(); index++)
        {
            comb.push_back(numbers[index]);
            dfs(comb, target, index + 1);
            comb.pop_back();
        }
    }
};