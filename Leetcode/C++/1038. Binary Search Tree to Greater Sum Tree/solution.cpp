// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution // DFS
{
public:
    int total = 0;
    TreeNode *bstToGst(TreeNode *root)
    {
        if (root == NULL)
        {
            return new TreeNode(0);
        }

        TreeNode *right = bstToGst(root->right);
        total += right->val;
        root->val = total;
        bstToGst(root->left);
        return root;
    }
};