// https://leetcode.com/problems/is-subsequence/

#include <string>

using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int count = 0;
        for (auto char_t : t)
        {
            if (s[count] == char_t)
            {
                count += 1;
            }
            if (count >= s.size())
            {
                break;
            }
        }
        return count >= s.size();
    }
};