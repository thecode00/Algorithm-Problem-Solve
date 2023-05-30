// https://leetcode.com/problems/valid-parentheses/

#include <vector>
#include <map>
#include <string>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        vector<int> stack;
        unordered_map<char, char> parenthesis = {
            {')', '('},
            {'}', '{'},
            {']', '['}};
        for (char c : s)
        {
            if (parenthesis.find(c) == parenthesis.end())
            {
                stack.push_back(c);
            }
            else
            {
                // If parenthesis invaild return false
                if (stack.empty() || stack.back() != parenthesis[c])
                {
                    return false;
                }
                stack.pop_back();
            }
        }
        // If stack is not empty invalid parenthesis
        return stack.empty();
    }
};