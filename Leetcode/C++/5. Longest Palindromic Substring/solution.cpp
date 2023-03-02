// https://leetcode.com/problems/longest-palindromic-substring/description/

#include <string>

using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int left = 0, right = 0;
        int start_point = 0, max_length = 0;
        for (int idx = 0; idx < s.size(); idx++)
        {
            right = idx;
            // s ~right - 1 = same s[idx] character palindrome
            while (right < s.size() & s[idx] == s[right])
            {
                right += 1;
            }
            left = idx - 1;
            // Find palindrome not same character s[idx]
            while (left >= 0 && right < s.size() && s[left] == s[right])
            {
                left -= 1;
                right += 1;
            }
            // [left + 1 ~ right - 1] is palindrome
            int length = right - left - 1;
            if (length > max_length)
            {
                start_point = left + 1;
                max_length = length;
            }
        }
        return s.substr(start_point, max_length);
    }
};