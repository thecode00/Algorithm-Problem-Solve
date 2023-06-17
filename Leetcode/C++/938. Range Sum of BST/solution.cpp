// https://leetcode.com/problems/range-sum-of-bst/description/

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
    int rangeSumBST(TreeNode *root, int low, int high)
    {
        if (root == NULL)
        {
            return 0;
        }
        // If root->val is out of low-high range not include current value and search left or right subtree
        if (root->val < low)
        {
            return rangeSumBST(root->right, low, high);
        }
        else if (root->val > high)
        {
            return rangeSumBST(root->left, low, high);
        }
        // root->val is low <= val <= high so include current value and search left and right subtree
        return root->val + rangeSumBST(root->right, low, high) + rangeSumBST(root->left, low, high);
        ;
    }
};