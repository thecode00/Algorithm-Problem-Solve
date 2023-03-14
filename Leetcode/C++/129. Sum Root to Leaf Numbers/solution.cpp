// https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

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

#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int sumNumbers(TreeNode *root)
    {
        int total = 0;
        vector<string> pathStack;
        pathStack.push_back("");
        vector<TreeNode *> nodeStack;
        nodeStack.push_back(root);
        while (!nodeStack.empty())
        {
            TreeNode *curNode = nodeStack.back();
            nodeStack.pop_back();
            string curPath = pathStack.back();
            pathStack.pop_back();
            if (curNode->left == nullptr && curNode->right == nullptr) // Leaf node
            {
                total += stoi(curPath + to_string(curNode->val));
                continue;
            }
            if (curNode->left != nullptr)
            {
                pathStack.push_back(curPath + to_string(curNode->val));
                nodeStack.push_back(curNode->left);
            }
            if (curNode->right != nullptr)
            {
                pathStack.push_back(curPath + to_string(curNode->val));
                nodeStack.push_back(curNode->right);
            }
        }
        return total;
    }
};