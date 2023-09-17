// https://leetcode.com/problems/unique-binary-search-trees/

#include <vector>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int numTrees(int n)
    {
        return search(1, n).size();
    }

    vector<TreeNode *> search(int start, int end)
    {
        vector<TreeNode *> result;
        if (start > end)
        {
            result.emplace_back(nullptr);
            return result;
        }

        for (int i = start; i <= end; i++)
        {
            vector<TreeNode *> leftTree = search(start, i - 1), rightTree = search(i + 1, end);
            for (auto left : leftTree)
            {
                for (auto right : rightTree)
                {
                    TreeNode *cur = new TreeNode(i);
                    cur->left = left;
                    cur->right = right;
                    result.emplace_back(cur);
                }
            }
        }
        return result;
    }
};