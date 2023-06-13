// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

#include <queue>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec
{
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root)
    {
        vector<char> data;
        data.push_back('#'); // Make 1-index
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty())
        {
            TreeNode *cur = q.back();
            q.pop();

            if (cur)
            {
                q.push(cur->left);
                q.push(cur->right);
                data.push_back(cur->val);
            }
            else
            {
                data.push_back('#');
            }
        }
        // Convert data vector to string
        stringstream ss;
        for (auto &c : data)
        {
            ss << c << " ";
        }
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data)
    {
        // Except NULL TreeNode
        if (data == "# # ")
        {
            return NULL;
        }
        return NULL;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));