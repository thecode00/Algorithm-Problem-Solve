// https://leetcode.com/problems/reverse-words-in-a-string/
// Ref: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

#include <string>

using namespace std;

class Solution
{
public:
    string reverseWords(string s)
    {
        reverse(s.begin(), s.end());
        // left, right = start, end index of word
        int left = 0, right = 0, index = 0;
        while (index < s.size())
        {
            // Find not empty word
            while (index < s.size() && s[index] != ' ')
            {
                s[right++] = s[index++];
            }
            // If find not empty word reverse it
            if (left < right)
            {
                reverse(s.begin() + left, s.begin() + right);
                if (right == s.size())
                    break;
                s[right++] = ' '; // Insert blank between word
                left = right;
            }

            index++;
        }
        // Delete last empty char
        if (right > 0 && s[right - 1] == ' ')
            --right;
        s.resize(right);
        return s;
    }
};