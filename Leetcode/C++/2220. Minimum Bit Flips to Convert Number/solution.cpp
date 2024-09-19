// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description

class Solution
{
public:
    int minBitFlips(int start, int goal)
    {
        int count = 0;
        start ^= goal;

        /*
        n & (n - 1) is an operation that delete the rightmost 1 bit
        If start = 7, binary is = 111 so start - 1 = 110
        start & (start - 1) = 111 & 110 = 110
        */
        while (start > 0)
        {
            count += 1;
            start &= start - 1;
        }

        return count;
    }
};