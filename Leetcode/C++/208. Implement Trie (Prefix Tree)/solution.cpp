// https://leetcode.com/problems/implement-trie-prefix-tree/description/

#include <map>
#include <string>

using namespace std;

struct TrieNode
{
    unordered_map<char, TrieNode *> children;
    bool complete; // If complete is true current node is end of word
    TrieNode() : children(), complete(false) {}
};

class Trie
{
public:
    TrieNode *root;
    Trie()
    {
        root = new TrieNode();
    }

    void insert(string word)
    {
        TrieNode *cur = root;
        for (auto s : word)
        {
            if (cur->children.find(s) == cur->children.end())
            {
                cur->children[s] = new TrieNode();
            }
            cur = cur->children[s];
        }
        cur->complete = true; // end of word set complete true
    }

    bool search(string word)
    {
        TrieNode *cur = root;
        for (auto s : word)
        {
            if (cur->children.find(s) == cur->children.end())
            {
                return false;
            }
            cur = cur->children[s];
        }
        // If insert apple and search app search not return false in for loop so we return complete variable
        return cur->complete;
    }

    bool startsWith(string prefix)
    {
        TrieNode *cur = root;
        for (auto s : prefix)
        {
            if (cur->children.find(s) == cur->children.end())
            {
                return false;
            }
            cur = cur->children[s];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */