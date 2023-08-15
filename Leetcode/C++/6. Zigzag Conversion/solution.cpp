// https://leetcode.com/problems/zigzag-conversion/

#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
        {
            return s;
        }
        int step = 1, index = 0;
        vector<string> rows(numRows);
        for (int i = 0; i < s.size(); i++)
        {
            rows[index] += s[i];
            // Change zigzag direction
            if (index == 0)
            {
                step = 1;
            }
            else if (index == numRows - 1)
            {
                step = -1;
            }

            index += step;
        }

        stringstream ss;
        for (auto row : rows)
        {
            ss << row;
        }
        return ss.str();
    }
};