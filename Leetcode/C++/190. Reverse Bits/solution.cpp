// https://leetcode.com/problems/reverse-bits/description/

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        uint32_t result = 0;
        for (int idx = 0; idx < 32; idx++)
        {
            if ((n & (1 << idx)) != 0)
            {
                result |= 1 << (31 - idx);
            }
        }

        return result;
    }
};