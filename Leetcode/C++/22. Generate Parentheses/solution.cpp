// https://leetcode.com/problems/generate-parentheses/description/

#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<string> result;
    int length;
    vector<string> generateParenthesis(int n)
    {
        length = n;
        string p = "";
        search(0, 0, p);
        return result;
    }
    // Search like DFS
    void search(int left, int right, string &parenthesis)
    {
        if (left == right && left == length)
        {
            result.push_back(parenthesis);
        }
        if (left < length)
        {
            parenthesis += "(";
            search(left + 1, right, parenthesis);
            parenthesis.pop_back();
        }
        if (right < left)
        {
            parenthesis += ")";
            search(left, right + 1, parenthesis);
            parenthesis.pop_back();
        }
    }
};