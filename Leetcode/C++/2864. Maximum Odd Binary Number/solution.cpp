// https://leetcode.com/problems/maximum-odd-binary-number/description/

#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    string maximumOddBinaryNumber(string s)
    {
        sort(s.rbegin(), s.rend());
        for (int i = s.size() - 1; i >= 0; i--)
        {
            if (s[i] == '1')
            {
                swap(s[i], s[s.size() - 1]);
                return s;
            }
        }
        // Error value
        return "2";
    }
};