// https://leetcode.com/problems/valid-number/

class Solution
{
public:
    bool isNumber(string s)
    {
        static const regex re("^([+-]?((\\d+\\.\\d*)|(\\.\\d+)|(\\d+))([eE][+-]?\\d+)?)$");

        return regex_match(s, re);
    }
};