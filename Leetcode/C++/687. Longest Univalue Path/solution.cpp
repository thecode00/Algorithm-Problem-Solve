// https://leetcode.com/problems/longest-univalue-path/description/

#include <algorithm>

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
    int length = 0;
    int longestUnivaluePath(TreeNode *root)
    {
        search(root, 0);
        return length;
    }

    int search(TreeNode *root, int parentVal)
    {
        if (root == NULL)
        {
            return 0;
        }

        int left = search(root->left, root->val), right = search(root->right, root->val);
        length = max(length, left + right);
        // If parent node has same value add current node to path else reset path
        return parentVal == root->val ? max(left, right) + 1 : 0;
    }
};