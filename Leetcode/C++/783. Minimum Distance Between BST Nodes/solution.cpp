// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

#include <vector>
#include <climits>

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
    int minDiffInBST(TreeNode *root)
    {
        int diff = INT_MAX, prev = INT_MIN;
        vector<TreeNode *> stack;
        TreeNode *node = root;
        while (!stack.empty() || node)
        {
            // Move deepest left node
            while (node)
            {
                stack.push_back(node);
                node = node->left;
            }
            node = stack.back();
            stack.pop_back();
            // If current node not first search node check diff
            if (prev != INT_MIN)
            {
                diff = min(diff, node->val - prev);
            }
            prev = node->val;

            node = node->right;
        }
        return diff;
    }
};