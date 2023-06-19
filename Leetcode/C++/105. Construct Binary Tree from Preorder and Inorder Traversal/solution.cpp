// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#include <vector>

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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        int preIndex = 0;
        return buildTreeHelper(preorder, inorder, 0, inorder.size() - 1, preIndex);
    }
    // Start, end param is inorder slice index
    TreeNode *buildTreeHelper(vector<int> &preorder, vector<int> &inorder, int start, int end, int &preIndex)
    {
        if (start > end)
        {
            return nullptr;
        }

        int midVal = preorder[preIndex++];
        TreeNode *node = new TreeNode(midVal);

        int mid = find(inorder.begin() + start, inorder.begin() + end, midVal) - inorder.begin();

        node->left = buildTreeHelper(preorder, inorder, start, mid - 1, preIndex);
        node->right = buildTreeHelper(preorder, inorder, mid + 1, end, preIndex);

        return node;
    }
};

class Solution
{
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        return buildTreeHelper(preorder, inorder, 0, inorder.size() - 1);
    }
    // Start, end param is inorder slice index
    TreeNode *buildTreeHelper(vector<int> &preorder, vector<int> &inorder, int start, int end)
    {
        if (start > end)
        {
            return NULL;
        }
        int midVal = preorder[0];
        TreeNode *node = new TreeNode(midVal);
        preorder.erase(preorder.begin()); // erase first element is O(N) need optimize
        int mid = find(inorder.begin() + start, inorder.begin() + end, midVal) - inorder.begin();
        node->left = buildTreeHelper(preorder, inorder, start, mid - 1);
        node->right = buildTreeHelper(preorder, inorder, mid + 1, end);
        return node;
    }
};