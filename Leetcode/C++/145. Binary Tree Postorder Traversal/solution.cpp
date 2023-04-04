// https://leetcode.com/problems/binary-tree-postorder-traversal/description/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>

using namespace std;

class Solution
{
    vector<int> answer;

public:
    vector<int> postorderTraversal(TreeNode *root)
    {
        postorder(root);
        return answer;
    }

    void postorder(TreeNode *node)
    {
        if (!node)
        {
            return;
        }
        postorder(node->left);
        postorder(node->right);
        answer.push_back(node->val);
    }
};