// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

#include <vector>
#include <iostream>

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
    TreeNode *sortedArrayToBST(vector<int> &nums)
    {
        return makeBST(nums, 0, nums.size());
    }

    TreeNode *makeBST(vector<int> &nums, int left, int right)
    {
        if (left >= right)
        {
            return NULL;
        }
        // Prevent overflow
        int mid = left + (right - left) / 2;
        TreeNode *root = new TreeNode(nums[mid]);
        // cout << left << " " << right << " " << nums[mid] << endl;    Debuging code
        root->left = makeBST(nums, left, mid);
        root->right = makeBST(nums, mid + 1, right);

        return root;
    }
};