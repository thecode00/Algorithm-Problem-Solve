// https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

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

#include <queue>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<double> averageOfLevels(TreeNode *root)
    {
        vector<double> average;
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            int size = q.size();
            double total = 0;
            for (int i = 0; i < size; i++)
            {
                total += q.front()->val;
                if (q.front()->left)
                {
                    q.push(q.front()->left);
                }

                if (q.front()->right)
                {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            average.push_back(total / size);
        }
        return average;
    }
};