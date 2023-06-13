// https://leetcode.com/problems/maximum-depth-of-binary-tree/

#include <queue>

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
    int maxDepth(TreeNode *root)
    {
        // Filter NULL root
        if (root == NULL)
        {
            return 0;
        }
        int depth = 0;
        TreeNode *curNode;
        queue<TreeNode *> level;
        level.push(root);
        // Search each level
        while (!level.empty())
        {
            depth += 1;
            // Save count of level node
            int levelLength = level.size();
            for (int i = levelLength; i > 0; i--)
            {
                curNode = level.front();
                level.pop();
                // Check child node
                if (curNode->left != NULL)
                {
                    level.push(curNode->left);
                }
                if (curNode->right != NULL)
                {
                    level.push(curNode->right);
                }
            }
        }

        return depth;
    }
};