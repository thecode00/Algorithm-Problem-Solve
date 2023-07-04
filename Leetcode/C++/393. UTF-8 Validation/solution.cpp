// https://leetcode.com/problems/utf-8-validation/

#include <vector>

using namespace std;

class Solution
{
public:
    bool validUtf8(vector<int> &data)
    {
        int cur = 0;
        while (cur < data.size())
        {
            if ((data[cur] >> 3 == 0b11110) && check(data, 3, cur + 1))
            {
                cur += 4;
            }
            else if ((data[cur] >> 4 == 0b1110) && check(data, 2, cur + 1))
            {
                cur += 3;
            }
            else if ((data[cur] >> 5 == 0b110) && check(data, 1, cur + 1))
            {
                cur += 2;
            }
            else if (data[cur] >> 7 == 0b0) // Single byte char
            {
                cur += 1;
            }
            else // Not vaild UTF-8 char
            {
                return false;
            }
        }
        return true;
    }

    bool check(vector<int> &data, int size, int index) // Check vaild n-bytes character (n > 1)
    {
        while (size > 0)
        {
            size--;
            if (index >= data.size() || data[index] >> 6 != 0b10)
            {
                return false;
            }
            index++;
        }
        return true;
    }
};