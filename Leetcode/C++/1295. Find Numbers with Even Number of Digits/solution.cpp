// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution
{
public:
    int findNumbers(vector<int> &nums)
    {
        int count = 0;
        for (auto num : nums)
        {
            int digits = 0;

            while (num > 0)
            {
                digits += 1;
                num /= 10;
            }

            if (digits % 2 == 0)
            {
                count += 1;
            }
        }

        return count;
    }
};