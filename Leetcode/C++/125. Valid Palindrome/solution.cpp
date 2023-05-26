// https://leetcode.com/problems/valid-palindrome/description/

#include <cctype>
#include <string>

using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        int left = 0, right = s.size() - 1;
        while (left < right)
        {
            // Move to alphanumeric characters
            while (left < right && !isalnum(s[left]))
            {
                left += 1;
            }
            while (left < right && !isalnum(s[right]))
            {
                right -= 1;
            }
            if (tolower(s[left]) != tolower(s[right])) // Check palindrome
            {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
};