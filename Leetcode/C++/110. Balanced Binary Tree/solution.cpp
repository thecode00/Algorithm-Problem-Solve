// https://leetcode.com/problems/balanced-binary-tree/

#include <cmath>
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
    bool isBalanced(TreeNode *root)
    {
        int diff = search(root);
        // If diff = -1 tree is not balanced
        return diff == -1 ? false : true;
    }

private:
    int search(TreeNode *root)
    {
        // Except NULL tree
        if (root == NULL)
        {
            return 0;
        }

        int left = search(root->left), right = search(root->right);
        // If left right subtree is not balanced or already not balanced tree exist return -1
        if (abs(left - right) > 1 || left == -1 || right == -1)
        {
            return -1;
        }
        // return height
        return max(left, right) + 1;
    }
};