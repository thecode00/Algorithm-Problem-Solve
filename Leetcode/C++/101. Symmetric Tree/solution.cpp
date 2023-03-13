// https://leetcode.com/problems/symmetric-tree/description/

/**
 * Definition for a binary tree node. */
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <queue>
#include <vector>

using namespace std;

class Solution
{
public:
    bool isSymmetric(TreeNode *root)
    {
        if (root == nullptr)
        {
            return true;
        }
        TreeNode *left, *right;
        queue<TreeNode *> q1, q2;
        q1.push(root->left);
        q2.push(root->right);
        while (!q1.empty())
        {
            left = q1.front();
            right = q2.front();
            q1.pop();
            q2.pop();
            if (left == nullptr && right == nullptr)
            {
                continue;
            }
            else if ((left == nullptr || right == nullptr) || left->val != right->val)
            {
                return false;
            }
            q1.push(left->left);
            q2.push(right->right);

            q1.push(left->right);
            q2.push(right->left);
        }
        return true;
    }
};