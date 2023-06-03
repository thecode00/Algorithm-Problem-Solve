// https://leetcode.com/problems/permutations/
// Ref: https://leetcode.com/problems/permutations/solutions/1257633/backtracking-solution-c-easy-to-understand-with-explanation/

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> result;
    vector<vector<int>> permute(vector<int> &nums)
    {
        permutation(nums, 0, nums.size() - 1);
        return result;
    }

    void permutation(vector<int> &nums, int start, int n)
    {
        if (start == n)
        {
            result.push_back(nums);
            return;
        }

        for (int idx = start; idx < nums.size(); idx++)
        {
            // cout << start << endl;
            swap(nums[idx], nums[start]);
            permutation(nums, start + 1, n);
            swap(nums[idx], nums[start]);
        }
    }
};