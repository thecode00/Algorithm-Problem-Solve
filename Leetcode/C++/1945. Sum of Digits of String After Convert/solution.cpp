// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description

class Solution
{
public:
    int getLucky(string s, int k)
    {
        int result = 0;
        for (auto c : s)
        {
            int val = c - 'a' + 1;

            // Transform
            if (val < 10)
                result += val;
            else
                result += (val / 10) + (val % 10);
        }

        k -= 1;
        // A single-digit number remains the same after a transformation, so process stops.
        while (k > 0 && result >= 10)
        {
            int total = 0;

            while (result > 0)
            {
                total += result % 10;
                result /= 10;
            }
            result = total;
            k -= 1;
        }

        return result;
    }
};