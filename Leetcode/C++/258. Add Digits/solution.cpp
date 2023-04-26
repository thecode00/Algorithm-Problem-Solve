// https://leetcode.com/problems/add-digits/
// Time complexity: O(1)

class Solution
{
public:
    int addDigits(int num)
    {
        if (num < 10)
        {
            return num;
        }
        int result = num % 9;
        return result == 0 ? 9 : result;
    }
};