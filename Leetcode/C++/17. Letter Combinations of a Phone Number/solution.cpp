// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    vector<string> letterCombinations(string digits)
    {
        unordered_map<char, string> numberPad = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}};
        vector<string> result;
        // DFS
        vector<pair<string, int>> stack;
        stack.push_back({"", 0});

        while (!stack.empty())
        {
            string curString = stack.back().first;
            int index = stack.back().second;
            stack.pop_back();
            // If current index is last digits add result curString + last digit char
            if (index == digits.size() - 1)
            {
                for (char c : numberPad[digits[index]])
                {
                    result.push_back(curString + c);
                }
                continue;
            }
            // Add digit char
            for (char c : numberPad[digits[index]])
            {
                stack.push_back({curString + c, index + 1});
            }
        }
        return result;
    }
};