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
        vector<string> encoded;
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            int length = q.size();
            for (int i = 0; i < length; i++)
            {
                TreeNode *cur = q.front();
                q.pop();
                if (cur == NULL)
                {
                    encoded.push_back("#");
                }
                else
                {
                    encoded.push_back(to_string(cur->val));

                    q.push(cur->left);
                    q.push(cur->right);
                }
            }
        }
        // Convert encoded vector to string
        stringstream ss;
        for (auto &s : encoded)
        {
            ss << s << " ";
        }
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data)
    {
        // Except NULL TreeNode
        if (data == "# ")
        {
            return NULL;
        }
        // Split whitespace and save values to nodes vector
        vector<string> nodes;
        stringstream ss(data);
        string val;
        while (ss >> val)
        {
            nodes.push_back(val);
        }

        TreeNode *root = new TreeNode(stoi(nodes[0]));
        queue<TreeNode *> q;
        q.push(root);
        int index = 1;
        while (!q.empty())
        {
            TreeNode *cur = q.front();
            q.pop();
            // Connect left, right node
            if (nodes[index] != "#")
            {
                cur->left = new TreeNode(stoi(nodes[index]));
                q.push(cur->left);
            }
            index += 1;

            if (nodes[index] != "#")
            {
                cur->right = new TreeNode(stoi(nodes[index]));
                q.push(cur->right);
            }
            index += 1;
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));