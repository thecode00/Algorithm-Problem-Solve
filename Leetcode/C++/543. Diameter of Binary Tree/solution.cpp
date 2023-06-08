// https://leetcode.com/problems/diameter-of-binary-tree/

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
    int maxDist = 0;
    int diameterOfBinaryTree(TreeNode *root)
    {
        search(root);
        return maxDist;
    }

    int search(TreeNode *root)
    {
        if (root == NULL)
        {
            return 0;
        }
        int left = search(root->left), right = search(root->right);
        // Compare max distance and current path distance
        maxDist = max(maxDist, left + right);
        // Add current node to the longest distance.
        return max(left, right) + 1;
    }
};