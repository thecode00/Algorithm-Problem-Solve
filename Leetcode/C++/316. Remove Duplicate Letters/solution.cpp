// https://leetcode.com/problems/remove-duplicate-letters/

#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <set>

using namespace std;

class Solution
{
public:
    string removeDuplicateLetters(string s)
    {
        unordered_map<char, int> count;
        for (auto c : s)
        {
            count[c] += 1;
        }

        set<char> used;
        vector<char> stack;
        for (auto c : s)
        {
            count[c] -= 1;
            if (used.find(c) != used.end())
            {
                continue;
            }
            used.insert(c);
            // When the character at the end of the stack is larger than the current character and it still has remaining count, remove it.
            while (!stack.empty() && stack.back() > c && count[stack.back()] > 0)
            {
                used.erase(stack.back());
                stack.pop_back();
            }
            stack.emplace_back(c);
        }

        stringstream ss;
        for (auto c : stack)
        {
            ss << c;
        }
        return ss.str();
    }
};