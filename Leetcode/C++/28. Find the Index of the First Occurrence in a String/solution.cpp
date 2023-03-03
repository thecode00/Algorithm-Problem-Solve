// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

#include <string>

using namespace std;

class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        for (int left = 0; left < haystack.size(); left++)
        {
            int right;
            for (right = 0; right < needle.size(); right++)
            {
                if (haystack[left + right] != needle[right])
                {
                    break;
                }
            }
            if (right == needle.size())
            {
                return left;
            }
        }
        return -1;
    }
};