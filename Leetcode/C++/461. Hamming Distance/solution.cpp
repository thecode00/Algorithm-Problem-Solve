// https://leetcode.com/problems/hamming-distance/submissions/981599269/

class Solution
{
public:
    int hammingDistance(int x, int y)
    {
        int count = 0, result = x ^ y;
        while (result > 0)
        {
            count += result % 2; // When LSB(Least Significant Bit) is 1 add 1 else add 0
            result >>= 1;
        }
        return count;
    }
};